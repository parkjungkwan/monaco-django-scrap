class VectorTest(object):

    ls = ['abcd', 786, 2.23, 'john', 70.2]
    tinyls = [123, 'john']
    tp = ('abcd', 786, 2.23, 'john', 70.2)
    tinytp = (123, 'john')
    dt = {'abcd': 786, 'john': 70.2}
    tinydt = {'홍': '30세'}

    def ls_create(self):
        # Create: ls 에 '100'을 추가 Create
        self.ls.append(100)

    def ls_read(self):
        # Read: ls 의 목록을 출력
        print(self.ls())

    def ls_update(self):
        # Update: ls와 tinyls 의 결합
        self.ls.extend(self.tinyls)

    def ls_delete(self):
        # Delete: ls 에서 786을 제거
        self.ls.remove(786)

    def tp_create(self):
        # Create: tp 에 '100'을 추가 Create
        self.tp = self.tp + (100,)
        print(self.tp)

    def tp_read(self):
        # Read: tp 의 목록을 출력
        print(self.tp)

    def tp_merge(self):
        # Merge: tp와 tinytp 의 결합
        self.tp + self.tinytp


    def tp_delete(self):
        # Delete: tp 에서 786을 제거
        print('Impossible')

    def dt_create(self):
        # Create: dt 에 키값으로 'tom', 밸류로 '100'을 추가 Create
        self.dt['tom'] = 100
        print(self.dt)

    def dt_read(self):
        # Read: dt 의 목록을 출력
        print(self.dt)

    def dt_update(self):
        # Update: dt와 tinydt 의 결합
        self.dt.update(self.tinydt)

    def dt_delete(self):
        # Delete: dt 에서 'abcd' 제거
        del self.dt['abcd']
        print(self.dt())

    @staticmethod
    def main():
        v = VectorTest()
        while 1:
            menu = input('0. Exit\n '
                         'LIST : 1. Create,2.Read,3.Update,4.Delete\n'
                         'Tuple : 5. Create,6.Read,7.Update,8.Delete\n '
                         'Dictionary : 9. Create,10.Read,11.Update,12.Delete')
            if menu == '0':
                break
            elif menu == '1':
                v.ls_create()
            elif menu == '2':
                v.ls_read()
            elif menu == '3':
                v.ls_update()
            elif menu == '4':
                v.ls_delete()
            elif menu == '5':
                v.tp_create()
            elif menu == '6':
                v.tp_read()
            elif menu == '7':
                v.tp_merge()
            elif menu == '8':
                v.tp_delete()
            elif menu == '9':
                v.dt_create()
            elif menu == '10':
                v.dt_read()
            elif menu == '11':
                v.dt_update()
            elif menu == '12':
                v.dt_delete()
            else:
                continue

VectorTest.main()
