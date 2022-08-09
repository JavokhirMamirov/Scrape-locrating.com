import requests



url_fist = "https://ignrando.fr/cirkwi-server/inc/ajax/carte/solrCluster.php?mb_ajax=&bounds%5B%5D=44.703802&bounds%5B%5D=2.958069&bounds%5B%5D=46.504064&bounds%5B%5D=8.231506&zoom=15&type=parcours"

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'DNT': '1',
    'Origin': 'ignrando.fr',
    'Referer': 'https://ignrando.fr/fr/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'frontend=40a7fa281c264c268b7a5841675366b3'
}

res = requests.get(url_fist)
if res.ok:
    data = res.json()
    print(len(data['data']))
