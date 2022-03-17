import requests
from requests.exceptions import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup 

url = 'https://www.youtube.com/watch?v=DnQ09ZZCjCs&t=7s'
val = list()

try :
    resp = requests.get(url)
    # html = urlopen(url)
    bsObject = BeautifulSoup(resp.text, "html.parser")
    resp.raise_for_status()

except HTTPError as Err :
    print('HTTP 에러 발생')

except Exception as Err :
    print('다른 에러 발생')

else:
    print('성공')
    # print(bsObject)

    # for meta in bsObject.body:
    #     print(meta.get('content'))

    # print(div.head.find('div', {"id", "watch7-content"}).get("content"))

    for div in bsObject.head.find('div'):
        # test = div.find('meta')
        # print(test)
        # print(div)
        val.append(div)
        # print(div.find('meta', {"id", "watch7-content"}).get("content"))
        
    for n in range(len(val)) :
        print(n,'. ',val[n],'\n')
    # print(val[2])
