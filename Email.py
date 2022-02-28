import smtplib, ssl
used_emails = open("used_emails.txt", "w")
used_emails.close()
used_emails = open("used_emails.txt", "r")
if used_emails.read() == "":
    used_emails.close()
    used_emails = open("used_emails.txt", "w")
    used_emails.write("[reyanshja@outlook.com]")
    used_emails.close()
    used_emails = open("used_emails.txt", "r")
    
used_email_list = list(used_emails.read())
used_emails.close()
for x in range(len(used_email_list)):
    print(x, used_email_list[x-1])
    
port = 587
smtp_server = "smtp.outlook.com"
sender_email = input("What is your email? ")
password = input("WHat is your password? ")
receiver_email_list = []

while True:
    receiveremail = input("What e-mail are you going to send this too? Type in STOP to keep on going.")
    if receiveremail.lower() == "stop":
        break
    else:
        receiver_email_list.append(receiveremail)
        
subject = input("What shall be the subject? ")
msg = input("What shall be the message? ")
pystamp = input("Should we put the python stamp at the end of the message? Yes or No?")
if pystamp.lower() == "yes":
    pystamp = "This message is sent from Python."
else:
    pystamp = ""
message = f"""\
Subject: {subject}

{msg}
{pystamp}"""

print("Sending...")

for receiver_email in receiver_email_list:
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

print("Sent!")
