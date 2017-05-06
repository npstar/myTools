#!/usr/bin/python
# _*_ coding:utf-8 _*_

from uiautomator import device as d
import time
import commands
import urllib2
import urllib
import json


d.screen.on()

data = {}

def get_num(text):
    maohao = d(text=text).right(className="android.widget.TextView")
    data = maohao.right(resourceId="com.antutu.ABenchMark:id/tv_score").info['text']
    return data

def s(num):
    time.sleep(num)

expand = d(className="android.widget.ExpandableListView")
linear = expand.child(className="android.widget.LinearLayout",index=0)
total_num = linear.child(resourceId="com.antutu.ABenchMark:id/tv_score",index=0).info['text']
s(1)

thirdD = d(text="3D")
thirdD_num = get_num("3D")
s(1)
thirdD.click()
marooned_num = get_num("3D [Marooned]")
s(1)
garden_num = get_num("3D [Garden]")
s(1)
thirdD.click()

UX = d(text="UX")
UX_num = get_num("UX")
s(1)
UX.click()
data_Secure = get_num("UX Data Secure")
s(1)
data_process = get_num("UX Data process")
s(1)
strategy_games = get_num("UX Strategy games")
s(1)
image_process = get_num("UX Image process")
s(1)
io_performance = get_num("UX I/O performance")
s(1)
UX.click()

CPU = d(text="CPU")
CPU_num = get_num("CPU")
s(1)
CPU.click()
mathematics = get_num("CPU Mathematics")
s(1)
common_Use = get_num("CPU Common Use")
s(1)
multi_Core = get_num("CPU Multi-Core")
s(1)
CPU.click()

RAM = d(text = "RAM")
RAM_num = get_num("RAM")
s(1)

# 项目名
project = commands.getoutput("adb shell getprop ro.product.device")
# 检测人邮件
text3 = commands.getoutput("git config --global --list")
emailStr = text3.split()
x = emailStr[1]
a = x.split('=')
email = a[1]

#版本类型
projectType = commands.getoutput("adb shell getprop ro.build.type")

#项目版本
text5 = commands.getoutput("adb shell getprop ro.build.description")
d = text5.split()
b = d[3]
o = b.split("-")
projectVersion = o[0]

#测试时间
test_time = commands.getoutput('date "+%Y-%m-%d"')


data['project'] = project
data['version'] = projectVersion
data['version_time'] = ""
data['test_time'] = test_time
data['tester_email'] = email
data['reviewer_email'] = email
data['total_num'] = total_num
data['3D'] = thirdD_num
data['3D [Marooned]'] = marooned_num
data['3D [Garden]'] = garden_num
data['UX'] = UX_num
data['UX Data Secure'] = data_Secure
data['UX Data process'] = data_process
data['UX Strategy games'] = strategy_games
data['UX Image process'] = image_process
data['UX I/O performance'] = io_performance
data['CPU'] = CPU_num
data['CPU Mathematics'] = mathematics
data['CPU Common Use'] = common_Use
data['CPU Multi-Core'] = multi_Core
data['RAM'] = RAM_num
data['is_frozen'] = False
data['hardware_version'] = ""
data['notes'] = ""

try:
    response = None
    # data = {'project': 'MICKEY6US', 'version': 'AF6', 'version_time': '1900-01-01', 'test_time': '2017-04-27', 'tester_email': 'chao.wang@jrdcom.com', 'reviewer_email': 'xiaobo.zhu@tcl.com', 'score': 17018, 'third_score': 1568, 'third_marooned_score': 5876, 'third_garden_score': 10457, 'ux_score': 5626, 'ux_data_secure_score': 2456, 'ux_data_process_score': 5648, 'ux_strategy_games_score': 6845, 'ux_image_process_score': 9854, 'ux_io_performance_score': 4568, 'cpu_score': 2485, 'cpu_mathematics_score': 8564, 'cpu_commom_use_score': 3254, 'cpu_multi_score': 8542, 'ram_score': 4557, 'is_frozen': False, 'hardware_version': 'PIO01', 'notes': 'just test'}
    url_values = urllib.urlencode(data)
    url = "http://172.24.218.40:8008/antutu_write_interface"
    full_url = url + '?' + url_values
    request = urllib2.Request(url, url_values)
    response = urllib2.urlopen(request)
    result = json.loads(response.read())
    if not result.get('state'):
        print "Error => %s"%result['errorMsg']

except urllib2.HTTPError, e:
    print 'Error code: %s'%e.code
except urllib2.URLError, e:
    print 'Error reason: %s'%e.reason

finally:
    if response:
        response.close()


