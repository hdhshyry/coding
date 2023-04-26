# Maze - By: Moalem -0 Fri Apr 21 2023
#p4=Tx p5=Rx
import sensor, image, time, math, pyb
from pyb import Pin
from pyb import UART
from image import SEARCH_EX, SEARCH_DS
thresholds = [(41, 70, 46, 81, 29, 63),(75, 95, -19, 8, 53, 96),(53, 76, -21, -3, -56, -19)]
send=[0,0,0,0,0]
a=0
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
uart = UART(3, 19200)
#Load sample of letter H
template1 = image.Image("/H0.pgm")
template2 = image.Image("/H1.pgm")
template4 = image.Image("/H2.pgm")
template3 = image.Image("/H3.pgm")
template5 = image.Image("/H4.pgm")
template6 = image.Image("/H5.pgm")
#Load sample of letter S
template7 = image.Image("/S0.pgm")
template8 = image.Image("/S1.pgm")
template9 = image.Image("/S2.pgm")
template10 = image.Image("/S3.pgm")
template11 = image.Image("/S4.pgm")
template12 = image.Image("/S5.pgm")
template13 = image.Image("/S6.pgm")
#Load sample of letter U
template14 = image.Image("/U0.pgm")
template15= image.Image("/U1.pgm")
template16= image.Image("/U2.pgm")
template17 = image.Image("/U3.pgm")
template18 = image.Image("/U4.pgm")
template19 = image.Image("/U5.pgm")
#template20 = image.Image("/U6.pgm")
data=[]
while(True):
    data=uart.readchar()
    print(data)
    #char S=83 byte

    if data==83 :
        print('color')
        uart.write('S')
        send=[0,0,0,0,0]
        for i in range(50):
            #Type of frame for color
            sensor.set_framesize(sensor.QVGA)
            sensor.set_pixformat(sensor.RGB565)
            clock.tick()
            img = sensor.snapshot()
            for blob in img.find_blobs(thresholds,
            pixels_threshold=100, area_threshold=100, merge=True):
                if blob.code() == 1:
                    print("Red Found")
                    send[0]=1
                        #char r=114 byte
                if blob.code() == 2:
                    print("Yellow Found")
                    send[1]=1
                        #char y=121 byte
        print('letter')
        for i in range(72):
           #Type of frame for letter
            sensor.set_framesize(sensor.QQCIF)
            sensor.set_pixformat(sensor.GRAYSCALE)
            img= sensor.snapshot().rotation_corr(0,0,a)
            #Search for letter H
            Ha = img.find_template(template1, 0.7, step=4, search=SEARCH_EX)
            Hb = img.find_template(template2, 0.7, step=4, search=SEARCH_EX)
            Hc = img.find_template(template3, 0.7, step=4, search=SEARCH_EX)
            Hd = img.find_template(template4, 0.7, step=4, search=SEARCH_EX)
            He = img.find_template(template5, 0.7, step=4, search=SEARCH_EX)
            Hf = img.find_template(template6, 0.7, step=4, search=SEARCH_EX)
            #Search for letter S
            Sa = img.find_template(template7, 0.7, step=4, search=SEARCH_EX)
            Sb = img.find_template(template8, 0.7, step=4, search=SEARCH_EX)
            Sc = img.find_template(template9, 0.7, step=4, search=SEARCH_EX)
            Sd = img.find_template(template10, 0.7, step=4, search=SEARCH_EX)
            Se = img.find_template(template11, 0.7, step=4, search=SEARCH_EX)
            Sf = img.find_template(template12, 0.7, step=4, search=SEARCH_EX)
            Sg = img.find_template(template13, 0.7, step=4, search=SEARCH_EX)
            #Search for letter U
            Ua = img.find_template(template14, 0.7, step=4, search=SEARCH_EX)
            Ub = img.find_template(template15, 0.7, step=4, search=SEARCH_EX)
            Uc = img.find_template(template16, 0.7, step=4, search=SEARCH_EX)
            Ud = img.find_template(template17, 0.7, step=4, search=SEARCH_EX)
            Ue = img.find_template(template18, 0.7, step=4, search=SEARCH_EX)
            Uf = img.find_template(template19, 0.7, step=4, search=SEARCH_EX)
            Ug = img.find_template(template20, 0.7, step=4, search=SEARCH_EX)
            if Ha:
            #char h=104 byte
                print("Detected H")
                send[-2]=1
            if Hb:
                print("Detected H")
                send[-2]=1
            if Hc:
                print("Detected H")
                send[-2]=1
            if Hd:
                print("Detected H")
                send[-2]=1
            if He:
                print("Detected H")
                send[-2]=1
            if Hf:
                print("Detected H")
                send[-2]=1
            if Sa:
            #char s=115 byte
                print("Detected S")
                send[-1]=1
            if Sb:
                print("Detected S")
                send[-1]=1
            if Sc:
                print("Detected S")
                send[-1]=1
            if Sd:
                print("Detected S")
                send[-1]=1
            if Se:
                print("Detected S")
                send[-1]=1
            if Sf:
                print("Detected S")
                send[-1]=1
            if Sg:
                print("Detected S")
                send[-1]=1
            if Ua:
                print("Detected U")
                send[-3]=1
            if Ub:
                print("Detected U")
                send[-3]=1
            if Uc:
                print("Detected U")
                send[-3]=1
            if Ud:
                print("Detected U")
                send[-3]=1
            if Ue:
                print("Detected U")
                send[-3]=1
            if Uf:
                print("Detected U")
                send[-3]=1
            if Ug:
                print("Detected U")
                send[-3]=1
            a+=5

        if send[0]==1:
            uart.write("r")
        else:
            uart.write("a")
        if send[1]==1:
            uart.write("y")
        else:
            uart.write("b")
        if send[-2]==1:
            uart.write("h")
        else:
            uart.write("c")
        if send[-1]==1:
            uart.write("s")
        else:
            uart.write("d")
        if send[-3]==1:
            uart.write("u")
        else:
            uart.write("e")
    print(send)
    print(send[0])



