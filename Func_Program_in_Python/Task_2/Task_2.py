from pymonad.tools import curry


# 2.3.1.
@curry(2)
def concat(greeting: str, name: str):
    return greeting + name


def f(name: str):
    return concat('Hello ', name)


print(f('Ivan'))


# 2.3.2.
# Необходимо чтобы последним параметром, был тот параметр, который будет задаваться
@curry(4)
def first_step(word: str, begin_mark: str, end_mark: str, name: str):
    return word + begin_mark + name + end_mark


final = first_step("Hello")(", ")("!")
print(final("Sergey"))