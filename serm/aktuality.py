#/usr/bin/python3

import smtplib
import hashlib
import urllib.request

# pošli na mail
def mail(telo):
    with open("pass.txt", "r", encoding="utf-8") as text:
        udaje = list(text)
    udaje = [s.rstrip() for s in udaje]
    jmeno, heslo = tuple(udaje)    # uloží údaje do samostatných proměných
    komu = "prokop.paruzek@paruzkovi.cz"
    telo += "Důležité odkazy: https://www.czechfencing.cz/portal/news a https://www.czechfencing.cz/portal/members/detail/2477\nTvůj bot"
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as m:
        m.ehlo()
        m.login(jmeno, heslo)
        subject = "Změna na stránkách svazu"
        msg = "FROM: " + jmeno + "\n" + "TO: " + komu + "\n" + "SUBJECT: " + subject + "\n\n" + telo
        msg = msg.encode()
        m.sendmail(jmeno, komu, msg)

telo = ""
send_mail = False

# Novinky
try:
    with open("news.md5") as news:
        s = urllib.request.urlopen("https://www.czechfencing.cz/portal/news")
        m = hashlib.md5()
        m.update(s.read())
        h = m.hexdigest()
        oh = news.read()
        if h != oh:
            telo += "Změna v novinkách.\n"
            send_mail = True
except FileNotFoundError:
    s = urllib.request.urlopen("https://www.czechfencing.cz/portal/news")
    m = hashlib.md5()
    m.update(s.read())
    h = m.hexdigest()
    telo += "Změna v novinkách.\n"
    send_mail = True
with open("news.md5", "w") as news:
    news.write(h)

# Status
try:
    with open("status.md5") as status:
        s = urllib.request.urlopen("https://www.czechfencing.cz/portal/members/detail/2477")
        m = hashlib.md5()
        m.update(s.read())
        h = m.hexdigest()
        oh = status.read()
        if h != oh:
            telo += "Změna ve statutu.\n"
            send_mail = True
except FileNotFoundError:
    s = urllib.request.urlopen("https://www.czechfencing.cz/portal/members/detail/2477")
    m = hashlib.md5()
    m.update(s.read())
    h = m.hexdigest()
    telo += "Změna ve statutu\n"
    send_mail = True
with open("status.md5", "w") as news:
    news.write(h)

if send_mail:
    mail(telo)
