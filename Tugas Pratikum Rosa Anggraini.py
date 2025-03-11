#daftar paket makanan
paket_ayam = 20000
print(f'paket 1:ayam Rp{paket_ayam}')
paket_sapi = 35000
print(f'paket 2:sapi Rp{paket_sapi}')
paket_cumi_cumi = 45000
print(f'paket 3:cumi cumi Rp{paket_cumi_cumi}')

#keterangan pesanan
pesanan = (input("pesanan paket:"))

#harga paket
if pesanan == "ayam":
    harga = 20000
elif pesanan == "sapi":
    harga = 35000
elif pesanan == "cumi-cumi":
    harga = 45000
else:
    
    print("pilihan tidak valid!")
#ongkos kirim
jarak= float(input("jarak rumah anda dengan restoran(dalam km):"))


if jarak<1:
    ongkir = 0
elif 1 <= jarak <= 3:
    ongkir = 7000
else:
    ongkir = 15000
    print(f'ongkir anda :{ongkir}')

#hitung biaya total
total_biaya = harga + ongkir
print(f'total biaya = rp{total_biaya}')