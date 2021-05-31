from titanic.models.dataset import Dataset
from titanic.models.service import Service


class Test(object):

    dataset: object = Dataset()
    service: object = Service()

    def __init__(self, fname):
        service = self.service
        self.dataset.context = './data/'
        self.dataset.fname = fname
        self.entity = service.new_model(fname)

    def plot(self):
        this = self.entity
        print(f'The data type of Train is {type(this)}.')
        print(f'Columns of Train is {this.columns}.')
        print(f'The top 5 superior data are {this.head}.')
        print(f'The top 5 inferior data are {this.tail}.')


