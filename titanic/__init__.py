from titanic.views.controller import Controller
from titanic.views.test import Test

if __name__ == '__main__':
    controller = Controller()

    while 1:
        menu = input('0-exit 1-data visualization\n'
                     ' 2-modeling\n'
                     ' 3-machine learning\n'
                     ' 4-machine release ')
        if menu == '0':
            break
        elif menu == '1':
            test = Test('train.csv')
            test.plot()
        elif menu == '2':
            pass
        elif menu == '3':
            pass
        elif menu == '4':
            pass
        else:
            continue