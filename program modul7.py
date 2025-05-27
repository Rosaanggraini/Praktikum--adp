def menu():
    print("""        
    menu
    1.tabel perkalian modulo n 
    2.mencari nilai sigma x 
    3.mencari nilai n!
    4.total dan rata-rata suatu data
    5.keluar""")
    
def tabel_modulo():
    while True:
        n= int(input("masukan nilai n(0 < n <= 10): "))
        if 0 < n <= 10:
            break
    print(f"tabel perkalian modulo {n} ")
    print(" ", end=" ")
    for i in range(n):
        print(f"{i:3}", end="")
    print()

    print("\n" + "-" * (n * 3 + 3))
    for i in range(n):
        print(f"{i:2}", end="")
        for j in range(n):
            print(f"{(i * j) % n:3}", end="")
        print()

def sigma_x():
    while True:
        batas_bawah = int (input("batas bawah: "))
        batas_atas = int (input("batas atas: "))
        if batas_atas >= batas_bawah:
           break
        print("batas atas harus lebih besar atau sama dengan batas bawah")

    jumlah=0
    for i in range(batas_bawah,batas_atas + 1):
        jumlah += i
    print(f"sigma_x dari{batas_bawah} hingga {batas_atas} adalah {jumlah}")

def n_faktorial():
    while True:
         n= int(input("masukan nilai n( n >= 0): "))
         if n >= 0:
             break
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    print(f"{n}! = {hasil}")

def total_rata_rata():
    while True:
         n= int(input("masukan banyak data ( n > 0): "))
         if n > 0:
             break
         
    data = []
    for i in range(n):
        angka =float(input(f"masukan data ke-{i+1} = "))
        data.append(angka)
        
    total= 0
    for nilai  in data:
        total += nilai
        
    rata_rata = total/n

    print(f"data yg dimasukkan = ")
    for i in range(n):
        print(f"masukan data ke-{i+1} = {data[i]}")

    print(f"total = {total}")
    print(f"rata_rata ={rata_rata}")    

def pilihan_menu():
    while True:
        menu()
        pilihan =input("pilih menu (1-5): ")
        if pilihan == "1":
            tabel_modulo()
        elif pilihan == "2":
            sigma_x()
        elif pilihan =="3":
            n_faktorial()
        elif pilihan == "4":
            total_rata_rata()
        elif pilihan == "5":
            print("keluar dari program ")
            break
        else:
            print("pilihan tidak valid!,silahkan inputkan kembali pilihan anda" )
pilihan_menu()

        



        
