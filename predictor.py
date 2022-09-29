from colorama import init, Back, Fore
import curses

from processing_data import preprocessing_columns,procesing_dict,parse_object_dataframe, transformn_data
from crudDataFrame import crudDataFrame
from data_input import Enter_data


def predictor():
    menu = Enter_data()
    menu.show_title("Welcome to Stroke predictor CLI")
    dict_answer = menu.user_input()
    dict_answer=procesing_dict(dict_answer)
    df = parse_object_dataframe(dict_answer)

    ## TODO: preprocesado de datos resultante del eda
    

    ## TODO : 2º preprocesado

    ## TODO : Modelo predictor (REcibe dataframe y devuelve)
        
        ## TODO: DataFrame --> modelo --> variable target (ictus : 0 | 1) --> Resultado convertirlo a string legible para usuario 

    ## Guardado
    crudDF=crudDataFrame()
    crudDF.create(df)
    ## person=createPerson(dictionary) --> Para Base de datos



if __name__ == '__main__':
    main()