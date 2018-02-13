from train import  train
from processing import  Processing

class Run(train, Processing):
    def final_function(self):
        print('This project is Data Science based, \nit predicts the persons who will survive if the same RMS Titanic ')
        print('incident happens again. It uses train.py to Learn automatically how to handle situations, \n based on the input  ')
        print('\n\nEnter the choice number \n')
        print('1. Train the software using different datasets(remember to keep it inside the "datasets" folder)\n')
        print('2. Predict the survivla of people, based on the experience of the software on train.py experiences')

        ch = int(input('\n\n CHOICE : '))
        if ch == 1:

            self.asking_values()
            self.assigningValues()
        elif ch == 2:
            print('reached here')
            self.input_file_storage()


object = Run()
object.final_function()