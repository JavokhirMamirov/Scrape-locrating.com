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

all_url = "https://ignrando.fr/cirkwi-server/inc/ajax/carte/solrCluster.php?mb_ajax=&bounds%5B%5D=39.095963&bounds%5B%5D=-15.073242&bounds%5B%5D=53.852527&bounds%5B%5D=20.083008&zoom=5&type=parcours"


def get_all_data(url):
    res = requests.get(url)
    if res.ok:
        data = res.json()
        return data['data']
    else:
        return []


def get_parcours(data):
    return ["name", 'info', 'coord', 'route']

def fetch_data(data):
    print(data)
    if "type" in data.keys():
        return
    elif "id_parcours" in data.keys():
        data = get_parcours(data)
        return data


def main():
    data = get_all_data(all_url)
    for dt in data:
        fetch_data(dt)



if __name__ == '__main__':
    main()
