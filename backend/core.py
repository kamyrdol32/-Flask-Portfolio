from flask import Flask, render_template
from flask_mail import Message, Mail
from forms import MailForm


####################
### CONFIG & DECORATOS
####################

Type = "Development" # Production or Development

# Pobieranie config'a z pliku config.py
app = Flask(__name__)
app.config.from_object("settings." + Type + "Config")
mail = Mail(app)

Technologie = [
    ["Python", "fab fa-git-alt", 4, 1, "Język programowania wysokiego poziomu ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek standardowych, którego ideą przewodnią jest czytelność i klarowność kodu źródłowego. Jego składnia cechuje się czytelnością, przejrzystością i zwięzłością."],
    ["Flask", "fas fa-pepper-hot", 3, 2, "Mikro framework aplikacji webowych napisany w języku Python. Jest sklasyfikowany jako micro-framework, ponieważ nie wymaga określonych narzędzi ani bibliotek. Jest to jeden z popularniejszych framework'ow wykorzystywanych do tworzenia stron internetowych."],
    ["Django", "fas fa-keyboard", 1, 4, "Wolny i otwarty framework przeznaczony do tworzenia aplikacji internetowych, napisany w Pythonie. Powstał pod koniec 2003 roku jako ewolucyjne rozwinięcie aplikacji internetowych, tworzonych przez grupę programistów związanych z Lawrence Journal-World."],
    ["SQL / MySQL", "fas fa-database", 3, 2, "Jest to język dziedzinowy używany do tworzenia, modyfikowania relacyjnych baz danych oraz do umieszczania i pobierania danych z tych baz. Decyzję o sposobie przechowywania i pobrania danych pozostawia się systemowi zarządzania bazą danych."],
    ["Git", "fab fa-git-alt", 2, 3, "Rozproszonym systemem kontroli wersji ułatwiającym pracę nad tworzeniem aplikacji, stron internetowych i innych narzędzi w grupach. System śledzi wszystkie wykonywane zmiany w plikach, a także umożliwia przywrócenie ich dowolnej, wcześniejszej wersji"],
    ["Linux", "fab fa-linux", 3, 2, "Rodzina uniksopodobnych systemów operacyjnych opartych na jądrze Linux. Linux jest jednym z przykładów wolnego i otwartego oprogramowania. Jego kod źródłowy może być dowolnie wykorzystywany, modyfikowany i rozpowszechniany."],
    ["React", "fab fa-react", 3, 2, "Biblioteka języka programowania JavaScript, która wykorzystywana jest do tworzenia interfejsów graficznych aplikacji internetowych. Często wykorzystywana do tworzenia aplikacji typu Single Page Application."],
    ["Docker & Docker-compose", "fab fa-docker", 3, 2, "Otwarte oprogramowanie służące do realizacji wirtualizacji na poziomie systemu operacyjnego (tzw. „konteneryzacji”), działające jako 'platforma dla programistów i administratorów do tworzenia, wdrażania i uruchamiania aplikacji rozproszonych'."],
    ["Nginx", "fab fa-docker", 2, 3, "Serwer WWW (HTTP) oraz serwer proxy dla HTTP i IMAP/POP3. Zaprojektowany z myślą o wysokiej dostępności i silnie obciążonych serwisach (nacisk na skalowalność i niską zajętość zasobów). Wydawany jest na licencji BSD."],
]

Portfolio = [
    ["Aplikacja do zarządzania kadrami", "/static/Images/Projects/1.png", "Jest to aplikacja stworzona w Pythonie (Flask) na potrzeby napisania pracy inżynierskiej.", "http://inzynierka.kamilzeglen.pl", "https://github.com/kamyrdol32"],
    ["Lorem ipsum", "/static/Images/400x400.png", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec nulla arcu, maximus sed erat a, lacinia aliquet justo. Ut in fringilla elit. Nunc vestibulum, quam at aliquam elementum, metus elit dignissim nibh, vel congue leo urna in urna", "http://kamilzeglen.pl", "https://github.com/kamyrdol32"],
    ["Lorem ipsum", "/static/Images/400x400.png", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec nulla arcu, maximus sed erat a, lacinia aliquet justo. Ut in fringilla elit. Nunc vestibulum, quam at aliquam elementum, metus elit dignissim nibh, vel congue leo urna in urna", "http://kamilzeglen.pl", "https://github.com/kamyrdol32"],
]

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MailForm()
    if form.validate_on_submit():
        send_mail(str(form.name.data), str(form.email.data), str(form.topic.data), str(form.text.data))

    return render_template("index.html", Technologie=Technologie, Portfolio=Portfolio, form=form)


####################
### Mail
####################

def send_mail(name, email, topic, text):
    msg = Message(name + " - " + topic, sender=email, recipients=["kam.zeglen@gmail.com"])
    msg.html = "Wiadomość od: <b>"+ name + "</b><br><br>" + text + "<br><br>###<br>Adres kontaktowy: " + email + "<br>###"
    mail.send(msg)



####################
### Others
####################


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=70)