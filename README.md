# Smart-Library
A project which aims at automating the Library Management System using IoT. The system will be used to borrow, return, and maintain the backend information. 

# Components involved in this project:
1. Python documentation tool - Sphinx
2. Unit Testing using Python
3. Socket Programming
4. self developed API using Python's microframework Flask
5. AI features (facial recognition, object detection, voice detection)
6. Agile methodology

# Hardware involved
There are 2 Raspberry Pi's that are used extensively in this project. One is called the Reception Pi and the other Master Pi.
Reception Pi: Used by library user once arrived at the reception, hence the name. Provides the user with a console-based application that allows them to login and register. Further,
      i. search for book within the catalogue using ISBN/Author name/Book name.
      ii. option for borrowing a book/books.
      iii. option for returning a book/books.
      iv. safe logout

Master Pi: There's only one admin for simplicity. This Pi runs that website application with admin priveleges to the cloud environment namely, the Google's GCP IoT platform.
    Admin website makes use of an API to
      i. Add books to catalogue.
      ii. Remove books.
      iii. Generate visualization reports.

# Software
 i.  Console Application - This application is basically the communication medium between Reception Pi and Master Pi.
 
 ii. Flask Admin Panel - This is for the Librarian in concept with priveleges that a normal library user would not have. Such as
            adding/removing a book.

# Files
1. add_event.py	     for google calendar event.
2. analytics.py	     data visualisation code.
3. authentication.py	     authenticates user login from Reception Pi to Master Pi.
4. client_io.py	     pass connection object that can be used for RPi to MPi communcations.
5. client_menu.py	     display available options to the user while interacting with the RPi.
6. database.py	           Database operations are carried out here.
7. server_on_MasterPi.py  Server that is listening to communication from Reception Pi.



# High Level Architecture Diagram

![alt text](https://github.com/jaitjacob/Smart-Library/blob/master/architecture.JPG)

