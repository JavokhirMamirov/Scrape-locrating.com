import openpyxl
import requests
import concurrent.futures
from bs4 import BeautifulSoup

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'DNT': '1',
    'Origin': 'ignrando.fr',
    'Referer': 'https://ignrando.fr/fr/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'frontend=40a7fa281c264c268b7a5841675366b3'
}

all_url = "https://ignrando.fr/cirkwi-server/inc/ajax/carte/solrCluster.php?mb_ajax=&bounds%5B%5D=39.095963&bounds%5B%5D=-7.073242&bounds%5B%5D=53.852527&bounds%5B%5D=-10.083008&zoom=8&type=parcours"

forward_url = "https://ignrando.fr/fr/cirkwi/proxy/forward/"


def get_all_data(url):
    res = requests.get(url)
    if res.ok:
        data = res.json()
        return data['data']
    else:
        return []


def get_parcours(dt):
    try:
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
            return [name, '', cords, route]
        else:
            return None
    except:
        return None


def fetch_data(data):
    try:
        if "type" in data.keys():
            return None
        elif "id_parcours" in data.keys():
            data = get_parcours(data)
            return data
    except:
        return None


def main():
    xlsfile = openpyxl.Workbook()

    sheet = xlsfile.worksheets[0]

    sheet['A1'].value = "Name"
    sheet['B1'].value = "Information"
    sheet['C1'].value = "Coordinates"
    sheet['D1'].value = "Route"
    data = get_all_data(all_url)
    print("Website scraping ....")
    with concurrent.futures.ProcessPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(fetch_data, dt): dt for dt in data}
        i = 2
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            if res is not None:
                sheet[f'A{i}'].value = res[0]
                sheet[f'B{i}'].value = res[1]
                sheet[f'C{i}'].value = res[2]
                sheet[f'D{i}'].value = res[3]

                i += 1

    xlsfile.save("report.xlsx")


if __name__ == '__main__':
    main()
