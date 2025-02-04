class Article:

    all = []

    def __init__(self, author, magazine, title):
        self._author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        if isinstance(self._title, str) and 4 < len(self._title) < 51:
            return self._title
        else:
            return "Title is invalid"

    @property
    def author(self):
        if isinstance(self._author, Author):
            return self._author
        else:
            return "Author is invalid"
    
    @author.setter
    def author(self, new_value):
        self._author = new_value

    @title.setter
    def title(self, new_value):
        pass

   
    

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = name 
        self.articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value):
        pass

    def articles(self):
        if isinstance(self.articles, Article):
            return self.articles
        else:
            return "No articles found"
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass