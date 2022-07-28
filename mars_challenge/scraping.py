import requests
from bs4 import BeautifulSoup

# scraper code

def scrape_all():
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    main_list = []
    temp_list = []
    data = soup.find_all('div', class_='item')
    for x in data:
        link = x.find('a', class_="itemLink product-item")['href']
        temp_list.append(f'https://astrogeology.usgs.gov{link}')

    for xx in temp_list:
        url = xx
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        img = soup.find('img', class_='wide-image')['src']
        img = f'https://astrogeology.usgs.gov/{img}'
        name = soup.find('h2', class_='title').text.strip()
        main_dir = {
            'img_url': img,
            'title': name,
        }
        main_list.append(main_dir)
    data = main_list
    return data
# print(main_list)


if __name__ == "_main_":
    scrape_all()
