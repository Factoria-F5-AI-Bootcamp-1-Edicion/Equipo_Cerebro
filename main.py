import click
from colorama import init, Back, Fore

from data_model import Person
from validations import Validation
from processing_data import preprocessing_columns,procesing_dict,parse_object_dataframe, transformn_data
from crudDataFrame import crudDataFrame

## Instancia de colorama
init()

AGE_MIN = 1
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



inputs_list = [AGE, GENDER, HYPER,HEART_DISEASE,MARRIED,WORK_TYPE,RESIDENCE_TYPE,GLUCOSE_LEVEL,BMI,SMOKER]
lista_res=["age","gender","hypertension","heart_disease","ever_married","work_type","Residence_type","avg_glucose_level","bmi","smoking_status","stroke"]

validator = Validation()


dictionary={}
def inputs_user():
    
    for index,input_data in enumerate(inputs_list):
        validator.input_validation(lista_res[index], input_data)
    return validator.get_dictionary()

def createPerson(dictionary):
        person = Person()
        person.set_age(dictionary["age"])
        person.set_bmi(dictionary["bmi"])
        person.set_gender(dictionary["gender"])
        person.set_glucose(dictionary["avg_glucose_level"])
        person.set_hypertension(dictionary["hypertension"])
        person.set_heart(dictionary["heart_disease"])
        person.set_married(dictionary["ever_married"])
        return (person)
@click.command()
def main():
    ## TODO : MENU
    
    dictionary =inputs_user()
    dictionary=procesing_dict(dictionary)
    df = parse_object_dataframe(dictionary)


    
    ## TODO: preprocesado de datos resultante del eda

    ## TODO : 2º preprocesado

    ## TODO : Modelo predictor (REcibe dataframe y devuelve)

    ## Guardado
    crudDF=crudDataFrame()
    crudDF.create(df)
    ## person=createPerson(dictionary) --> Para Base de datos



if __name__ == '__main__':
    main()