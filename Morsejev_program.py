morsejev_slovar = {}
with open("morsejevi_znaki.txt", "r", encoding="utf-8") as znaki:
    for vrstica in znaki.readlines():
        if ":" in vrstica:
            morsejev_slovar[str(vrstica[:vrstica.index(":")])] = str(vrstica[vrstica.index(":") + 1:]).replace("\n", "").replace(" ","")
        else:
            continue

def sifriranje_v_morseja_niz(niz):
    morse_niz = "|"
    for znak in niz.replace(".", "").replace("!", "").replace("?", "").replace("Ž", "Z").replace(",", "").upper():
        if znak == " ":
            morse_niz += "  |"
        elif znak == "\n":
            morse_niz += "\n\n"
        else:
            morse_niz += morsejev_slovar[znak] + "|"
    return morse_niz


