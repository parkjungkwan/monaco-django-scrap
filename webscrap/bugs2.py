import requests
from bs4 import BeautifulSoup


class Bugs2(object):

    url = 'https://www.melon.com/chart/index.htm?dayTime='
    headers = {'User-Agent':'Mozilla/5.0'}
    class_name = []

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}',headers=self.headers).text

    def set_class_name(self, class_name):
        self.class_name = class_name

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('------- 제목 --------')
        ls = soup.find_all("div", {"class": self.class_name[0]})
        for i in ls:
            print(f' {i.find("a").text}')
        print('------ 가수 --------')
        ls = soup.find_all("div", {"class": self.class_name[1]})
        for i in ls:
            print(f' {i.find("a").text}')

    @staticmethod
    def main():
        b = Bugs2()
        while 1:
            menu = input('0, 1-input time, 2-output')
            if menu == '1':
                b.set_url(input('스크래핑할 날짜 입력')) # '2021052511'
            elif menu == '2':
                b.class_name.append('ellipsis rank01')
                b.class_name.append('ellipsis rank02')
                b.get_ranking()
            else:
                print('Wrong number')

Bugs2.main()