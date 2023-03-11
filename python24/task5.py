class Famyly:
    surname = 'Common fam'
    money = 100000
    have_a_house = False

    def info(self):
        print(
            'Fam name: {}\nFam Funds: {}\nHav a house{}\n'.format(
                self.surname, self.money, self.have_a_house
            )
        )

    def earn_money(self, amount):
        self.money += amount
        print('Earned {} money! Curr value: {}'.format(amount, self.money))

    def buy_house(self, house_price, discount=0):
        house_price -= house_price * discount / 100
        if self.money >= house_price:
            self.money -= house_price
            self.have_a_house = True
            print('House purchased! Current money: {}\n'.format(self.money))
        else:
            print("Not enough money!\n")
            