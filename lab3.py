#!usr/bin/env python3.5
#Daniel Solus
#Assignment LAB 3
"""Write a program that computes the number of tiles, the number of boxes of tiles, and the
number of extra tiles for a room."""


def tile_conv(*args):
    #program should prompt the user for the number of tiles in inches.
    tile_size = input("What is the size of the tile in inches?")
    if tile_size <= 24 and tile_size >= 4:
        print (tile_size)
    else:
        print("Invalid tile size.\nTile size should be between 4 and 24 inches.\n Good bye.")

    #Enter the width of the room
    room_width_ft = input("Enter room width in feet: ")
    room_width_in = input("and inches: ")
    #Convert room width to inches
    room_width_ft = room_width_ft * 12
    room_width = room_width_ft + room_width_in

    #Enter the length of the room
    room_length_ft = input("Enter the room length in feet: ")
    room_length_in = input("and inches: ")
    #Convert room length to inches
    room_length_ft = room_length_ft * 12
    room_length = room_length_ft + room_length_in

    #convert room size to inches
    tile_width = room_width / tile_size
    print(tile_width)
    if room_width % tile_size != 0:
        tile_width  = tile_width + 1

    tile_length = room_length / tile_size
    print(tile_length)
    if room_length % tile_size != 0:
        tile_width  = tile_width + 1

    total_tiles = tile_width*tile_length

    # a box contains 24 tiles
    print("The total number of tiles needed to cover the room: {}".format(total_tiles))

tile_conv()

