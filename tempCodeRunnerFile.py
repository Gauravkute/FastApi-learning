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

from pydantic import BaseModel

class Patient(BaseModel):
    name:str
    age:str

def insert_patient_data(patinet:Patient):
    print(patinet.name)
    print(patinet.age)
    print('inserted into database')

patient_info = {'name':'yash','age':29}

patient1 = Patient(**patient_info)

insert_patient_data('patient1')