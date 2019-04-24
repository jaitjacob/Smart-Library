# Smart-Library
An attempt at automating the Library Management System using IoT. The system will be used to borrow, return, and maintain the backend information. 

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
