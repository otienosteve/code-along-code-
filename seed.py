from faker import Faker
from faker.providers import DynamicProvider
from models import session, Student, BioData,Payment,Class, student_class
from random import randint


religion_provider = DynamicProvider(
     provider_name="religion",
     elements=["Christianity", "Muslim", "Jew", "Atheist", "Buddhism"],
)
nationality_provider = DynamicProvider(
     provider_name="nationality",
     elements=["Kenyan", "Ugandan", "Rwandese", "Tanzanian" ],
)
highschool_grade = DynamicProvider(
     provider_name="grade",
     elements=["A", "A-", "B+", "B","B-",'C+',"C","C-","D+","D","D-","E"],
)
class_names= DynamicProvider(
    provider_name="class_data",
    elements = ['Information Literacy',"Computing Fundamentals","Financial Literacy","Accounting", "Programming fundamentals",
                "Communication Skils","Hiv/Aids Literacy"]
)



faker = Faker()


faker.add_provider(religion_provider)
faker.add_provider(nationality_provider)
faker.add_provider(highschool_grade)
faker.add_provider(class_names)

students =[]


# for i in range(10):
#     student =Student(
#         first_name = faker.first_name(),
#         last_name = faker.last_name(),
#         age = randint(16,35),
#         home_town = faker.street_name()
#     )
#     students.append(student)
# session.bulk_save_objects(students)
# session.commit()

students = session.query(Student).all()

for i in range(19):
    biodata = BioData(aspiration=faker.job(),religion=faker.religion(),nationality=faker.nationality(),highschool=faker.grade())
    biodata.student = students[i]
    session.add(biodata)
    session.commit()

# for i in range(19):
#     payment = Payment(amount=float(faker.pricetag().replace('$','').replace(',','')),description='tution')
#     payment.student=students[i]
#     session.add(payment)
#     session.commit()

# for i in range(40):
#     class_data=Class(name=faker.class_data())
#     class_data.students.append(students[randint(0,18)])
#     session.add(class_data)
#     session.commit()

