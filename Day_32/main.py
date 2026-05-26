import smtplib

if __name__ == "__main__":
    my_email = input("typer user: ")
    password = input("type password: ")

    connection = smtplib.SMTP("smtp.gmail.com")
    _ = connection.starttls()
    _ = connection.login(user=my_email, password=password)

    _ = connection.sendmail(from_addr=my_email, to_addrs=input("type addr: "), msg="Hello")

    connection.close()
