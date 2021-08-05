# 모듈을 읽어 들입니다.
from urllib import request
from bs4 import BeautifulSoup

# urlopen() 함수로 기상청의 전국 날씨를 읽습니다.
target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

# BeautifulSoup을 사용해 웹 페이지를 분석합니다.
soup = BeautifulSoup(target, "html.parser")
# print(soup)

# location 태그를 찾습니다.
for location in soup.select("location"):
    # 내부의 city, wf, tmn, tmx 태그를 찾아 출력합니다.
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()


# 추가 내용
import requests
from bs4 import BeautifulSoup

url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('#s_content > div.section > ul > li:nth-child(1) > dl > dt > a')

    # print(soup)

else : 
    print(response.status_code)

print(title)
print(title.get_text())