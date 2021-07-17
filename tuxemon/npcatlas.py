# NOTICE THIS IS EXTREMELY BETA CODE AND IS SUBJECT TO CHANGE
from PIL import Image
import sys

def createatlas(inpcdat):
    # Add all of the images to a list
    inpc = '' + inpcdat
    images = [Image.open(x) for x in [inpcdat+'_back_walk.001.png', inpcdat+'_back_walk.000.png', inpcdat+'_back_walk.002.png', inpcdat+'_front_walk.001.png', inpcdat+'_front_walk.000.png', inpcdat+'_front_walk.002.png', inpcdat+'_left_walk.001.png', inpcdat+'_left_walk.000.png', inpcdat+'_left_walk.002.png', inpcdat+'_right_walk.001.png', inpcdat+'_right_walk.000.png', inpcdat+'_right_walk.002.png']]
    total_width = 0
    max_height = 0

    # find the width and height of the final image
    for img in images:
    total_width += img.size[0]
    max_height = max(max_height, img.size[1])

    # create a new image with the appropriate height and width
    new_img = Image.new('RGB', (total_width, max_height))

    # Write the contents of the new image
    current_width = 0
    for img in images:
    new_img.paste(img, (current_width,0))
    current_width += img.size[0]

    # Save the image
    new_img.save(inpc + '.atlas.png')

def test():
    #put data here
