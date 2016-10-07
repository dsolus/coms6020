#!usr/bin/env python3.5
#Daniel Solus
#Assignment LAB 3
"""Write a program that computes the number of tiles, the number of boxes of tiles, and the
number of extra tiles for a room."""
import math

def tile_conv(*args):
    #program should prompt the user for the number of tiles in inches.
    tile_size = input("What is the size of the tile in inches?")
    if tile_size <= 24 and tile_size >= 4:
        print (tile_size)
    else:
        print("Invalid tile size.\nTile size should be between 4 and 24 inches.\nGood bye.")
        quit()

    #Enter the width of the room
    room_width_ft = input("Enter room width in feet: ")
    room_width_in = input("and inches: ")
    if room_width_in >= 12:
        print("Number of inches must be less than 12.\nGood bye.")
        quit()
    #Convert room width to inches
    room_width_ft = room_width_ft * 12.0
    room_width = room_width_ft + room_width_in
    #Enter the length of the room
    room_length_ft = input("Enter the room length in feet: ")
    room_length_in = input("and inches: ")
    if room_length_in >= 12:
        print("Number of inches must be less than 12.\nGood bye.")
        quit()
    #Convert room length to inches
    room_length_ft = room_length_ft * 12.0
    room_length = room_length_ft + room_length_in

    #calculate number of tiles for the room
    tile_width = room_width / tile_size
    tile_width = math.ceil(tile_width)
    print(tile_width)

    tile_length = room_length / tile_size
    tile_length = math.ceil(tile_length)
    print(tile_length)

    total_tiles = tile_width*tile_length

    #copmute the number of boxes of tile, a box contains 24 tiles.
    boxes = math.ceil(total_tiles / 24)
    print("The number of boxes of tile needed to cover the room: {}".format(boxes))

    #the number of extra tiles for a room
    extra = (24 * boxes) - int(total_tiles)
    print("The extra tiles leftover: {}".format(extra))

    print("The total number of tiles needed to cover the room: {}".format(total_tiles))

tile_conv()

