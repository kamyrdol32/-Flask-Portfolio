from flask import Flask, render_template

####################
### CONFIG & DECORATOS
####################

Type = "Development" # Production or Development

# Pobieranie config'a z pliku config.py
app = Flask(__name__)
app.config.from_object("settings." + Type + "Config")

Technologie = [
    ["Python", "fab fa-git-alt", 4, 1, "Język programowania wysokiego poziomu ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek standardowych, którego ideą przewodnią jest czytelność i klarowność kodu źródłowego. Jego składnia cechuje się czytelnością, przejrzystością i zwięzłością."],
    ["Flask", "fas fa-pepper-hot", 3, 2, "Mikro framework aplikacji webowych napisany w języku Python. Jest sklasyfikowany jako micro-framework, ponieważ nie wymaga określonych narzędzi ani bibliotek. Jest to jeden z popularniejszych framework'ow wykorzystywanych do tworzenia stron internetowych."],
    ["Django", "fas fa-keyboard", 1, 4, "Wolny i otwarty framework przeznaczony do tworzenia aplikacji internetowych, napisany w Pythonie. Powstał pod koniec 2003 roku jako ewolucyjne rozwinięcie aplikacji internetowych, tworzonych przez grupę programistów związanych z Lawrence Journal-World."],
    ["SQL / MySQL", "fas fa-database", 3, 2, "Jest to język dziedzinowy używany do tworzenia, modyfikowania relacyjnych baz danych oraz do umieszczania i pobierania danych z tych baz. Decyzję o sposobie przechowywania i pobrania danych pozostawia się systemowi zarządzania bazą danych."],
    ["Git", "fab fa-git-alt", 2, 3, "Rozproszonym systemem kontroli wersji ułatwiającym pracę nad tworzeniem aplikacji, stron internetowych i innych narzędzi w grupach. System śledzi wszystkie wykonywane zmiany w plikach, a także umożliwia przywrócenie ich dowolnej, wcześniejszej wersji"],
    ["Linux", "fab fa-linux", 3, 2, "Rodzina uniksopodobnych systemów operacyjnych opartych na jądrze Linux. Linux jest jednym z przykładów wolnego i otwartego oprogramowania. Jego kod źródłowy może być dowolnie wykorzystywany, modyfikowany i rozpowszechniany."]
]

@app.route('/')
def index():
    return render_template("index.html", Technologie=Technologie)




####################
### Others
####################


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=70)
