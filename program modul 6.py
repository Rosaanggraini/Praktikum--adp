titik = []
for i in range(3):
    x = float(input("masukan koordinat titik x: "))
    y= float(input("masukan koordinat titik y: "))
    titik.append([x,y])
print(titik)

sisi_1 =((titik[0][0]-titik[0][1])**2 + (titik[0][1]-titik[1][1])**2 )**0.5
sisi_2 =((titik[1][0]-titik[2][0])**2 + (titik[1][1]-titik[2][1])**2 )**0.5
sisi_3 =((titik[0][0]-titik[2][0])**2 + (titik[0][1]-titik[2][1])**2 )**0.5
print(f"sisi_1 = {round(sisi_1, 3)}")
print(f"sisi_2 = {round(sisi_2, 3)}")
print(f"sisi_3 = {round(sisi_3, 3)}")

if sisi_1==sisi_2 or sisi_1==sisi_3 or sisi_2==sisi_3:
    print("ketiga titik tersebut membentuk segitiga sama kaki")
else:
    print("ketiga titik tersebut tidak membentuk segitiga sama kaki")