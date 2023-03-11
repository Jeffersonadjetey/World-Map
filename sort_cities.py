#Name: Jefferson Adjetey
#Date: 03/02/2021
# Purpose: Create functions to sort through a list of cities based on different criteria


from city import City
from quicksort import *

in_file = open("world_cities.txt", "r")  # opens world_cities file
world_cities = []

for line in in_file:
    stripped_line = line.strip()  # strips white space from the end of the line

    line_list = stripped_line.split(",")  # creates a list of each city's information

    city = City(line_list[0], line_list[1], line_list[2], int(line_list[3]), float(line_list[4]),
                float(line_list[5]))  # creates a city object using the list of each city's information

    world_cities.append(city)  # appends city object to the list of world cities

in_file.close()  # closes world_cities file for reading


# compare function for population
def compare_population(city1, city2):
    if city2.population <= city1.population:
        return True


# compare function for city name
def compare_alpha(city1, city2):
    if city1.name <= city2.name:
        return True


# compare function for latitude
def compare_latitude(city1, city2):
    if city1.longitude <= city2.longitude:
        return True


# create a file to alphabetically sort the cities
out_file = open("cities_alpha.txt", "w")
# call the quicksort on world_cities using the alphabet comparsion function
sort(world_cities, compare_alpha)
#writes out each line in the world_cities
for city in world_cities:
    out_file.write(str(city) + "\n")
#closes file for reading
out_file.close()


#create a file to sort the cities by population
out_file = open("cities_population.txt", "w")
#call the quicksort on world_cities using the population comparison function
sort(world_cities, compare_population)
#writes out each line in the world_cities
for city in world_cities:
    out_file.write(str(city) + "\n")
#closes file for reading
out_file.close()


#create a file to sort the cities by latitude
out_file = open("cities_latitude.txt", "w")
#call the quicksort on world_cities using the latitude comparison function
sort(world_cities, compare_latitude)
#writes out each line in the world_cities
for city in world_cities:
    out_file.write(str(city) + "\n")
#closes file for reading
out_file.close()
