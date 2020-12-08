from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


# 邮件内容信息
product_name = "产品名称"
remark_info = "备注信息"
product_domain = "产品域名"

# 邮件主要信息
email_title = "邮件标题"
sender_name = "发件人姓名"
sender_email = "发件人邮箱"

# 邮件服务器和授权码
smtp_ssl = "发送邮件服务器"
password = "授权码"


# 发送 QQ 邮箱验证码，参数为收件箱地址和随机生成的验证码
def send_email(receiver, ecode):
    content = "<div style='width: 400px; padding: 20px 30px; border: 1px solid #007bff; background-color: #007bff; margin: 0 auto; border-radius: 0.25rem 0.25rem 0 0;'>" \
              "<span style='font-weight: bold; color: #ffffff;'>" \
              f"<h2 style='margin: 0;'>{product_name}</h2>" \
              "</span>" \
              "</div>" \
              "<div style='width: 400px; padding: 30px; border: 1px solid #f0f2f7; border-top: none; margin: 0 auto; border-radius: 0 0 0.25rem 0.25rem;'>" \
              "<span>亲爱的用户</span>" \
              f"<p>以下是邮箱 <span style='color: #007bff;'>{receiver}</span> 所需要的验证码：</p>" \
              f"<h1 style='color: #007bff; margin: 100px 0 100px 0; text-align: center;'>{ecode}</h1>" \
              "<hr style='height: 1px; border: none; border-top: 1px dashed #c5c5c5; margin-bottom: 30px;'/>" \
              f"<p style='color: #c5c5c5;'>{remark_info}</p>" \
              f"<div style='color: #c5c5c5; text-align: right;'>{product_domain}</div>" \
              "</div>"
    message = MIMEText(content, "html", "utf-8")   # 实例化邮件对象，并指定格式和编码
    message["Subject"] = Header(email_title, "utf-8")   # 邮件标题以及编码
    message["From"] = formataddr(pair=(sender_name, sender_email))   # 发件人
    message["To"] = receiver   # 收件人

    smtp = SMTP_SSL(smtp_ssl)
    smtp.login(user=sender_email, password=password)   # 授权码
    smtp.sendmail(sender_email, receiver, str(message))
    smtp.quit()


if __name__ == "__main__":
    send_email("接收人邮件", "随机验证码")