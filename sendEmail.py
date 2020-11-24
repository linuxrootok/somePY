#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="3050598281"    #用户名
mail_pass="ＸＸＸＸＸＸ"   #口令,需要主动发短信设置，可查询ＱＱ邮件设置


sender = '3050598281@qq.com'
receivers = ['316455517@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱,可多加

message = MIMEText('服务警告', 'plain', 'utf-8')
message['From'] = Header("服务异常", 'utf-8')
message['To'] =  Header("WARNING", 'utf-8')

subject = ('MYSQL服务出现异常','域名15秒内无响应,可能被墙了')
if len(sys.argv) == 1:
    message['Subject'] = Header(subject[0], 'utf-8')

else:
    #if int(sys.argv[1])==1:
    message['Subject'] = Header(subject[1]+sys.argv[1], 'utf-8')


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
