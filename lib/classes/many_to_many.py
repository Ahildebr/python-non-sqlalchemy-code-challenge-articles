class Article:

    all = []

    def __init__(self, author, magazine, title):
        self._author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)
        author._articles.append(self)

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
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = name 
        self._articles = []
        Author.all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_value):
        pass

    def articles(self):
        return self._articles

    def magazines(self):
        unique_magazines = []
        for article in self._articles:
            if article.magazine not in unique_magazines:
                unique_magazines.append(article.magazine)
        return unique_magazines

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = {article.magazine.category for article in self._articles}
        return list(categories) if categories else None

class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        counts = {}
        for article in self.articles():
            author = article.author
            if author in counts:
                counts[author] += 1
            else:
                counts[author] = 1
        authors = [author for author, count in counts.items() if count > 2]
        return authors if authors else None