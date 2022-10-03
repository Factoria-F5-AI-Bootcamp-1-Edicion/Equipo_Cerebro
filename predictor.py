from colorama import init, Back, Fore
import sklearn
import os
import curses

from processing_data import apply_transformer,procesing_dict,parse_object_dataframe, predict_ictus
from crudDataFrame import crudDataFrame
from data_input import Enter_data
import time

## Rutas de Archivos de datasets
PATH_MAIN ="db_predictions.csv"
PATH_SECONDARY="db_additional.csv"

## Metodo que muestra mensaje en box de una nueva ventana 
def show_result(title,result,dictio):
    time.sleep(5)
    os.system('cls')   
    print()
    curses.initscr()
    win = curses.newwin(5, 40, 10, 20)
    win.box()
    win.move(0, 3)
    win.addstr(title)
    win.move(1, 1)
    print()
    win.addstr(result)
    win.addstr("\n")
    win.addstr("\n")
    win.addstr("Press any key to continue")
    
    win.getch()
    curses.endwin()
def predictor():
    print("\033[2J\033[1;1f") 

    ################################################################################################################################
    ###                                                                                                                         ####
    ### Predictor -->  SOLICITUD DE PREGUNTAS DE USUARIO                                                                          ####
    ###                                                                                                                         ####
    ################################################################################################################################
    ## Peticion de datos del usuario (Variables independientes o predictoras)
    menu = Enter_data()
    menu.show_title("Welcome to Stroke predictor CLI")
    dict_answer = menu.user_input()
    
    ################################################################################################################################
    ###                                                                                                                         ####
    ### DataFrame --> Transformer --> modelo --> variable target (ictus : 0 | 1) --> Resultado convertirlo a string legible para usuario        ####
    ###                                                                                                                         ####
    ################################################################################################################################
    
    #  Preprocesado (Conversion de valores, casteo de tipo de datos)
    dict_answer=procesing_dict(dict_answer)
    # Conversion de diccionario a dataframe
    df = parse_object_dataframe(dict_answer)

    # Aplicar transformador a columnas del dataframe y predecir variable target (Riesgo de ictus)
    y = predict_ictus(apply_transformer(df))
    
    
    # Formatear salida del modelo(prediccion) por consola
    if int(y) == 1:
        ictus = "Tienes riesgo de padecer ictus"
    elif int(y) ==0:
        ictus = "No tienes riesgo de padecer ictus"
    

    show_result('Resultado:',ictus,dict_answer)

    # Preguntas adicionales (Voluntario)
    dict_answer_additonal =menu.additional_questions()

    # Agrego prediccion a dataframe a guardar
    df["ictus"] = y

     # TODO: PROBAR CORRECTO GUARDADO (AGREGAR CONCATENACION EN METODO UPDATE DE CLASE CRUDDATAFRAME)
    ################################################################################################################
    ####        PERSISTENCIA DE INFORMACION DE USUARIO  --> 2 archivos como medio de persistencia:          ########
    ####           1)Respuestas basicas + prediccion --> archivo csv                                        ########
    ####           2)Respuestas basicas + prediccion + Respuestas complementarias --> archivo csv           ########
    ################################################################################################################
    crudDF=crudDataFrame()
    # Guardar Dataframe con preguntas y prediccion , actualizando dataset existente
    crudDF.update(df,PATH_MAIN)
    # Guardar Dataframe (preguntas adicionales + basicas +prediccion), actualizando dataset existente
    if dict_answer_additonal != None:
        # Unir dos diccionarios (Respuestas basicas + adicionales)
        df_additional = parse_object_dataframe(dict_answer_additonal)
        df_additional["ictus"] = y
        crudDF.update(df_additional,PATH_SECONDARY)
    
if __name__ == '__main__':
    predictor()


