stromkosten = input("Bitte geben sie ihre Stromkosten pro KWh, in Euro, an\n")
stromverbrauch = input("Bitte geben sie den Durchschnittlichen Stromverbrauch des Geräts, in Watt, an\n")
zeit = input("Bitte geben sie in Stunden an, wie lange das Gerät pro Tag läuft\n")
sk = float(stromkosten)
sv = float(stromverbrauch)
z = float(zeit)
sv = sv / 1000
igs = z * sk * sv
print("Die Täglichen Stromkosten des Geräts betragen " + str(igs) + " Euro")
print("Die Wöchenlichen Stromkosten des Geräts betragen " + str(igs * 7) + " Euro")
print("Die Monatlichen Stromkosten des Geräts betragen " + str(igs * 30) + " Euro")
print("Die Jährlichen Stromkosten des Geräts betragen " + str(igs * 365) + " Euro")