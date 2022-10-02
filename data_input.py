from __future__ import print_function, unicode_literals
from collections.abc import Mapping
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from colorama import init, Back, Fore

from validations import AgeValidation, GlucoseValidation, HeightValidation, WeightValidation

class Enter_data():
    compl=['Has sufrido perdida de sensibilidad en uno de los dos lados de la cara?',

'Cuando sonries la parte izquierda o derecha de la boca no se mueve?',

'Has sentido hormigueo en el rostro?',

'Te cuesta articular palabras?',

'Levanta los brazos al frente. Te ha quedado uno mas bajo que el otro o uno de los brazos cae desplomado?'

'Has tenido perdida de vision repentina?',

'Pierdes la vision de uno o de los dos ojos durante momentos?',

'Sufres de migrañas?',


'Dificultad para caminar o desequilibrio?',

'Tienes antecedentes familiares (Padre/Madre) de ictus?',

'perdida repentina de memoria?',


'Ha empezado con la menopausea?',


'tomas anticonceptivos?',
]
    ## CONSTANTES CON CADENAS DE PREGUNTAS AL USUARIO
    AGE =" Enter your age ( number between 0 and 99): "
    GENDER ="Enter your gender(Male or female): "
    HYPER="Enter if you have hypertension(Yes or no): "
    HEART_DISEASE = "Enter if you have heart_disease (Yes or no): "
    MARRIED= "Enter if you are married (Yes or no): "
    WORK_TYPE= "Enter your work type (government / self-employed / private / No Working): "

    RESIDENCE_TYPE= "Enter your residence type (urban or rural): "	
    GLUCOSE_LEVEL="Enter your glucose level ( number between 0 and 300): "
    SMOKER = "Enter your smoker status ( never /  formerly / smokes): "
    PESO =" Enter your weight(Kg)"
    ALTURA ="Enter your weight(cm)"

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
            'name': 'weight',
            'message': self.PESO,
            'validate': HeightValidation,
        },
        {
            'type': 'input',
            'name': 'height',
            'message': self.ALTURA,
            'validate': WeightValidation,
        }
        ,
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
            'choices': ["Government","Self-employed","Private","No Job"],
        },
        {
            'type': 'list',
            'name': 'Residence_type',
            'message':self.RESIDENCE_TYPE,
            'choices': ["Urban","Rural"],
        },
        {
        'type': 'list',
        'name': 'smoking_status',
        'message':self.SMOKER,
        'choices': ["Never","Formerly","Smokes"],
        }
        ]
        answers = prompt(questions, style=self.style)
        print('Data receipt:')
        pprint(answers)
        return (answers)

    def additional_questions(self):
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
            'name': 'weight',
            'message': self.PESO,
            'validate': HeightValidation,
        },
        {
            'type': 'input',
            'name': 'height',
            'message': self.ALTURA,
            'validate': WeightValidation,
        }
        ,
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
            'choices': ["Government","Self-employed","Private","No Job"],
        },
        {
            'type': 'list',
            'name': 'Residence_type',
            'message':self.RESIDENCE_TYPE,
            'choices': ["Urban","Rural"],
        },
        {
        'type': 'list',
        'name': 'smoking_status',
        'message':self.SMOKER,
        'choices': ["Never","Formerly","Smokes"],
        }
        ]
        answers = prompt(questions, style=self.style)
        print('Data receipt:')
        pprint(answers)
        return (answers)


