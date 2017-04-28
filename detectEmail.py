# coding:utf-8

import poplib
from email.header import decode_header
import email

_email = "andy_52010@126.com"
_password = "***********"

host='pop.sina.com'
read=poplib.POP3(host)
read.user(_email)
read.pass_(_password)
#使用帐号密码登录

a=read.stat()
print a
