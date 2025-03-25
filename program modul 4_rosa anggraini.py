n = int(input("Masukkan ukuran grid (minimal 4): "))

if n < 4:
    print("Minimal nilai n adalah 4")
else:
    total_boom = 0  
    tengah = n//2

    for i in range(n):
        for j in range(n):
            if n % 2 == 1 and i == tengah and j == tengah: 
                print(" HORE ", end=" ")
            elif i == j:  
                print(" 1 ", end=" ")
            elif i + j == n - 1:  
                print(" 2 ", end=" ")
            else:
                print(" BOOM ", end=" ")
                total_boom += 1  

        print() 
        
    print(f"\nTotal BOOM yang muncul sebanyak = {total_boom}")