class Wikipedia(object):
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return self.url

    @staticmethod
    def main():
        while 1:
            menu = int(input('0.Exit\n 1.Input URL\n 2.Print URL\n'))
            if menu == 0:
                break
            elif menu == 1:
                wiki = Wikipedia(input('Input URL'))
            elif menu == 2:
                print(f'{wiki}')
            else:
                continue

Wikipedia.main()