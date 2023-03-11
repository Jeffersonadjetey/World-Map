#Name: Jefferson Adjetey
#Date: 03/02/2021
# Purpose: Driver code for city class


from city import City

in_file = open("world_cities.txt", "r")  # opens world_cities file for reading
world_cities = []  # creates an empty list of world cities

for line in in_file:
    stripped_line = line.strip()  # strips white space from the end of the line

    line_list = stripped_line.split(",")  # creates a list of each city's information

    city = City(line_list[0], line_list[1], line_list[2], int(line_list[3]), float(line_list[4]),
                float(line_list[5]))  # creates a city object using the list of each city's information

    world_cities.append(city)  # appends city object to the list of world cities

in_file.close()  # closes world_cities file for reading

out_file = open("cities_out.txt", "w")  # opens cities_out file for writing

for city in world_cities:  # for each city in the world_cities list, call the str method
    out_file.write(str(city) + "\n")  # from the city class and jump to a new line

out_file.close()  # closes cities_out file for writing