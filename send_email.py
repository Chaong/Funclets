from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


EMAIL_TITLE = "蒲公英的验证码"   # 邮件标题
SENDER_NAME = "蒲公英"   # 发送者姓名
SENDER_EMAIL = "hi@puonin.com"   # 发送者邮箱

SMTP = "smtp.exmail.qq.com"   # 发送邮件服务器
PASSWORD = ""   # 授权码


def send_email(receiver, ecode):
    """
    发送验证码样式的电子邮件
    参数 - receiver : 收件人邮箱地址
    参数 - ecode : 验证码
    """

    # 邮件内容
    user = receiver.split("@")[0]   # 获得邮箱昵称
    title = "蒲公英"
    greet_1 = f"嘿，亲爱的 {user}"
    greet_2 = "下面的神秘蓝色代码是你在蒲公英网所获取的验证码："
    prompt_1 = "蒲公英的小提示：如果你并未在蒲公英网获取过该验证码，"
    prompt_2 = "也许是其他用户注册或找回密码，误输你的邮箱而使你收到了这封邮件。"
    prompt_3 = "你可以放心忽略此邮件。当然，你也可以选择登录蒲公英网修改密码。"
    prompt_4 = "最后，若有任何问题，可以联系我们，我们将尽快为你解答 ~"
    domain = "puonin.com"
    content = "<table cellspacing='0' style='margin: 0 auto;'>" \
              "<tr>" \
              "<td style='padding: 30px; background-color: #007bff; border-top-left-radius: 0.25rem; border-top-right-radius: 0.25rem;'>" \
              f"<h2 style='margin: 0; color: #ffffff;'>{title}</h2>" \
              "</td>" \
              "</tr>" \
              "<tr>" \
              "<td style='padding: 30px; border: 1px solid #f0f2f7; border-top: none; border-bottom-left-radius: 0.25rem; border-bottom-right-radius: 0.25rem;'>" \
              f"<p style='margin: 0;'>{greet_1}</p>" \
              f"<p>{greet_2}</p>" \
              f"<h1 style='color: #007bff; margin-top: 100px; margin-bottom: 100px; text-align: center;'>{ecode}</h1>" \
              "<hr style='border: 1px dashed #c5c5c5; margin-bottom: 30px;'/>" \
              f"<p style='color: #c5c5c5;'>{prompt_1}</p>" \
              f"<p style='color: #c5c5c5;'>{prompt_2}</p>" \
              f"<p style='color: #c5c5c5;'>{prompt_3}</p>" \
              f"<p style='color: #c5c5c5;'>{prompt_4}</p>" \
              f"<p style='margin: 0; color: #c5c5c5; text-align: right;'>{domain}</p>" \
              "</td>" \
              "</tr>" \
              "</table>"

    # 定义MIMEText
    mail = MIMEText(content, "html", "utf-8")   # 实例化邮件对象，并指定格式和编码
    mail["Subject"] = Header(EMAIL_TITLE, "utf-8")   # 邮件标题以及编码
    mail["From"] = formataddr(pair=(SENDER_NAME, SENDER_EMAIL))   # 发件人
    mail["To"] = receiver   # 收件人

    # 定义SMTP_SSL
    smtp = SMTP_SSL(SMTP)   # 接收邮件服务器
    smtp.login(user=SENDER_EMAIL, password=PASSWORD)   # 发送者邮件和授权码
    smtp.sendmail(SENDER_EMAIL, receiver, str(mail))   # 发送者邮件、接收者邮件、邮件对象
    smtp.quit()   # 关闭连接


if __name__ == "__main__":
    
    send_email("", "Puonin")   # 收件人邮箱、验证码
