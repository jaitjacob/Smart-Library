class Book:
    """This class defines a Book object."""
    def __init__(self, bookid: int, title: str, author: str, publisheddate: str):
        self.bookid = bookid
        self.title = title
        self.author = author
        self.publisheddate = publisheddate

    def get_bookid(self):
        """This method grabs and returns the unique ID of a book."""
        return self.bookid

    def get_title(self):
        """This method grabs and returns the title of a book."""
        return self.title

    def get_author(self):
        """This method grabs and returns the author of a book."""
        return self.author

    def get_publisheddate(self):
        """This method grabs and returns the published data of a book."""
        return self.publisheddate
