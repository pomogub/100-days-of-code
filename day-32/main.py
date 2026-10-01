# # Name 	Alda Fay
#
# my_email = 'alda.fay@ethereal.email'
# password = 'f1dJ5TPZdrtb3ZcWhD' # noqa
#
# with smtplib.SMTP("smtp.ethereal.email", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs='loscakes@gmail.com', # noqa
#                         msg="Subject:Hello\n\nJust checking in on you."
#                         )

import datetime as dt
from random import choice
import smtplib

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
my_email = 'alda.fay@ethereal.email'
password = 'f1dJ5TPZdrtb3ZcWhD' # noqa

with open('quotes.txt', 'r') as file:
    quotes = [line.strip() for line in file.readlines()]
random_quote = choice(quotes)

if day_of_week == 1:
    with smtplib.SMTP("smtp.ethereal.email", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='loscakes@gmail.com', # noqa
                            msg=f"Subject:Motivational Monday!\n\n{random_quote}"
                            )
