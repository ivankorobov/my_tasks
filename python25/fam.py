def wife_life_func(wife, i):
    if wife.satiety < 0:
        return f"{wife.name} умер прожив {i} дней"
    elif wife.satiety < 20:
        wife.eat()
    elif Home.refrigerator < 10:
        wife.buy_food()
        wife.satiety -= 10
    elif Home.dirt_count > 45:
        wife.cleaning()
        wife.satiety -= 10
    elif Home.cat_food < 5:
        wife.buy_food_4_cat()
        wife.satiety -= 10
    elif wife.happiness < 20:
        wife.buy_coat()
        wife.satiety -= 10
    else:
        wife.petting_the_cat()
        wife.satiety -= 10

def husband_life_func(husband, i):
    if husband.satiety < 0:
        return f"{husband.name} умер прожив {i} дней"
    elif husband.satiety < 20:
        husband.eat()
    elif Home.locker_w_money < 50:
        husband.work()
        husband.satiety -= 10
    elif husband.happiness < 20:
        husband.play()
        husband.satiety -= 10
    else:
        husband.petting_the_cat()
        husband.satiety -= 10
def cat_life_func(cat, i):
    if husband.satiety < 0:
        return f"{cat.name} умер прожив {i} дней"
    elif cat.satiety < 20:
        cat.eat()
    elif Home.dirt_count < 10:
        cat.tear_walls()
        cat.satiety -= 10
    else:
        cat.sleep()
        cat.satiety -= 10