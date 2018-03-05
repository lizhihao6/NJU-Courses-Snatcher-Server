#!/usr/bin/python3
# -*- coding:utf8 -*-
import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
import random
import pickle

# sender_qq为发件人的qq号码
sender_qq = '' 
# pwd为qq邮箱的授权码
pwd = ''
# 收件人邮箱
receiver = ''
# 选课url exp：url = "http://elite.nju.edu.cn/jiaowu/student/elective/courseList.do?method=submitDiscussRenew&classId=80071&campus=%E4%BB%99%E6%9E%97%E6%A0%A1%E5%8C%BA"
url = ''

def sendMsg(_msg):
    msg = MIMEText(_msg, 'plain', 'utf-8')
    # qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    # 发件人的邮箱
    sender_qq_mail = sender_qq+'@qq.com'
    # 邮件的正文内容
    mail_content = _msg
    # 邮件标题
    mail_title = 'Course Server'
    # ssl登录
    smtp = smtplib.SMTP_SSL(host_server)
    # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(0)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()

if __name__ == "__main__":
    succeed = False
    cookies = None
    with open('cookies','rb') as file:
        cookies = pickle.load(file)
    while not succeed:
        try:
            InAndOut = requests.post(url=url, cookies=cookies)
            html = InAndOut.text
            if "已满" in InAndOut.text:
                continue
            elif "初次登录" in InAndOut.text:
                sendMsg("Cookies TimeOut")
                break
            elif "课程选择成功" in InAndOut.text:
                succeed = True
                sendMsg("选课成功")
            elif "您的“已修通识学分+本学期已选通识学分”，在同年级学生中属于正常进度，暂时无法参加补选。" in InAndOut.text:
                sendMsg("太贪心了！")
                break
            else:
                sendMsg("蜜汁bug")
                break
            sec = random.uniform(1,2)
            time.sleep(sec)
        except:
            sendMsg("Error")
            break