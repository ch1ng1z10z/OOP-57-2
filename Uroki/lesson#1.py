class Negr:

    def __init__(self, name, lvl, hp):
        self.name_1 = name
        self.lvl_1 = lvl
        self.hp_1 = hp

    def action(self):
        print(f'{self.name_1} base action!!')


kirito = Negr("Kirito",100,1000)
asuna = Negr("asuna",100,900)

print(kirito.hp_1)

kirito.action()
asuna.action()