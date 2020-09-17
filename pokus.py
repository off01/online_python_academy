klient = input("Zadejte Vaše jméno: ")
ODELOVAC = 60*'#'
DESTINACE = ('Prague','Wien','Brno','Svitavy','Zlin','Ostava')
CENA = ('1000','1100','2000','1500','2300','3400')
print("Dobrý den", klient,  "Vítete v naší aplikaci")
print("We can offer you the following destinations:"
, ODELOVAC,
'''1 - Prague  | 1000
2 - Wien    | 1100
3 - Brno    | 2000
4 - Svitavy | 1500
5 - Zlin    | 2300
6 - Ostrava | 3400
''')

volba_destinace = int(input("Zadejte číslo vaší destinace: "))
print('Budeme pokračovat registrací')

klient_jmeno = input("Zadejte vaše jméno: ")
klient_prijmeni = input("Zadejte vaše přijmení: ")
klient_rok_narozeni = input("Zadejte rok narození: ")
klient_email = input("Zadjete emailovou adresu: ")
klient_pass = input("Zadejte heslo: ")

