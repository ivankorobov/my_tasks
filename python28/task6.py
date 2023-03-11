from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, color, velocity):
        self._color = color
        self._velocity = velocity

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity = value

    @abstractmethod
    def ride_on_earth(self):
        pass

    @abstractmethod
    def ride_on_water(self):
        pass


class MusicMixin:

    def play_music(self):
        print("Играет музыка")


class Automobile(Transport, MusicMixin):
    def ride_on_earth(self):
        print("едем по земле")


class Boat(Transport, MusicMixin):
    def ride_on_water(self):
        print("идём по воде")



class Amphibia(Automobile, Boat, MusicMixin):
    pass

amphibia = Amphibia('red', 1337)
amphibia.play_music()
amphibia.ride_on_earth()
amphibia.ride_on_water()
print(amphibia.color)
amphibia.color = 'white'
print(amphibia.color)

