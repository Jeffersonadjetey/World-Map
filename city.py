#Name: Jefferson Adjetey
#Date: 03/02/2021
#Purpose: Create a city class to store information about cities of the world


class City:
    #instance variables
    def __init__(self, c_code, name, region, pop, long, lat):
        self.c_code = c_code
        self.name = name
        self.region = region
        self.population = pop
        self.longitude = long
        self.latitude = lat

    # prints the city along with its' population, longitude, and latitude
    def __str__(self):
        return self.name + "," + str(self.population) + "," + str(self.longitude) + "," + str(self.latitude)