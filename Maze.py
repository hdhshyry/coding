import sensor, image, time, math, pyb
from pyb import Pin
from pyb import UART
from image import SEARCH_EX, SEARCH_DS
thresholds = [(41, 70, 46, 81, 29, 63),(75, 95, -19, 8, 53, 96),(53, 76, -21, -3, -56, -19)]
Bin = (0, 100)
#camera sitting
sensor.reset()
sensor.set_contrast(1)
sensor.set_gainceiling(16)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
clock = time.clock()
#Load sample of letter
template1 = image.Image("/U0.pgm")
template2 = image.Image("/S.pgm")
template4 = image.Image("/1.pgm")
template3 = image.Image("/h.pgm")
template5 = image.Image("/H1.pgm")
while (True):
#Type of frame for color
    sensor.set_framesize(sensor.QVGA)
    sensor.set_pixformat(sensor.RGB565)
    clock.tick()
    img = sensor.snapshot()
    #clor detection
    for blob in img.find_blobs(thresholds,
    pixels_threshold=100, area_threshold=100, merge=True):
        if blob.code() == 1:
            print("Red Found")

        if blob.code() == 2:
           print("Yellow Found")

        if blob.code() == 3:
            print("Blue Found")
    #Type of frame for letter
    sensor.set_framesize(sensor.QQCIF)
    sensor.set_pixformat(sensor.GRAYSCALE)
    img1= sensor.snapshot()
    #Detection of letter
    harmed = img1.find_template(template1, 0.6, step=4, search=SEARCH_EX)
    unharmed = img1.find_template(template2, 0.6, step=4, search=SEARCH_EX)
    ff = img1.find_template(template3, 0.6, step=4, search=SEARCH_EX)
    H = img1.find_template(template5, 0.6, step=4, search=SEARCH_EX)
    stable = img1.find_template(template4, 0.5, step=4, search=SEARCH_EX)
    if harmed:
        img.draw_rectangle(harmed,5)
        #ser.write(0x01)
        print("Detected U")
    if ff:
        img.draw_rectangle(ff,5)
        #ser.write(0x01)
        print("Detected..H")
    if unharmed:
        img.draw_rectangle(unharmed,5)
        #ser.write(0x02)
        print("Detected...S")
    if stable:
        img.draw_rectangle(stable,5)
        ##ser.write(0x03)
        print("Detected S")
    if H:
        img.draw_rectangle(H,5)
        ##ser.write(0x03)
        print("Detected h")
