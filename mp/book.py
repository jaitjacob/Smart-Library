
class Book:
    def __init__(self, bookid: int, title: str, author: str, publisheddate: str):
        self.bookid = bookid
        self.title = title
        self.author = author
        self.publisheddate = publisheddate

    def get_bookid(self):
        return self.bookid

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_publisheddate(self):
        return self.publisheddate
