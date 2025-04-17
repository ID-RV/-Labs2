BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    },
]


# TODO: написать класс Book
class Book:
    def __init__(self, id_, name, pages):
        """
        Создание и подготовка к работе объекта "Книга"

        :param id_: id книги
        :param name: название книги
        :param pages: количество страниц
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id}, name=\'{self.name}\', pages={self.pages})'


# TODO: написать класс Library
class Library:
    def __init__(self, books: list = None):
        """
        Создание и подготовка к работе объекта "Библиотека"

        :param books: список книг в библиотеке
        """
        self.books = books if books is not None else []

    def get_next_book_id(self):
        """
        Функция которая возвращает индекс для добавления новой книги
        """
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        """
        Функция которая возвращает индекс книги в списке

        :param book_id: id книги
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()
    print(empty_library.get_next_book_id())

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())
    print(library_with_books.get_index_by_book_id(1))
