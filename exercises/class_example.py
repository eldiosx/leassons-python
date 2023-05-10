"""
implement the Person, Student and Teacher class in the way
you deem most convenient. Implement a small test program.

This code implements the classes Person, Student, and Teacher,
with an introduce() method that returns a string with information about the person.
An instance of each class is then created and the introduce() 
method is called to print its information.
"""

#create class Person
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.segender = gender

    def introduce(self):
        return "Hello, my name is " + self.name

#create class Student
class Student(Person):
    def __init__(self, name, age, gender, course):
        super().__init__(name, age, gender)
        self.course = course

    def introduce(self):
        return super().introduce() + " and I'm a student of " + self.course

#create class Teacher
class Teacher(Person):
    def __init__(self, name, age, gender, specialty):
        super().__init__(name, age, gender)
        self.specialty = specialty

    def introduce(self):
        return super().introduce() + " and I'm a teacher of " + self.specialty


person = Person("John", 30, "Male")
#print by console
print(person.introduce())

student = Student("Ana", 20, "Female", "Programming")
#print by console
print(student.introduce())

teacher = Teacher("Peter", 40, "Male", "Math")
#print by console
print(teacher.introduce())
