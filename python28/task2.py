from abc import ABC, abstractmethod


class Transport(ABC):

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

amphibia = Amphibia()
amphibia.play_music()
amphibia.ride_on_earth()
amphibia.ride_on_water()

