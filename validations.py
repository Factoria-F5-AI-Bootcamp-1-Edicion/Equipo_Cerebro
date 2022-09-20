from colorama import init, Back, Fore

print(Back.LIGHTBLUE_EX)
print(Fore.RED)

class Validation():
    dictionary= {}
    def __init__(self) -> None:
        self.dictionary= {}
    
    def is_numeric(self,data,str,min,max):
        while not data.isnumeric():
            data = input(str)
        while int(data) < min or int(data) > max:
            print(f'You must enter a number between {min} and {max}')
            data = input(str)
        print()
        return data
    def is_categorical(self,data,str,list_values):
        while data not in list_values :
            print("Insert the following options: ", list_values)
            data = input(str)
        print()
        return data

    def input_validation(self,type, str):
        if type == "age":
            age= input(str)
            age = self.is_numeric(age,str,0,99)
            self.dictionary["age"]= age
        elif type== "gender":
            gender= input(str)
            gender = gender.lower()
            gender = self.is_categorical(gender,str,["male","female"])
            self.dictionary["gender"]= gender
        elif type== "hypertension":
            hypertension= input(str)
            hypertension = hypertension.lower()
            hypertension = self.is_categorical(hypertension,str,["yes","no"])
            self.dictionary["hypertension"]= hypertension
        elif type== "heart_disease":
            heart_disease= input(str)
            heart_disease = heart_disease.lower()
            heart_disease = self.is_categorical(heart_disease,str,["yes","no"])
            self.dictionary["heart_disease"]= heart_disease
        elif type== "ever_married":
            ever_married= input(str)
            ever_married = ever_married.lower()
            ever_married = self.is_categorical(ever_married,str,["yes","no"])
            self.dictionary["ever_married"]= ever_married
        elif type== "work_type":
            work_type= input(str)
            work_type = work_type.lower()
            work_type = self.is_categorical(work_type,str,["government","self-employed","private","children"]) 
            self.dictionary["work_type"]= work_type
        elif type== "Residence_type":
            Residence_type= input(str)
            Residence_type = Residence_type.lower()
            Residence_type = self.is_categorical(Residence_type,str,["urban","rural"]) 
            self.dictionary["Residence_type"]= Residence_type
        elif type== "avg_glucose_level":
            avg_glucose_level= input(str)
            avg_glucose_level = self.is_numeric(avg_glucose_level,str,0,300)
            self.dictionary["avg_glucose_level"]= avg_glucose_level
        elif type== "smoking_status":
            smoking_status= input(str)
            smoking_status = smoking_status.lower()
            smoking_status = self.is_categorical(smoking_status,str,["never","unknown","formerly","smokes"])
            self.dictionary["smoking_status"]= smoking_status
        elif type == "bmi":
            bmi= input(str)
            bmi = self.is_numeric(bmi,str,0,100)
            self.dictionary["bmi"]= bmi
        print()
    def get_dictionary(self):
        return self.dictionary



            
