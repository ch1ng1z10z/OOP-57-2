
class Hero:

    def __init__(self, name, lwl, hp ):
        self.name = name
        self.lwl = lwl
        self.hp = hp

    def action(self):
        print(f'{self.name} готов к атаке!')


iuda = Hero("iuda",100,200)



class HeroWarrior(Hero):

    def __init__(self, name, lwl, hp, attack, rage):
        super().__init__(name, lwl, hp)
        self.attack = attack
        self.rage = rage
        if rage >= 100:
            print('герой наносит мoщную атаку') and rage == 0
        elif rage < 100:
            print('Герой наносит обычную атаку')
            rage += 25
    def action(self):
        print(f'HeroWarrior = Имя:{self.name}, Уровень: {self.lwl}, ХП:{self.hp},  имбовая атака(1-100): {self.rage}')
tanjiro = HeroWarrior("Tanjiro",80,110,90, 0)
print(tanjiro.action())




class HeroMage(Hero):
    spell_book = ['Водная тюрьма', 'Совместная атака', 'сюрикеном', 'Сюрикен-призрак', 'Разящие волны воздуха', 'Песчаный гроб']
    show_spells = ['Сюрикен-призрак', 'Разящие волны воздуха', 'Песчаный гроб']
    def __init__(self, name, lwl, hp, chakra, napadenie):
        super().__init__(name, lwl, hp)
        self.chakra = chakra
        self.napadenie = napadenie
    def action(self):
        print(f'HeroMage = Имя:{self.name}, Уровень: {self.lwl}, ХП:{self.hp}, Уровень Чакры: {self.chakra}, сила Атаки: {self.napadenie}, Список доступных техних: {self.show_spells}')

    def vse_tehniki(self):
        print(f'все доступные техники: {self.spell_book}')
kakachi = HeroMage("kakachi", 50, 80,  400, 100)





"""gg"""

















