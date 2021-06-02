from titanic.models.dataset import Dataset
import pandas as pd
import numpy as np

class Service(object):

    dataset = Dataset()

    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis = 1)

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, *feature) -> object:
        for i in feature:
            this.train = this.train.drop([i], axis=1)
            this.test = this.test.drop([i], axis=1)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked':'S'})
        this.test = this.test.fillna({'Embarked':'S'})
        this.train['Embarked'] =  this.train['Embarked'].map({'S':1,'C':2,'Q':3})
        this.test['Embarked'] =  this.test['Embarked'].map({'S':1,'C':2,'Q':3})
        return this

    @staticmethod
    def fare_ordinal(this) -> object:
        this.test['Fare'] = this.test['Fare'].fillna(1)
        print(f' Test 의 null {this.test[this.test.isna().any(axis=1)]}')
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4)
        # quct 으로 bins 값 설정 {this.train["FareBand"].head(10)}
        # bins = list(pd.qcut(this.train['Fare'], 4, retbins=True))
        # 은 list 구조로 첫번째 인덱스는 str 타입의 문자이고 2번째 인덱스가 구간 값이다.
        # 그래서 [1] 을 주고 bins 로 처리한다.
        bins = list(pd.qcut(this.train['Fare'], 4, retbins=True))[1]
        this.train = this.train.drop(['FareBand'], axis=1)
        for these in this.train, this.test:
            these['FareBand'] = pd.cut(these['Fare'], bins=bins, labels=[1,2,3,4])  # {[labels]:[bins]}

        return this

    @staticmethod
    def title_norminal(this) -> object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mme', 'Rare')
            title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
            dataset['Title'] = dataset['Title'].fillna(0)
            dataset['Title'] = dataset['Title'].map(title_mapping)
        return this

    @staticmethod
    def gender_norminal(this) -> object:
        gender_mapping = {'male': 0, 'female': 1}
        for these in [this.train, this.test]:
            these['Gender'] = these['Sex'].map(gender_mapping)
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        train = this.train
        test = this.test
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_title_mapping = {'Unknown':0 , 'Baby': 1, 'Child': 2, 'Teenager' : 3, 'Student': 4, 'Young Adult': 5,
                             'Adult':6,  'Senior': 7}
        for i in train, test:
            i['AgeGroup'] = pd.cut(i['Age'], bins=bins, labels=labels) # {[labels]:[bins]}
            i['AgeGroup'] = i['AgeGroup'].map(age_title_mapping)

        return this

    @staticmethod
    def create_k_fold(this) -> object:
        return







