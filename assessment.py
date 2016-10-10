"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

    Encapsulation:
    where the complexity of the created object is hidden. It helps us understand what
    the function for that class does easily wihtout having to look at all the 
    code and keeps our code for that object simple. An analogy would be knowing how to 
    drive a car without knowing how it works. 

    Abstraction:
    It refers to presenting essential features without including 
    the background details or specifcs.

    Polymorphism:
    Creating a function with the same name that can execute different functions
    depending on the class.

2. What is a class?
    A class is like a module you can call with the (dot) operator. you can group
    together a bunch of functions (or methods) and data and then you can access them.


3. What is an instance attribute?
    When you instantiate the class by calling the function you are creating as
    an instance attribute. while class attributes belong to the class, instance 
    attributes belong the instance specifcially.

4. What is a method?
    a funtion that is defined in eht class definition

5. What is an instance in object orientation?
    a specifc object of a class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   While class attributes belong to the class, instance 
   attributes belong the instance specifcially. The visual difference is that
   when you are calling the class attribute you are using self (self.attribute) and when you call the 
   instance you replace self with the name of the instance (instance_name.attribute).


"""


# Parts 2 through 5:
class Student(object):
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def show_question(self, question, correct_answer):
        print self.question,
        answer = raw_input("Enter answer here:")
        return self.correct_answer == answer



class Exam(object):
  
    def __init__(self, name):
        self.name = name
        self.question = []

    def add_question(self, question, correct_answer):
        new_question = (question, correct_answer)
        self.question.append(new_question)

    def admin(self, question, score):
        score = 0
        for question in Question:
            if question.show_question == True:
                score = score + 1
                return score



        