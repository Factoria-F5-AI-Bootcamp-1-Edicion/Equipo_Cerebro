from colorama import init, Back, Fore
import curses
import sklearn

from processing_data import apply_transformer,procesing_dict,parse_object_dataframe, predict_ictus
from crudDataFrame import crudDataFrame
from data_input import Enter_data


def predictor():
    ## Peticion de datos del usuario (Variables independientes o predictoras)
    menu = Enter_data()
    menu.show_title("Welcome to Stroke predictor CLI")
    dict_answer = menu.user_input()
    
    

    ##  Preprocesado (Conversion de valores, casteo de tipo de datos)
    dict_answer=procesing_dict(dict_answer)

    # Conversion de diccionario a dataframe
    df = parse_object_dataframe(dict_answer)

    # Aplicar transformador a columnas del dataframe y predecir variable target (Riesgo de ictus)
    y = predict_ictus(apply_transformer(df))

    # Formatear salida por consola
    if y == 1:
        ictus = "Tienes riesgo de padecer ictus"
    else:
        ictus = "No ienes riesgo de padecer ictus"
    print(ictus)
    



    ## TODO : Modelo predictor (REcibe dataframe y devuelve)
        
        ## TODO: DataFrame --> modelo --> variable target (ictus : 0 | 1) --> Resultado convertirlo a string legible para usuario 

    ## Guardado
    crudDF=crudDataFrame()
    crudDF.create(df)
    ## person=createPerson(dictionary) --> Para Base de datos
if __name__ == '__main__':
    predictor()

