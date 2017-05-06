#! /usr/bin/env python
# _*_ coding:UTF-8 _*_

'''
    @author chengqiang.hu
    @date 2017-05-05
'''

import commands
import os
from uiautomator import device as d
import time
import logging

class Antutu(object):
    __install_3Dbench_command = "adb install -r ./apks/3DBench.apk"
    __install_Antutu_command = "adb install -r ./apks/Antutu.apk"
    __project_name_command = "adb shell getprop ro.product.device"
    __tester_email_command = "git config --global --list"
    __version_type_command = "adb shell getprop ro.build.type"
    __project_version_command = "adb shell getprop ro.build.description"
    __test_time_command = "date \"+%Y-%m-%d\""

    data = {}
    __project_name = ""
    __project_version = ""
    __version_type = ""
    __version_time = ""
    __test_time = ""
    __tester_email = ""
    __review_tester_email = ""
    __thirdD_num = ""
    __marooned_num = ""
    __garden_num = ""
    __UX_num = ""
    __data_Secure = ""
    __data_process = ""
    __strategy_games = ""
    __image_process = ""
    __io_performance = ""
    __CPU_num = ""
    __mathematics = ""
    __common_Use = ""
    __multi_Core = ""
    __RAM = ""
    __RAM_num = ""
    __total_score = ""


    def get_project_information(self):
        self.project_name = commands.getoutput(self.__project_name_command)
        self.project_version = commands.getoutput(self.__project_version_command).split()[3].split("-")[0]
        self.version_type = commands.getoutput(self.__version_type_command)
        self.version_time = ""
        self.test_time = commands.getoutput(self.__test_time_command)
        self.tester_email = commands.getoutput(self.__tester_email_command).split("user.email=")[1].split("\n")[0]
        self.review_tester_email = "chengqiang.hu@jrdcom.com"
        #print project_name,project_version,version_type,version_time,test_time,tester_email,review_tester_email

    def install_antutu_apk(self):
        os.system(self.__install_3Dbench_command)
        os.system(self.__install_Antutu_command)

    def text_click(self,text):
        if (d(text = text).exists):
            d(text = text).click()
            time.sleep(1)
        else:
            d(scrollable = True).scroll.to(text = text)
            d(text = text).click()
            time.sleep(3)

    def description_click(self,description):
        if (d(description = description).exists):
            d(description = description).click()
            time.sleep(1)
        else:
            d(scrollable = True).scroll.to(description = description)
            d(description = description).click()
            time.sleep(3)

    def setting_env(self):
        if (d.screen == "off"):
            d.screen.on()
        time.sleep(1)
        d.press.home()
        d(description="Apps").click()
        time.sleep(1)

        self.description_click("Settings")

        self.text_click("Lock screen")

        self.text_click("Screen lock")

        self.text_click("None")
        d.press.back()
        self.text_click("Display")
        self.text_click("Sleep")
        self.text_click("Never")
        d.press.back()
        self.text_click("Apps")
        self.text_click("AnTuTu Benchmark")
        self.text_click("Permissions")
        if(d(text = "Call").exists):
            self.text_click("Call")
        if(d(text = "Phone").exists):
            self.text_click("Phone")
        self.text_click("Camera")
        self.text_click("Location")
        self.text_click("Storage")

    def run_Antutu(self):
        d.press.home()
        d(description="Apps").click()
        self.description_click("AnTuTu Benchmark")
        time.sleep(5)
        d(resourceId = "com.antutu.ABenchMark:id/start_test_region").click()
        #time.sleep(600)

    def get_score_action(self,text):
        maohao = d(text = text).right(className = "android.widget.TextView")
        data = maohao.right(resourceId="com.antutu.ABenchMark:id/tv_score").info['text']
        return data

    def get_totalScore(self):
        expand = d(className="android.widget.ExpandableListView")
        linear = expand.child(className="android.widget.LinearLayout", index=0)
        self.total_score = linear.child(resourceId="com.antutu.ABenchMark:id/tv_score", index=0).info['text']
        time.sleep(1)
        return self.total_score

    def get_score(self):

        run_antutuIsEnd = True

        self.run_Antutu()

        while True and run_antutuIsEnd:
            if(d(resourceId="com.antutu.ABenchMark:id/tv_score", index=0).exists):
                run_antutuIsEnd = False
                print "ok"
                self.get_allscore_antion()
            else:
                time.sleep(5)
                print "not ok"

    def get_allscore_antion(self):
        thirdD = d(text="3D")
        self.thirdD_num = self.get_score_action("3D")
        time.sleep(1)
        thirdD.click()
        self.marooned_num = self.get_score_action("3D [Marooned]")
        time.sleep(1)
        self.garden_num = self.get_score_action("3D [Garden]")
        time.sleep(1)
        thirdD.click()

        UX = d(text="UX")
        self.UX_num = self.get_score_action("UX")
        time.sleep(1)
        UX.click()
        self.data_Secure = self.get_score_action("UX Data Secure")
        time.sleep(1)
        self.data_process = self.get_score_action("UX Data process")
        time.sleep(1)
        self.strategy_games = self.get_score_action("UX Strategy games")
        time.sleep(1)
        self.image_process = self.get_score_action("UX Image process")
        time.sleep(1)
        self.io_performance = self.get_score_action("UX I/O performance")
        time.sleep(1)
        UX.click()

        CPU = d(text="CPU")
        self.CPU_num = self.get_score_action("CPU")
        time.sleep(1)
        CPU.click()
        self.mathematics = self.get_score_action("CPU Mathematics")
        time.sleep(1)
        self.common_Use = self.get_score_action("CPU Common Use")
        time.sleep(1)
        self.multi_Core = self.get_score_action("CPU Multi-Core")
        time.sleep(1)
        CPU.click()

        self.RAM = d(text="RAM")
        self.RAM_num = self.get_score_action("RAM")
        time.sleep(1)

        return True

    def get_data(self):
        self.get_project_information()
        self.get_score()
        self.get_totalScore()

        self.data['project'] = self.project_name
        self.data['version'] = self.project_version
        self.data['versin_type'] = self.version_type
        self.data['version_time'] = "2017-05-06"
        self.data['test_time'] = self.test_time
        self.data['tester_email'] = self.tester_email
        self.data['reviewer_email'] = self.review_tester_email
        self.data['total_num'] = self.total_score
        self.data['3D'] = self.thirdD_num
        self.data['3D [Marooned]'] = self.marooned_num
        self.data['3D [Garden]'] = self.garden_num
        self.data['UX'] = self.UX_num
        self.data['UX Data Secure'] = self.data_Secure
        self.data['UX Data process'] = self.data_process
        self.data['UX Strategy games'] = self.strategy_games
        self.data['UX Image process'] = self.image_process
        self.data['UX I/O performance'] = self.io_performance
        self.data['CPU'] = self.CPU_num
        self.data['CPU Mathematics'] = self.mathematics
        self.data['CPU Common Use'] = self.common_Use
        self.data['CPU Multi-Core'] = self.multi_Core
        self.data['RAM'] = self.RAM_num
        self.data['is_frozen'] = False
        self.data['hardware_version'] = "PIO02"
        self.data['notes'] = "NONE"

        print self.data
        return self.data



    def runtest(self):
        logging.info("start test")
        self.install_antutu_apk()
        self.setting_env()
        self.get_data()

        return self.data


if __name__ == "__main__":
    antutu = Antutu()
    antutu.runtest()
