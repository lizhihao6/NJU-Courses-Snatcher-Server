#!/usr/bin/python3
# -*- coding:utf8 -*-
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import pickle

# sender_qq为发件人的qq号码
sender_qq = '' 
# pwd为qq邮箱的授权码
pwd = ''
# 收件人邮箱
receiver = ''
# 学号
userName = ''
# 密码
password = ''

def sendPic():
    # qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    # 发件人的邮箱
    sender_qq_mail = sender_qq+'@qq.com'

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'jw验证码'
    msgText = MIMEText(
        ''' 验证码''', 'html', 'utf-8')
    msgRoot.attach(msgText)
    fp = open('Code.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    msgImage.add_header('Content-ID', '')
    msgRoot.attach(msgImage)

    # ssl登录
    smtp = smtplib.SMTP_SSL(host_server)
    # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(0)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)
    smtp.sendmail(sender_qq_mail, receiver,  msgRoot.as_string())
    smtp.quit()

def login():

    codeUrl = 'http://elite.nju.edu.cn/jiaowu/ValidateCode.jsp'
    code = requests.get(url=codeUrl)
    cookies = code.cookies  # 保存验证码cookies
    f = open('Code.png', 'wb')
    f.write(code.content)  # 按照content(二进制)写入
    f.close()

    sendPic()

    codeNum = input()  # 手动打开Code.png输入验证码

    jw = requests.session()  # 开始登录教务

    data = {'userName': userName,
            'password': password,
            'returnUrl': 'null',
            'ValidateCode': codeNum}

    jwRes = jw.post("http://elite.nju.edu.cn/jiaowu/login.do", data=data, cookies=cookies)
    return cookies

if __name__ == '__main__':
    cookies  = login()
    with open('cookies','wb') as file:
        pickle.dump(cookies,file)

