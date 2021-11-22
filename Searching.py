from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from selenium import webdriver


plusurl = input('크롤링할 키워드 입력').split()
baseurl = 'https://google.com/search?q='

Crawling_List = []
def Google():
    for keyword in plusurl:
        url = baseurl + quote_plus(keyword)
        driver = webdriver.Chrome()
        driver.get(url)

        html = driver.page_source
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')

        r = soup.select('.r')

        for i in r:
            Crawling_one =  {
                '제목' : i.select_one('.LC20lb.DKYOMd').text,
                '링크' : i.a.attrs['href']
            }
            print(Crawling_one)
            Crawling_List.append(Crawling_one)
        driver.close()

    return Crawling_List

Google()
print(Crawling_List)

