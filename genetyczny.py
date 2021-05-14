import time
import sys
import math
from person import Person

sports = [ "martial arts", "football", "basketball", "powerlifing"]

chosen_sport = "football"
    

test_person = Person(21, 192, 82, 7, 8, 5, 7, 11)
print(test_person.print_stats())
string = test_person.stats_to_bits()
print(string)
test_person.bits_to_stats(string)
print(test_person.print_stats())
