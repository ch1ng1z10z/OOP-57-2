class Anime:
    def __init__(self, name, power_live ,love, beautiful):
        self.name = name
        self.power = power_live
        self.love = love
        self.beautiful = beautiful

    def obozvat(self):
        print(f'Выбранный вами {self.name} является умственно осталым')


Naruto = Anime("Naruto",1000,"hinata","the_best")
Saske = Anime('Saske', 1000, 'himself', 'nothing')
you = Anime('хз', '-31','nothing', 'no')

