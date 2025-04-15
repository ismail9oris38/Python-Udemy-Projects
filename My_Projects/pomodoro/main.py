from tkinter import *
import math

# ---------------------------- SABİTLER ------------------------------- #
RENK_PEMBE = "#e2979c"
RENK_KIRMIZI = "#e7305b"
RENK_YESIL = "#9bdeac"
RENK_SARI = "#f7f5dd"
YAZI_TIPI = "Courier"
CALISMA_DK = 25
KISA_MOLA_DK = 5
UZUN_MOLA_DK = 20

tur = 0
zamanlayici = None

# ---------------------------- ZAMANLAYICIYI SIFIRLA ------------------------------- #
def sifirla():
    window.after_cancel(zamanlayici)
    kanvas.itemconfig(sure_yazi, text="00:00")
    baslik.config(text="Zamanlayıcı", fg=RENK_YESIL)
    tikler.config(text="")
    global tur
    tur = 0

# ---------------------------- ZAMANLAYICI BAŞLAT ------------------------------- #
def baslat():
    global tur
    tur += 1

    calisma_saniye = CALISMA_DK * 60
    kisa_mola_saniye = KISA_MOLA_DK * 60
    uzun_mola_saniye = UZUN_MOLA_DK * 60

    if tur % 8 == 0:
        geri_say(uzun_mola_saniye)
        baslik.config(text="Uzun Mola", fg=RENK_KIRMIZI)
    elif tur % 2 == 0:
        geri_say(kisa_mola_saniye)
        baslik.config(text="Kısa Mola", fg=RENK_PEMBE)
    else:
        geri_say(calisma_saniye)
        baslik.config(text="Çalış", fg=RENK_YESIL)

# ---------------------------- GERİ SAYIM MEKANİZMASI ------------------------------- #
def geri_say(sayac):
    dakika = math.floor(sayac / 60)
    saniye = sayac % 60
    kanvas.itemconfig(sure_yazi, text=f"{dakika:02}:{saniye:02}")

    if sayac > 0:
        global zamanlayici
        zamanlayici = window.after(1000, geri_say, sayac - 1)
    else:
        baslat()
        tik_isaretleri = "✔" * (tur // 2)
        tikler.config(text=tik_isaretleri)

# ---------------------------- ARAYÜZ OLUŞTUR ------------------------------- #
window = Tk()
window.title("Pomodoro Zamanlayıcı")
window.config(padx=100, pady=50, bg=RENK_SARI)

baslik = Label(text="Zamanlayıcı", fg=RENK_YESIL, bg=RENK_SARI, font=(YAZI_TIPI, 50))
baslik.grid(column=1, row=0)

kanvas = Canvas(width=200, height=224, bg=RENK_SARI, highlightthickness=0)
domates_resmi = PhotoImage(file="tomato.png")
kanvas.create_image(100, 112, image=domates_resmi)
sure_yazi = kanvas.create_text(100, 130, text="00:00", fill="white", font=(YAZI_TIPI, 35, "bold"))
kanvas.grid(column=1, row=1)

baslat_butonu = Button(text="Başlat", highlightthickness=0, command=baslat)
baslat_butonu.grid(column=0, row=2)

sifirla_butonu = Button(text="Sıfırla", highlightthickness=0, command=sifirla)
sifirla_butonu.grid(column=2, row=2)

tikler = Label(fg=RENK_YESIL, bg=RENK_SARI)
tikler.grid(column=1, row=3)

window.mainloop()