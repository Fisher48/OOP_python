from pymonad.maybe import Just, Nothing
from pymonad.tools import curry


# посадка птиц на левую сторону
@curry(2)
def to_left(num, state):
    l, r = state
    if abs((l + num) - r) > 4:
        return Nothing
    return Just((l + num, r))


# посадка птиц на правую сторону
@curry(2)
def to_right(num, state):
    l, r = state
    if abs((r + num) - l) > 4:
        return Nothing
    return Just((l, r + num))


# банановая кожура
def banana(_):
    return Nothing


# отображение результата
def show(maybe):
    if maybe == Nothing:
        print('Упал')
    else:
        l, r = maybe.value
        print(f"Слева: {l} Справа: {r}")


# начальное состояние
def begin():
    return Just((0, 0))


show(begin().bind(to_left(2)).bind(to_right(5)).bind(to_left(-2)))  # канатоходец упадёт тут
show(begin().bind(to_left(2)).bind(to_right(5)).bind(to_left(-1)))  # в данном случае всё ок
show(begin().bind(to_left(2)).bind(banana).bind(to_right(5)).bind(to_left(-1)))  # кожура всё испортит
