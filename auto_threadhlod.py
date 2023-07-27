import sensor, image, time
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # 颜色跟踪必须关闭自动增益
sensor.set_auto_whitebal(False) # 颜色跟踪必须关闭白平衡
sensor.set_auto_exposure(8300) #设置一个固定曝光时间
clock = time.clock()

# 捕捉图像中心的颜色阈值。
r = [(320//2)-(50//2), (240//2)-(50//2), 50, 50] # 50x50 center of QVGA.
for i in range(60):
    img = sensor.snapshot()
    img.draw_rectangle(r)
    hist = img.get_histogram(roi=r)#获取直方图
    a = hist.get_statistics()

k=[(a[2]-25,a[2]+25,a[10]-25,a[10]+25,a[18]-25,a[18]+25)]

while(True):
    clock.tick()
    img = sensor.snapshot()
    img.binary(k)#二值化图像

