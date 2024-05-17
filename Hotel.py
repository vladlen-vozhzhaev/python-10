class Hotel:
    def __init__(self, rooms):
        self.rooms = rooms
    def getFreeRooms(self):
        print("Список свободных комнат: ")
        for room in self.rooms:
            if not room.reserved:
                print(room.number)
    def reserveRoom(self):
        roomNumber = int(input("Введите номер комнаты: "))
        error = True
        for room in self.rooms:
            if roomNumber == room.number and not room.reserved:
                room.reserved = True
                print(f"Комната {room.number} забронирована")
                error = False
        if error:
            print("Ошибка при бронировании комнаты")
    def getReservedRooms(self):
        print("Список забронированных комнат: ")
        for room in self.rooms:
            if room.reserved:
                print(room.number)
    def filter(self):
        place = int(input("Кол-во спальных мест: "))
        tv = input("Наличие tv (Да/Нет/Неважно): ")
        wifi = input("Наличие wifi (Да/Нет/Неважно): ")
        for room in self.rooms:
            if (
                    room.place == place and
                    (room.tv and tv=="Да" or not room.tv and tv=="Нет" or tv=="Неважно") and
                    (room.wifi and wifi=="Да" or not room.wifi and wifi=="Нет" or wifi=="Неважно")
            ):
                print(room.number)
class Room:
    def __init__(self, number, place, tv, wifi):
        self.number = number
        self.place = place
        self.tv = tv
        self.wifi = wifi
        self.reserved = False

hotel = Hotel( [
    Room(11, 3, True, True),
    Room(12, 2, False, False),
    Room(13, 2, False, True),
    Room(21, 1, True, True),
    Room(22, 1, False, False),
    Room(23, 3, False, True),
    Room(31, 2, True, True),
    Room(32, 3, True, False),
    Room(33, 1, True, True)
] )


command = input("Введите команду: ")
while command != 'exit':
    if command == "getFreeRooms":
        hotel.getFreeRooms()
    elif command == "reserveRoom":
        hotel.reserveRoom()
    elif command == "getReservedRooms":
        hotel.getReservedRooms()
    elif command == "filter":
        hotel.filter()
    command = input("Введите команду: ")