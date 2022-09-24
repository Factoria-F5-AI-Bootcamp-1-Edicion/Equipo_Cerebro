from __future__ import print_function, unicode_literals
from collections.abc import Mapping
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from colorama import init, Back, Fore

from validations import AgeValidation, GlucoseValidation,BmiValidation

class Enter_data():

    ## CONSTANTES CON CADENAS DE PREGUNTAS AL USUARIO
    AGE =" Enter your age ( number between 0 and 99): "
    GENDER ="Enter your gender(Male or female): "
    HYPER="Enter if you have hypertension(Yes or no): "
    HEART_DISEASE = "Enter if you have heart_disease (Yes or no): "
    MARRIED= "Enter if you are married (Yes or no): "
    WORK_TYPE= "Enter your work type (government / self-employed / private / children): "

    RESIDENCE_TYPE= "Enter your residence type (urban or rural): "	
    GLUCOSE_LEVEL="Enter your glucose level ( number between 0 and 300): "
    BMI= "Enter your bmi ( number between 0 and 100): "
    SMOKER = "Enter your smoker status ( never / unknown / formerly / smokes): "

    style = style_from_dict({
        Token.QuestionMark: '#E91E63 bold',
        Token.Selected: '#673AB7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#2196f3 bold',
        Token.Question: '',
    })

    def show_title(self,message):
        print()
        init()
        print(Back.LIGHTBLUE_EX)
        print(Fore.RED)
        print(message)
        print(Back.BLACK)
        print(Fore.WHITE)

    def user_input(self):
        questions = [
        {
            'type': 'input',
            'name': 'age',
            'message': self.AGE,
            'validate': AgeValidation,
        },

        {
            'type': 'list',
            'name': 'gender',
            'message': self.GENDER,
            'choices': ["Male","Female"],
        },

        {
            'type': 'input',
            'name': 'avg_glucose_level',
            'message':self.GLUCOSE_LEVEL,
            'validate': GlucoseValidation,
        },
        {
            'type': 'input',
            'name': 'bmi',
            'message':self.BMI,
            'validate': BmiValidation,
        },

        {
            'type': 'list',
            'name': 'hypertension',
            'message':self.HYPER,
            'choices': ["Yes","No"],
        },
        {
            'type': 'list',
            'name': 'heart_disease',
            'message':self.HEART_DISEASE,
            'choices': ["Yes","No"],
        },
         {
            'type': 'list',
            'name': 'ever_married',
            'message':self.MARRIED,
            'choices': ["Yes","No"],
        },
        {
            'type': 'list',
            'name': 'work_type',
            'message':self.WORK_TYPE,
            'choices': ["government","self-employed","private","children"],
        },
        {
            'type': 'list',
            'name': 'Residence_type',
            'message':self.RESIDENCE_TYPE,
            'choices': ["urban","rural"],
        },
        {
        'type': 'list',
        'name': 'smoking_status',
        'message':self.SMOKER,
        'choices': ["never","unknown","formerly","smokes"],
        }
        ]
        answers = prompt(questions, style=self.style)
        print('Data receipt:')
        pprint(answers)
        return (answers)
