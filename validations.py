from PyInquirer import Validator, ValidationError

AGE_LIMIT =[0,99]
GLUCOSE_LIMIT =[0,300]
BMI_LIMIT =[0,100]

class AgeValidation(Validator):
     def validate(self, document):
        validator = invalid_inputs()
        try:
            value = int(document.text)
            if validator.is_numeric_invalid(value,AGE_LIMIT[0],AGE_LIMIT[1]) :
                messager = validator.verify_message("age")
                raise ValidationError(
                message=messager,
                cursor_position=len(document.text))  # Move cursor to end
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end

class GlucoseValidation(Validator):
     def validate(self, document):
        validator = invalid_inputs()
        try:
            value = int(document.text)
            if validator.is_numeric_invalid(value,GLUCOSE_LIMIT[0],GLUCOSE_LIMIT[1]) :
                messager = validator.verify_message("avg_glucose_level")
                raise ValidationError(
                message=messager,
                cursor_position=len(document.text))  # Move cursor to end
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end

class BmiValidation(Validator):
    def validate(self, document):
        validator = invalid_inputs()
        try:
            value = int(document.text)
            if validator.is_numeric_invalid(value,BMI_LIMIT[0],BMI_LIMIT[1]) :
                messager = validator.verify_message("bmi")
                raise ValidationError(
                message=messager,
                cursor_position=len(document.text))  # Move cursor to end
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end

class invalid_inputs():

    def is_numeric_invalid(self,data,min,max):
        return (int(data) < min or int(data) > max)
            
    def verify_message(self,type):
        message = ""
        if str(type)== "age" :
            message = (f'You must enter a number between {AGE_LIMIT[0]} and {AGE_LIMIT[1]}')
        elif str(type)== "avg_glucose_level" :
            message = (f'You must enter a number between {GLUCOSE_LIMIT[0]} and {GLUCOSE_LIMIT[1]}')
        elif str(type) == "bmi" :
            message = (f'You must enter a number between {BMI_LIMIT[0]} and {BMI_LIMIT[1]}')
        return message
    


            
