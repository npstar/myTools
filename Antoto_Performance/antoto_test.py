#! /usr/bin/env python
# _*_ coding:UTF-8  _*_

'''
    @author: chengqiang.hu@jrdcom.com
    @data: 2017-04-28
'''

from uiautomator import device as d
import commands
import os
import time
import subprocess
from datetime import datetime


if d.screen == "off":
    d.screen.on()

#aa = subprocess.check_output("adb install -r ./apks/3DBench.apk", shell=True)
#print 'aa:', aa
text = os.system("adb install -r ./apks/3DBench.apk")
text1 = os.system("adb install -r ./apks/Antutu.apk")
text2 = commands.getoutput("adb shell getprop ro.product.device")
text3 = commands.getoutput("git config --global --list")
text4 = commands.getoutput("adb shell getprop ro.build.type")
#获取版本信息
text5 = commands.getoutput("adb shell getprop ro.build.description")
text6 = commands.getoutput(" date \"+%Y-%m-%d %H-%M-%S\"")
#a = time.mktime(time.strptime(text6,"%Y-%m-%d"))


print text2,text3,text6

time.sleep(10)

#print text,text1

d.press("home")
time.sleep(1)
d(description = "Apps").click()
time.sleep(1)
test1 =d(index = 1,className = "android.widget.TextView").info['text']
print test1
range1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i  in range1:
    test =d(index = i,className = "android.widget.TextView").info['text']
    print test
    if(test == "AnTuTu Benchmark"):
        d(index = i,className = "android.widget.TextView").click()
        break
