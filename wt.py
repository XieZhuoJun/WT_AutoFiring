#############
#War Thunder# 
#Auto Firing#
#############

#running on Python2.7#

#work With following libs:#

import time
import csv
from PIL import ImageGrab
import win32api,win32gui,win32con

#左键单击事件
def clickLeftCur():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN or win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

#自动射击次数计数
aim = 0 
#设置瞄准区矩形范围,当前值为1080P分辨率下的较优值
x1=850
x2=1150
y1=225
y2=625
ran = (x1,y1,x2,y2)

#主循环函数
while(True):
    beg = time.time()   #计时器开始
    #截图
    im = ImageGrab.grab(ran)
    pix = im.load()     #重置flag
    s_found=0
    X=0
    Y=0
    #在瞄准区寻找RGB值为 0 255 0 的点，即绿色准心
    for x in range(0,x2-x1,5): 
        if s_found == 1:
            break
        for y in range(0,y2-y1,5):
            r, g, b = pix[x, y]
            if (r,g,b)==(0,255,0):
                print("AIMED! time: "+str(aim)+" x:"+str(x)+" y:"+str(y))   #输出目标坐标
                end = time.time()   #计时器停止
                print(end-beg)      #输出延迟时间
                s_found=1           #flag置1
                aim+=1              #计数+1
                clickLeftCur()      #单击左键射击

                #储存日志文件，用于分析准心分布范围
                #csvFile=open("aimpoint.csv","ab+")
                #writer=csv.writer(csvFile)
                #writer.writerow([x+x1,y+y1])
                #csvFile.close()

                break