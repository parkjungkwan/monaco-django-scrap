from titanic.models.dataset import Dataset
from titanic.models.service import Service


class Controller(object):

    dataset = Dataset()
    service = Service()

    def modeling(self, train, test) -> object:
        service = self.service

    def preprocess(self, train) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        print(f'Train 의 type 은 {type(this.train)} 이다.')
        print(f'Train 의 column 은 {this.train.columns} 이다.')
        print(f'Train 의 상위 5개 데이터는 {this.train.head()} 이다.')
        print(f'Train 의 하위 5개 데이터는 {this.train.tail()} 이다.')



