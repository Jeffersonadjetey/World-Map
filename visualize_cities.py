#Name: Jefferson Adjetey
#Date: 03/02/2021
# Purpose: Visualize a list of cities using coordinates and a map


from cs1lib import *
from city import City

# constants
FRAME_WIDTH = 720
FRAME_HEIGHT = 360
FRAME_RATE = 15
ZERO_X = 360
ZERO_Y = 180

framecount = 0
mapDraw = False

in_file = open("cities_population.txt", "r")  # opens world_cities file for reading
world_cities = []  # creates an empty list of world cities
count = 0
for line in in_file:
    stripped_line = line.strip()  # strips white space from the end of the line

    line_list = stripped_line.split(",")  # creates a list of each city's information

    world_cities.append((line_list[2], line_list[3]))  # appends a tuple that contains the first 50 longitude and
    # latitudes
    count += 1
    if count == 50:
        break

in_file.close()  # closes world_cities file for reading


#  draw function
def draw_map():
    global framecount
    global mapDraw

    #if the map isn't already drawn, draw it
    if mapDraw is False:
        img = load_image("world.png")
        draw_image(img, 0, 0)
        mapDraw = True

    set_stroke_color(1, 0, 0)
    enable_fill()

    #creates one point for each city for each frame
    if framecount < 50:
        y, x = world_cities[framecount]
        lat, long = float(y), float(x)
        print(framecount + 1, lat, long)
        #draws the points using 2 as a factor to scale the latitude and longitude
        draw_rectangle(ZERO_X + (long * 2), ZERO_Y - (lat * 2), 5, 5)
        framecount += 1


start_graphics(draw_map, width=FRAME_WIDTH, height=FRAME_HEIGHT, framerate=FRAME_RATE)
