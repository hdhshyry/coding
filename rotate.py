# Hello World Example
#
# Welcome to the OpenMV IDE! Click on the green run arrow button below to run the script!

import sensor, image, time

sensor.reset()                      # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)   # Set frame size to QVGA (320x240)
sensor.skip_frames(time = 2000)     # Wait for settings take effect.
sensor.set_pixformat(sensor.GRAYSCALE)
#sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
#sensor.set_vflip(True)
#sensor.set_hmirror(False)
#sensor.set_transpose(True)
#sensor.set_windowing((128, 160))

clock = time.clock()


while(True):
    for i in range(360):
        clock.tick()
        img = sensor.snapshot().rotation_corr(0,0,i)

