""" Email verification model """
from django.db import models
from django.conf import settings
from django.core.mail import send_mail

class EmailVerificationRecord(models.Model):
    """ Email verification for user """
    expiration_time = 24 # hours
    email_type = (("register", u"Register"), ("forget", u"Reset password"))

    token = models.CharField(max_length=50, verbose_name=u"Code")
    email = models.EmailField(max_length=50, verbose_name=u"Email")
    send_type = models.CharField(
        verbose_name=u"Veification type",
        max_length=10, choices=email_type)
    send_time = models.DateTimeField(verbose_name=u"Send time", auto_now=True)

    is_valid = models.BooleanField(default=True)

    user = models.ForeignKey("backend.User", verbose_name=u"User", on_delete=models.CASCADE)

    class Meta:
        """ meta """
        verbose_name = u"Email verification code"
        verbose_name_plural = verbose_name

    def __str__(self):
        """ to str """
        return '{0}({1})'.format(self.token, self.email)

    def send_email(self):
        """ send email to user """
        email_title = ""
        email_body = "Dear " + self.user.username + ":"
        # local test
        # domain = "https://127.0.0.1:8000"
        domain = "https://never404-never404.app.secoder.net"
        if self.send_type == "register": # if register
            email_title = "[Wen Quan Platform] Activate your account"
            url = domain + "/#/activate/{0}".format(self.token)
            email_body_plain = email_body + "\nPlease click this link to activate your account: "
            email_body_plain += url
            email_body_html = email_body + """<div><br></div>Welcome to <b>WenQuan Platform</b>!<br>
Please click <a href="%s" target="_blank">this link</a> to activate your account.
</div><div><br></div><div>Best regards,</div><div>WenQuan Platform</div>""" % url
            send_mail(
                email_title,
                email_body_plain,
                settings.DEFAULT_FROM_EMAIL,
                [self.email],
                html_message=email_body_html
                )
        elif self.send_type == "forget":
            email_title = "[Wen Quan Platform] Change your password"
            url = domain + "/#/forget_password/{0}".format(self.token)
            email_body_plain = "\nPlease click this link to change your password: " + url
            email_body_html = email_body + """<div><br></div>
Please click <a href="%s" target="_blank">this link</a> to change your password.
</div><div><br></div><div>Best regards,</div><div>WenQuan Platform</div>""" % url
            # send email
            # self.user.email_user(email_title, email_body)
            send_mail(
                email_title,
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                [self.email],
                html_message=email_body_html
                )

    def is_time_valid(self, time):
        """ check if time is valid """
        return (time - self.send_time).seconds < self.expiration_time * 3600
