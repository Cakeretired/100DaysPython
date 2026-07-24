import smtplib

MY_EMAIL = "jinadufahd@gmail.com"
MY_PASSWORD = "uirrpuhndqahfogq"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()

connection.login(MY_EMAIL, MY_PASSWORD)

connection.sendmail(
    from_addr=MY_EMAIL,
    to_addrs=MY_EMAIL,
    msg="Subject:Test Email\n\nHello, this is a test email"
)

connection.quit()

print("Email sent successfully!")