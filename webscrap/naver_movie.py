from selenium import webdriver
from bs4 import BeautifulSoup
class NaverMove(object):

    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    classes = ''
    driver = 'C:/Program Files/Google/Chrome/chromedriver'

    def scrap(self):
        chromedriver = self.driver
        chromedriver.get(self.url)
        soup = BeautifulSoup(chromedriver.page_source, 'html.parser')
        all_div = soup.find_all('',{})

        # print(i)
        chromedriver.close()




if __name__ == '__main__':
    naver = NaverMove()
    #
    naver.scrap()