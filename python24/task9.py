from clases import PotatoGarden

garden = PotatoGarden(5)

for _ in range(3):
    garden.grow_all()

garden.are_all_ripe()