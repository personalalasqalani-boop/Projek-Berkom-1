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

# Price
total_price = 0
a = 1000000
b = 200000
c = 500000

# Items
grilled_bird_meat = 5
lizard_kebab = 4
steamed_whale_meat = 3
keranjang = []
menu = """
[Menu]

[Appetizer]
[$] Desert Dumplings: 
[$] Ham Sandwich:

[Main Course]
[$$] Grilled Bird Meat: 5
[$$] Lizard Kebab: 
[$$] Steamed Whale Meat: 

[Dessert]
[$] Black Dessert (Signature):
[$] Dark Pudding:

[Drinks]
[$] Sutaecha: 
[$] Milk Tea: 

[Pet Menu]
[] Good Feed:
[] Organic Feed:

[Keluar]
"""

menu_appetizer = """
[Appetizer]
[$]
[$]
"""
menu_mainCourse = """
[Main Course]
[$$] Grilled Bird Meat: 5
[$$] Order 2
[$$] Order 3
"""
menu_dessert = """
[Dessert]
[$] Black Dessert (Signature):
[$]
"""
menu_drinks = """
[Drinks]
[$]
[$]
"""
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
            if grilled_bird_meat >= 0:
                grilled_bird_meat = grilled_bird_meat - 1
                keranjang.append("Grilled Bird Meat")
                print("Grilled Bird Meat sudah ditambahkan ke keranjang!")
                total_price = total_price + a
            else:
                print("Order habis! Silahkan pilih order lain")

        elif pilihan_order == "2":
            if lizard_kebab >= 0:
                lizard_kebab = lizard_kebab - 1
                keranjang.append("Lizard Kebab")
                print("Lizard Kebab sudah ditambahkan ke keranjang!")
                total_price = total_price + b
            else:
                print("Order habis! Silahkan pilih order lain")

        elif pilihan_order == "3":
            if steamed_whale_meat >= 0:
                steamed_whale_meat = steamed_whale_meat - 1
                keranjang.append("Steamed Whale Meat")
                print("Steamed Whale Meat sudah ditambahkan ke keranjang!")
                total_price = total_price + c
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
                    print(f"Total pembayaran: {total_price}")
                break

            elif not keranjang:
                post_order = input(
                    "Keranjang kosong, apakah ingin keluar atau memilih lagi? [Pilih/Keluar] ").lower()
                if post_order == "keluar":
                    break

# Pengecekan keranjang, pembayaran akhir, dan exit jika tidak membeli
print("Terima kasih telah datang, sampai jumpa!")
