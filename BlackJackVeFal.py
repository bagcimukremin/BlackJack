import random

def deste_olustur():
    # Sıralı kart destesini oluşturur.
    sinif = ["♠-Maça ", "♦-Karo ", "♣-Sinek ", "♥-Kupa "]
    deste = []
    for i in range(len(sinif)):
        for j in range(1, 14):
            if j == 1:
                j = "As"
            elif j == 11:
                j = "Vale"
            elif j == 12:
                j = "Kız"
            elif j == 13:
                j = "Papaz"
            deste.append(sinif[i] + str(j))
    degerli_deste = {}
    deger_veren = 1
    for i in range(52):
        if i == 13 or i == 26 or i == 39:
            deger_veren = 1
        for j in range(deger_veren, deger_veren + 1):
            if deger_veren == 11 or deger_veren == 12:
                deger_veren = 10
            degerli_deste[deste[i]] = deger_veren  # kartlar değerleriyle eşleşir
            deger_veren += 1
    return degerli_deste, deste


# ==============================================================
def kagık_cek(deste, degerli_deste, oyun_ismi):
    if oyun_ismi == "Blackjack":  # blacjack oyunu için
        sayi = random.randint(0, len(deste) - 1)
        kart_ismi = deste[sayi]  # rastgele kart çeker
        puan = degerli_deste[kart_ismi]  # rastgele çekilen kartın puanı
        deste.pop(sayi)  # desteden rastgele çekilen kartı siler
        return deste, kart_ismi, puan
    else:  # fal oyunu için
        kart_ismi = deste[0]
        puan = degerli_deste[0]
        return deste, degerli_deste, puan


def blackjack():  # blackjack oyunu
    degerli_deste, deste = deste_olustur()
    kasa = []  # kasanın kartlarının eklendiği liste
    oyuncu = []  # oyuncunun kartlarının eklendiği liste
    kasa_puan = oyuncu_puan = black_o = black_d = 0
    print("\nDağıtıcının Açık Kağıdı:", end="")
    for i in range(2):  # kasanın ilk iki kart çekimi
        deste, kart_ismi, deger = kagık_cek(deste, degerli_deste, "Blackjack")
        if deger == 1:  # as'ın değerinin ilk 11 puan alınması
            deger = 11
        kasa_puan += deger  # dağıtıcının puanını toplama
        kasa.append(kart_ismi)  # çekilen kartı dağıtıcının listesine ekleme
        if i == 1:
            a = kart_ismi  # dağıtıcının ikinci kartını başka bir yerde tutulması
            break
        print(kart_ismi)
    if kasa_puan == 22:
        kasa_puan = 12
        girdi = 1
    print("Oyuncunun Kağıtları: ", end="")
    for j in range(2):  # oyuncunun kart çekimi
        deste, kart_ismi, deger = kagık_cek(deste, degerli_deste, "Blackjack")
        print(kart_ismi, end=", ")
        oyuncu.append(kart_ismi)
        oyuncu_puan += deger
    kagit_sor = "e"

    def bak(deste, puan):  # as isimli kartlar varsa avantaja göre 11 ya da 1 alınması
        aslar = ["♠-Maça As", "♦-Karo As", "♥-Kupa As", "♣-Sinek As"]
        yada_puan = a = as_say = 0
        for k in range(4):
            a = deste.count(aslar[k])
            if a == 1:
                as_say += 1
                if 2 <= puan <= 11:
                    yada_puan += puan + 10
                    if puan > 21:
                        yada_puan = yada_puan - 9
                elif as_say > 1:
                    yada_puan = yada_puan
                if yada_puan > 21:
                    yada_puan = 0
        return puan, yada_puan

    # ========================================
    oyuncu_puan, oyuncu_yada = bak(oyuncu,
                                   oyuncu_puan)  # oyuncuda as isimli kartlar varsa oyuncunun avantaja göre 11 ya da 1 alınması
    if oyuncu_yada == 21 and len(oyuncu) == 2:  # oyuncunun blackjack yapıp yapmadığı kontrol edilir
        print("Oyuncu Blackjack yaptı!")
        black_o = 1
        kagit_sor = "h"
    if oyuncu_yada != 0 and black_o == 0 and oyuncu_yada != 21:  # oyuncuda as isimli kart varsa iki çeşit puan toplamı yazılır
        print("(Toplam:", oyuncu_puan, "ya da", oyuncu_yada, ")")
    elif oyuncu_yada != 21:  # oyuncunun kart toplamının yazdırılması
        print("(Toplam:", oyuncu_puan, ")")
    while kagit_sor == "e" and oyuncu_puan <= 21:  # oyuncu kart istiyor mu diye sorulur
        kagit_sor = input("Kağıt istiyor musunuz? (e/h):")
        while kagit_sor not in ["e", "E", "H", "h"]:  # yanlış giriş yapıldığında oyuncuya tekrar sorulması
            kagit_sor = input("Yanlış giriş yaptınız,tekrar kağıt istiyor musunuz? (e/E/h/H):")
            kagit_sor.lower()
        if kagit_sor == "e":
            deste, kart_ismi, deger = kagık_cek(deste, degerli_deste, "Blackjack")
            oyuncu.append(kart_ismi)  # çekilen kart oyuncunun destesine eklenir
            oyuncu_puan += deger
            print("\nOyuncunun Kağıtları: ", end="")
            for kart_sirasi in range(len(oyuncu)):
                print(oyuncu[kart_sirasi], end=", ")
            oyuncu_puan, oyuncu_yada = bak(oyuncu, oyuncu_puan)  # çekilen kart as mı değil mi diye bakılır
            if oyuncu_yada != 0:
                print("(Toplam:", oyuncu_puan, "ya da", oyuncu_yada, ")")
            else:
                print("(Toplam:", oyuncu_puan, ")")
                if oyuncu_puan > 21:
                    print("-Oyuncu Battı!")
            if oyuncu_yada == 21 or oyuncu_puan == 21:  # oyuncunun puanı 21 ise kasa kağıt çekmeye başlar
                kagit_sor = "h"  # dağıtıcı kart çekmeye devam eder.
    if kagit_sor == "h" or oyuncu_puan >= 21:  # oyuncun kart toplamı 21 veya 21den fazla ya da kart istemezse...
        kagit_sor = "h"  # dağıtıcı kart çekmeye devam eder.

    while kagit_sor.lower() == "h":  # dağıtıcıya geçilir
        if len(kasa) == 2 and oyuncu_puan <= 21:
            print("\nDağıtıcının kağıtları:", end='')
            for kart_sirasi in range(len(kasa)):
                print(kasa[kart_sirasi], end=', ')
        if len(kasa) == 2:  # dağıtıcının blackjack yapıp yapmadığı kontrol edilir
            if kasa_puan == 21 and oyuncu_puan <= 21:
                print("Dağıtıcı Blackjack yaptı!")
                d_black = 1
            elif oyuncu_puan <= 21:
                print("(Toplam:", kasa_puan, ")")
        if kasa_puan < 17 and oyuncu_puan <= 21 and black_o != 1:
            deste, kart_ismi, deger = kagık_cek(deste, degerli_deste, "Blackjack")
            kasa.append(kart_ismi)
            kasa_puan += deger
            print("Dağıtıcının kağıtları:", end='')
            for kart_sirasi in range(len(kasa)):
                print(kasa[kart_sirasi], end=', ')
            kasa_puan, kasa_yada = bak(kasa,
                                       kasa_puan)  # dağıtıcının çekilen kartında as varsa puan değerlendirlmesi yapılır
            if kasa_yada != 0:
                if kasa_yada < 17:  # duruma göre dağıtıcının toplam puan yazdırılması
                    print("(Toplam:", kasa_puan, "ya da", kasa_yada, ")")
                else:
                    print("(Toplam:", kasa_yada, ")")
            elif oyuncu_puan <= 21 and len(oyuncu) != 1:
                print("(Toplam:", kasa_puan, ")")
                if kasa_puan > 21:
                    print("-Kasa battı!")
        else:
            kagit_sor = "e"
    # kazananın belirlenmesi
    if oyuncu_yada > oyuncu_puan and oyuncu_yada <= 21:
        oyuncu_puan = oyuncu_yada
    if kasa_puan <= 21 and (kasa_puan > oyuncu_puan or oyuncu_puan > 21):
        print("_" * 17, "\nDağıtıcı kazandı!\n", "=" * 17, sep="")
    elif kasa_puan == oyuncu_puan:
        if len(kasa) == 2 and kasa_puan == 21 and black_o != 1:
            print("_" * 17, "\nDağıtıcı kazandı!\n", "=" * 17, sep="")
        elif len(oyuncu) == 2 and oyuncu_puan == 21 and black_d != 1:
            print("_" * 15, "\nOyuncu kazandı!\n", "=" * 15, sep="")
        else:
            print("_" * 8, "\nBerabere\n", "=" * 8, sep="")
    elif oyuncu_puan <= 21 and (oyuncu_puan > kasa_puan or kasa_puan > 21):
        print("_" * 15, "\nOyuncu kazandı!\n", "=" * 15, sep="")
    tekrar = input("Blackjack oyununu tekrar oynamak ister misiniz?(e/h):")
    while tekrar not in ["e", "h", "E", "H"]:  # girdi kontrolü
        tekrar = input("Yanlış giriş yaptınız,Blackjack oyununu tekrar oynamak ister misiniz?(e/h):")
        tekrar.lower()
    if tekrar == "e":
        blackjack()
    else:
        menu()
        # ==================================


def deste_karistir():  # sıralı destenin karıştırılması
    karisik_degerli_deste = []
    karisik_deste = []
    deger_deste, deste = deste_olustur()
    for i in range(0, len(deste)):
        randomm = random.randint(0, len(deste) - 1)
        kart_ismi = deste[randomm]  # ramdom sayi ile kart çeker
        puan = deger_deste[kart_ismi]
        karisik_deste.append(kart_ismi)
        karisik_degerli_deste.append(puan)
        deste.remove(deste[randomm])
    return karisik_degerli_deste, karisik_deste


# ==================================
def fal():  # fal oyunu
    sinif = ["♠-Maça ", "♦-Karo ", "♣-Sinek ", "♥-Kupa "]
    goster = yuzde = 0
    karisik_degerli_deste, karisik_deste = deste_karistir()
    niyet = "e"
    acilan_kart = []
    acilan_kart_deger = []
    karisik_deste, karisik_degerli_deste, es_deger = kagık_cek(karisik_deste, karisik_degerli_deste, "Fal")
    while niyet == "e":
        niyet = input("Niyetinizi tuttunuz mu(e/h)?:")

        while niyet not in ["e", "h", "H", "E"]:  # girdi kontrolü
            niyet = input("Yanlış giriş yaptınız,niyetinizi tuttunuz mu(e/h)?:")
            niyet.lower()
        if niyet == "h":
            tekrar = input("Fal Bakma Oyununu tekrar oynamak ister misiniz(e/h):")
            while tekrar not in ["e", "E", "H", "h"]:  # girdi kontrolü
                tekrar = input("Fal Bakma Oyununu tekrar oynamak ister misiniz(e/h):")
                tekrar.lower()
            if tekrar == "e":
                fal()
            else:
                menu()
        while len(karisik_deste) > 0:
            es_deger = karisik_degerli_deste[0]
            goster += 1
            print(goster, ".", karisik_deste[0], sep="", end="")
            for i in range(4):  # vale,kız ve papaz için yeniden puandırılma
                if karisik_deste[0] == sinif[i] + "Vale":
                    es_deger = 11
                elif karisik_deste[0] == sinif[i] + "Kız":
                    es_deger = 12
                elif karisik_deste[0] == sinif[i] + "Papaz":
                    es_deger = 13
            # ==========================
            acilan_kart.append(karisik_deste[0])
            acilan_kart_deger.append(karisik_degerli_deste[0])
            b = karisik_degerli_deste.pop(0)
            a = karisik_deste.pop(0)
            input()  # diğer kartı görmek için enter tuşuna basılması
            if goster == es_deger:
                print("(Eşleşti, saymaya yeniden başlanıyor...)\n")
                if es_deger == 11 or es_deger == 12 or es_deger == 13:  # vale,kız ve papaz için puanın 10 alınması
                    es_deger = 10
                yuzde += es_deger  # eşleşen kartların toplanması
                acilan_kart.pop(-1)
                acilan_kart_deger.pop(-1)
                karisik_deste = karisik_deste + acilan_kart  # eşleşen kartı başka destede tutmak
                karisik_degerli_deste = karisik_degerli_deste + acilan_kart_deger
                goster = 0  # sayacın sıfırlanması
                acilan_kart_deger.clear()
                acilan_kart.clear()
            if goster == 13:
                print("(Hiç eşleşmedi, saymaya yeniden başlanıyor...)\n")
                acilan_kart_deger.clear()  # eşleşme olmayan kartların silinmesi
                acilan_kart.clear()
                goster = 0
        print("Bitti, toplam puanınız: ", yuzde, "\nNiyetiniz %", yuzde, " ihtimalle gerçekleşecek", sep="")
        tekrar = input("Fal Bakma Oyununu tekrar oynamak ister misiniz(e/h):")
        while tekrar not in ["e", "h", "E", "H"]:  # girdi kontrolü
            tekrar = input("Fal Bakma Oyununu tekrar oynamak ister misiniz? (e/h):")
            tekrar.lower()
        if tekrar == "e":
            fal()
        else:
            menu()


def menu():
    print("1.Blackjack Oyunu", "\n", "2.Fal Bakma Oyunu", "\n", "3.Çıkış", sep="")
    secim = input("Seçiminizi giriniz:")
    while secim not in ["1", "2", "3"]:
        secim = input("Yanlış giriş yaptınız, seçiminizi tekrar giriniz:")
    if secim == "1":  # blackjack oyununun çalıştırılması
        print("♥ " * 16, "\n", "♦ " * 16, "\n", "Blackjack Oyununa Hoşgeldiniz\n", "♣ " * 14, "\n", "♠ " * 16, sep=" ")
        blackjack()
    elif secim == "2":  # fal bakma oyununun çalıştırılması
        print("♠ " * 18, "\n", "♠ Fal Bakma Oyununa Hoşgeldiniz ♠\n", "♠ " * 18, sep="")
        fal()
    else:  # çıkış
        cikis = input("Programdan çıkmak istediğinize emin misiniz? (e/h): ")
        while cikis not in ["e", "E", "H", "h"]:
            cikis = input("Yanlış giriş yaptınız,programdan çıkmak istediğinize emin misiniz? (e/h): ")
            cikis.lower()
        if cikis == "e":
            print("Programdan çıkılıyor...")
            exit()
        else:
            menu()


menu()
