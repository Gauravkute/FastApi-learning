# def insert_patient_data(name:str,age:int):
#     if type(name)==str and type(age)==int:
#         if age<0:
#             raise ValueError('Age cant be Negative')
#         print(name)
#         print(age)
#         print('inserted into database')
#     else:
#         raise TypeError('Incorrect data type')
    
# insert_patient_data('nitish',9)

from pydantic import (BaseModel , 
                      EmailStr ,
                      AnyUrl,
                      Field,
                      field_validator,
                      model_validator,
                      computed_field
)
from typing import List , Dict , Optional , Annotated

class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):

    # name:str = Field(max_length=50)
    name:Annotated[str,Field(max_length=50,title='Name of the Patient',
                   description='Give the name of patient in less than 50 chars',
                   examples=['Nitish','Amit'])]
    age:int = Field(gt=0,lt=120)
    email: EmailStr
    Linkedin_url:AnyUrl
    # weight:float = Field(gt=0,lt=150)
    weight: Annotated[float,Field(gt=0,strict=True)]
    height:Annotated[float,Field(gt=0,strict=True)]
    married:bool = False
    # allergies:Optional[List[str]] = Field(max_length=5)
    allergies:Annotated[Optional[List[str]],Field(max_length=5)] = None
    contact_details: Dict[str,str]
    address:Address

    address_dict={'city':'mumbai','state':'maharastra','pin':'345'}
    addess1 = Address(**address_dict)

    patient_dict={}

    @model_validator(mode='after')
    def validate_emergency_contact(model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient is older than 60 mush have an emergency contact')
        return model

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icici.com']
        domain_name=value.split('@')[-1].lower()

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value

    @field_validator('name')
    @classmethod
    def transfrom_name(cls,value):
        return value.upper()

    @field_validator('age',mode='after')
    @classmethod
    def validate_age(cls,value):
        if 0<value<120:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')


    @computed_field
    @property
    def calculate_bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age) 
    print(patient.email)
    print(patient.allergies)
    print(patient.married)
    print(patient.weight)
    print('BMI ',patient.calculate_bmi)
    print(patient.height)
    print(patient.contact_details)
    print('inserted into database')

patient_info = {'name':'yash',
                'age':'99',
                'email':'yash@hdfc.com',
                'weight':56.7,
                'height':1.76,
                'married':True,
                'Linkedin_url':'https://linkedin.com/in/yash',
                'allergies':['pollen','dust'],
                'contact_details':{'phone':'7637283928','emergency':'123456789'}
                }

patient1 = Patient(**patient_info)

insert_patient_data(patient1)