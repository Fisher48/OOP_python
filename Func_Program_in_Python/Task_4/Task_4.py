from pymonad.maybe import Just, Nothing
from pymonad.tools import curry
from pymonad.list import ListMonad


@curry(2)
def add(x, y):
    return x + y


def add10(value):
    return value.then(add(10))


addNumber = add10(Just(10))
addNothing = add10(Nothing)
addList = add10(ListMonad(1, 5, 10))

print(addNumber)
print(addNothing)
print(addList)
