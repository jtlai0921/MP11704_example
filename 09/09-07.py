import os.path
from flask import Flask
from flask.ext.mail import Mail, Message

app = Flask(__name__)
#以126免費郵件為例
app.config['MAIL_SERVER'] = 'smtp.126.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
#如果電子郵件帳號是abcd@126.com，便應填寫abcd
app.config['MAIL_USERNAME'] = 'your own username of your email'
app.config['MAIL_PASSWORD'] = 'your own password of the username'

def sendEmail(From, To, Subject, Body, Html, Attachments):
    '''To:must be a list'''
    msg = Message(Subject, sender=From, recipients=To)
    msg.body = Body
    msg.html = Html
    for f in Attachments:
        with app.open_resource(f) as fp:
            msg.attach(filename=os.path.basename(f), data=fp.read(),
                     content_type = 'application/octet-stream')
    mail = Mail(app)
    with app.app_context():
        mail.send(msg)

if __name__=='__main__':
    #From的電子郵件帳號必須與前面相同
    From = '<your email address>'
    #這是筆者的QQ帳號，大家測試時一定要記得修改啊
    To = ['<306467355@qq.com>']
    Subject = 'hello world'
    Body = 'Only a test.'
    Html = '<h1>test test test.</h1>'
    Attachments =['c:\\python35\\python.exe']
    sendEmail(From, To, Subject, Body, Html, Attachments)
