
import smtlib
sendermail = input("Enter your Gmail:")
receiversmail = input("Enter receivers Gmail:")
massage = """From: From Persone %s
To : To Person %s
subject : Sending SMTP e-mail
This is a test e-mail massage.
"""%(sendermail, receiversmail)
try:
    password = input("Enter the password:")
    smtpObj = smtplib.SMTP("gmail.com", 587)
    smtpobj.login(sendermail, password)
    smtpObj.sendmail(sendermail, receiversmail, massage)
    print("Successfully sent email")
except Exception:
    print("Error: unable to send email")
