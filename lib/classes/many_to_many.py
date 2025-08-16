class Article:
    all = []
    def __init__(self, author, magazine, title):
        # Validate author
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        # Validate magazine
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")
        # Validate title
        if not isinstance(title, str):
            raise Exception("title must be a string")
        if not (5 <= len(title) <= 50):
            raise Exception("title must be between 5 and 50 characters")
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise Exception("title is immutable")
    # Removed all() static method; use Article.all directly

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an Author instance")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("magazine must be a Magazine instance")
        self._magazine = value
        

class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("name must be a string")
        if len(name) == 0:
            raise Exception("name must be longer than 0 characters")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise Exception("name is immutable")


    def articles(self):
        # Return all Article instances for this author
        return [article for article in Article.all if article.author == self]


    def magazines(self):
        # Unique list of Magazine instances for this author
        return list({article.magazine for article in self.articles()})


    def add_article(self, magazine, title):
        # Create and return a new Article instance
        return Article(self, magazine, title)


    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        return list({mag.category for mag in mags})


class Magazine:
    def __init__(self, name, category):
        # Validate name
        if not isinstance(name, str):
            raise Exception("name must be a string")
        if not (2 <= len(name) <= 16):
            raise Exception("name must be between 2 and 16 characters")
        # Validate category
        if not isinstance(category, str):
            raise Exception("category must be a string")
        if len(category) == 0:
            raise Exception("category must be longer than 0 characters")
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("name must be a string")
        if not (2 <= len(value) <= 16):
            raise Exception("name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("category must be a string")
        if len(value) == 0:
            raise Exception("category must be longer than 0 characters")
        self._category = value


    def articles(self):
        # Return all Article instances for this magazine
        return [article for article in Article.all if article.magazine == self]


    def contributors(self):
        # Unique list of Author instances who have written for this magazine
        return list({article.author for article in self.articles()})


    def article_titles(self):
        arts = self.articles()
        if not arts:
            return None
        return [article.title for article in arts]


    def contributing_authors(self):
        from collections import Counter
        authors = [article.author for article in self.articles()]
        count = Counter(authors)
        result = [author for author, num in count.items() if num > 2]
        return result if result else None
    @classmethod
    def top_publisher(cls):
        # Return the Magazine instance with the most articles
        if not Article.all:
            return None
        from collections import Counter
        mags = [article.magazine for article in Article.all]
        if not mags:
            return None
        count = Counter(mags)
        return count.most_common(1)[0][0]