'''
Hardware Lab device driver exercise.

TODO: PLEASE ADD AN APPROPRIATE DESCRIPTION HERE
'''
import machine, microbit

OUT_address = 0x50000504
OUT_SET_address = 0x50000508
OUT_CLEAR_address = 0x5000050C

microbit.display.off()

def clear_display():
    '''
    Turn off all pixels.
    
    TODO: Implement function.
    '''
    microbit.display.off()

def illuminate_display():
    '''
    Turn on all pixels.
    
    TODO: Implement function
    '''
    machine.mem16[0x50000504] = 0xE000
    
def display_pixel(row, column):
    '''
    Turn on one specific pixel.
    
    TODO: Implement function
    '''
    if row == 0:
        pixels = [0x3FE0, 0x5F70, 0x3FD0, 0x5EF0, 0x3FB0]

    elif row == 1:
        pixels = [0x9F70, 0x9EF0, 0x9DF0, 0x9BF0, 0x97F0]

    elif row == 2:
        pixels = [0x5FD0, 0x2FF0, 0x5FB0, 0x8FF0, 0x5FE0]

    elif row == 3:
        pixels = [0x37F0, 0x3BF0, 0x3DF0, 0x3EF0, 0x3F70]

    elif row == 4:
        pixels = [0x9FB0, 0x5BF0, 0x9FE0, 0x5DF0, 0x9FD0]

    pixel_on = pixels[column]

    machine.mem16[OUT_address] = pixel_on

def main():
    '''
    Standalone test of device driver.
    '''
    '''
    '''
    display_pixel(2,2)
    microbit.sleep(1000)
    display_pixel(1,1)

    '''
    TODO: clear display, wait 1 second, display centre pixel, wait 1 second,
          turn on all pixels, wait 1 second, clear display
    '''
    #Test 1
    clear_display()
    microbit.sleep(1000)
    display_pixel(2,2)
    microbit.sleep(1000)
    illuminate_display()
    microbit.sleep(1000)
    clear_display()
    #Test 2
    illuminate_display()
    microbit.sleep(1000)
    clear_display()
    i = 0
    while i < 5:
        j = 0
        while j < 5:
            display_pixel(i, j)
            microbit.sleep(1000)
            j = j + 1
        i = i + 1
if __name__ == "__main__":
    main()
