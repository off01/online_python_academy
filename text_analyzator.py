TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
# Zadane promenne s kterymi budu pracovat
POCET_TEXTU = len(TEXTS)
ODDELOVAC = 60 * '-'
REGISTROVANI_UZIVATELE = {'USER': ['bob','ann','mike','liz'], 'PASSWORD': [123,'pass123','password123','pass123']}
print(ODDELOVAC)
# Prihlaseni do aplikace
print(f'Welcome to the app. Please log in: ')
USERNAME = input('USERNAME: ')
PASSWORD = input('PASSWORD: ')
print(ODDELOVAC)
# Overeni spravnosti uzivatelskeho jmena spolu s uzivatelskym heslem. spolu s nahardcodovanym resenim pro prveho uzivatele ktery ma pouze cisla
if (USERNAME == list(REGISTROVANI_UZIVATELE.values())[0][0] and int(PASSWORD) == list(REGISTROVANI_UZIVATELE.values())[1][0]) or (USERNAME == list(REGISTROVANI_UZIVATELE.values())[0][1] and PASSWORD == list(REGISTROVANI_UZIVATELE.values())[1][1]) or (USERNAME == list(REGISTROVANI_UZIVATELE.values())[0][2] and PASSWORD == list(REGISTROVANI_UZIVATELE.values())[1][2]):
# Privitani do aplikace po zadani spravnych udaju
    print(f'We have {POCET_TEXTU} texts to be analyzed.')
# Zadani casti textu k analyzovani
    number = int(input('Enter a number: '))
    text_k_analyze = TEXTS[number - 1]
    print(ODDELOVAC)
#Definice ktera pocita pocet slov v dane casti textu
    def pocet_slov(text: str) -> int:
        jednotliva_slova = text.split()
        ciste_slovo = [slovo.strip('.,') for slovo in jednotliva_slova]
        jednotliva_slova_ = []
        for v in ciste_slovo:
            jednotliva_slova_.append(v)
        return (len(jednotliva_slova_))
# Definice ktera pocita pocet velkych pismen v casti textu
    def pocet_slov_velky_pismeno(text: str) -> int:
        jednotliva_slova = text.split()
        ciste_slovo = [slovo.strip('.,') for slovo in jednotliva_slova]
        jednotliva_slova_ = []
        for v in ciste_slovo:
            if v.istitle():
                jednotliva_slova_.append(v)
        return (len(jednotliva_slova_))
# Definice ktera pocita pocet slov velkymi pismeny
    def pocet_slov_velky_pismeny(text: str) -> int:
        jednotliva_slova = text.split()
        ciste_slovo = [slovo.strip('.,') for slovo in jednotliva_slova]
        jednotliva_slova_ = []
        for v in ciste_slovo:
            if v.isupper():
                jednotliva_slova_.append(v)
        return (len(jednotliva_slova_))
# Definice ktera pocita pocet slov psanymi malymi pismeny
    def pocet_slov_malými_pismeny(text: str) -> int:
        jednotliva_slova = text.split()
        ciste_slovo = [slovo.strip('.,') for slovo in jednotliva_slova]
        jednotliva_slova_ = []
        for v in ciste_slovo:
            if v.islower():
                jednotliva_slova_.append(v)
        return (len(jednotliva_slova_))
# Definice ktera pocita pocet slov obsahujici cisla v textu
    def pocet_slov_cisly(text: str) -> int:
        jednotliva_slova = text.split()
        ciste_slovo = [slovo.strip('.,') for slovo in jednotliva_slova]
        jednotliva_slova_ = []
        for v in ciste_slovo:
            if v.isnumeric():
                jednotliva_slova_.append(v)
        return (len(jednotliva_slova_))
    print(f'There are {pocet_slov(text_k_analyze)} words in the selected text.')
    print(f'There are {pocet_slov_velky_pismeno(text_k_analyze)} titlecase words.')
    print(f'There are {pocet_slov_velky_pismeny(text_k_analyze)} uppercase words.')
    print(f'There are {pocet_slov_malými_pismeny(text_k_analyze)} lowercase words.')
    print(f'There are {pocet_slov_cisly(text_k_analyze)} lowercase words.')
    print(ODDELOVAC)
# Promenne ktere vyuziji v grafu
    cast_textu = str(text_k_analyze)
    jednotliva_slova = cast_textu.split()
    ciste_slovo = [slovo.strip('.,') for slovo in jednotliva_slova]
    jednotliva_slova_ = []
    slova_slozena_z_pismen = []
# For cyclus ktery prevede ocistena slova na pocet znaku
    for v in ciste_slovo:
        jednotliva_slova_.append(len(v))
# For cyclus ktery vytvori novy list a odtsrani duplicitni polozky
    for x in list(set(jednotliva_slova_)):
        slova_slozena_z_pismen.append(x)
# For cyclus ktery jiz vytvori dany graf kde je zobrazen unikatnost slov a jejich prvku spolu s poctem kolikrat se vyskytuje
    for y in slova_slozena_z_pismen:
        cetnost = jednotliva_slova_.count(y)
        graf = cetnost * '*'
        print(f'{y}  {graf} {cetnost}')
    print(ODDELOVAC)
# Definice ktera secte vsechny cisla v textu
    def soucet_cifer(text: str) -> int:
        jednotliva_slova = text.split()
        jednotliva_slova_ = []
        for v in jednotliva_slova:
            if v.isnumeric():
                jednotliva_slova_.append(int(v))
        return (sum(jednotliva_slova_))
    print(f'If we summed all the numbers in this text we would get: {soucet_cifer(text_k_analyze)} .')
    print(ODDELOVAC)
else:
    print('Heslo, nebo uživatelské jméno je špatně!')
