lanjut = True
while lanjut :
    angka_pertama = int(input("masukan angka pertama = "))
    angka_kedua = int(input("masukan angka kedua = "))

    #tampilkan menu
    print("1.penjumlahan")
    print("2.pengurangan")
    print("3.perkalian")
    print("4.pembagian")
    print("5.keluar")
    pilihan = (input("masukan pilihan="))

    #operasi kalkulator
    if pilihan == "1" :
        hasil = angka_pertama + angka_kedua
        print(f"hasilnya adalah = {hasil}")
    elif pilihan == "2" :
        hasil = angka_pertama - angka_kedua
        print(f"hasilnya adalah = {hasil}")
    elif pilihan == "3" :
        hasil = angka_pertama * angka_kedua
        print(f"hasilnya adalah = {hasil}")
    elif pilihan == "4" :
        if angka_kedua == 0 :
            print("angka kedua tidak boleh nol")
        else:
            hasil = angka_pertama / angka_kedua
        print(f"hasilnya adalah = {hasil}")
    elif pilihan == "5":
      break
    else:
      print("pilihan tidak valid")
