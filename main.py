"""1. Aplikacija za beleženje nalog (To-Do List)
Osnovni opis: Uporabnik lahko ustvari, ureja, briše in označi naloge kot zaključene. Sistem vsebuje uporabniški sistem za registracijo, prijavo in zaščito zasebnosti nalog.

Funkcionalnosti:
    Registracija in prijava: Uporabniki se lahko registrirajo z e-pošto, uporabniškim imenom in geslom. Gesla so shranjena v šifrirani obliki z uporabo bcrypt ali werkzeug.security.
    Kreiranje nalog: Uporabniki lahko ustvarijo naloge, jih označijo kot opravljene, jih razvrstijo po datumu ali prioritete.
    Interakcija z bazo: Uporabniški podatki (uporabniško ime, e-pošta, geslo) in naloge se shranijo v bazi (npr. SQLite). Naloge so povezane z uporabnikom (relacija "one-to-many").
    Seznam nalog: Seznam vseh nalog z možnostjo filtriranja glede na status (npr. neopravljene, opravljene).
    Urejanje in brisanje nalog: Uporabnik lahko ureja ali izbriše svoje naloge, vendar ne more spreminjati nalog drugih uporabnikov.
    AJAX: Dinamično nalaganje nalog brez ponovnega nalaganja celotne strani.
"""

"""
2. Aplikacija za beleženje knjig (Book Tracker)
Osnovni opis: Uporabniki lahko beležijo knjige, ki so jih prebrali ali jih želijo prebrati, ocenijo knjige, pišejo mnenja, iščejo knjige po različnih kriterijih (avtor, žanr itd.).

Funkcionalnosti:
    Registracija in prijava: Uporabniki se lahko registrirajo in prijavijo. Gesla so shranjena varno.
    Upravljanje knjig: Uporabnik lahko doda knjige v svojo zbirko (z naslovom, avtorjem, letnico izdaje, žanrom, oceno in mnenjem).
    Filtriranje in iskanje: Knjige je mogoče filtrirati po avtorju, žanru, letu izida in oceni.
    Povezava z bazo: Knjige in uporabniški podatki so shranjeni v bazi, povezani so (relacija "many-to-many" med uporabniki in knjigami, ker uporabniki lahko preberejo več knjig).
    Urejanje in brisanje: Uporabnik lahko ureja svoje vnose, vendar ne more spreminjati knjig drugih uporabnikov.
    AJAX: Dinamično nalaganje knjig ob iskanju, brez osvežitve strani.
"""

"""
5. Aplikacija za ocenjevanje filmskih vsebin (Movie Review)
Osnovni opis: Uporabniki lahko ocenijo filme, pišejo mnenja, delijo svoje ocene s prijatelji in iščejo filme po različnih kriterijih (žanr, leto izdaje).

Funkcionalnosti:
    Registracija in prijava: Uporabniki se lahko registrirajo in prijavijo za uporabo aplikacije
       Ocenjevanje filmov: Uporabniki lahko ocenijo filme z zvezdami, napišejo mnenje in jih dodajo v svojo zbirko.
    Povezava z bazo: Filme in uporabniške ocene shranimo v bazi (relacija "one-to-many" med filmi in ocenami).
    Seznam filmov: Uporabnik lahko išče filme po žanru, letu izdaje ali oceni.
    AJAX: Dinamično nalaganje filmov in ocen brez ponovnega nalaganja strani.

Implementacija funkcionalnosti:
    Za vsako od zgoraj navedenih aplikacij boste morali poskrbeti za:
    Ustrezno strukturo map: Uporaba map static, templates, models in routes je ključna za dobro organizacijo.
    Uporaba templata (Jinja2): Uporabite templating za dinamično generiranje HTML strani.
    Varno shranjevanje gesel: Uporabite ustrezne tehnike za varno shranjevanje gesel (npr. bcrypt).
    Preprečevanje napak in validacija: Skrbno obravnavajte napake, kot so napačni podatki v obrazcih ali napake pri povezavi z bazo.
    API & AJAX: Implementirajte API-je za dinamično nalaganje podatkov z uporabo AJAX-a, da bodo vaše strani bolj interaktivne.
"""

"""
9. Aplikacija za spremljanje navad (Habit Tracker)
Osnovni opis: Uporabniki lahko spremljajo svoje dnevne navade, kot so pitje vode, telovadba, branje knjig itd., ter spremljajo svoj napredek v določenih intervalih.

Funkcionalnosti:
    Registracija in prijava: Uporabniki se prijavijo in ustvarijo profil za spremljanje svojih navad.
    Ustvarjanje navad: Uporabnik lahko doda navade, ki jih želi spremljati (npr. pitje vode, vadba, prehranjevanje).
    Spremljanje napredka: Uporabnik označi, ali je vsak dan izpolnil določeno navado (na primer, ali je šel na tek).
    Povezava z bazo: Shranjevanje navad in dnevnih nalog v bazi.
    Seznam navad: Prikaz vseh navad in filtriranje po dnevu, tednu ali mesecu.
    AJAX: Dinamično nalaganje novih vnosov in napredka brez osvežitve strani.
"""

from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            user = users.get(User.username == username)
            if user:
                if user['password'] == password:
                    session['username'] = username
                    return jsonify({'success': True})
                else:
                    return jsonify({'success': False, 'error': 'Napačno geslo'})
            else:
                users.insert({'username': username, 'password': password})
                session['username'] = username
                return jsonify({'success': True})
                
        except Exception as e:
            print(f"Napaka pri prijavi: {str(e)}")
            return jsonify({'success': False, 'error': 'Prišlo je do napake'})
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)