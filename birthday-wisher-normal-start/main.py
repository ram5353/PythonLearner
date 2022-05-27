from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "ayansh5677@gmail.com"
MY_PASSWORD = "Ramkiran@123"

now = datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

birthdays_data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (index, row) in birthdays_data.iterrows()}

if today in birthdays_dict:
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as letter:
        birthday_person = birthdays_dict[today]
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
