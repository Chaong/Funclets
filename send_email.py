from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


EMAIL_TITLE = ""   # 邮件标题
SENDER_NAME = ""   # 发送者姓名
SENDER_EMAIL = ""   # 发送者邮箱

SMTP = ""   # 发送邮件服务器
PASSWORD = ""   # 授权码


def send_email(receiver, ecode):
    """
    发送验证码样式的电子邮件
    参数 - receiver : 收件人邮箱地址
    参数 - ecode : 验证码
    """
    # HTML Message
    title = ""
    greet_one = ""
    greet_two = ""
    greet_three = ""
    remark_one = ""
    remark_two = ""
    remark_three = ""
    remark_four = ""
    domain = ""
    content = "<table cellspacing='0' style='margin: 0 auto;'>" \
              "<tr>" \
              "<td style='padding: 30px; background-color: #007bff; border-top-left-radius: 0.25rem; border-top-right-radius: 0.25rem;'>" \
              f"<h2 style='margin: 0; color: #ffffff;'>{title}</h2>" \
              "</td>" \
              "</tr>" \
              "<tr>" \
              "<td style='padding: 30px; border: 1px solid #f0f2f7; border-top: none; border-bottom-left-radius: 0.25rem; border-bottom-right-radius: 0.25rem;'>" \
              f"<p style='margin: 0;'>{greet_one}</p>" \
              f"<p>{greet_two}<span style='color: #007bff;'>{receiver}</span>{greet_three}</p>" \
              f"<h1 style='color: #007bff; margin-top: 100px; margin-bottom: 100px; text-align: center;'>{ecode}</h1>" \
              "<hr style='border: 1px dashed #c5c5c5; margin-bottom: 30px;'/>" \
              f"<p style='color: #c5c5c5;'>{remark_one}</p>" \
              f"<p style='color: #c5c5c5;'>{remark_two}</p>" \
              f"<p style='color: #c5c5c5;'>{remark_three}</p>" \
              f"<p style='color: #c5c5c5;'>{remark_four}</p>" \
              f"<p style='margin: 0; color: #c5c5c5; text-align: right;'>{domain}</p>" \
              "</td>" \
              "</tr>" \
              "</table>"
    mail = MIMEText(content, "html", "utf-8")   # 实例化邮件对象，并指定格式和编码
    mail["Subject"] = Header(EMAIL_TITLE, "utf-8")   # 邮件标题以及编码
    mail["From"] = formataddr(pair=(SENDER_NAME, SENDER_EMAIL))   # 发件人
    mail["To"] = receiver   # 收件人

    smtp = SMTP_SSL(SMTP)   # 接收邮件服务器
    smtp.login(user=SENDER_EMAIL, password=PASSWORD)   # 发送者邮件和授权码
    smtp.sendmail(SENDER_EMAIL, receiver, str(mail))   # 发送者邮件、接收者邮件、邮件对象
    smtp.quit()   # 关闭连接


if __name__ == "__main__":
    
    send_email("", "")
