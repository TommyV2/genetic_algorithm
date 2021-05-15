
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
        self.stats_string=""
        self.valid_person = True
        self.update()  
                      
    def update(self):
        self.modify_attributes()
        if self.validate_stats() == 0:
            self.valid_person = False
        else:
            self.stats_string = self.stats_to_bits()

    def modify_attributes(self):
        if self.height > 190:
            bonus = int((self.height - 190)/5)
            self.agility -= bonus
            self.speed += bonus
        elif self.height < 170:
            bonus = int((170-self.height)/5)
            self.agility += bonus
            self.speed -= bonus
        if self.weight > 90:
            bonus = int((self.weight - 90)/5)
            self.agility -= bonus
            self.endurance -= bonus
            self.explosivness -= bonus
            self.strength += bonus
        elif self.weight < 70:
            bonus = int((70 - self.weight)/5)
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

    def validate_stats(self):
        if self.age < 15 or self.age > 60:
            return 0
        if self.height > 220 or self.height < 160:
            return 0
        if self.weight > 120 or self.weight < 50:
            return 0
        if self.strength > 15 or self.strength < 0:
            return 0
        if self.endurance > 15 or self.endurance < 0:
            return 0
        if self.agility > 15 or self.agility < 0:
            return 0
        if self.speed > 15 or self.speed < 0:
            return 0
        if self.explosivness > 15 or self.explosivness < 0:
            return 0
        return 1

    def evaluate_fitness(self, sport): 
        if sport == "martial_arts":
            fitness = self.explosivness * 2 + self.endurance * 2 + self.agility * 2 + self.strength + self.speed
            return fitness
        elif sport == "football":
            fitness = self.explosivness + self.endurance * 2 + self.agility * 2 + self.strength + self.speed * 2
            return fitness
        elif sport == "basketball":
            fitness = 5/6 * (self.height * 2 + self.explosivness + self.endurance  + self.agility * 2 + self.strength + self.speed * 2)
            return fitness
        elif sport == "powerlifing": 
            fitness = 5/6 * (self.weight * 2 + self.explosivness * 2 + self.endurance  + self.agility  + self.strength * 2 + self.speed)
            return fitness
        else:
          return 0

    def mutate(self):
        ### na koncu metod zmieniajacych atrybuty nalezy dodac update()
        self.update()

    def crossing(self, another_person):
        ###
        return new_person  

    def print_stats(self):
        return print("\nAge: ", self.age, "\nHeight: ", self.height, "cm", "\nWeight: ", self.weight, "kg", "\nStrenght: ", self.strength,
                     "\nEndurance: ", self.endurance, "\nAgility: ", self.agility, "\nSpeed: ", self.speed, "\nExplosivness: ", self.explosivness)
