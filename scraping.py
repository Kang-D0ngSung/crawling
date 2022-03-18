import requests
from requests.exceptions import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup 

url = 'https://www.youtube.com/watch?v=DnQ09ZZCjCs&t=7s'
val = list()

try :
    saveHtml = open("./crawling_html.txt", 'w', encoding="UTF8")
    resp = requests.get(url)
    # html = urlopen(url)
    bsObject = BeautifulSoup(resp.text, "html.parser")
    resp.raise_for_status()

except HTTPError as Err :
    print('HTTP 에러 발생')

except Exception as Err :
    print('다른 에러 발생')

else:
    print('접속 성공')

    for div in bsObject.head.find('div'):
        saveHtml.write(div)


saveHtml.close()