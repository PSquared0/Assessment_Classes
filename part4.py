from assessment import Exam
from assessment import Student
from assessment import Question

def take_test(exam, student):
    score =  exam.admin()
    student.score = score

    return score

def example():

    exam = Exam()

    exam.add_question("What are the basic Concepts of OOPs?","Abstraction,Encapsulation, Inheritance, Polymorphism.") 

    exam.add_question("What is a blueprint for a software object is called?","A Class")
    
    exam.add_question("What is an object","They are instance of classes")   

# take_test(exam, student)