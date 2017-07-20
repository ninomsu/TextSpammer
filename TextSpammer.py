import time
import smtplib
count = 0
server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( 'Your email', 'Your password' )

while(count < 1000):
    cout += 1
    server.sendmail( 'From email', 'PhoneNumber@mms.att.net', 'Message you want to spam with' )
    time.sleep(1)

