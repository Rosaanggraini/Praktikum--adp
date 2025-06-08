with open("data_praktikan.txt", "w") as file: 
    file.write("Nim,Nama,Nilai pretest,Nilai postest,Nilai tugas\n") 
    file.write("2410431033,mifta,80,85,90 \n")
    file.write("2410432033,sonia,75,80,85 \n")
    file.write("2410433033,bela,70,75,80 \n") 
    file.write("2410434033,yeni,98,98,75 \n") 
    file.write("2410435033,refiana,45,55,70 \n") 
    file.write("2410436033,nafisa,35,35,65 \n") 
    file.write("2410437033,ilfi,30,20,60 \n")
    file.write("2410438033,susanti,44,50,70 \n")
    file.write("2410439033,kia,100,10,70 \n")
    file.write("2410430033,fatia,5,30,82 \n")

praktikan_dict = {}

with open("data_praktikan.txt", "r") as file:
        next(file)
        for baris in file:
            nim, nama, pretest, posttest, tugas = baris.strip().split(",") 
            praktikan_dict[nim] = {
                "Nama": nama,
                "pretest": int(pretest),
                "postest": int(posttest), 
                "tugas": int(tugas)
            }

with open("data_nilai_akhir.txt", "w") as file_output:
    file_output.write(" Nim,Nama,Nilai pretest,Nilai postest,Nilai tugas,nilai akhir \n")
 
    print("\n rekapan data praktikan algoritma dan pemprograman:")
    print(f"{"nim":<12} | {"Nama":<10} | {"pretest":<8} | {"postest":<8} | {"tugas":<6}")
    print("-" * 50)
    for nim, data in praktikan_dict.items():
        print(f"{nim:<12} | {data["Nama"]:<10} | {data["pretest"]:<8} | {data["postest"]:<8} | {data["tugas"]:<6}")
        pretest = data["pretest"]
        postest = data["postest"]
        tugas = data["tugas"]

        nilai_akhir = (0.35 * pretest) + (0.35 * postest) + (0.30 * tugas)
        praktikan_dict[nim]["nilai akhir"] = nilai_akhir

        file_output.write(f"{nim},{data["Nama"]},{pretest},{postest},{tugas},{round(nilai_akhir, 2)}\n")

print("\nNilai akhir praktikan sudah selesai dihitung dan disimpan ke file 'data_nilai_akhir.txt'.")

nilai_tertinggi = 0
nilai_terendah = 100 
praktikan_tertinggi = " "
praktikan_terendah = " "
total_nilai = 0
jumlah_praktikan = len(praktikan_dict)

for nim, data in praktikan_dict.items():
    nilai_akhir = data["nilai akhir"]
    total_nilai += nilai_akhir

    if nilai_akhir > nilai_tertinggi:
        nilai_tertinggi = nilai_akhir
        praktikan_tertinggi = data["Nama"]

    if nilai_akhir < nilai_terendah:
        nilai_terendah = nilai_akhir
        praktikan_terendah = data["Nama"]

rata_rata = total_nilai / jumlah_praktikan

rata2_dibawah = sum(1 for data in praktikan_dict.values() if data["nilai akhir"] < rata_rata)

print(f"{"-"*50}")
print(f"{"rekapan data nilai praktikan algoritma dan pemprograman":^50}")
print(f"{"-"*50}")

print(f"{"Praktikan dengan Nilai Tertinggi":<30} =  {praktikan_tertinggi}:({nilai_tertinggi})")
print(f"{"Praktikan dengan Nilai Terendah":<30}  = {praktikan_terendah}:({nilai_terendah})")
print(f"{"Rata-rata Nilai Akhir":<30}  = {round(rata_rata, 2)}")
print(f"{"Jumlah di Bawah Rata-rata":<30} = {rata2_dibawah} orang")

print(f"{"-"*50}")