#  Реализуйте композицию для двух иерархий классов из предыдущего занятия.
#  Напишите код для работы с объектами соответствующих классов, из которого наглядно понятна идея композиции.
# 4.2. Расскажите своими словами, как вы поняли пример с двумя видами полиморфизма.

# 4.3. Напишите функцию, которая получает на вход список list[Animal] из этого примера, очищает его,
# и затем заполняет 500 объектами,
# где будут случайно перемешаны 500 объектов двух дочерних классов.

# Не забывайте, что объекты обычным присваиванием не копируются.
# Получите с её помощью результат, и в цикле, не зная, где какой объект, вызывайте foo().
# Почему получился такой вывод?

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

    def __str__(self):
        return (f"{self.__name} здоровье - {self.__health} сила - {self.__strength} "
                f"скорость - {self.__speed} состояние - {self.__state}")


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
            self.__damage = new_damage

    def __str__(self):
        return f"{self.__title} (урон: {self.__damage})"


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


class Armor:
    def __init__(self, name, defense):
        self.__name = name
        self.__defense = defense

    def get_name(self):
        return self.__name

    def get_defense(self):
        return self.__defense

    def __str__(self):
        return f"{self.__name} защита -{self.__defense}"


class Warrior(Person):
    def __init__(self, new_name, new_health, new_strength, new_speed, new_stamina, new_weapon, new_armor):
        super().__init__(new_name, new_health, new_strength, new_speed)
        # Warrior имеет Оружие и Броню - Композиция
        self.weapon = new_weapon  # Оружие - класс
        self.armor = new_armor  # Броня - класс
        self.__stamina = new_stamina  # Выносливость

    def attack(self):
        if self.weapon:
            print("Атака воина - " + str(self.weapon))

    def show_equipment(self):
        print(f"== Снаряжение {self.get_name()} ==")
        print(f"Оружие: {self.weapon}")
        print(f"Броня: {self.armor}")

    def set_sword(self, new_weapon):
        self.weapon = new_weapon

    def get_sword(self):
        return self.weapon

    def set_stamina(self, new_stamina):
        self.__stamina = new_stamina

    def get_stamina(self):
        return self.__stamina

    def foo(self):  # Аналог attack(), использует композицию (оружие и броню)
        if self.weapon:
            print(f"{self.get_name()} атакует с {self.weapon}!")
        else:
            print(f"{self.get_name()} без оружия!")


class Spellbook:
    def __init__(self, title):
        self.__title = title
        self.__spells = ["Огненный шар", "Ледяная стрела", "Молния", "Щит"]

    def get_random_spell(self):
        import random
        return random.choice(self.__spells)

    def get_title(self):
        return self.__title

    def __str__(self):
        return f"{self.__title} ({len(self.__spells)} заклинаний)"


class Mage(Person):
    def __init__(self, new_name, new_health, new_strength, new_speed, new_mana, new_spellbook):
        super().__init__(new_name, new_health, new_strength, new_speed)
        self.__mana = new_mana  # Мана
        # Маг имеет Книгу Заклинаний - Композиция
        self.spellbook = new_spellbook

    def set_mana(self, value):
        self.__mana = value

    def get_mana(self):
        return self.__mana

    def attack(self):
        if self.spellbook:
            spell = self.spellbook.get_random_spell()
            print(f"{self.get_name()} читает заклинание: {spell}!")
        else:
            print("У мага нет книги заклинаний!")

    def foo(self):  # Аналог attack(), использует композицию (книгу заклинаний)
        mana_cost = 10  # Пример: заклинание тратит ману
        if self.get_mana() >= mana_cost:
            spell = self.spellbook.get_random_spell()
            self.set_mana(self.get_mana() - mana_cost)  # Тратим ману
            print(f"{self.get_name()} кастует {spell} из {self.spellbook}! Остаток маны: {self.get_mana()}")
        else:
            print(f"{self.get_name()} без маны!")


def fill_person_list(person_list):
    # 1. Очищаем список
    person_list.clear()
    print("Список очищен")
    import random

    # 2. Заполняем 500 объектами
    for i in range(500):
        # Случайно выбираем: Воин или Маг
        if random.choice([True, False]):
            # Создаём Воина с броней и оружием
            rand_weapon = Sword(f"Меч {i}", 100 + random.randint(0, 50),
                                random.uniform(0.5, 10.0), random.uniform(0.1, 1.0))
            rand_armor = Armor(f"Доспех {i}", 200 + random.randint(0, 100))
            rand_warrior = Warrior(f"Воин {i}", 1000 + random.randint(0, 500), 20 + random.randint(0, 10),
                                   random.uniform(0.5, 10.0), 50 + random.randint(0, 50), rand_weapon, rand_armor)
            person_list.append(rand_warrior)
        else:
            # Создаём Мага с книгой
            rand_spellbook = Spellbook(f"Книга {i}")
            mage = Mage(f"Маг {i}", 800 + random.randint(0, 200), 15 + random.randint(0, 5),
                        random.randint(0, 50), 50 + random.randint(0, 50), rand_spellbook)
            person_list.append(mage)

    print(f"Добавлено {len(person_list)} персонажей")
    return person_list


sword = Sword("Меч", 100, 2.5, 1.0)
armor = Armor("Доспех", 200)
spellbook = Spellbook("Книга Заклинателей")

warrior1 = Warrior("Воин", 1000, 20, 0, 10, sword, armor)
mage1 = Mage("Маг", 800, 15, 15, 10, spellbook)

print(sword)
print(warrior1.show_equipment())

print(warrior1)
warrior1.move(20)
print(warrior1)

warrior1.attack()
mage1.attack()

print(f"{mage1.get_name()} hp: {mage1.get_health()} mana: {mage1.get_mana()}")
mage1.set_mana(50)
print(f"{mage1.get_name()} hp: {mage1.get_health()} mana: {mage1.get_mana()}")


# Использование
persons = []  # Пустой список

fill_person_list(persons)  # Заполняем 500 объектами

# Цикл: вызываем attack() у каждого, не зная типа (полиморфизм)
for person in persons:
    person.attack()  # Автоматически: если Warrior — атака оружием, если Mage — заклинание
print(f"Всего объектов: {len(persons)}")  # 500
