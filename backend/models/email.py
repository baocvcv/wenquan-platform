""" Email verification model """
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from .user import User

class EmailVerificationRecord(models.Model):
    """ Email verification for user """
    email_type = (("register",u"Register"), ("forget",u"Reset password"))

    token = models.CharField(max_length=20, verbose_name=u"Code")
    email = models.EmailField(max_length=50, verbose_name=u"Email")
    send_type = models.CharField(verbose_name=u"Verification type", max_length=10, choices=email_type)
    send_time = models.DateTimeField(verbose_name=u"Send time")

    is_valid = models.BooleanField(default=True)

    user = models.ForeignKey("backend.User", verbose_name=u"User", on_delete=models.CASCADE)

    class Meta:
        """ meta """
        verbose_name = u"Email verification code"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        """ to unicode """
        return '{0}({1})'.format(self.code, self.email)

    def send_email(self):
        # 初始化为空
        email_title = ""
        email_body = ""
        # 如果为注册类型
        if send_type == "register":
            email_title = "注册激活链接"
            email_body = "请点击下面的链接激活你的账号:http://127.0.0.1:8000/active/{0}".format(code)
            # 发送邮件
            send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
