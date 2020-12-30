import sensor, image, time, lcd

lcd.init(freq=15000000)
sensor.reset()

sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()
sensor.set_vflip(1)
sensor.set_hmirror(1)

x1 = 156
x2 = 226
y1 = 64
y2 = 130

clock.tick()
img = sensor.snapshot()
img.draw_rectangle(156,64,70,66, color = (0,0,0))

while x1 < x2:
        while y1 < y2:
            cor = []
            cor = img.get_pixel(x1,y1)
            if((cor[0] + cor[1] + cor[2]) > 127):
                img.set_pixel(x1,y1, color=(255,255,255))
            else:
                img.set_pixel(x1,y1, color=(127,127,127))
            y1 = y1 + 1
        x1 = x1 + 1
        y1 = 60
res = img.find_qrcodes()
if len(res) > 0:
    img.draw_string(2,2, res[0].payload(), color=(0,128,0), scale=2)
    v = res[0].payload()
    print(v)
lcd.display(img)
print(clock.fps())



