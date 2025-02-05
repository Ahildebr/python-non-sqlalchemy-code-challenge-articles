class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            self._title = "Title is invalid"
        Article.all.append(self)
        author._articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_value):
        pass

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_value):
        self._author = new_value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_value):
        self._magazine = new_value


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
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        cats = {article.magazine.category for article in self._articles}
        return list(cats) if cats else None


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value):
        if isinstance(new_value, str) and 2 <= len(new_value) <= 16:
            self._name = new_value
        else:
            pass

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_value):
        if isinstance(new_value, str) and len(new_value) > 0:
            self._category = new_value
        else:
            pass

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        counts = {}
        for article in self.articles():
            author = article.author
            counts[author] = counts.get(author, 0) + 1
        authors = [author for author, count in counts.items() if count > 2]
        return authors if authors else None