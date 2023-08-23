from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str
    email: str = 'email@domain.com'
    password: str
    age: int


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
u1 = User(first_name="Ada", last_name="Lovelace", password="adalve123", age=34)
print(u1)
