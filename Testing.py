def display_pixel(row, column):
    '''
    Turn on one specific pixel.

    TODO: Implement function
    '''
    if row == 0:
        pixels = ['3FE0', '5F70', '3FD0', '5EF0', '3FB0']

    elif row == 1:
        pixels = ['9F70', '9EF0', '9DF0', '9BF0', '97F0']

    elif row == 2:
        pixels = ['5FD0', '2FF0', '5FB0', '8FF0', '5FE0']

    elif row == 3:
        pixels = ['37F0', '3BF0', '3DF0', '3EF0', '3F70']

    elif row == 4:
        pixels = ['9FB0', '5DF0', '9FE0', '5DF0', '9FD0']

    pixel_on = pixels[column]

    location = str('0x')+pixel_on
    print(location)

display_pixel(1,1)