import requests
import openpyxl
from bs4 import BeautifulSoup


all_url = "https://ignrando.fr/cirkwi-server/inc/ajax/carte/solrCluster.php?mb_ajax=&bounds%5B%5D=39.095963&bounds%5B%5D=-15.073242&bounds%5B%5D=53.852527&bounds%5B%5D=20.083008&zoom=5&type=parcours"

url_template = "https://ignrando.fr/cirkwi-server/inc/ajax/carte/solrCluster.php?mb_ajax=&bounds%5B%5D={lat}&bounds%5B%5D={lng}&bounds%5B%5D={lat}&bounds%5B%5D={lng}&zoom=12&type=parcours"

forward_url = "https://ignrando.fr/fr/cirkwi/proxy/forward/"

payload = {
    "json": {"url": "/inc/ajax/accueil/recherche/infobulle_consultation.php",
             "json": {"id": 329127, "langue": "fr_FR", "type": "parcours"}}
}

ligne_payload = {
    "json": {"url": "/inc/ajax/carte/trace.php", "json": {"id": 603936}}
}

xlsfile = openpyxl.Workbook()

sheet = xlsfile.worksheets[0]

sheet['A1'].value = "Name"
sheet['B1'].value = "Information"
sheet['C1'].value = "Coordinates"
sheet['D1'].value = "Route"

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'DNT': '1',
    'Origin': 'ignrando.fr',
    'Referer': 'https://ignrando.fr/fr/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'frontend=40a7fa281c264c268b7a5841675366b3'
}

res = requests.get(
    "https://ignrando.fr/cirkwi-server/inc/ajax/carte/solrCluster.php?mb_ajax=&bounds%5B%5D=46.637651&bounds%5B%5D=1.672668&bounds%5B%5D=46.869111&bounds%5B%5D=2.221985&zoom=11&type=parcours")
if res.ok:
    data = res.json()
    i = 2
    for dt in data['data']:
        payload = {
            'json': '{"url":"/inc/ajax/accueil/recherche/infobulle_consultation.php","json":{"id":' + str(
                dt['id_objet']) + ',"langue":"fr_FR","type":"parcours"}}'}

        res = requests.post(forward_url, data=payload, headers=headers)
        if res.ok:
            per = res.json()
            lng = dt['lng']
            lat = dt['lat']
            soup = BeautifulSoup(per['result']['html'], 'html.parser')
            h3 = soup.find('h3', attrs={'class': 'cdf_VignetteTitle'})
            name = h3.find('a', attrs={'class': 'cdf_VignetteTitleLink'}).text
            cords = f"lat:{lat}, lng:{lng}"

            p_rout = {
                'json': '{"url":"/inc/ajax/carte/trace.php","json":{"id":' + str(dt['id_parcours']) + '}}'}
            res = requests.post(url=forward_url, headers=headers, data=p_rout)
            route = "[]"
            if res.ok:
                ccc = res.json()
                route = ccc['result']
            sheet[f'A{i}'].value = name
            sheet[f'B{i}'].value = ""
            sheet[f'C{i}'].value = cords
            sheet[f'D{i}'].value = route

            i += 1

xlsfile.save("report.xlsx")
