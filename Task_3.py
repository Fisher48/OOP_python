# 1. Разделите видимость полей (сделайте все поля приватными) и методов во всех классах вашей программы.
#
# 2. Постройте две небольшие и косвенно логически связанные иерархии классов в вашей программе (например, Животное -
# Кот/Собака, и Переноска животных - Сумка для котика/Чемодан для собаки). Не выдумывайте никакие абстрактные
# сущности, только запутаетесь. Возьмите простые физические вещи, например, автомобиль и двигатель, тарелка и еда,
# кошелёк и деньги и т. п. У родительского класса в каждой иерархии должно быть не менее двух наследников. В каждом
# дочернем классе должно быть не менее двух оригинальных методов, характеризующих уникальность этих классов,
# их отличие от родительского.

CREATE = 0
RUN = 1
STAND = 2


class Person:
    def __init__(self, new_name, new_health, new_strength, new_speed):
        self.__name = new_name  # имя
        self.__health = new_health  # здоровье
        self.__strength = new_strength  # сила
        self.__speed = new_speed  # скорость
        self.__state = CREATE  # 0 - Создан, 1 - Идёт, 2 - Стоит

    def set_strength(self, new_strength):
        self.__strength = new_strength

    def set_health(self, new_health):
        self.__health = new_health

    def set_name(self, new_name):
        self.__name = new_name

    def set_speed(self, new_speed):
        self.__speed = new_speed

    def set_state(self, new_state):
        self.__state = new_state

    def get_strength(self):
        return self.__strength

    def get_health(self):
        return self.__health

    def get_name(self):
        return self.__name

    def get_speed(self):
        return self.__speed

    def get_state(self):
        return self.__state

    def move(self, new_speed):
        self.__speed = new_speed
        self.__state = RUN

    def stop(self):
        self.__speed = 0
        self.__state = STAND


class Warrior(Person):
    def __init__(self, new_name, new_health, new_strength, new_speed, new_stamina):
        super().__init__(new_name, new_health, new_strength, new_speed)
        self.__stamina = new_stamina  # Выносливость

    def set_stamina(self, new_stamina):
        self.__stamina = new_stamina

    def get_stamina(self):
        return self.__stamina


class Mage(Person):
    def __init__(self, new_name, new_health, new_strength, new_speed, new_mana):
        super().__init__(new_name, new_health, new_strength, new_speed)
        self.__mana = new_mana  # Мана

    def set_mana(self, value):
        self.__mana = value

    def get_mana(self):
        return self.__mana

    def spelling(self, spell):
        if spell == "Frost":
            print("Mage attack - " + spell)
        if spell == "Fire":
            print("Mage attack - " + spell)
        else:
            print("Unknown attack")


class Weapon:
    def __init__(self, new_title, new_damage, new_rate):
        self.__title = new_title  # название оружия
        self.__damage = new_damage  # урон
        self.__rate = new_rate  # индекс увеличения силы

    def get_title(self):
        return self.__title

    def get_damage(self):
        return self.__damage

    def get_rate(self):
        return self.__rate

    def set_title(self, new_title):
        self.__title = new_title

    def set_rate(self, value):
        if value > 0:
            self.__rate = value

    def set_damage(self, new_damage):
        if new_damage > 0:
            self.__damage += new_damage


class Elbow(Weapon):
    def __init__(self, new_title, new_damage, new_rate, new_accuracy):
        super().__init__(new_title, new_damage, new_rate)
        self.__accuracy = new_accuracy  # Точность

    def set_accuracy(self, new_accuracy):
        self.__accuracy = new_accuracy

    def get_accuracy(self):
        return self.__accuracy


class Sword(Weapon):
    def __init__(self, new_title, new_damage, new_rate, new_sharpening):
        super().__init__(new_title, new_damage, new_rate)
        self.__sharpening = new_sharpening  # Заточка (процент)

    def set_sharpening(self, new_sharpening):
        self.__sharpening = new_sharpening

    def get_sharpening(self):
        return self.__sharpening


warrior1 = Warrior("Воин", 1000, 20, 0, 10)
mage1 = Mage("Маг", 800, 15, 15, 10)
sword = Sword("Меч", 100, 2.5, 1.0)

print(f"{sword.get_title()} sharpening: {sword.get_sharpening()} rate: {sword.get_rate()}")


print(f"{warrior1.get_name()} hp: {warrior1.get_health()} speed: {warrior1.get_speed()} state: {warrior1.get_state()}")
warrior1.move(20)
print(f"{warrior1.get_name()} hp: {warrior1.get_health()} speed: {warrior1.get_speed()} state: {warrior1.get_state()}")

print(f"{mage1.get_name()} hp: {mage1.get_health()} mana: {mage1.get_mana()}")
mage1.set_mana(50)
mage1.spelling("Fire")
print(f"{mage1.get_name()} hp: {mage1.get_health()} mana: {mage1.get_mana()}")


