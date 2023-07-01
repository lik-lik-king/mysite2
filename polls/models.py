import datetime
# We import models from django.db, this is needed to create our own models
from django.db import models
from django.utils import timezone
from django.contrib import admin
# A class in Python is like a blueprint or a template for creating objects. 
# Objects have characteristics and behaviors, which in the context of a class are called properties and methods respectively.
# Here we're defining a class, 'Question', which will represent the concept of a 'question' in our application.

# The syntax of 'models.Model' means that our 'Question' class is inheriting from 'models.Model'.
# In Python, inheritance is a way to form new classes using classes that have already been defined.
# The new classes, known as derived classes, inherit attributes and behavior of the existing classes, which are referred to as base classes.

# 'models.Model' is the base class provided by Django that represents a database table (model).
# So, when we're creating a class 'Question' that inherits from 'models.Model', 
# we're saying "Create a new type of model, called 'Question', that has all the capabilities of a standard Django model, 
# and some extra fields and behaviors that we're defining."
class Question(models.Model):
    
    # This is a field that stores a string of max 200 characters
    question_text = models.CharField(max_length=200)
    # This field, 'pub_date', is a DateTimeField, a special type of field provided by Django. 
# It is designed to store both a date and a time value together, allowing precise time tracking.
# In this specific model, 'pub_date' is intended to store the date and time when a particular question was published.
# This can be useful for various purposes such as tracking the age of the question or 
# for displaying the question's publication date to users for context.
    pub_date = models.DateTimeField('date published')
# This is a method within a Django model. A Django model is essentially your database table, and it contains the fields 
# and behaviors of the data that you will be storing. This method is named "__str__", which is a special method in Python 
# classes. When Python needs to convert an object into a string for whatever reason (for instance, for printing), it will 
# call this __str__ method. 
    def __str__(self):
       # self is a reference to the instance of the class. It's automatically passed as the first argument when you call a 
    # method on an object. For example, if you had an object q of type Question and you did q.__str__(), then q would be 
    # passed in as self.
    
    # self.question_text refers to the value of the field "question_text" in the current object (i.e., the specific 
    # instance of the model where this method is being called). We're simply returning this string value.

        return self.question_text
    
# Here we are defining another method within the same model. This method will be used to check whether the object (a 
# "Question", presumably) was published recently.

    def was_published_recently(self):
        # Again, self is a reference to the instance of the class. In this case, we're using it to access the pub_date field 
    # of the object.

    # timezone.now() gets the current date and time. This is a Django utility function.

    # datetime.timedelta(days=1) represents a duration of one day. datetime is a standard Python library for handling 
    # dates and times.

    # So, timezone.now() - datetime.timedelta(days=1) gets the date and time exactly one day before the current moment.

    # The >= operator checks if the date on the left is later than or the same as the date on the right.

    # Therefore, self.pub_date >= timezone.now() - datetime.timedelta(days=1) checks if the object's publication date 
    # is later than or the same as (i.e., is within) one day before the current moment.
    
    # If the publication date is within this range, it means the object was published recently. In this case, the method 
    # returns True; otherwise, it returns False.
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
#testing to see if the question was published recently

@admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

# Here we define another model named Choice
class Choice(models.Model):
    # This is a ForeignKey field, it links each Choice instance to a specific Question instance.
    # You can think of 'Question' as a blueprint and each 'question' as an individual item built from that blueprint.
    # For example, if 'Question' is 'trivia question', then a 'question' could be 'What is the capital of France?'.
    # Hence, this field allows us to link multiple choices (like 'Paris', 'London', 'Rome') to one question.
    # The on_delete parameter specifies what to do when the referenced question is deleted. 
    # models.CASCADE means the choice will be deleted too (i.e., "cascade" the deletion).
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # This field is for the choice text, which is a string of max 200 characters
    choice_text = models.CharField(max_length=200)
    # This field is for the number of votes this choice received.
    # It's an integer field and defaults to 0 when a choice is first created.
    votes = models.IntegerField(default=0)

# This is a method within a Django model. A Django model is essentially your database table, and it contains the fields 
# and behaviors of the data that you will be storing. This method is named "__str__", which is a special method in Python 
# classes. When Python needs to convert an object into a string for whatever reason (for instance, for printing), it will 
# call this __str__ method.
    def __str__(self):
        # self is a reference to the instance of the class. It's automatically passed as the first argument when you call a 
    # method on an object. For example, if you had an object c of type Choice and you did c.__str__(), then c would be 
    # passed in as self.
    
    # self.choice_text refers to the value of the field "choice_text" in the current object (i.e., the specific 
    # instance of the model where this method is being called). We're simply returning this string value.
        return self.choice_text
