from public.readconf import Readconfig
from public.weblog import MyLog
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib


logger = MyLog().get_logger()


# 发送通知邮件
def send_mail(text, file):
    sender = Readconfig().get_value('EMAIL', 'sender')
    receiver = Readconfig().get_value('EMAIL', 'receiver')
    subject = Readconfig().get_value('EMAIL', 'subject')
    smtpserver = Readconfig().get_value('EMAIL', 'smtpserver')
    password = Readconfig().get_value('EMAIL', 'password')

    # 组装邮件标题和内容
    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver

    # 邮件正文内容
    msg.attach(MIMEText(text, 'plain', 'utf-8'))

    fp = None
    try:
        fp = open(file, 'rb')
    except FileNotFoundError:
        logger.error("此文件路径有误 {} ！".format(file), exc_info=True)
        exit()
    # 构造附件，传送新生成的测试报告
    attachment = MIMEText(fp.read(), 'base64', 'utf-8')
    attachment["Content-Type"] = 'application/octet-stream'
    # 这里的filename即邮箱中显示的附件名，理论可以随便设置
    # 我这里依然使用原文件名，可以用file[-35:]从文件路径中截取
    attachment["Content-Disposition"] = 'attachment; filename="' + file[-35:] + '"'
    msg.attach(attachment)

    # 登录并发送邮件
    smtp = smtplib.SMTP()
    try:
        smtp.connect(smtpserver)
        smtp.login(sender, password)
        smtp.sendmail(sender, msg['To'].split(";"), msg.as_string())
        logger.info('邮件发送成功！')
        # print("邮件发送成功！")
    except:
        logger.error('邮件发送失败', exc_info=True)
        # print("邮件发送失败！")
    finally:
        smtp.quit()
        fp.close()


# 测试代码
if __name__ == "__main__":
    filename = 'C:\\Users\\Administrator\\Desktop\\web_auto\\result\\testreport\\test.txt'
    text = "最新Web自动化测试报告请接收，见附件。"
    send_mail(text, filename)
