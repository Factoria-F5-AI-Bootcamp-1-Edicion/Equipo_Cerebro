
from data_model import Person
import pandas as pd

class crudDataFrame():
    def create(self,df,path) -> str:
        df.to_csv(path)

    def read(self,path) -> dict:
        pass
    
    def update(self,df,path):
        try:
            data = pd.read_csv(path)
            ## TODO: CONCATENAR DATAFRAME
        except Exception:
            self.create(df,path)


    def delete(self):
        pass
    
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