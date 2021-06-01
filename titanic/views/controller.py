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
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        this = service.embarked_nominal(this)
        self.print_this(this)

        return this

    @staticmethod
    def print_this(this):
        print('<Type Check>')
        print(f'Train 의 type 은 {type(this.train)} 이다.')
        print(f'Train 의 column 은 {this.train.columns} 이다.')
        print(f'Train 의 상위 5개 행은 {this.train.head()} 이다.')
        print(f'Test 의 type 은 {type(this.test)} 이다.')
        print(f'Test 의 column 은 {this.test.columns} 이다.')
        print(f'Test 의 상위 5개 행은 {this.test.head()} 이다.')
        print(f'타입체크 {type(this.train["Embarked"])}')


