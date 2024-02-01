class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
        Инициализация класса книги

        :param name: название книги
        :param author: автор книги

        :raise TypeError: если name или author не являются типом str, вызываем ошибку
        """
        if not isinstance(name, str):
            raise TypeError("Название книги должно иметь строковый тип")
        self._name = name

        if not isinstance(author, str):
            raise TypeError("Имя автора должно иметь строковый тип")
        self._author = author

    """
    Так как атрибуты name и author не могут изменяться, то следует написать для них
    только getter-свойства - таким образом атрибуты будут доступны только на чтение и пользователь
    не сможет изменить их значение
    """
    @property
    def name(self) -> str:
        """
        Возвращает название книги
        """
        return self._name

    @property
    def author(self) -> str:
        """
        Возвращает автора книги
        """
        return self._author

    def __str__(self):
        return f"Книга '{self.name}'. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс бумажной книги, унаследованный от класса книги """
    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализация класса бумажной книги

        :param name: название книги
        :param author: автор книги
        :param pages: количество страниц
        """
        super().__init__(name=name, author=author)
        self.pages = pages

    """
    Так как на pages накладываются ограничения по типу и допустимым значениям, для него стоит написать
    setter-свойство с валидацией данных (и, соответственно, getter-свойство)
    """
    @property
    def pages(self) -> int:
        """
        Возвращает количество страниц печатной книги
        """
        return self._pages

    @pages.setter
    def pages(self, set_pages: int) -> None:
        """
        Устанавливает значение кол-ва страниц после валидации данных pages

        :param set_pages: количество страниц, которое следует установить

        :raise TypeError: если set_pages не является типом int, вызываем ошибку
        :raise ValueError: если set_pages <= 0, вызываем ошибку
        """
        if not isinstance(set_pages, int):
            raise TypeError("Количество страниц должно быть целочисленным (тип int)")
        if set_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = set_pages

    """ 
    Исходя из кода, для дочерних классов при вызове __str__ результат вывода не меняется, 
    (выводим только автора и название), поэтому метод __str__ можно унаследовать от базового 
    
    Метод __repr__ следует перегрузить, с учетом добавления атрибута pages
    """
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """ Дочерний класс аудиокниги, унаследованный от класса книги """
    def __init__(self, name: str, author: str, duration: float):
        """
        Инициализация класса аудиокниги

        :param name: название книги
        :param author: автор книги
        :param duration: длительность аудиокниги
        """
        super().__init__(name=name, author=author)
        self.duration = duration

    """
    Так как на duration накладываются ограничения по типу и допустимым значениям, для него стоит написать
    setter-свойство с валидацией данных (и, соответственно, getter-свойство)
    """
    @property
    def duration(self) -> float:
        """
        Возвращает длительность аудиокниги
        """
        return self._duration

    @duration.setter
    def duration(self, set_duration: float) -> None:
        """
        Устанавливает значение кол-ва страниц после валидации данных duration

        :param set_duration: длительность аудиокниги, которую следует установить

        :raise TypeError: если set_duration не является типом float или int, вызываем ошибку
        :raise ValueError: если set_duration <= 0, вызываем ошибку
        """
        if not isinstance(set_duration, (int, float)):
            raise TypeError("Длительность аудиокниги должна быть числом (типы float или int)")
        if set_duration <= 0:
            raise ValueError("Длительность аудиокниги должна быть положительной")
        self._duration = set_duration

    """ 
    Исходя из кода, для дочерних классов при вызове __str__ результат вывода не меняется 
    (выводим только автора и название), поэтому метод __str__ можно унаследовать от базового
    
    Метод __repr__ следует перегрузить, с учетом добавления атрибута duration
    """
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


if __name__ == '__main__':
    book = Book(name='Евгений Онегин', author='А.С.Пушкин')
    print(book)
    print(repr(book))

    paper_book = PaperBook(name='Евгений Онегин', author='А.С.Пушкин', pages=500)
    print(paper_book)
    print(repr(paper_book))

    audio_book = AudioBook(name='Евгений Онегин', author='А.С.Пушкин', duration=3.96)
    print(audio_book)
    print(repr(audio_book))
