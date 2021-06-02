from titanic.models.dataset import Dataset
from titanic.models.service import Service


class Controller(object):

    dataset = Dataset()
    service = Service()

    def modeling(self, train, test) -> object:
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def preprocess(self, train, test) -> object:
        service = self.service
        this = self.dataset
        # 초기 모델(DF) 생성
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        # 불필요한 feature (Cabin, Ticket) 제거
        this = service.drop_feature(this, 'Cabin', 'Ticket')
        # norminal, ordinal 로 정형화
        this = service.embarked_nominal(this)
        this = service.title_norminal(this)
        this = service.gender_norminal(this)
        # 불필요한 feature (Name) 제거
        this = service.drop_feature(this, 'Name', 'Sex')
        this = service.age_ordinal(this)
        self.print_this(this)

        return this

    @staticmethod
    def print_this(this):
        print('*'*100)
        print(f'1. Train 의 type \n {type(this.train)} ')
        print(f'2. Train 의 column \n {this.train.columns} ')
        print(f'3. Train 의 상위 1개 행\n {this.train.head(1)} ')
        print(f'4. Train 의 null 의 갯수\n {this.train.isnull().sum()}개')
        print(f'5. Test 의 type \n {type(this.test)}')
        print(f'6. Test 의 column \n {this.test.columns}')
        print(f'7. Test 의 상위 1개 행\n {this.test.head(1)}개')
        print(f'8. Test 의 null 의 갯수\n {this.test.isnull().sum()}개')
        print('*' * 100)


