from abc import ABC, abstractmethod

class Client:
    def __init__(self,name,balance,password):
        self.name = name
        self._balance = balance
        self.__password = password

    def zamena_password(self,new_password):
        self.__password = new_password
        print(f"Пароль изменен на {new_password}")

    def info_for_human(self):
        print(f"Имя: {self.name}, Баланс: {self._balance}")

# client2456 = Client("Константин", 3000, "2323")
# client2456.zamena_password("3345")
# client2456.info_for_human()

class Machinu(ABC):
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Machinu):
    def move(self):
        print("Машина едет")

    def stop(self):
        print("Машина остановился")

class Lodki(Machinu):
    def move(self):
        print("Лодка плывет")

    def stop(self):
        print("Лодка остановился")

class Samolet(Machinu):
    def move(self):
        print("Самолет летит")
    def stop(self):
        print("Самолет приземлился")

samolet1 = Samolet()
print(samolet1.move())
