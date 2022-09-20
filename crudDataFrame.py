
from data_model import Person
import pandas as pd

class crudDataFrame():
    def create(self,df) -> str:
        df.to_csv("db_person.csv")

    def read(self,data) -> dict:
        """Extract text from the currently loaded file."""
        pass
    
    def update(self):
        pass
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