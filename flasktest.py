from flask import *
#importing all the methods, classes, functions from flask


app = Flask(__name__)


#This is the first page that comes when you type localhost:5000... it will have a a tag that redirects to a page
@app.route("/")
def  HomePage():
    return "<a href='/runscript'>EXECUTE SCRIPT </a>"

#Once it redirects here (to localhost:5000/runscript) it will run the code before the return statement
@app.route("/runscript")
def ScriptPage():
    import smtplib
    import ssl

    port = 587
    smtp_server = "smtp.outlook.com"
    sender_email = 'the2coders@outlook.com'
    password = 'Blank@123'
    receiver_email_list = ['reyanshja@outlook.com']
    subject = 'subject'
    msg = 'msg'
    message = f"""\
    Subject: {subject}

    {msg}"""

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

    return redirect(url_for("HomePage"))

#Running it only if we are running it directly from the file... not by importing
if __name__ == "__main__":
    app.run(debug=True)