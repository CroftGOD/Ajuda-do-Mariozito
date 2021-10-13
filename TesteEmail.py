import smtplib, ssl, csv, random

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
receiver_email = ""
a=0
skiparEmails=1
numeroLinhasMensagens = 19
quantidadePorConta = 15
context = ssl.create_default_context()
with open ("Recevedores.csv") as Ficheleiro:
    receiver_email = csv.reader(Ficheleiro)
    next(receiver_email)
    for Emailes in receiver_email:
        with open ("emails.csv") as file :
            emails = csv.reader(file)
            for i in range (skiparEmails):
                next(emails)
            for email, password in emails:
                while (a<quantidadePorConta):
                    with open("Mensagens.csv") as ficheiro:
                        mensagems = csv.reader(ficheiro)
                        Linha=1
                        LinhaLer=int(random.random()*(numeroLinhasMensagens - 2))+3
                        print(LinhaLer)
                        for topico, mensagem in mensagems:
                            Linha+=1
                            if (Linha == LinhaLer):
                                break
                        message = """\
Subject: {topico}
            
{mensagem}.""".format(topico=topico, mensagem=mensagem)
                        print (topico," ",mensagem)
                        output = ficheiro.read()
                    with smtplib.SMTP(smtp_server, port) as server :
                        server.ehlo()
                        server.starttls(context = context)
                        server.ehlo()
                        print("Email: ",email)
                        server.login(email, password)
                        server.sendmail(email, Emailes, message)
                    a+=1
                    server.close()
                a=0

