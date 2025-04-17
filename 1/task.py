import re
import doctest


# TODO: Подробно описать три произвольных класса


# TODO: описать класс
class Account:
    def __init__(self, number: str, age: int, username: str):
        '''
        Создание и подготовка к работе объекта "Аккаунт"

        :param number: Номер телефона
        :param age: Возраст
        :param username: Имя пользователя

        Пример:
        >>> user1 = Account("89217778899", 19, "Fiodor")
        '''
        if re.fullmatch(re.compile(r'8\d{10}'), number) or (re.fullmatch(re.compile(r'[+][7]\d{10}'), number)):
            self.number = number
        else:
            raise TypeError('Номер введен не корректно')

        if not isinstance(age, int):
            raise TypeError("Год рождения должен быть типа int")
        if age < 0:
            raise ValueError("Введен некорректный возраст")
        self.age = age

        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть типа str")
        if len(username) == 0:
            raise ValueError("Имя пользователя должно содержать хотябы 1 символ")
        self.username = username

    def user_information(self) -> str:
        '''

        Функция которая возвращает информацию об аккаунте

        :return:Имя пользователя: Fiodor, телефон: 89217778899, возраст: 19

        Пример:
        >>> user1 = Account("89217778899", 19, "Fiodor")
        >>> info = user1.user_information()
        '''
        return f'Имя пользователя: {self.username}, телефон: {self.number}, возраст: {self.age}'

    def new_username(self, new_name: str = 'user123') -> None:
        '''

        Смена имени пользователя

        :param new_name: Новое имя пользователя (по умолчанию "user123")

        :raise TypeError: Если новое имя пользователя не является строкой, то вызываем ошибку

        Пример:
        >>> user1 = Account("89217778899", 19, "Fiodor")
        >>> user1.new_username()
        '''
        if not isinstance(new_name, str):
            raise TypeError("Имя пользователя должно быть типа str")
        self.username = new_name


# TODO: описать ещё класс
class BankAccount:
    def __init__(self, owner_name: str, balance: float):
        '''

        Создание и подготовка к работе объекта "Банковский счет"

        :param owner_name: Имя владельца счета
        :param balance: Сумма денег на счете

        Пример:
        >>> owner1 = BankAccount("Fiodor", 10000)
        '''
        if not isinstance(owner_name, str):
            raise TypeError("Имя должно быть быть типа str")
        self.owner_name = owner_name

        if not isinstance(balance, (int, float)):
            raise TypeError("баланс должен быть тип int или float")
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.balance = balance

    def show_balance(self) -> str:
        '''

        Функция которая возвращает имя владельца и баланс его счета

        :return: Имя владельца: Fiodor, Баланс: 10000

        Пример:
        >>> owner1 = BankAccount("Fiodor", 10000)
        '''
        return f'Имя владельца: {self.owner_name}, Баланс: {self.balance}'

    def deposit(self, deposit_sum: float = 100) -> None:
        '''

        Пополнение счета

        :param deposit_sum: сумма депозита (по умолчанию равна 100)

        :raise TypeError: Если сумма депозита не является числом, то вызываем ошибку
        :raise ValueError: Если сумма депозита меньше 100, то вызываем ошибку

        Пример:
        >>> owner1 = BankAccount("Fiodor", 10000)
        >>> owner1.deposit(5000)
        '''
        if not isinstance(deposit_sum, (int, float)):
            raise TypeError("Сумма депозита должна быть числом")
        if deposit_sum < 100:
            raise ValueError("Сумма депозита не должна быть меньше 100 ")
        self.balance += deposit_sum

    def withdrawal(self, cash_sum: float = 100) -> None:
        '''

        Вывод денег со счета

        :param cash_sum: Сумма вывода

        :raise TypeError: Если сумма вывода не является числом, то вызываем ошибку
        :raise ValueError: Если сумма вывода больше чем есть на балансе или меньше 100, то вызываем ошибку

        Пример:
        >>> owner1 = BankAccount("Fiodor", 10000)
        >>> owner1.withdrawal(3000)
        '''
        if not isinstance(cash_sum, (int, float)):
            raise TypeError("Сумма вывода должна быть числом")
        if cash_sum > self.balance:
            raise ValueError("Невозможно снять больше чем есть на счете")
        if cash_sum < 100:
            raise ValueError("Минимальна сумма вывода должна быть не меньше 100 ")
        self.balance -= cash_sum


# TODO: и ещё один
class Fraction:
    def __init__(self, num: int, den: int):
        '''

        Создание и подготовка к работе объекта "Дробь"

        :param num: Числиитель дроби
        :param den: Знаменатель дроби

        Пример:
        >>> frac1 = Fraction(8, 10)
        '''
        if not isinstance(num, int):
            raise TypeError("Числитель должен быть типа int")
        self.num = num

        if not isinstance(den, int):
            raise TypeError("Знаменатель должен быть типа int")
        if den == 0:
            raise ValueError("Знаменатель не может быть равен нулю")
        self.den = den

    def decimalization(self) -> float:
        '''

        Преревод из обыкновенной дроби в десятичную

        :return: Десятичную дробь

        Пример:
        >>> frac1 = Fraction(8, 10)
        '''
        return self.num / self.den

    def fract_multiplication(self, num1: int = 1, den1: int = 1) -> str:
        '''

        Перемножение обыкновенных дробей

        :param num1: Числитель второй дроби
        :param den1: Знаменатель второй дроби

        :raise TypeError: Если числитель или знаменатель не являются целым числом, то вызываем исключение
        :raise ValueError: Если знаменатель равен нулю, то вызываем исключение

        :return: Обыкновенную дробь

        Пример:
        >>> frac1 = Fraction(8, 10)
        >>> frac = frac1.fract_multiplication(8, 10)
        '''
        if not isinstance(num1, int):
            raise TypeError("Числитель второй дроби должен быть типа int")

        if not isinstance(den1, int):
            raise TypeError("Знаменатель второй дроби должен быть типа int")
        if den1 == 0:
            raise ValueError("Знаменатель второй дроби не может быть равен нулю")

        return f'{self.num * num1}/{self.den * den1}'


if __name__ == "__main__":
    doctest.testmod()
