from selenium import webdriver
from bs4 import BeautifulSoup


class NaverMove(object):

    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    class_name = ''
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.find_all('div',{"class":self.class_name})

        # print(i)
        driver.close()


if __name__ == '__main__':
    naver = NaverMove()
    # tit3
    naver.scrap()