# KAMUS:

# order_1, order_2, order_3: Makanan
# menu: Tampilan menu
# keranjang: list untuk isi keranjang
# pilihan_action: Apa yang ingin user lakukan? (Beli/Keluar)
# pilihan_order: Apa yang ingin user lakukan? (Pilih order/Keluar)
# next_choice: Apa yang ingin user lakukan setelah memilih order(Jika memilih)? (Bayar/Liat menu lagi)
# post_order: Apa yang ingin user lakukan setelah memilih order(Jika selesai)? (Bayar/Liat menu lagi)

# KODE:

# Deklarasi variabel awal yang akan digunakan: stock, menu, dll
order_1 = 5
order_2 = 4
order_3 = 3
menu = """[Menu]

Order 1
Order 2
Order 3

[Keluar] """
keranjang = []

# Tampilan awal menu dan input
print(menu)

pilihan_action = str(
    input("Selamat datang di restoran A, apakah mau membeli? [Y/N] ")).lower()

# Untuk memastikan input benar
while pilihan_action != "y" and pilihan_action != "n":
    print("Invalid input!")
    pilihan_action = input("Apakah ingin membeli? [Y/N] ").lower()

# Pemilihan order jika user memilih "y"
if pilihan_action == "y":

    while True:

        pilihan_order = input(
            "Pilih order atau keluar: [1/2/3/Keluar] ").lower()

        if pilihan_order == "1":
            order_1 = order_1 - 1  # Ngurangin stock
            if order_1 >= 0:
                keranjang.append("Order 1")  # Nambah order ke keranjang
                print("Order 1 sudah ditambahkan ke keranjang!")
            else:
                print("Order habis! Silahkan pilih order lain")

        elif pilihan_order == "2":
            order_2 = order_2 - 1
            if order_2 >= 0:
                keranjang.append("Order 2")
                print("Order 2 sudah ditambahkan ke keranjang!")
            else:
                print("Order habis! Silahkan pilih order lain")

        elif pilihan_order == "3":
            order_3 = order_3 - 1
            if order_3 >= 0:
                keranjang.append("Order 3")
                print("Order 3 sudah ditambahkan ke keranjang!")
            else:
                print("Order habis! Silahkan pilih order lain")

        if pilihan_order in ("1", "2", "3"):
            next_choice = input("Apakah ingin lanjut memilih? [Y/N] ").lower()

            while next_choice not in ("y", "n"):
                print("Invalid input!")
                next_choice = input(
                    "Apakah ingin lanjut memilih? [Y/N] ").lower()

            if next_choice == "n":
                print("Berikut adalah pesanan anda: ")
                for pesanan in keranjang:
                    print(pesanan)
                break

        if pilihan_order == "keluar":
            if keranjang:
                print("Berikut adalah pesanan anda: ")
                for pesanan in keranjang:
                    print(pesanan)
                break

            elif not keranjang:
                post_order = input(
                    "Keranjang kosong, apakah ingin keluar atau memilih lagi? [Pilih/Keluar] ").lower()
                if post_order == "keluar":
                    break

# Pengecekan keranjang, pembayaran akhir, dan exit jika tidak membeli
print("Terima kasih telah datang, sampai jumpa!")
