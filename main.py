import json
import xlsxwriter

# plik z wiadomościami
mesagesfile = "example.json"

f = open(mesagesfile, encoding="utf-8")
data = json.load(f)





class trojmiejski:
    def __init__(self, imie, wiadomosci, zdjecia, reakcje, zapostowanestopy):
        self.imie = imie
        self.wiadomosci = wiadomosci
        self.zdjecia = zdjecia
        self.reakcje = reakcje
        self.zapostowanestopy = zapostowanestopy

    def dodajwiadomosc(self):
        self.wiadomosci += 1
        return self.wiadomosci

    def dodajzdjecie(self):
        self.zdjecia += 1
        return self.zdjecia

    def dodajreakcje(self, ile):
        self.reakcje += ile

    def stopy(self):
        self.zapostowanestopy += 1

topmsg = {
    "imie": "",
    "wiadomosc": "",
    "reakcje": 0,
    "maxreakje":0

}
topfoto = {
    "imie": "",
    "zdj": "",
    "reakcje": 0,
    "maxreakje":0
}
mostreacts = 0

# hardcode każdego z trójmiejskich trzeba zrobić
listauczestnikow = []
for uczestnicy in data["participants"]:
    listauczestnikow.append(trojmiejski(uczestnicy.get("name"), 0, 0, 0, 0))

for msg in data["messages"]:

    for kto in range(len(listauczestnikow)):
        if msg.get("sender_name") == listauczestnikow[kto].imie:    #dodawanie użytkowników
            listauczestnikow[kto].dodajwiadomosc()
            lista_stop = ["stopy","stopki","stópki","stóp","stópeczki"]
            tresc_wiadomosci = str(msg.get("content")).lower()
            stopkarz = False
            for stopa in lista_stop:
                if stopa in tresc_wiadomosci:
                    stopkarz = True
            if stopkarz:
                listauczestnikow[kto].stopy()                             #szukanie stóp
            if msg.get("photos"):                                       #przeglad zdjec
                listauczestnikow[kto].dodajzdjecie()



            if msg.get("reactions"):
                lizodup=False
                for i in range(len(msg.get("reactions"))):
                    #print(msg.get("reactions")[i]["actor"]) #w długości listy rekacji pokazuje każdego reagujacego
                    if msg.get("sender_name") == msg.get("reactions")[i]["actor"]:#jeżeli wysyłający jest też lajkującym to jest lizodupem
                        lizodup = True
                if lizodup:
                    break
                else:
                    listauczestnikow[kto].dodajreakcje(len(msg.get("reactions")))






                if len(msg.get("reactions")) > topfoto["maxreakje"] and msg.get("photos"):
                    topfoto["imie"]=msg.get("sender_name")
                    topfoto["zdj"]=msg.get("photos")[0]["uri"]
                    topfoto["reakcje"]=len(msg.get("reactions"))
                    topfoto["maxreakje"] = len(msg.get("reactions"))
                elif len(msg.get("reactions")) > topmsg["maxreakje"]:
                    topmsg["imie"]=msg.get("sender_name")
                    topmsg["wiadomosc"]=msg.get("content")
                    topmsg["reakcje"]=len(msg.get("reactions"))
                    topmsg["maxreakje"] = len(msg.get("reactions"))

for msg in data["messages"]:
    if msg.get("reactions") and len(msg.get("reactions")) == topmsg["maxreakje"]:
        if msg.get("photos"):
            pass
        else:
            pass
            #print(msg.get("content"))

    if msg.get("reactions") and msg.get("photos") and len(msg.get("reactions")) == topfoto["maxreakje"]:
        pass
        #print(msg.get("photos")[0]["uri"])






print(topmsg)
print(topfoto)
for j in range(len(listauczestnikow)):
    if listauczestnikow[j].wiadomosci == 0:
        pass
    else:
        pass
        #print(listauczestnikow[j].__dict__)
f.close()
workbook = xlsxwriter.Workbook('trojmiejskie3v3.xlsx')
worksheet = workbook.add_worksheet()

#
worksheet.write('A1', 'Kto')
worksheet.write('B1', 'Wiadomosci')
worksheet.write('C1', 'Zdjęcia')
worksheet.write('D1', 'Reakcje')
atrybuty = 5
for uzytkownik in range(len(listauczestnikow)):
    worksheet.write(1, atrybuty * uzytkownik, listauczestnikow[uzytkownik].imie)
    worksheet.write(1, 1 + atrybuty * uzytkownik, listauczestnikow[uzytkownik].wiadomosci)
    worksheet.write(1, 2 + atrybuty * uzytkownik, listauczestnikow[uzytkownik].zdjecia)
    worksheet.write(1, 3 + atrybuty * uzytkownik, listauczestnikow[uzytkownik].reakcje)
    worksheet.write(1, 4 + atrybuty*uzytkownik,listauczestnikow[uzytkownik].zapostowanestopy)
workbook.close()














