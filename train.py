import csv
import random

'''csv_file = open('./datasets/train.csv', 'r')
reader = csv.reader(csv_file)
for row in reader:
    print(row)'''

class train:
    def __init__(self):
        self.csv_file = open('./datasets/train.csv', 'r')
        self.reader = csv.reader(self.csv_file)

        self.id = []
        self.survived = []
        self.pclass = []
        self.name = []
        self.sex = []
        self.age = []
        self.sibsp = []
        self.parch = []
        self.ticket = []
        self.fare = []
        self.cabin = []
        self.embarked = []
        self.no_of_rows = -1
        '''for i in self.reader:
            self.no_of_rows = self.no_of_rows + 1
        '''
        print(self.no_of_rows)
        for i in self.reader:
            self.id.append(str(i[0]))
            self.survived.append(i[1])
            self.pclass.append(i[2])
            self.name.append(i[3])
            self.sex.append(i[4])
            self.age.append(i[5])
            self.sibsp.append(i[6])
            self.parch.append(i[7])
            self.ticket.append(i[8])
            self.fare.append(i[9])
            self.cabin.append(i[10])
            self.embarked.append(i[11])



    def assigningValues(self):
        print('got in')

        print(len(self.id))
        '''for i in range(1, len(self.id)):
            print(self.id[i] + ' ' + self.survived[i] + ' ' + self.pclass[i] + ' ' + self.name[i])'''
        

obj = train()
obj.assigningValues()