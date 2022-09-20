import numpy as np 
import pandas as pd

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

# retorna un dataframe intermedio
def procesing_dict(dictionary):
    integer_columns=["hypertension","heart_disease","ever_married"]
    float_columns =["age","avg_glucose_level","bmi"]
    union=integer_columns
    union.extend(float_columns)
    for i in union:
        if  dictionary[i] == "yes":
            dictionary[i] = "1"
        elif dictionary[i] == "no":
            dictionary[i] = "0"
        if  i in integer_columns:
            dictionary[i] = int(dictionary[i])
        if  i in float_columns:
            dictionary[i] = float(dictionary[i])
    return dictionary

def parse_object_dataframe(object):
    return pd.DataFrame([object])


def preprocessing_columns(df):
    # Transformaciones resultantes del EDA
    df = df.age.round()
    numericas = ["age", "avg_glucose_level" , "bmi"]
    binarias = ["gender", "hypertension", "heart_disease"  , "ever_married" , "Residence_type" ]
    
def transformn_data():
    ## Aplicar OneHotEncoder y MinMaxScaler
    pass