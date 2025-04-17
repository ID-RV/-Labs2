from task import Account, BankAccount, Fraction

# TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
    # TODO: инстанцировать все описанные классы, создав три объекта.C()
    user1 = Account("89217778899", 19, "Fiodor")
    owner1 = BankAccount("Fiodor", 10000)
    frac1 = Fraction(8, 10)
    try:
        user1.new_username(10)
    # TODO: вызвать метод с некорректными аргументами(b)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        owner1.deposit("qwerty")
    # TODO: вызвать метод с некорректными аргументами(a)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        frac1.fract_multiplication("a", "a")
    # TODO: вызвать метод с некорректными аргументами(a)
    except TypeError:
        print('Ошибка: неправильные данные')
