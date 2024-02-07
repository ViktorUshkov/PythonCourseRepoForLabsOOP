"""
Система классов описывает персонажей в онлайн-игре. Класс Character является базовым и содержит атрибуты и методы,
присущие персонажам всех игровых ролей (такие как id, имя персонажа, опыт, здоровье, игровой уровень).

Классы Magician и Warrior описывают персонажей с ролями мага и воина, соответственно, для них существуют уникальные
атрибуты и методы, например: у мага есть мана и он может произносить заклинания, у воина - показатель выносливости
в бою и возможность наносить удары противнику и т.п.
"""


class Character:
    """ Базовый класс, описывающий персонажа онлайн-игры """

    """ Атрибуты класса, задающие начальные значения характеристик опыта, здоровья и уровня персонажа """
    START_XP = 0
    START_HP = 100
    START_LVL = 1
    
    """ Количество опыта, которое нужно заработать, чтобы перейти на следующий уровень """
    XP_TO_PROMOTE = 1000

    """ Величина, на которую увеличивается максимальное здоровье игрока после повышения на один уровень """
    BONUS_HP = 10

    def __init__(self, id_: int, name: str):
        """
        Инициализация класса Character. При вызове конструктора создаётся новый персонаж с переданными значениями
        id_ и name, а начальные значения опыта (xp), здоровья (hp) и уровня персонажа (lvl) ставятся по умолчанию
        Атрибуты xp, hp и lvl имеют целочисленный тип int. Для описания здоровья вводится два атрибута - текущее
        здоровье (current_hp) и максимальное здоровье (max_hp)

        :param id_: уникальный идентификатор игрока
        :param name: никнейм игрока
        """
        self._id_ = id_
        self.name = name
        self.xp = self.START_XP
        self.current_hp = self.START_HP
        self.max_hp = self.START_HP
        self.lvl = self.START_LVL

    def __str__(self) -> str:
        """ Магический метод str """
        return f'Персонаж {self.name} (id={self.id_}), роль: не выбрана'

    def __repr__(self) -> str:
        """ Магический метод repr """
        return f"{self.__class__.__name__}(id_={self.id_}, name={self.name!r})"

    def name_validation(self, name: str) -> bool:
        """
        Проводит валидацию никнейма на использование недопустимых символов, на соответствие этическим нормам и пр.

        :params name: имя, которое хочет установить игрок

        :return: True, если никнейм прошел валидацию (в ином случае вызывается соответствующая ошибка)
        """
        if not isinstance(name, str):
            raise TypeError("Никнейм должен быть строкового типа")
        """
        Далее можно реализовать дополнительные проверки: если никнейм не проходит какую-либо из них - вызываем ошибку.
        После всех успешных проверок возвращаем True
        """
        return True

    def int_values_validation(self, value: int) -> bool:
        """
        Проводит валидацию целочисленных значений, передаваемых при изменении целочисленных характеристик, таких как
        опыт (xp), здоровье (hp), уровень (lvl)
        Данный метод также может быть унаследован дочерними классами для валидации изменения специфических характеристик

        :params value: абсолютное значение, на которое изменяется характеристика

        :raise TypeError: Значение value должно иметь целочисленный тип данных
        :raise ValueErroe: Значение value должно быть положительным

        :return: True, если value прошло валидацию (в ином случае вызывается соответствующая ошибка)
        """
        if not isinstance(value, int):
            raise TypeError("Значение value должно быть типа int")
        if value <= 0:
            raise ValueError("Значение value должно быть положительным")
        return True

    """ Атрибут id не может изменяться, поэтому он непубличен и для него реализовано только getter-свойство"""
    @property
    def id_(self) -> int:
        """ Возвращает идентификатор игрока"""
        return self._id_

    """ 
    Игрок может пожелать изменить никнейм, но это должно быть проконтролировано системой, 
    поэтому для name реализуем getter и setter свойства с валидацией данных
    """
    @property
    def name(self) -> str:
        """ Возвращает никнейм игрока"""
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Устанавливает новый никнейм для игрока после валидации

        :param new_name: новый никнейм игрока
        """
        if self.name_validation(new_name):
            self._name = new_name

    def get_current_characteristics(self) -> str:
        """
        Возвращает f-строку с текущими значениями характеристик игрока

        :return: f-строка с характеристиками
        """
        return f'Уровень: {self.lvl}\nОпыт: {self.xp}\nЗдоровье: {self.current_hp}\n'

    def heal(self, healed_hp: int) -> None:
        """
        Симулирует восстановление здоровья на величину healed_hp. Если сумма текущего значения здоровья и
        восстанавливаемого больше максимально возможного, то в current_hp выставляется значение max_hp

        :param healed_hp: количество восстанавливаемого здоровья. Если healed_hp не целочисленное или меньше 0, то
                          healed_hp не пройдет валидацию в функции int_values_validation
        """
        if self.int_values_validation(healed_hp):
            if self.current_hp + healed_hp > self.max_hp:
                self.current_hp = self.max_hp
            else:
                self.current_hp += healed_hp

    def get_damage(self, damaged_hp: int) -> None:
        """
        Симулирует получение урона величиной damaged_hp. Если damaged_hp больше текущего значения здоровья, то
        персонаж погибает, вследствие чего печатается соответствующее сообщение и вызывается метод restart()

        :param damaged_hp: количество полученного урона. Если damaged_hp не целочисленное или меньше 0, то
                           damaged_hp не пройдет валидацию в функции int_values_validation
        """
        if self.int_values_validation(damaged_hp):
            if damaged_hp > self.current_hp:
                print("Ваш персонаж погиб. Игра начинается сначала.")
                self.restart()
            else:
                self.current_hp -= damaged_hp

    def get_xp(self, new_xp: int) -> None:
        """
        Получение опыта персонажем. Если кол-во опыта после получения превышает XP_TO_PROMOTE, то печатается сообщение
        о повышении уровня и вызывается метод level_up(). Новое текущее количество опыта рассчитывается, как остаток от
        целочисленного деления суммарного опыта на XP_TO_PROMOTE

        :param new_xp: количество полученного опыта. Если new_xp не целочисленное или меньше 0, то
                       new_xp не пройдет валидацию в функции int_values_validation
        """
        if self.int_values_validation(new_xp):
            if new_xp + self.xp >= self.XP_TO_PROMOTE:
                levels_to_promote = (new_xp + self.xp) // self.XP_TO_PROMOTE
                self.xp = (new_xp + self.xp) % self.XP_TO_PROMOTE
                print(f"Новый уровень! Вы достигли {self.lvl + levels_to_promote} уровня")
                self.level_up(levels_to_promote)
            else:
                self.xp += new_xp

    def level_up(self, levels_to_promote: int) -> None:
        """
        Повышение уровня игрока на levels_to_promote уровней: при повышении уровня увеличивается максимально возможное
        количество здоровья, а также текущее кол-во здоровья восстаналивается до максимального

        :param levels_to_promote: количество полученного опыта. Если levels_to_promote не целочисленное или меньше 0, то
                       levels_to_promote не пройдет валидацию в функции int_values_validation
        """
        if self.int_values_validation(levels_to_promote):
            self.lvl += levels_to_promote
            self.max_hp += self.BONUS_HP * levels_to_promote
            self.current_hp = self.max_hp

    def restart(self) -> None:
        """
        Рестарт игры после гибели персонажа - выставление начальных значений характеристик
        """
        self.xp = self.START_XP
        self.current_hp = self.START_HP
        self.max_hp = self.START_HP
        self.lvl = self.START_LVL


class Magician(Character):
    """ Класс, описывающий персонажа роли Маг """

    """ Атрибут класса, задающий начальное значение характеристики маны новому персонажу класса Маг """
    START_MANA = 100

    """ Величина, на которую увеличивается максимальная мана при повышении на один уровень """
    BONUS_MANA = 10

    """ Заклинания, которые может кастовать маг: ключи - названия заклинаний, значения - количество требуемой маны """
    SPELLS = {'Attack Spell': 30, 'Shield Spell': 20, 'Teleport Spell': 50}

    def __init__(self, id_: int, name: str):
        """
        Инициализация класса Magician. При вызове конструктора создаётся новый персонаж роли Magician.
        Основные характеристики инициализируются в конструкторе родительского класса, начальное значение атрибута mana
        (мана) ставится по умолчанию.
        Атрибут mana имеет целочисленный тип int. Для описания маны вводятся два атрибута - текущее количество
        маны (current_mana) и максимальное количество маны (max_mana)

        :param id_: уникальный идентификатор игрока
        :param name: никнейм игрока
        """
        super().__init__(id_=id_, name=name)
        self.current_mana = self.START_MANA
        self.max_mana = self.START_MANA

    def __str__(self) -> str:
        """ Магический метод str перегружаем, с добавлением информации о роли персонажа"""
        return f'Персонаж {self.name} (id={self.id_}), роль: {self.__class__.__name__}'

    """ 
    Магический метод repr можно унаследовать, так как для дочернего класса не передается никаких дополнительных
    обязательных аргументов
    """

    def get_current_characteristics(self) -> str:
        """
        Возвращает f-строку с текущими значениями характеристик игрока класса Маг

        :return: f-строка с характеристиками
        """
        return f'Уровень: {self.lvl}\nОпыт: {self.xp}\nЗдоровье: {self.current_hp}\nМана: {self.current_mana}\n'

    def restart(self) -> None:
        """
        Рестарт игры после гибели персонажа - выставление начальных значений характеристик.
        Для персонажа роли Magician также нужно выставить начальное значение маны.
        """
        super().restart()
        self.current_mana = self.START_MANA
        self.max_mana = self.START_MANA

    def level_up(self, levels_to_promote: int) -> None:
        """
        Повышение уровня игрока на levels_to_promote уровней: при повышении уровня увеличивается максимально возможное
        количество здоровья, а также текущее кол-во здоровья восстаналивается до максимального
        Перегрузка для класса Magician - аналогично здоровью, увеличивается максимальная мана и восстанавливается текущая

        :param levels_to_promote: количество полученного опыта. Если levels_to_promote не целочисленное или меньше 0, то
                       levels_to_promote не пройдет валидацию в функции int_values_validation
        """
        super().level_up(levels_to_promote)
        self.max_mana += self.BONUS_MANA * levels_to_promote
        self.current_mana = self.max_mana

    def cast_the_spell(self, spell: str) -> None:
        """
        Симулирует произнесение заклинания spell. Если spell есть в словаре заклинаний SPELLS, то у персонажа
        отнимается соответствующее количество маны.

        :param spell: заклинание, произносимое магом

        :raise ValueError: вызываем ошибку, если заклинания spell нет в словаре SPELLS или если текущее кол-во маны
                           меньше, чем значение в словаре SPELLS по ключу spell
        """
        if spell not in self.SPELLS.keys():
            raise ValueError("Такого заклинания не существует")
        if self.SPELLS[spell] > self.current_mana:
            raise ValueError("Недостаточно маны для заклинания")
        self.current_mana -= self.SPELLS[spell]


class Warrior(Character):
    """ Класс, описывающий персонажа роли Воин """

    """ Атрибут класса, задающий начальное значение характеристики выносливости новому персонажу класса Воин """
    START_STAMINA = 100

    """ Величина, на которую увеличивается максимальная выносливость при повышении на один уровень """
    BONUS_STAMINA = 10

    """ Удары, которые может наносить воин: ключи - тип удара, значения - количество требуемой выносливости """
    HITS = {'Light Hit': 15, 'Heavy Hit': 30, 'Ultimate Hit': 55}

    def __init__(self, id_: int, name: str):
        """
        Инициализация класса Warrior. При вызове конструктора создаётся новый персонаж роли Warrior.
        Основные характеристики инициализируются в конструкторе родительского класса, начальное значение атрибута
        stamina (выносливость) ставится по умолчанию.
        Атрибут stamina имеет целочисленный тип int. Для описания выносливости вводятся два атрибута - текущее кол-во
        выносливости (current_stamina) и максимальное количество выносливости (max_stamina)

        :param id_: уникальный идентификатор игрока
        :param name: никнейм игрока
        """
        super().__init__(id_=id_, name=name)
        self.current_stamina = self.START_STAMINA
        self.max_stamina = self.START_STAMINA

    def __str__(self) -> str:
        """ Магический метод str перегружаем, с добавлением информации о роли персонажа"""
        return f'Персонаж {self.name} (id={self.id_}), роль: {self.__class__.__name__}'

    """
    Магический метод repr можно унаследовать, так как для дочернего класса не передается никаких дополнительных
    обязательных аргументов
    """

    def get_current_characteristics(self) -> str:
        """
        Возвращает f-строку с текущими значениями характеристик игрока класса Воин.

        :return: f-строка с характеристиками
        """
        return f'Уровень: {self.lvl}\nОпыт: {self.xp}\nЗдоровье: {self.current_hp}\nВыносливость: {self.current_stamina}\n'

    def restart(self) -> None:
        """
        Рестарт игры после гибели персонажа - выставление начальных значений характеристик.
        Для персонажа роли Warrior также нужно выставить начальное значение выносливости.
        """
        super().restart()
        self.current_stamina = self.START_STAMINA
        self.max_stamina = self.START_STAMINA

    def level_up(self, levels_to_promote: int) -> None:
        """
        Повышение уровня игрока на levels_to_promote уровней: при повышении уровня увеличивается максимально возможное
        количество здоровья, а также текущее кол-во здоровья восстаналивается до максимального
        Перегрузка для класса Warrior - аналогично здоровью, увеличивается максимальная выносливость и восстанавливается текущая

        :param levels_to_promote: количество полученного опыта. Если levels_to_promote не целочисленное или меньше 0, то
                       levels_to_promote не пройдет валидацию в функции int_values_validation
        """
        super().level_up(levels_to_promote)
        self.max_stamina += self.BONUS_STAMINA * levels_to_promote
        self.current_stamina = self.max_stamina

    def hit_the_enemy(self, hit: str) -> None:
        """
        Симулирует нанесение удара типа hit. Если hit есть в словаре заклинаний HITS, то у персонажа
        отнимается соответствующее количество выносливости.

        :param hit: удар, наносимый воином

        :raise ValueError: вызываем ошибку, если удара hit нет в словаре HITS или если текущее кол-во выносливости
                           меньше, чем значение в словаре HITS по ключу hit
        """
        if hit not in self.HITS.keys():
            raise ValueError("Такого удара не существует")
        if self.HITS[hit] > self.current_stamina:
            raise ValueError("Недостаточно выносливости для удара")
        self.current_stamina -= self.HITS[hit]


if __name__ == "__main__":
    # Write your solution here
    new_character = Character(id_=53641, name="OnlineGamer31")
    print(new_character)
    print(repr(new_character))
    print(new_character.get_current_characteristics())
    new_character.get_damage(30)
    print(new_character.get_current_characteristics())
    new_character.heal(40)
    print(new_character.get_current_characteristics())
    new_character.get_xp(1250)
    print(new_character.get_current_characteristics())
    new_character.get_damage(120)
    print(new_character.get_current_characteristics())

    new_magician = Magician(id_=53642, name="MasterMerlin")
    print(new_magician)
    print(repr(new_magician))
    print(new_magician.get_current_characteristics())
    new_magician.get_damage(30)
    print(new_magician.get_current_characteristics())
    new_magician.heal(40)
    print(new_magician.get_current_characteristics())
    new_magician.cast_the_spell('Attack Spell')
    print(new_magician.get_current_characteristics())
    new_magician.get_xp(1250)
    print(new_magician.get_current_characteristics())
    new_magician.get_damage(120)
    print(new_magician.get_current_characteristics())

    new_warrior = Warrior(id_=53643, name="TrollSlayer")
    print(new_warrior)
    print(repr(new_warrior))
    print(new_warrior.get_current_characteristics())
    new_warrior.get_damage(30)
    print(new_warrior.get_current_characteristics())
    new_warrior.heal(40)
    print(new_warrior.get_current_characteristics())
    new_warrior.hit_the_enemy('Light Hit')
    print(new_warrior.get_current_characteristics())
    new_warrior.get_xp(1250)
    print(new_warrior.get_current_characteristics())
    new_warrior.get_damage(120)
    print(new_warrior.get_current_characteristics())
