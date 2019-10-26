""" Email verification model """
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from .user import User

class EmailVerificationRecord(models.Model):
    """ Email verification for user """
    email_type = (("register",u"Register"), ("forget",u"Reset password"))

    token = models.CharField(max_length=50, verbose_name=u"Code")
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
        if self.send_type == "register":
            email_title = "[Wen Quan Platform] Activate your account"
            # local test
            # email_body = "Please click this link to activate your account: http://127.0.0.1:8000/active/{0}".format(self.token)
            # remote deploy
            email_body = "Please click this link to activate your account: http://https://never404-never404.app.secoder.net:8000/active/{0}".format(self.token)
            # 发送邮件
            print(email_title)
            send_status = self.user.email_user(email_title, email_body)
            # send_status = send_mail(email_title, email_body, "a@b.com", [self.email])
            print(email_body)
        if send_status:
            pass
