# pip install requests beautifulsoup4
import requests
import re
from bs4 import BeautifulSoup


def crawler(page):
    soup = BeautifulSoup(page, 'html.parser')
    found_list = soup.find_all('span',
                               attrs={'data-role': 'list-title-text'})

    for item in found_list:
        try:
            title = item.text.strip()
            # print(title) # 클리앙 글 출력
            if re.search('아이패드', title):  # 아이패드에 관련된 글만 출력
                print(title.strip())

        except Exception as e:
            print('예외가 발생했 습니다.', e)
            pass


def get_page():
    header = {
        'referer': 'https://www.clien.net',
        'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, '
                      'like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'
    }

    url = 'https://www.clien.net/service/board/sold?&od=T31&po=0'
    req = requests.get(url, headers=header)
    #print(req.text)
    return req.text


if __name__ == '__main__':
    page = get_page()
    crawler(page)
