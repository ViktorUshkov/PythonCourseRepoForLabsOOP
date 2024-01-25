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

        :param id_: идентификатор книги (целое положительное число int)
        :param name: название книги (строка str)
        :param pages: количество страниц в книге (целое положительное число int)

        :raise TypeError: в случаях, если подается неверный тип данных для любого из параметров, вызываем ошибку
        :raise ValueError: если переданный идентификатор меньше или равен 0 или количество страниц меньше или равно
        0, вызываем ошибку
        """
        if not isinstance(id_, int):
            raise TypeError("Идентификатор должен быть типа int")
        if id_ <= 0:
            raise ValueError("Идентификатор описывается положительным числом")
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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
