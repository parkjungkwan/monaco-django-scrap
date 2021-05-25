class Melon(object):
    url = ''

    def set_url(self, url):
        self.url = url

    @staticmethod
    def main():
        melon = Melon()
        while 1:
            menu = input('0 Exit 1.Input URL 2.Rank 1~100')
            if menu == '0':
                break
            elif menu == '1':
                melon.set_url(input('URL'))
            elif menu == '2':
                melon.get_ranking()
            else:
                continue
