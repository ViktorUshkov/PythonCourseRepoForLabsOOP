import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
class PlayerInfo:
    def __init__(self, nickname: str, wins: int, loses: int):
        """
        Создание и подготовка к работе объекта "Информация об игроке"

        :param nickname: Никнейм игрока
        :param wins: Количество побед игрока
        :param loses: Количество поражений игрока

        Примеры:
        >>> new_player_info = PlayerInfo("something", 50, 20)
        """
        if not isinstance(nickname, str):
            raise TypeError("Никнейм игрока должен быть строкой (тип str)")
        self.nickname = nickname

        if not isinstance(wins, int):
            raise TypeError("Количество побед должно быть целым числом (тип int)")
        if wins < 0:
            raise ValueError("Количество побед не может быть отрицательным")
        self.wins = wins

        if not isinstance(loses, int):
            raise TypeError("Количество поражений должно быть целым числом (тип int)")
        if loses < 0:
            raise ValueError("Количество поражений не может быть отрицательным")
        self.loses = loses

    def change_nickname(self, new_nickname: str) -> None:
        """
        Функция, которая меняет никнейм игрока

        :param new_nickname: Новый никнейм игрока

        :raise TypeError: если новый никнейм не является строкой, вызываем ошибку

        Примеры:
        >>> new_player_info = PlayerInfo("something", 50, 20)
        >>> new_player_info.change_nickname("forsaken")
        """
        if not isinstance(new_nickname, str):
            raise TypeError
        ...

    def is_balance_positive(self) -> bool:
        """
        Функция, которая проверяет, является ли баланс побед и поражений игрока положительным

        :return: Является ли баланс побед и поражений положительным

        Примеры:
        >>> new_player_info = PlayerInfo("something", 50, 20)
        >>> new_player_info.is_balance_positive()
        """
        ...

    def update_stats(self, new_wins: int, new_loses: int) -> None:
        """
        Функция, которая обновляет статистику игрока после игровой сессии

        :param new_wins: Количество побед, которые нужно занести в статистику
        :param new_loses: Количество поражений, которые нужно занести в статистику

        :raise TypeError: Если количество побед или количество поражений не является целым числом, вызываем ошибку
        :raise ValueError: Если введено отрицательное количество побед или поражений, вызываем ошибку

        Примеры:
        >>> new_player_info = PlayerInfo("something", 50, 20)
        >>> new_player_info.update_stats(15, 5)
        """
        if not isinstance(new_wins, int):
            raise TypeError("Количество побед должно быть целым числом (тип int)")
        if new_wins < 0:
            raise ValueError("Количество побед не может быть отрицательным")

        if not isinstance(new_loses, int):
            raise TypeError("Количество поражений должно быть целым числом (тип int)")
        if new_loses < 0:
            raise ValueError("Количество поражений не может быть отрицательным")
        ...


class StudentPerformance:
    def __init__(self, name: str, grades: list[int]):
        """
        Создание и подготовка к работе объекта "Успеваемость студента"

        :param name: Имя студента
        :param grades: Список с оценками студента

        Примеры:
        >>> student = StudentPerformance("Иван Иванов", [4, 3, 4, 4, 2, 5, 4, 3])
        """
        if not isinstance(name, str):
            raise TypeError("Имя студента должно быть строкой (тип str)")
        self.name = name

        if not isinstance(grades, list):
            raise TypeError("Оценки студента должны быть переданы списком (тип list)")
        if not all(isinstance(grade, int) for grade in grades):
            raise TypeError("Оценки студента должны быть целыми числами (тип int)")
        if not all(2 <= grade <= 5 for grade in grades):
            raise ValueError("Оценки студента могут быть не меньше двойки и не больше пятёрки")
        self.grades = grades

    def calculate_mean_score(self) -> float:
        """
        Функция, вычисляющая средний балл студента по оценкам в списке grades

        :return: Средний балл студента

        Примеры:
        >>> student = StudentPerformance("Иван Иванов", [4, 3, 4, 4, 2, 5, 4, 3])
        >>> student.calculate_mean_score()
        """
        ...

    def has_failed_exams(self) -> bool:
        """
        Функция, которая проверяет, получал ли студент "неуд." (есть ли в grades хотя бы одно значение равное 2)

        :return: Получал ли студент "неуд."

        Примеры:
        >>> student = StudentPerformance("Иван Иванов", [4, 3, 4, 4, 2, 5, 4, 3])
        >>> student.has_failed_exams()
        """
        ...


class FootballClub:
    def __init__(self, squad: list[str], budget: float, points: int):
        """
        Создание и подготовка к работе объекта "Футбольный клуб"

        :param squad: Состав команды
        :param budget: Бюджет клуба
        :param points: Количество очков, набранное клубом в чемпионате

        Примеры:
        >>> real_madrid = FootballClub(["Куртуа", "Карвахаль", "Беллингем", "Винисиус"], 750000000.0, 91)
        """
        if not isinstance(squad, list):
            raise TypeError("Состав команды должен быть передан списком (тип list)")
        if not all(isinstance(player, str) for player in squad):
            raise TypeError("Имена игроков должны быть строками (тип str)")
        self.squad = squad

        if not isinstance(budget, (int, float)):
            raise TypeError("Бюджет клуба должен быть числом (int или float)")
        if budget < 0:
            raise ValueError("Бюджет клуба не может быть отрицательным")
        self.budget = budget

        if not isinstance(points, int):
            raise TypeError("Количество набранных очков должно быть целым числом (int)")
        if points < 0:
            raise ValueError("Количество очков не может быть отрицательным")
        self.points = points

    def buy_new_player(self, player: str, transfer_sum: float) -> None:
        """
        Покупка нового игрока в состав

        :param player: Игрок, которого покупает клуб
        :param transfer_sum: Сумма трансфера, отнимаемая от бюджета

        :raise TypeError: Если имя игрока не является строкой или сумма трансфера не является числом, вызываем ошибку
        :raise ValueError: Если сумма трансфера отрицательная или превышает оставшийся бюджет, вызываем ошибку

        Примеры:
        >>> real_madrid = FootballClub(["Куртуа", "Карвахаль", "Беллингем", "Винисиус"], 750000000.0, 91)
        >>> real_madrid.buy_new_player("Холанд", 100000000.0)
        """
        if not isinstance(player, str):
            raise TypeError("Имя игрока должно быть строкой (str)")
        if not isinstance(transfer_sum, (int, float)):
            raise TypeError("Сумма трансфера должна быть числом (int или float)")
        if transfer_sum < 0:
            raise ValueError("Сумма трансфера не может быть отрицательной")
        if transfer_sum > self.budget:
            raise ValueError("Сумма трансфера превышает оставшийся бюджет клуба")
        ...

    def sell_player(self, player: str, transfer_sum: float) -> None:
        """
        Продажа игрока в другой клуб

        :param player: Игрок, которого продаёт клуб
        :param transfer_sum: Сумма трансфера, добавляемая в бюджет

        :raise TypeError: Если имя игрока не является строкой или сумма трансфера не является числом, вызываем ошибку
        :raise ValueError: Если сумма трансфера отрицательная или переданного игрока нет в составе, вызываем ошибку

        Примеры:
        >>> real_madrid = FootballClub(["Куртуа", "Карвахаль", "Беллингем", "Винисиус"], 750000000.0, 91)
        >>> real_madrid.sell_player("Винисиус", 100000000.0)
        """
        if not isinstance(player, str):
            raise TypeError("Имя игрока должно быть строкой (str)")
        if not isinstance(transfer_sum, (int, float)):
            raise TypeError("Сумма трансфера должна быть числом (int или float)")
        if transfer_sum < 0:
            raise ValueError("Сумма трансфера не может быть отрицательной")
        if player not in self.squad:
            raise ValueError("Игрок, которого клуб пытается продать, не числится в составе")
        ...

    def get_points_for_match(self, points: int) -> None:
        """
        Функция, которая добавляет очки команде за успешный исход матча (3 за победу, 1 за ничью)

        :param points: Количество очков, заработанное командой в матче (3 или 1)

        :raise TypeError: Если количество очков не является целым числом, вызываем ошибку
        :raise ValueError: Если количество очков имеет значение отличное от 3 или от 1, вызываем ошибку

        Примеры:
        >>> real_madrid = FootballClub(["Куртуа", "Карвахаль", "Беллингем", "Винисиус"], 750000000.0, 91)
        >>> real_madrid.get_points_for_match(3)
        """
        if not isinstance(points, int):
            raise TypeError("Количество очков должно быть целым числом (int)")
        if points not in [1, 3]:
            raise ValueError("Команда может набрать либо 1 очко за ничью, либо 3 очка за победу")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
