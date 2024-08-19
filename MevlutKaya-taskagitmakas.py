import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class TasKagitMakas:
    def __init__(self, root):
        self.root = root
        self.root.title("Taş Kağıt Makas Oyunu")

        # Oyun değişkenleri
        self.oyun_no = 0
        self.tur_no = 0
        self.oyuncu_skor = 0
        self.bilgisayar_skor = 0

        # Simge yükleme
        self.images = {
            "taş": ImageTk.PhotoImage(Image.open("/files/taş.png")),
            "kağıt": ImageTk.PhotoImage(Image.open("/files/kağıt.png")),
            "makas": ImageTk.PhotoImage(Image.open("/files/makas.png"))
        }

        # UI bileşenleri
        self.setup_ui()

    def setup_ui(self):
        self.oyun_no_label = tk.Label(self.root, text=f"{self.oyun_no}. Oyun")
        self.oyun_no_label.pack()

        self.tur_no_label = tk.Label(self.root, text=f"{self.tur_no}. Tur")
        self.tur_no_label.pack()

        self.skor_label = tk.Label(self.root, text=f"Siz: {self.oyuncu_skor} - Bilgisayar: {self.bilgisayar_skor}")
        self.skor_label.pack()

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()

        tk.Button(self.buttons_frame, text="Taş", command=lambda: self.oyuncu_secimi("taş")).pack(side=tk.LEFT)
        tk.Button(self.buttons_frame, text="Kağıt", command=lambda: self.oyuncu_secimi("kağıt")).pack(side=tk.LEFT)
        tk.Button(self.buttons_frame, text="Makas", command=lambda: self.oyuncu_secimi("makas")).pack(side=tk.LEFT)

        self.gorsel_frame = tk.Frame(self.root)
        self.gorsel_frame.pack(pady=20)

        self.oyuncu_image_label = tk.Label(self.gorsel_frame)
        self.oyuncu_image_label.pack(side=tk.LEFT, padx=20)

        self.bilgisayar_image_label = tk.Label(self.gorsel_frame)
        self.bilgisayar_image_label.pack(side=tk.RIGHT, padx=20)

        self.sonuc_label = tk.Label(self.root, text="")
        self.sonuc_label.pack(pady=20)

    def oyuncu_secimi(self, secim):
        if self.tur_no == 0:
            self.oyun_no += 1

        self.tur_no += 1

        bilgisayar_secimi = random.choice(["taş", "kağıt", "makas"])
        self.oyuncu_image_label.config(image=self.images[secim])

        if secim == bilgisayar_secimi:
            sonuc = "Berabere!"
        elif (secim == "taş" and bilgisayar_secimi == "makas") or \
                (secim == "kağıt" and bilgisayar_secimi == "taş") or \
                (secim == "makas" and bilgisayar_secimi == "kağıt"):
            sonuc = "Bu turu siz kazandınız!"
            self.oyuncu_skor += 1
        else:
            sonuc = "Bu turu bilgisayar kazandı!"
            self.bilgisayar_skor += 1

        self.bilgisayar_image_label.config(image=self.images[bilgisayar_secimi])

        self.sonuc_label.config(text=sonuc)
        self.oyun_no_label.config(text=f"{self.oyun_no}. Oyun")
        self.tur_no_label.config(text=f"{self.tur_no}. Tur")
        self.skor_label.config(text=f"Siz: {self.oyuncu_skor} - Bilgisayar: {self.bilgisayar_skor}")

        if self.oyuncu_skor == 2 or self.bilgisayar_skor == 2:
            self.oyun_bitti()

    def oyun_bitti(self):
        kazanan = "Siz kazandınız!" if self.oyuncu_skor > self.bilgisayar_skor else "Bilgisayar kazandı!"
        messagebox.showinfo("Oyun Bitti",
                            f"{kazanan}\nFinal Skoru: Siz - {self.oyuncu_skor}, Bilgisayar - {self.bilgisayar_skor}")
        self.yeni_oyun_sor()

    def yeni_oyun_sor(self):
        sonuc = messagebox.askquestion("Yeni Oyun?", "Başka bir oyun oynamak ister misiniz?", icon='question')
        bilgisayar_cevabi = random.choice(["evet", "hayır"])

        # Bilgisayar cevabını ve kullanıcı cevabını kontrol et
        if sonuc == "yes":  # 'yes' veya 'no' dönüyor
            if bilgisayar_cevabi == "evet":
                self.reset_oyun()
            else:
                messagebox.showinfo("Oyun Sonu", "Bilgisayar oynamak istemedi, oyun sonlandırıldı!")
                self.root.quit()
        else:
            messagebox.showinfo("Oyun Sonu", "Oyun sonlandırıldı!")
            self.root.quit()

    def reset_oyun(self):
        self.tur_no = 0
        self.oyuncu_skor = 0
        self.bilgisayar_skor = 0
        self.sonuc_label.config(text="")
        self.oyun_no_label.config(text=f"{self.oyun_no}. Oyun")
        self.tur_no_label.config(text=f"{self.tur_no}. Tur")
        self.skor_label.config(text=f"Siz: {self.oyuncu_skor} - Bilgisayar: {self.bilgisayar_skor}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TasKagitMakas(root)
    root.mainloop()
