from pymonad.tools import curry
from pymonad.state import State

game_state = State.insert([])

@curry(2)
def take_damage(damage, log):
    def computation(hp):
        return log + [f"Получил урон: {damage}"], hp - damage
    return State(computation)

@curry(2)
def heal(amount, log):
    def computation(hp):
        return log + [f"Вылечился: {amount}"], hp + amount
    return State(computation)

@curry(2)
def trap(damage, log):
    def computation(hp):
        return log + [f"Ловушка! -{damage} HP"], hp - damage
    return State(computation)

adventure = game_state.then(take_damage(20)).then(heal(10)).then(trap(15)).then(heal(5))
result = adventure.run(100)

print(result)


