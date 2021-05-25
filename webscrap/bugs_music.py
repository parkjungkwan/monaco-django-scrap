from bs4 import BeautifulSoup
from urllib.request import urlopen
class BugsMusic(object):

    url = ''

    def __str__(self):
        return self.url

    def scrap(self, class_name):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        count = 0
        print("< ARTIST >")
        for i in soup.find_all(name='p', attrs=({"class": class_name[0]})): # "artist"
            count += 1
            print(f'{str(count)} RANKING')
            print(f'{class_name[0]}: {i.find("a").text}')
        print("< TITLE >")
        for i in soup.find_all(name='p', attrs=({"class": class_name[1]})): # "title"
            count += 1
            print(f'{str(count)} RANKING')
            print(f'{class_name[1]}: {i.find("a").text}')

# https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01
    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = int(input('0.Exit\n 1.Input URL\n 2.Get Ranking \n 3.'))
            if menu == 0:
                break
            elif menu == 1:
                bugs.url = input('Input URL')
            elif menu == 2:
                bugs.scrap(["artist", "title"])
            else:
                print('Wrong Number')
                continue

BugsMusic.main()

