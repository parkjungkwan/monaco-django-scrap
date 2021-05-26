class Member(object):
    member_lst = list()
    member_id, pw, name, mail_address = ('', '', '', '')
    member_num = 0
    member_cnt = 0
    now_in = 0

    @staticmethod
    def join():
        member_id = input('아이디: ')
        pw = input('비밀번호: ')
        name = input('이름: ')
        mail_address = input('이메일 주소: ')
        Member.member_add(member_id, pw, name, mail_address)
        print('회원가입에 성공했습니다.')

    @classmethod
    def member_add(cls, member_id, pw, name, mail_address):
        mb = Member()
        mb.member_id = member_id
        mb.pw = pw
        mb.name = name
        mb.mail_address = mail_address
        mb.member_num = cls.member_cnt + 1
        cls.member_lst.append(mb)
        cls.member_cnt += 1

    @classmethod
    def log_in(cls):
        member_id = input('아이디: ')
        pw = input('비밀번호: ')
        log_in = 0
        for mb in cls.member_lst:
            if member_id == mb.member_id:
                if pw == mb.pw:
                    cls.now_in = mb.member_num
                    print('로그인에 성공했습니다.')
                    log_in = 1
                    break
        if log_in == 0:
            print('존재하지 않는 회원정보입니다.')

    @classmethod
    def log_out(cls):
        cls.now_in = 0

    @classmethod
    def show_info(cls):
        if cls.now_in:
            mb = cls.member_lst[cls.now_in - 1]
            print(f'아이디: {mb.member_id}')
            print(f'이름: {mb.name}')
            print(f'이메일 주소: {mb.mail_address}')
        else:
            print('로그인해주세요.')

    @classmethod
    def update_info(cls):
        if cls.now_in:
            while True:
                mb = cls.member_lst[cls.now_in - 1]
                mn = int(input('이름 변경\t\t1\n이메일 주소 변경\t2\n종료\t\t\t\t0'))
                if mn == 1:
                    print(f'현재 이름: {mb.name}')
                    mb.name = input('변경할 이름: ')
                    break
                elif mn == 2:
                    print(f'현재 이메일 주소: {mb.mail_address}')
                    mb.mail_address = input('변경할 이메일 주소: ')
                    break
                elif mn == 0:
                    break
                else:
                    print('잘못된 번호입니다.')
        else:
            print('로그인해주세요.')

    @classmethod
    def sign_out(cls):
        if cls.now_in:
            mb = cls.member_lst[cls.now_in - 1]
            if input('비밀번호를 입력해주세요: ') == mb.pw:
                del cls.member_lst[cls.now_in - 1]
                # cls.member_lst[cls.now_in - 1] 대신에 mb 로는 삭제 안되는 지 여쭤보기
                print('탈퇴후 재가입은 일주일 후 가능합니다.')
                cls.now_in = 0
            else:
                print('비밀번호가 틀렸습니다.')

    @staticmethod
    def main():
        while True:
            mn = int(input('-회원가입\t\t1\n-로그인\t\t\t2\n-로그아웃\t\t3\n-마이페이지\t\t4\n-회원정보 수정\t5\n-회원탈퇴\t\t6\n-종료\t\t\t0'))
            if mn == 1:
                Member.join()
            elif mn == 2:
                Member.log_in()
            elif mn == 3:
                Member.log_out()
            elif mn == 4:
                Member.show_info()
            elif mn == 5:
                Member.update_info()
            elif mn == 6:
                Member.sign_out()
            elif mn == 0:
                break
            else:
                print('Wrong menu')


Member.main()