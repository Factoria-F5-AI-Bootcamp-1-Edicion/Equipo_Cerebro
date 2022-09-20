from marshmallow import Schema, fields, validate, ValidationError

AGE_MIN = 1

class Person(Schema):
    age = fields.Integer(validate=validate.Range(min=1,max= 99))
    gender = fields.Str(validate=validate.Regexp("/^(male|female)*$"))
    hypertension = fields.Integer(validate=validate.Regexp("[0-1]"))
    heart_disease = fields.Integer(validate=validate.Regexp("[0-1]"))
    ever_married = fields.Integer(validate=validate.Regexp("/^(0-)*$"))
    work_type = fields.Str(validate=validate.Regexp("/^(Private|Self-employed|children|Govt_job)*$"))
    residence_type= fields.Str(validate=validate.Regexp("/^(Urban|Rural)*$"))
    avg_glucose_level = fields.Integer(validate=validate.Range(min=0))
    bmi = fields.Integer(validate=validate.Range(min=0))
    smoking_status= fields.Str(validate=validate.Regexp("/^(never |formerly| smokes | Unknow)*$"))

    def __init__(self) -> None:
        self.age = 0
        self.gender =''
        self.hypertension= 0
        self.heart_disease= ''
        self.ever_married =''
        self.work_type=''
        self.residence_type=''
        self.avg_glucose_level = 0
        self.bmi = 0
        self.smoking_status =''

    ## SETTERS
    def set_age(self,age):
        self.age= age
    def set_gender(self,gender):
        self.gender =gender
    def set_hypertension(self,hyper):
        self.hypertension=hyper
    def set_heart(self,disease):
        self.heart_disease= disease
    def set_married(self,married):
        self.ever_married =married
    def set_work(self,work_type):
        self.work_type= work_type
    def set_residence_type(self,residence_type):
        self.residence_type = residence_type
    def set_glucose(self,glucose_level):
        self.avg_glucose_level = glucose_level
    def set_bmi(self,bmi):
         self.bmi = bmi
    def set_smoking(self,smoker):
        self.smoking_status = smoker
    ## GETTERS
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def get_hypertension(self):
        return self.hypertension
    def get_heart(self):
        return self.heart_disease
    def get_married(self):
        return self.ever_married 
    def get_work(self):
        return self.work_type
    def get_residence_type(self):
        return self.residence_type
    def get_glucose(self):
        return self.avg_glucose_level
    def get_bmi(self):
         return self.bmi
    def get_smoking(self):
        return self.smoking_status
    def __str__(self):
        return ('Edad:' +str(self.age) + ' Gender:' + str(self.gender) + ' Hypertension:' +  str(self.hypertension) + ' Heart disease:' + str(self.heart_disease) + ' Married:' + str(self.ever_married) + ' Work_type:' + str(self.work_type) + ' residence type:' + str(self.residence_type) + ' glucose level:'+  str(self.avg_glucose_level) + ' bmi:'+str(self.bmi)+' smoker: '+str(self.smoking_status))