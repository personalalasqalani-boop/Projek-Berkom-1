A = 3
B = 2
C = 5
D = 7
E = 9
F = 10
G = 4
H = 9
I = 3


menu = """[Menu]

Order 1
Order 2
Order 3

[Keluar] """

print(menu)
pilihan_keluar = str
pilihan_action = str(
    input("Selamat datang di restoran A, apakah mau membeli? [Y/N] "))

if pilihan_action == "y" or pilihan_action == "Y":

    pilihan_order = str(input("Pilih order: "))

    if pilihan_order == "1":
        print("Order 1")
    elif pilihan_order == "2":
        print("Order 2")
    elif pilihan_order == "3":
        print("Order 3")
    elif pilihan_order == "Keluar":
        print("Selesai, terima kasih")

elif pilihan_action == "n" or pilihan_action == "N":
    pilihan_keluar = str(input("Apakah ingin membayar atau keluar? "))
    if pilihan_keluar == "keluar":
        print("Terima kasih, sampai jumpa")
