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

    machine.mem16[OUT_address] = pixel_on+str('0x')



def main():
    '''
    Standalone test of device driver.
    '''
    
    display_pixel(2,2)
    microbit.sleep(1000)
    display_pixel(1,1)
    
    '''
    TODO: clear display, wait 1 second, display centre pixel, wait 1 second,
          turn on all pixels, wait 1 second, clear display
    '''

if __name__ == "__main__":
    main()
