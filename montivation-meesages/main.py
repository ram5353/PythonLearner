import smtplib
import datetime as dt
import random


def send_mail(quote):
    my_email = "ayansh5677@gmail.com"
    password = "Ramkiran@123"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="kiranram306@gmail.com",
                            msg=f"Subject:Thursday Motivational Quote\n\n{quote}")
        connection.close()


with open("quotes.txt", mode="r") as quote_file:
    content = quote_file.readlines()
print(content)

now = dt.datetime.now()
week = now.weekday()

print(week)

motivational_quote = random.choice(content)
print(motivational_quote)


if week == 3:
    send_mail(motivational_quote)
