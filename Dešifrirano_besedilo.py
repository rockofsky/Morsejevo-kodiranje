morsejev_slovar = {"":" "}
with open("morsejevi_znaki.txt", "r", encoding="utf-8") as znaki:
    for vrstica in znaki.readlines():
        if ":" in vrstica:
            morsejev_slovar[str(vrstica[vrstica.index(":") + 1:]).replace("\n", "").replace(" ","")] = str(vrstica[:vrstica.index(":")])
        else:
            continue

input("\nTo je program za predelavo Morsejevih znakov v črke.")
if str(input("\nŽeliš začetno predstavitev programčka? ")) in ["JA", "ja", "Ja"]:
    input("\nVstavi znake in napisal ti bom besedilo v novo datoteko .txt (za nadaljevanje pritisni ENTER)")
    input("\nV primeru, da si zaključil z Morsejevim znakom, pritisni ENTER")
    input("\nČe sledi daljši premor (presledek), pritisni samo ENTER")
    input("\nV primeru, ko hočeš zaključiti s pretvarjanjem besedila, napiši KONEC in pritisni ENTER. Datoteka se ti bo shranila.")
else:
    pass

if str(input("\nŽeliš ponastaviti vnos v datoteko besedila? ")) in ["ja", "JA", "Ja", "Da", "da", "DA"]:
    str(input("\nNa prihajajoča vprašanja odpisuj z malimi tiskanim \"ja\" ali z malim tiskanim \"ne\". "))
    if str(input("\nŽeliš imeti možnost vnašati tudi znake/besede, ki niso v Morsejevem kodni abecedi? ")) == "ja":
        nastavitev1 = str(input("\nAli ti pri vsakem takem primeru ponudimo izbiro o vnosu v datoteko? "))
else:
    pass

dešifriranje = ""
with open("besedilo_morsejevega_dešifriranja.txt", "w", encoding="utf-8") as dešifrirano:
    kodni_input = str(input("Začni pisati zdaj! "))
    while kodni_input not in ["KONEC", "konec", "Konec"]:
        if kodni_input not in morsejev_slovar and nastavitev1 == "ja": 
            if str(input("Ali vnesem to besedo/znak v besedilo? (odgovori z malimi tiskanimi \"ja\" oziroma \"ne\") ")) == "ja":
                dešifriranje += kodni_input
                kodni_input = str(input(""))
            else:
                pass
            continue
        elif kodni_input not in morsejev_slovar and nastavitev1 == "ne":
            dešifriranje += kodni_input
            kodni_input = str(input(""))
            continue
        else:
            pass
        dešifriranje += morsejev_slovar[kodni_input]
        kodni_input = str(input(""))
    print(dešifriranje, file=dešifrirano)
        