# coding:utf-8

import smtplib
import poplib
import email
from email.mime.text import MIMEText
from email.header import decode_header 
from email.header import Header
import os
import time

#定义全局变量
_email = "andy_52010@sina.com"
_password = "**************";
"""
此函数用来重置邮箱里面的内容，如果不重置，下次打开程序就会立即获取邮箱里面的命令（关机）
"""
def _reset():
	#连接到发件服务器
    sent=smtplib.SMTP()
    sent.connect('smtp.sina.com')
    sent.login(_email, _password)
    
	#创建邮件内容
    content=MIMEText('reset shutdown', "html", _charset='utf-8')
    content['Subject']=Header('reset', 'utf-8')
    content['From'] = _email
    sent.sendmail(_email, _email, content.as_string())
    sent.close()

"""
用POP3来读取远程邮箱内容作为命令
"""
while True:
    host='pop.sina.com'
    _read=poplib.POP3(host)
    _read.user(_email)
    _read.pass_(_password)
    total=_read.stat()
    
    str=_read.top(total[0],0)
    strr=[]
    for x in str[1]:
        try:
            strr.append(x.decode())
        except:
            try:
                strr.append(x.decode('gbk'))
            except:
                strr.append(x.decode('big5'))
    msg=email.message_from_string('\n'.join(strr))
    Titt=decode_header(msg['subject'])

    if Titt[0][1]:
        ttle=Titt[0][0].decode(Titt[0][1])
    else:
        ttle=Titt[0][0]
    if ttle=='shutdown':
        print ttle
        _reset()
        
        os.system('shutdown -s -t 10')
        