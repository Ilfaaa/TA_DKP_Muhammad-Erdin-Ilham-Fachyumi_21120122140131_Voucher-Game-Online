import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font

class AkiraTopUp:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Akira Top-up")
        self.main_window.geometry("500x500")

        self.main_window.configure(bg="light blue")

        self.title_font = font.Font(family="Calibri Light", size=20, weight="bold")

        self.title_label = tk.Label(self.main_window, text="Akira Top-up", font=self.title_font, bg="light blue")
        self.title_label.pack()

        self.selected_game_label = tk.Label(self.main_window, text="Game yang dipilih: -", font=("Calibri Light", 15), bg="light blue")
        self.selected_game_label.pack()

        self.game_combobox = ttk.Combobox(self.main_window, values=["Mobile Legends: Bang Bang", "PUBGM"], font=("Calibri Light", 15), background="light blue")
        self.game_combobox.set("Pilih Game")
        self.game_combobox.bind("<<ComboboxSelected>>", self.select_game)
        self.game_combobox.pack()

        self.quantity_label = tk.Label(self.main_window, text="Jumlah Voucher:", font=("Calibri Light", 15), bg="light blue")
        self.quantity_label.pack()
        self.voucher_combobox = ttk.Combobox(self.main_window, font=("Calibri Light", 15), background="light blue")
        self.voucher_combobox.pack()

        self.payment_label = tk.Label(self.main_window, text="Metode Pembayaran:", font=("Calibri Light", 15), bg="light blue")
        self.payment_label.pack()
        self.payment_combobox = ttk.Combobox(self.main_window, values=["Go-Pay", "DANA", "BRI", "BNI", "BCA", "Mandiri"], font=("Calibri Light", 15), background="light blue")
        self.payment_combobox.pack()

        self.email_label = tk.Label(self.main_window, text="Masukkan Email:", font=("Calibri Light", 15), bg="light blue")
        self.email_label.pack()

        self.email_entry = tk.Entry(self.main_window, font=("Calibri Light", 15))
        self.email_entry.pack()

        self.spacing_label = tk.Label(self.main_window, text="", bg="light blue")  # Spasi antara menu "Masukkan Email" dan tombol "Konfirmasi"
        self.spacing_label.pack()

        self.confirmation_button = tk.Button(self.main_window, text="Konfirmasi", command=self.show_confirmation_popup, font=("Calibri Light", 15), bg="light green")
        self.confirmation_button.pack()

        self.prices = {
            "12 Diamond": "6000 IDR",
            "53 Diamond": "17000 IDR",
            "87 Diamond": "26000 IDR",
            "115 Diamond": "42000 IDR",
            "167 Diamond": "50000 IDR",
            "204 Diamond": "63000 IDR",
            "243 Diamond": "76000 IDR",
            "52 UC": "10000 IDR",
            "100 UC": "20000 IDR",
            "250 UC": "50000 IDR",
            "500 UC": "100000 IDR",
            "1500 UC": "300000 IDR",
            "2500 UC": "500000 IDR"
        }

    def select_game(self, event):
        self.selected_game_label.config(text="Game yang dipilih: " + self.game_combobox.get())
        self.update_voucher_choices()

    def update_voucher_choices(self):
        selected_game = self.game_combobox.get()

        if selected_game == "Mobile Legends: Bang Bang":
            self.voucher_combobox.config(values=["12 Diamond", "53 Diamond", "87 Diamond", "115 Diamond", "167 Diamond", "204 Diamond", "243 Diamond"])
            self.voucher_combobox.current(0)
        elif selected_game == "PUBGM":
            self.voucher_combobox.config(values=["52 UC", "100 UC", "250 UC", "500 UC", "1500 UC", "2500 UC"])
            self.voucher_combobox.current(0)
        else:
            self.voucher_combobox.config(values=[])
            self.voucher_combobox.set("Pilih Game terlebih dahulu")

    def show_confirmation_popup(self):
        game = self.game_combobox.get()
        quantity = self.voucher_combobox.get()
        payment = self.payment_combobox.get()
        email = self.email_entry.get()

        if game == "" or quantity == "" or payment == "" or email == "":
            messagebox.showwarning("Peringatan", "Mohon lengkapi semua menu sebelum melakukan konfirmasi.")
        elif ".com" not in email:
            messagebox.showwarning("Peringatan", "Masukkan email Anda dengan benar.")
        else:
            price = self.prices.get(quantity, "Unknown")
            message = f"Konfirmasi Pemesanan Voucher:\n\nGame: {game}\nJumlah voucher: {quantity}\nHarga: {price}\nMetode pembayaran: {payment}\nEmail: {email}"
            messagebox.showinfo("Konfirmasi Pemesanan Voucher", message)
            self.ask_for_transaction()

    def ask_for_transaction(self):
        answer = messagebox.askquestion("Transaksi Lain", "Apakah Anda ingin melakukan transaksi lain?")
        if answer == "yes":
            self.reset_fields()
            self.main_window.deiconify()
        else:
            self.main_window.destroy()

    def reset_fields(self):
        self.game_combobox.set("Pilih Game")
        self.selected_game_label.config(text="Game yang dipilih: -")
        self.voucher_combobox.set("")
        self.payment_combobox.set("")
        self.email_entry.delete(0, tk.END)

    def run(self):
        self.main_window.mainloop()

    def show_menu_prices(self):
        game = self.game_combobox.get()

        if game == "Mobile Legends: Bang Bang":
            prices = {
                "12 Diamond": "6000 IDR",
                "53 Diamond": "17000 IDR",
                "87 Diamond": "26000 IDR",
                "115 Diamond": "42000 IDR",
                "167 Diamond": "50000 IDR",
                "204 Diamond": "63000 IDR",
                "243 Diamond": "76000 IDR"
            }
        elif game == "PUBGM":
            prices = {
                "52 UC": "10000 IDR",
                "100 UC": "20000 IDR",
                "250 UC": "50000 IDR",
                "500 UC": "100000 IDR",
                "1500 UC": "300000 IDR",
                "2500 UC": "500000 IDR"
            }
        else:
            prices = {}

        price_message = "Harga:\n"
        for voucher, price in prices.items():
            price_message += f"{voucher}: {price}\n"

        messagebox.showinfo("Harga Voucher", price_message)

app = AkiraTopUp()
app.run()
