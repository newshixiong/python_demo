# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "xxxxx@163.com"  # 用户名
mail_pass = "xxxxxx"  # 口令


sender = mail_user
receivers = [mail_user, '635672377@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('小可爱，今天晚上我们买点板栗哦', 'plain', 'utf-8')
message['From'] = mail_user
message['To'] = "635672377@qq.com"

subject = '服务器异常情况'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    # 调试的时候可以打开
    # smtpObj.set_debuglevel(1)
    smtpObj.connect(mail_host)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
# except smtplib.SMTPException:
except:
    print("Error: 无法发送邮件")
