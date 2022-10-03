import numpy as np 
import pandas as pd
import joblib as jb
## Todas los valores(correspondiente a cada una de las claves) del diccionario son de tipo string
## Este metodo transforma el tipo de dato de los valores del diccionario al tipo de dato segun el siguiente esquema
    #gender             object 
    #age                float64
    #hypertension       int64  
    #heart_disease      int64  
    #ever_married       object 
    #work_type          object 
    #Residence_type     object 
    #avg_glucose_level  float64
    #bmi                float64
    #smoking_status     object 
#gender ----- ['Male' 'Female']
#hypertension ----- [0 1]
#heart_disease ----- [1 0]
#ever_married ----- ['Yes' 'No']
#work_type ----- ['Private' 'Self-employed' 'Govt_job' 'children']
#Residence_type ----- ['Urban' 'Rural']
#smoking_status ----- ['formerly smoked' 'never smoked' 'smokes' 'Unknown']
#stroke ----- [1 0]

# retorna un dataframe intermedio
def procesing_dict(dictionary):
    integer_columns=["hypertension","heart_disease"]
    float_columns =["age","avg_glucose_level","weight","height"]

    for i in integer_columns:
        if  dictionary[i] == "Yes":
            dictionary[i] = "1"
        elif dictionary[i] == "No":
            dictionary[i] = "0"
    ## Conversion de values de string a numerico (int o float)  
    integer_columns=["hypertension","heart_disease"]
    float_columns =["age","avg_glucose_level","weight","height"]      
    for  i in integer_columns:
        dictionary[i] = int(dictionary[i])
    for  i in float_columns:
        dictionary[i] = float(dictionary[i])
    # Calculo de BMI en funcion de peso y altura
    dictionary["bmi"]= (dictionary["weight"] / (dictionary["height"]*dictionary["height"]))*100
    dictionary.pop("weight")
    dictionary.pop("height")

    # Convertir values de diccionario para que puedan ser interpretados durante la transformacion
    if dictionary["smoking_status"] == 'Formerly':
        dictionary["smoking_status"] ='formerly smoked'
    if dictionary["smoking_status"] == 'Never':
        dictionary["smoking_status"] ='never smoked'
    if dictionary["smoking_status"] == 'Smokes':
        dictionary["smoking_status"] ='smokes'
    
    if dictionary["work_type"] == 'Government':
        dictionary["work_type"] ='Govt_job'
    if dictionary["work_type"] == 'No Job':
        dictionary["work_type"] ='children'

    print(dictionary)
    return dictionary

def parse_object_dataframe(object):
    return pd.DataFrame([object])


def apply_transformer(df):
    # Transformaciones
    transfromer = jb.load('transformer_entrenado.pkl')
    df_transformed =transfromer.transform(df)
    return df_transformed
    
def predict_ictus(df_transformed):
    model = jb.load('modelo_entrenado.pkl')
    return (model.predict(df_transformed))