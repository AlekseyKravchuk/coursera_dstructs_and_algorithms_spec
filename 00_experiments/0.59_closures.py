# Closures (Замыкания)
# Замыкание - это внутренняя функция, которая возвращается из внешней и использует переменные из области видимости
# внешней функции.
# Каждое замыкание хранит своё состояние. Т.о. замыкания не пересекаются.
# Основное преимущество: Замыкание хранит своё состояние и с этим состоянием можно работать ТОЛЬКО через интерфейс,
# предоставляемый этим замыканием (внутренней функцией).
def names():
    all_names = []

    def inner(name: str) -> list:
        all_names.append(name)
        return all_names

    return inner


def average():
    values = []

    def inner(value: int) -> float:
        values.append(value)
        return sum(values)/len(values)

    return inner


def counter():
    count = 0

    def inner(value: int) -> int:
        nonlocal count
        count += value
        return count

    return inner


# def pow_(power):
#
#     def inner(base):
#         return base**power
#
#     return inner

def power_(power):
    return lambda value: value**power


if __name__ == '__main__':
    # boys = names()
    #
    # boys('Vasya')
    # print(boys.__closure__[0].cell_contents)

    # p = pow_(2)
    # print(p(5))

    # p = power_(2)
    # print(p(5))
    # print(p(6))
    boys = names()
    boys('Vasya')
    boys('Dmitry')
    print(type(boys.__closure__))
    print(len(boys.__closure__))
    print(f'closure info: {boys.__closure__}')
    print(boys.__closure__[0].cell_contents)
