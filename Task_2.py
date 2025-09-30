# Задание Дополните два класса, которые вы спроектировали в предыдущем задании, методами, подходящими для логики
# работы с ними. В каждом классе должно быть не менее трёх методов. Добавьте в каждый класс конструктор. Если
# предыдущий вариант оказался не очень удачным (так как вы создавали классы, исходя из списка их атрибутов),
# придумайте новые классы. Создайте несколько объектов этих классов, по вызывайте их методы, выведите вычисляемые с
# помощью методов значения на экран.

CREATE = 0
RUN = 1
STAND = 2


class Warrior:
    def __init__(self, new_name, new_health, new_strength, new_speed):
        self.name = new_name  # имя
        self.health = new_health  # здоровье
        self.strength = new_strength  # сила
        self.speed = new_speed  # скорость
        self.state = CREATE  # 0 - Создан, 1 - Идёт, 2 - Стоит

    def move(self, new_speed):
        self.speed = new_speed
        self.state = RUN

    def stop(self):
        self.speed = 0
        self.state = STAND

    def increase_strength(self, value):
        self.strength += value


class Dwarf:
    def __init__(self, new_name, new_health, new_strength, new_stamina, new_speed):
        self.name = new_name  # имя
        self.health = new_health  # здоровье
        self.strength = new_strength  # сила
        self.stamina = new_stamina  # мана
        self.speed = new_speed  # скорость
        self.state = CREATE  # 0 - Создан, 1 - Идёт, 2 - Стоит

    def move(self, new_speed):
        self.speed = new_speed
        self.state = RUN

    def stop(self):
        self.speed = 0
        self.state = STAND

    def increase_strength(self, value):
        self.strength += value

    def increase_stamina(self, value):
        self.stamina += value


class Weapon:
    def __init__(self, new_title, new_damage, new_rate):
        self.title = new_title  # название оружия
        self.damage = new_damage  # урон
        self.rate = new_rate  # индекс увеличения силы

    def upgrade(self, new_damage):
        self.damage += new_damage


class Clothes:
    def __init__(self, new_title, new_armor, new_magic_defence):
        self.title = new_title  # название одежды
        self.armor = new_armor  # броня
        self.magic_defence = new_magic_defence  # маг. защита

    def upgrade(self, new_armor):
        self.armor += new_armor


dwarf1 = Dwarf("Гном", 500, 10, 50.0, 0)
warrior1 = Warrior("Воин", 1000, 40, 0)
elbow = Weapon("Лук", 200, 2.0)
helmet = Clothes("Шлем", 100, 50)

print(f"Нач. выносливость гнома - {dwarf1.stamina}")
dwarf1.increase_stamina(20.0)
print(f"После повышения у гнома - {dwarf1.stamina}")


print(f"{warrior1.name} скорость: {warrior1.speed} Состояние: {warrior1.state}")
warrior1.move(200)
print(f"{warrior1.name} скорость: {warrior1.speed} Состояние: {warrior1.state}")

print(f"{elbow.title} урон: {elbow.damage}")
elbow.upgrade(100)
print(f"После вызова метода улучшения - {elbow.title} урон: {elbow.damage}")
