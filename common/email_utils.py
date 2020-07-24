#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/24 17:21

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.local_config_utils import local_config


class EmailUtils:
    def __init__(self, smtp_body, smtp_attch_path=None):
        self.smtp_server = local_config.SMTP_SERVER
        self.smtp_sender = local_config.SMTP_SENDER
        self.smtp_password = local_config.SMTP_PASSWORD
        self.smtp_receiver = local_config.SMTP_RECEIVER
        self.smtp_cc = local_config.SMTP_CC
        self.smtp_subject = local_config.SMTP_SUBJECT
        self.smtp_body = smtp_body
        self.smtp_attch = smtp_attch_path

    def mail_message_body(self):
        meassge = MIMEMultipart()
        meassge['from'] = self.smtp_sender
        meassge['to'] = self.smtp_receiver
        meassge['Cc'] = self.smtp_cc
        meassge['subject'] = self.smtp_subject
        meassge.attach(MIMEText(self.smtp_body, 'html', 'utf-8'))
        if self.smtp_attch:
            attach_file = MIMEText(open(self.smtp_attch, 'rb').read(), 'base64', 'utf-8')
            attach_file['Content-Type'] = 'application/octet-stream'
            attach_file.add_header('Content-Disposition', 'attachment',
                                   filename=('gbk', '', os.path.basename(self.smtp_attch)))
            meassge.attach(attach_file)
        return meassge

    def send_mail(self):
        smtp = smtplib.SMTP()
        smtp.connect(self.smtp_server)
        smtp.login(user=self.smtp_sender, password=self.smtp_password)
        smtp.sendmail(self.smtp_sender, self.smtp_receiver.split(",") + self.smtp_cc.split(","),
                      self.mail_message_body().as_string())


if __name__ == '__main__':
    html_path = os.path.dirname(__file__) + r'/../test_reports/VXAPI接口自动化报告V1.0/VXAPI接口自动化报告V1.0.html'
    EmailUtils('<h3 align="center">自动化测试报告</h3>', html_path).send_mail()
