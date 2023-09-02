
# class User(BaseModel):
#     first_name: str
#     last_name: str
#     email: str = 'email@domain.com'
#     password: str
#     age: int


user1 ={
  "first_name": "Emilee",
  "last_name": "Seckington",
  "email": "eseckington0@biblegateway.com",
  "password": "eleifend",
  "age": 27
}
user2 = {
  "first_name": "Cathryn",
  "last_name": "Hars",
  "email": "chars1@psu.edu",
  "password": "venenatis",
  "age": 23
}
user3 ={
  "first_name": "Anjela",
  "last_name": "Squeers",
  "email": "asqueers2@g.co",
  "password": "integer",
  "age": 55
}
user4 ={
  "first_name": "Lisette",
  "last_name": "McClure",
  "email": "lmcclure3@yale.edu",
  "password": "eleifend donec",
  "age": 52
}
user5= {
  "first_name": "Mirella",
  "last_name": "Salisbury",
  "email": "msalisbury4@washingtonpost.com",
  "password": "mattis egestas",
  "age": 64
}
from typing import Optional
# class User(BaseModel):
#     first_name: Optional[str] = None
#     last_name: Optional[str] = None 
#     email: Optional[str] = None
#     password: Optional[str] = None
#     age: Optional[int] = None
# u1 = User(first_name="Ada", last_name="Lovelace", password="adalve123", age=34)
# print(u1)

from datetime import datetime, timedelta, date
from pydantic import BaseModel,constr,conint,condate,FieldValidationInfo,field_validator,ValidationError

class User(BaseModel):
   
    first_name: constr(min_length=2,max_length=20) # length constrains added
    last_name: constr(min_length=2,max_length=20) # length constrains added
    email: constr(min_length=8,max_length=50) # length constrains added
    password: constr(min_length=9,max_length=50) # length constrains added
    age: conint(strict=True,gt=14,le=70) # range constrains added

    @field_validator('first_name','last_name')
    @classmethod
    def validate_name(cls, value, info:FieldValidationInfo):
        if re.findall(r'\d',value):
            raise ValidationError('Name must not contain a number')
        if re.findall(r'\W',value):
            raise ValidationError('Name must not contain special character')
        return value.title()
    
    @field_validator('password')
    @classmethod
    def validate_password(cls, value):
        if not re.findall(r'\d',value):
            raise ValidationError('Password must contain a number')
        if not re.findall(r'\W',value):
            raise ValidationError('Password must contain a special character')
        if not re.findall(r'[A-Z]',value):
            raise ValidationError('Password must contain a capital letter')
        if not re.findall(r'[a-z]',value):
            raise ValidationError('Password must contain a lowercase letter')
        return value
  
    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
      mailregex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
      if re.fullmatch(mailregex,value):
         return value.lower()
      raise ValidationError("Error in the email entered")


    
u1 = User(first_name="lorem", last_name="Lovelace",email="gAdalve4@gmail.com",password="#A123456789a", age=70 ,date=date(2023,9,2))
print(u1)


