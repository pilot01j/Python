#
# --------------------- SEND EMAIL MESSAGES--------------- #
# import smtplib
# my_email = "mucuta@yahoo.com"
# gmail_password = "Tekwill4848@"
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=gmail_password)
#     connection.sendmail(from_addr=my_email, to_addrs="pilot01j@gmail.com",
#                         msg="Subject:Hello Python\n\n This is may email")
#
#
# --------------------- SEND DAILY EMAIL QUOTES --------------- #
import smtplib
import datetime as dt
import random

MY_EMAIL = "pilot01j@gmail.com"
GMAIL_PASSWORD = "Maib4848@"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, GMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Daily Motivation\n\n{quote}"
        )
