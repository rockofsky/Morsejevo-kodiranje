morsejev_slovar = {"":" "}
with open("morsejevi_znaki.txt", "r", encoding="utf-8") as znaki:
    for vrstica in znaki.readlines():
        if ":" in vrstica:
            morsejev_slovar[str(vrstica[vrstica.index(":") + 1:]).replace("\n", "").replace(" ","")] = str(vrstica[:vrstica.index(":")])
        else:
            continue

print("\nTo je program za predelavo Morsejevih znakov v črke.")
input("\nVstavi znake in napisal ti bom besedilo v novo datoteko .txt (za nadaljevanje pritisni ENTER)")
input("\nV primeru, da si zaključil z Morsejevim znakom, pritisni ENTER")
input("\nČe sledi daljši premor (presledek), pritisni samo ENTER")
input("\nV primeru, ko hočeš zaključiti s pretvarjanjem besedila, napiši KONEC in pritisni ENTER. Datoteka se ti bo shranila.")


dešifriranje = ""
with open("besedilo_morsejevega_dešifriranja.txt", "w", encoding="utf-8") as dešifrirano:
    kodni_input = str(input("Začni pisati zdaj! "))
    while kodni_input not in ["KONEC", "konec", "Konec"]:
        dešifriranje += morsejev_slovar[kodni_input]
        kodni_input = str(input(""))
    print(dešifriranje, file=dešifrirano)
        