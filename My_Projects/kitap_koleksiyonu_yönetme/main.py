import turtle
from tkinter import *
from tkinter import messagebox
import pandas
import time


# -------------------------------------------------- OPENING SCREEN  --------------------------------------------------#

def opening_screen():
    # Turtle ekranı oluşturuluyor ve arka plan rengi lightblue olarak ayarlanıyor
    screen = turtle.Screen()
    screen.bgcolor("lightblue")

    # Turtle nesnesi oluşturuluyor ve görünmez yapılıyor
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()  # Kalem kaldırılıyor, çizim yapmaması için
    t.goto(0, 0)  # Başlangıç noktası (0,0)

    # Mesaj yazdırılıyor
    t.write("Welcome To The Book Collection!", align="center", font=("Arial", 18, "bold"))

    # 3 saniye bekleniyor
    time.sleep(3)

    # Turtle ekranı kapatılıyor
    turtle.bye()


opening_screen()  # Bu fonksiyon çağrılıyor ve açılış ekranı gösteriliyor.

# -------------------------------------------------- FILE OPERATION --------------------------------------------------#

try:
    # CSV dosyasından kitap verileri okunuyor
    data_file = pandas.read_csv("Book_Collection.csv")
except FileNotFoundError:
    # Eğer dosya bulunamazsa, boş bir veri seti oluşturuluyor
    data = {
        "Book Name": [],
        "Author": [],
        "Publishing House": [],
        "Years": [],
        "ISBN": []
    }
    data_records = []  # Veri kayıtları
    data_file = []  # Boş veri seti
else:
    # CSV dosyasındaki veriler bir dictionary'ye dönüştürülüyor
    data = data_file.to_dict(orient='list')
    data_records = data_file.to_dict(orient='records')


# --------------------------------------------------- SEARCH --------------------------------------------------- #

def search():
    # Kullanıcıdan alınan kitap adı ve yazar adı
    book_name = book_name_entry.get()
    author = author_entry.get()

    # Kitap adı veya yazar adı girilmemişse hata mesajı gösteriliyor
    if not author and not book_name:
        messagebox.showerror(title="Warning", message="Please you write the book name or author name.")
        return

    # Kitap adı ve yazar adı ile arama yapılıyor
    if book_name and author:
        book_names = data_file[
            data_file["Book Name"].str.contains(book_name, case=False, na=False) & data_file["Author"].str.contains(
                author, case=False, na=False)]
    elif book_name:
        book_names = data_file[data_file["Book Name"].str.contains(book_name, case=False, na=False)]
    else:
        book_names = data_file[data_file["Author"].str.contains(author, case=False, na=False)]

    # Eğer arama sonuçları boşsa, uyarı mesajı gösteriliyor
    if book_names.empty:
        messagebox.showerror(title="Warning", message="The book you are looking for is not available.")
        return

    # Bulunan kitaplar listeleniyor
    for index, row in book_names.iterrows():
        message = f"{row['Book Name']} - {row['Author']} - {row['Publishing House']} - {row['Years']} - {row['ISBN']}\n"
        messagebox.showinfo(title="Books", message=message)


# ---------------------------- ALL BOOK ------------------------------- #

def see_books():
    # Eğer kitap kaydı yoksa uyarı mesajı gösteriliyor
    if not data_records:
        messagebox.showerror(title="Warning", message="You don't have any book records.")
        return
    # Tüm kitaplar listeleniyor
    messages = "\n".join(
        [f"{book['Book Name']} - {book['Author']} - {book['Publishing House']} - {book['Years']} - {book['ISBN']}" for
         book in data_records])
    messagebox.showinfo(title="All Books", message=messages)


# ---------------------------- SAVE ------------------------------- #

def save():
    # Kullanıcıdan kitap bilgileri alınıyor
    book_name = book_name_entry.get()
    author = author_entry.get()
    yayinevi = yayinevi_entry.get()
    years = years_entry.get()
    ISBN = ISBN_entry.get()

    # Eğer herhangi bir bilgi eksikse, hata mesajı gösteriliyor
    if not book_name or not author or not yayinevi or not years or not ISBN:
        messagebox.showerror(title="Warning", message="There are empty places.")
        return

    # Kullanıcıdan onay alınıyor
    is_on = messagebox.askokcancel(title="confirm", message="Are you sure?")
    if is_on:
        # Yeni kitap kaydı oluşturuluyor
        new_record = {
            "Book Name": book_name,
            "Author": author,
            "Publishing House": yayinevi,
            "Years": years,
            "ISBN": ISBN
        }
        # Yeni kayıt ekleniyor ve CSV dosyasına kaydediliyor
        data_records.append(new_record)
        pandas.DataFrame(data_records).to_csv("Book_Collection.csv", index=False)

        # Giriş alanları temizleniyor
        book_name_entry.delete(0, END)
        author_entry.delete(0, END)
        yayinevi_entry.delete(0, END)
        years_entry.delete(0, END)
        ISBN_entry.delete(0, END)

        # Başarı mesajı gösteriliyor
        messagebox.askokcancel(title="success", message="Book saved successfully.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Book Collection")
window.config(padx=50, pady=50)

# Canvas nesnesi oluşturuluyor ve resim ekleniyor
canvas = Canvas(width=416, height=416)
book_image = PhotoImage(file="book_image.png")
canvas.create_image(208, 208, image=book_image)
canvas.grid(row=0, column=0, columnspan=3)

# LABEL
# Kitap adı, yazar, yayınevi, yıl ve ISBN için etiketler oluşturuluyor ve hücrelere yerleştiriliyor
book_name_label = Label(text="Book Name:")
book_name_label.grid(row=1, column=0, sticky="w")

author_label = Label(text="Author:")
author_label.grid(row=2, column=0, sticky="w")

yayinevi_label = Label(text="Publishing House:")
yayinevi_label.grid(row=3, column=0, sticky="w")

years_label = Label(text="Years:")
years_label.grid(row=4, column=0, sticky="w")

ISBN_label = Label(text="ISBN:")
ISBN_label.grid(row=5, column=0, sticky="w")

# ENTRY
# Kullanıcıdan bilgi almak için giriş alanları oluşturuluyor
book_name_entry = Entry(width=30)
book_name_entry.grid(row=1, column=1)

author_entry = Entry(width=30)
author_entry.grid(row=2, column=1)

yayinevi_entry = Entry(width=40)
yayinevi_entry.grid(row=3, column=1, columnspan=2)

years_entry = Entry(width=40)
years_entry.grid(row=4, column=1, columnspan=2)

ISBN_entry = Entry(width=40)
ISBN_entry.grid(row=5, column=1, columnspan=2)

# BUTTON
# Kaydetme, tüm kitapları görme ve arama butonları oluşturuluyor
save_button = Button(text="SAVE", command=save, width=38, height=3)
save_button.grid(row=6, column=1, columnspan=2, pady=10)

all_book_button = Button(text="ALL BOOK", command=see_books, width=38, height=2)
all_book_button.grid(row=7, column=1, columnspan=2)

search_button = Button(text="SEARCH", command=search, height=3)
search_button.grid(row=1, column=2, rowspan=2)

window.mainloop()  # Tkinter GUI çalıştırılıyor
