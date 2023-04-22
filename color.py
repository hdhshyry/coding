import sensor, image, time, math, pyb
from pyb import Pin



#Red == 1
#Blue == 2
#Yellow == 3


thresholds = [(41, 70, 46, 81, 29, 63),(75, 95, -19, 8, 53, 96),(53, 76, -21, -3, -56, -19)]



sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
clock = time.clock()



while(True):
    clock.tick()
    img = sensor.snapshot()
    for blob in img.find_blobs(thresholds,
    pixels_threshold=100, area_threshold=100, merge=True):
        clock.tick()
        if blob.code() == 1:
            print("Red Found")

        if blob.code() == 2:
           print("Yellow Found")

        if blob.code() == 3:
            print("Blue Found")
