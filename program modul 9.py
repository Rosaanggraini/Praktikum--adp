import time
from termcolor import colored
teks = "Happy Eid"
langkah = 20
durasi = 20
time.sleep(1)

for i in range(langkah):
    teks_bergerak = " "*i + teks
    teks_yg_terlihat = teks_bergerak[:langkah]

    print(colored(teks_yg_terlihat, "magenta"))
    time.sleep(1)