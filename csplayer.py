class Player:
    def __init__(self, id, kd, hp, armor, nickname, age):
        self.__nickname = nickname
        self.__id = id
        self.__kd = kd
        self.__hp = 100
        self.__armor = 0
        self.__age = 13
    
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 13 < age < 100:
            self.__age = age
        else:
            print("Unacceptable age.")

    def player_info(self):
        print(f"Nickname: {self.__nickname}, Age: {self.__age}, ID: {self.__id}")
    def game_info(self):
        print(f"KD: {self.__kd}, HP: {self.__hp}, Armor: {self.__armor}")


tom = Player("1", 0, 100, 0, "tommy", 18)
tom.player_info()
tom.game_info()