class MyDataFrame(object):

    def __init__(self, columns, index):
        self.columns = columns
        self.index = index

    @staticmethod
    def from_dict(dt, oriented="index"):
        pass

    @staticmethod
    def to_dict(dt, oriented="index"):
        pass

    @staticmethod
    def main():
        df = MyDataFrame(10, 3)