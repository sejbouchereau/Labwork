import smtplib

class Email:
    SMTP_USER = "sejbouchereau@gmail.com"
    SMTP_PASSWORD = "Prjtpst25742"
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 25

    emailFrom: str
    nameFrom: str
    emailTo: str
    nameTo: str

    def __init__(self, emailFrom, nameFrom, emailTo, nameTo):
        self.emailFrom = emailFrom
        self.nameFrom = nameFrom
        self.emailTo = emailTo
        self.nameTo = nameTo

    def send(self, objet, msg):
        entete = ("From: "+ self.nameFrom +" <" + self.emailFrom + ">\n"
            "To: " + self.nameFrom + " <" + self.emailTo + ">\n"
            "Subject:" + objet + "\n\n")
        print(entete + msg)
        try:
            server = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)
            server.ehlo()
            server.login(self.SMTP_USER, self.SMTP_PASSWORD)
            server.sendmail(self.emailFrom, self.emailTo, (entete + msg))
            server.close()
        except smtplib.SMTPException:
            print("Impossible d'envoyer le mail a " + self.emailTo)
        except (smtplib.socket.error, smtplib.SMTPConnectError):
            print("Connexion impossible au serveur SMTP")

if __name__ == "__main__":
    print ("Début du test")
    email = Email("sejbouchereau@gmail.com", "Samuel B",
                  "sejbouchereau@gmail.com", "Samuel Bouch")
    email.send("Alarme", "Ceci est un test")
    print("Fin du test")