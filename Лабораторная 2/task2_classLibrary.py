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
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Класс для описания книги

        :param id_: идентификатор книги (целое число int)
        :param name: название книги (строка str)
        :param pages: количество страниц в книге (целое положительное число int)

        :raise TypeError: в случаях, если подается неверный тип данных для любого из параметров, вызываем ошибку
        :raise ValueError: если количество страниц меньше или равно 0, вызываем ошибку
        """
        if not isinstance(id_, int):
            raise TypeError("Идентификатор должен быть типа int")
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self.pages = pages

    def __str__(self) -> str:
        """
        Магический метод __str__ - определяет поведение функции str(), вызванной для экземпляра класса
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Магический метод __repr__ - определяет поведение функции repr(), вызванной для экземпляра класса
        """
        return f'{self.__class__.__name__}(id_={self.id_}, name={self.name!r}, pages={self.pages})'


# TODO написать класс Library
class Library:
    def __init__(self, books: list[Book] = None):
        """
        Класс, описывающий библиотеку

        :param books: список книг в библиотеке (list объектов класса Book)

        :raise TypeError: если передан не список или какой-либо из элементов списка не является экземпляром класса Book,
        вызываем ошибку
        """
        if books is not None:
            if not isinstance(books, list):
                raise TypeError("Список книг должен быть типа list")
            if not all(isinstance(book, Book) for book in books):
                raise TypeError("Книги должны быть экземплярами класса Book")
        self.books = books or []

    def get_next_book_id(self) -> int:
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку

        :return: 1, если книг в библиотеке нет,
        в ином случае - идентификатор последней книги, увеличенный на 1
        """
        if not self.books:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса

        :params book_id: идентификатор искомой книги

        :return: индекс книги с переданным идентификатором в списке books

        :raise TypeError: если переданный идентификатор не является объектом типа int, вызываем ошибку
        :raise ValueError: в случае, если книги с переданным идентификатором нет в списке, вызываем ошибку
        """
        if not isinstance(book_id, int):
            raise TypeError("Передаваемый идентификатор должен быть типа int")
        if book_id not in [book.id_ for book in self.books]:
            raise ValueError("Книги с таким идентификатором нет в библиотеке")

        for index, book in enumerate(self.books):
            if book.id_ == book_id:
                return index


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
