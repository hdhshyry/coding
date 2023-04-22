import time, sensor, image
from pyb import UART
from image import SEARCH_EX, SEARCH_DS
ser = UART(3,115200,timeout_char=1000)
# Reset sensor
sensor.reset()
low_threshold = (0, 100)
high_threshold = (0,130)
# Set sensor settings
sensor.set_contrast(1)
sensor.set_gainceiling(16)
# Max resolution for template matching with SEARCH_EX is QQVGA
sensor.set_framesize(sensor.QQCIF
)
# You can set windowing to reduce the search image.
#sensor.set_windowing(((640-80)//2, (480-60)//2, 80, 60))
sensor.set_pixformat(sensor.GRAYSCALE)


# Load template.
# Template should be a small (eg. 32x32 pixels) grayscale image.
template1 = image.Image("/H..pgm")
template2 = image.Image("/S.pgm")
template4 = image.Image("/1.pgm")
template3 = image.Image("/h.pgm")
clock = time.clock()
# Run template matching
while (True):
    print(sensor.width(),sensor.height())
    clock.tick()
    img = sensor.snapshot()
    img.binary([low_threshold], invert = 1)

    # find_template(template, threshold, [roi, step, search])
    # ROI: The region of interest tuple (x, y, w, h).
    # Step: The loop step used (y+=step, x+=step) use a bigger step to make it faster.
    # Search is either image.SEARCH_EX for exhaustive search or image.SEARCH_DS for diamond search
    #
    # Note1: ROI has to be smaller than the image and bigger than the template.
    # Note2: In diamond search, step and ROI are both ignored.
    harmed = img.find_template(template1, 0.6, step=4, search=SEARCH_EX)
    unharmed = img.find_template(template2, 0.6, step=4, search=SEARCH_EX)
    ff = img.find_template(template3, 0.6, step=4, search=SEARCH_EX)
    stable = img.find_template(template4, 0.5, step=4, search=SEARCH_EX)

    if harmed:
        img.draw_rectangle(harmed,5)
        #ser.write(0x01)            #Error: TypeError: Object with buffer protocol required.
        print("Detected H")
    if ff:
        img.draw_rectangle(ff,5)
        #ser.write(0x01)            #Error: TypeError: Object with buffer protocol required.
        print("Detected..H")
    if unharmed:
        img.draw_rectangle(unharmed,5)
        #ser.write(0x02)            # same Error
        print("Detected...S")
    if stable:
        img.draw_rectangle(stable,5)
        ##ser.write(0x03)            # same Error
        print("Detected S")
    #if l:
    #  img.draw_rectangle(l,5)
    #  ser.write(0x02)
