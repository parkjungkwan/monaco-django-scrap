from bs4 import BeautifulSoup
from urllib.request import urlopen
class BugsMusic(object):

    url = ''
    class_name = []

    def __str__(self):
        return self.url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        print('---------------- ARTIST RANKING ------------------')

        count = 0
        for i in soup.find_all(name='p', attrs=({"class": self.class_name[0]})):
            count += 1
            print(f'{str(count)} RANKING')
            print(f'artist: {i.find("a").text}')

        print('---------------- TITLE RANKING -----------------')
        count = 0
        for i in soup.find_all(name='p', attrs=({"class": self.class_name[1]})):
            count += 1
            print(f'{str(count)} RANKING')
            print(f'title: {i.find("a").text}')

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
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.scrap()
            else:
                print('Wrong Number')
                continue

BugsMusic.main()

