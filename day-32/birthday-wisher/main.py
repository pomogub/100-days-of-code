##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
#    actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# Angela's solution:

# MY_EMAIL = "YOUR EMAIL"
# MY_PASSWORD = "YOUR PASSWORD"
#
# today = datetime.now()
# today_tuple = (today.month, today.day)
#
# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])
#
#     with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )

from datetime import datetime
from smtplib import SMTP
from pandas import read_csv
from random import choice
from os import listdir

birthdays = read_csv('birthdays.csv')
my_email = 'alda.fay@ethereal.email'
password = 'f1dJ5TPZdrtb3ZcWhD' # noqa
now = datetime.now()
month = now.month
day = now.day


with open(f'./letter_templates/{choice(listdir("./letter_templates"))}', 'r') as x:
    letter = x.read()

for _, row in birthdays.iterrows():
    if row['month'] == month and row['day'] == day:
        letter = letter.replace('[NAME]', row['name'])
        with SMTP("smtp.ethereal.email", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=row['email'],  # noqa
                                msg=f"Subject:Happy Birthday!\n\n{letter}"
                                )
