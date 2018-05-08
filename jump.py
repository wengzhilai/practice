import os
import PIL, numpy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation #更新图片类
import time
need_update = True
def get_screen_imag():
    #获取手机当前屏幕
    os.system('adb shell screencap -p /sdcard/screen.png')
    #下载屏幕的图到当前文件夹
    os.system('adb pull /sdcard/screen.png')
    return numpy.array(PIL.Image.open('screen.png'))


def jump_to_next(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    print("距离：%.1f 像素" % distance)
    timsp=int(distance * 2.35)
    print("按住时长：%d 毫秒" % timsp)
    os.system('adb shell input swipe 320 410 320 410 {0} '.format(timsp))
    

def on_click(event, coor=[]):
    global need_update
    coor.append((event.xdata, event.ydata))
    if len(coor) == 2:
        jump_to_next(coor.pop(), coor.pop())
    need_update = True


def update_sceen(frame):#重画图片
    global need_update
    if need_update:
        time.sleep(1) #等跳完
        dir(axes_image)
        axes_image.set_array(get_screen_imag())
        need_update = False
    return axes_image,


figure = plt.figure()  #创建一张空白图片
axes_image = plt.imshow(get_screen_imag(), animated=True)  #把获取的照片画坐标上
figure.canvas.mpl_connect('button_press_event', on_click)
#参数1 更新对象;参数2：图片
ani = FuncAnimation(figure, update_sceen, interval=50, blit=True)
plt.show()
