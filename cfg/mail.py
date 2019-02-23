from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL


class Mail:
    def __init__(self, address, message=''):
        self.source = 'register@s-savelyev.ru'
        self.pw = 'StepanidA2000'
        self.destination = address
        self.message = message

        self.msg = MIMEMultipart()
        self.msg['From'] = self.source
        self.msg['To'] = self.destination
        self.msg['Subject'] = "Subscription"

        addr = 'smtp.mail.ru'
        port = 465

        print('Connect to SMTP..')
        self.server = SMTP_SSL(f'{addr}:{port}')
        print('Login..')
        self.server.login(self.source, self.pw)
        print('Connected.')

    def send(self):
        print('Send message..')
        message = "Header\nHello!"

        self.msg.attach(MIMEText(message, 'plain'))

        self.server.sendmail(self.source, self.destination, self.msg.as_string())
        print('Mail sent.')

    def __del__(self):
        print('Disconnect..')
        self.server.quit()
        print('Disconnected.')


if __name__ == '__main__':
    server = Mail('savelyev_stepan@mail.ru')
    server.send()
    exit(0)
