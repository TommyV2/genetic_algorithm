
class Person:
    def __init__(self, age, height, weight, strength, endurance, agility, speed, explosivness):
        self.age = age
        self.height = height
        self.weight = weight
        self.strength = strength
        self.endurance = endurance
        self.agility = agility
        self.speed = speed
        self.explosivness = explosivness
        self.modify_attributes()
        self.stats_string = self.stats_to_bits()

    def modify_attributes(self):
        if self.height > 180:
            bonus = int((self.height - 180)/10)
            self.agility -= bonus
            self.speed += bonus
        elif self.height < 160:
            bonus = int((160-self.height)/10)
            self.agility += bonus
            self.speed -= bonus
        if self.weight > 90:
            bonus = int((self.weight - 90)/10)
            self.agility -= bonus
            self.endurance -= bonus
            self.explosivness -= bonus
            self.strength += bonus
        elif self.weight < 70:
            bonus = int((70 - self.weight)/10)
            self.agility += bonus
            self.endurance += bonus
            self.explosivness += bonus
            self.strength -= bonus
        if self.age > 30 or self.age < 20:
            self.strength = int(0.6 * self.strength)
            self.endurance = int(0.6 * self.endurance)
            self.agility = int(0.6 * self.agility)
            self.speed = int(0.6 * self.speed)
            self.explosivness = int(0.6 * self.explosivness)

    def stats_to_bits(self):
        stats_string = ""
        age = bin(self.age)[2:]
        size = len(age)
        if size<6:
          age = (6-size)*"0" + age
        stats_string += age
        height = bin(self.height-160)[2:]
        size = len(height)
        if size<6:
          height = (6-size)*"0" + height
        stats_string += height
        weight = bin(self.weight-50)[2:]
        size = len(weight)
        if size<6:
          weight = (6-size)*"0" + weight     
        stats_string += weight
        strength = bin(self.strength)[2:]
        size = len(strength)
        if size<4:
          strength = (4-size)*"0" + strength
        stats_string += strength
        endurance = bin(self.endurance)[2:]
        size = len(endurance)
        if size<4:
          endurance = (4-size)*"0" + endurance
        stats_string += endurance
        agility = bin(self.agility)[2:]
        size = len(agility)
        if size<4:
          agility = (4-size)*"0" + agility
        stats_string += agility
        speed = bin(self.speed)[2:]
        size = len(speed)
        if size<4:
          speed = (4-size)*"0" + speed
        stats_string += speed
        explosivness = bin(self.explosivness)[2:]
        size = len(explosivness)
        if size<4:
          explosivness = (4-size)*"0" + explosivness
        stats_string += explosivness
        return stats_string

    def bits_to_stats(self, stats_string):
        str = '0b'+stats_string[0:6]
        self.age = int(str, 2)
        str = '0b'+stats_string[6:12]
        self.height = int(str, 2)+160
        str = '0b'+stats_string[12:18]
        self.weight = int(str, 2)+50
        str = '0b'+stats_string[18:22]
        self.strength = int(str, 2)
        str = '0b'+stats_string[22:26]
        self.endurance = int(str, 2)
        str = '0b'+stats_string[26:30]
        self.agility = int(str, 2)
        str = '0b'+stats_string[30:34]
        self.speed = int(str, 2)
        str = '0b'+stats_string[34:38]
        self.explosivness = int(str, 2)

    def print_stats(self):
        return print("\nAge: ", self.age, "\nHeight: ", self.height, "cm", "\nWeight: ", self.weight, "kg", "\nStrenght: ", self.strength,
                     "\nEndurance: ", self.endurance, "\nAgility: ", self.agility, "\nSpeed: ", self.speed, "\nExplosivness: ", self.explosivness)
