# TODO: описать базовый класс
class Manager:
    """
    Базовый класс для всех менеджеров

    Атрибуты:
        salary(float): зарплата
        working_schedule: график работы
    """

    def __init__(self, salary: float, working_schedule: str):
        if not isinstance(salary, (str, float)):
            raise TypeError("Зарплата должна быть типа int или float")
        if salary <= 0:
            raise ValueError("Зарплата должна быть больше нуля")
        self.salary = salary
        if not isinstance(working_schedule, str):
            raise TypeError("График быть быть типа str")
        self.working_schedule = working_schedule

    def __str__(self) -> str:
        return f"{self.salary} {self.working_schedule} "

    def __repr__(self) -> str:

        return f"Manager(salary='{self.salary}', working_schedule='{self.working_schedule}'"

    def monthly_earnings(self) -> str:
        """
        Показывает стандартный доход менеджера за месяц

        :return: Строку с зарплатой менеджера за месяц
        """
        return f'Заработок менеджера за месяц {self.salary}'


# TODO: описать дочерний класс
class Person(Manager):
    """
    Дочерний класс для конкретного менеджера

    Атрибуты:
        salary(float): зарплата
        working_schedule: график работы
        name: имя менеджера
    """

    def __int__(self, salary: float, working_schedule: str, name: str):
        super().__init__(salary, working_schedule)
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        self.name = name

    def __str__(self) -> str:
        return f"{self.name} {self.salary} {self.working_schedule} "

    def give_bonus(self, bonus: float) -> None:
        """
        Выписывает премию менеджеру
        """
        if not isinstance(bonus, (float, int)):
            raise TypeError("Сумма премии должна быть больше нуля")
        if bonus < 0:
            raise ValueError("Премия не может быть отрицательной")
        self.salary += bonus

    def monthly_earnings(self) -> str:
        """
        Перегрузка метода доход за месяц
        Этот метод отличается от базовых верси для других менеджеров

        :return: Строку с зарплатой конкретного менеджера за месяц
        """
        return f'Заработок менеджера {self.name} за месяц {self.salary}'
