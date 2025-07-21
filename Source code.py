import re
from datetime import datetime

class DataKendaraan:
    def __init__(self, pemilik, merk, tahun, jenis, nopol, warna):
        self.__pemilik = pemilik
        self.__merk = merk
        self.__tahun = tahun
        self.__jenis = jenis
        self.__nopol = nopol
        self.__warna = warna

    def ambildata(self):
        return f"{self.__pemilik},{self.__merk},{self.__tahun},{self.__jenis},{self.__nopol},{self.__warna}"

    def get_pemilik(self): return self.__pemilik
    def get_merk(self): return self.__merk
    def get_tahun(self): return self.__tahun
    def get_jenis(self): return self.__jenis
    def get_nopol(self): return self.__nopol
    def get_warna(self): return self.__warna


class CekKendaraan(DataKendaraan):
    def __init__(self, pemilik, merk, tahun, jenis, nopol, warna):
        super().__init__(pemilik, merk, tahun, jenis, nopol, warna)

    def cek_kendaraan_tua(self):
        tahun_sekarang = datetime.now().year
        umur = tahun_sekarang - int(self.get_tahun()) 
        return umur > 10


def simpan(data):
    try:
        with open("kendaraan.log", "a") as file:
            file.write(data + "\n")
        print("Data disimpan.")
    except Exception as eror:
        print("Gagal simpan data:", eror)

def mulai():
    print("Input Kendaraan")

    while True:
        try:
            pemilik = input("Nama pemilik  : ")
            if not re.match(r"^[a-zA-Z\s]+$", pemilik):
                raise ValueError("Nama pemilik cuma boleh huruf dan spasi.")

            merk = input("Merk kendaraan: ")
            if not re.match(r"^[A-Za-z\s]{2,}$", merk):
                raise ValueError("Merk kendaraan hanya huruf dan spasi, min 2 karakter.")

            tahun = input("Tahun kendaraan: ")
            if not (tahun.isdigit() and 1980 <= int(tahun) <= 2025):
                raise ValueError("Tahun harus antara 1980 sampai 2025.")

            jenis = input("Jenis kendaraan (Mobil/Motor/Truk): ")
            if jenis.lower() not in ["mobil", "motor", "truk"]:
                raise ValueError("Jenis kendaraan harus Mobil, Motor, atau Truk.")

            nopol = input("Nomor Polisi (cth: AB1234CD) tanpa spasi: ").upper()
            if not re.match(r"^[A-Z]{1,2}\d{1,4}[A-Z]{1,3}$", nopol):
                raise ValueError("Format nomor polisi tidak valid.")

            warna = input("Warna kendaraan: ")
            if not re.match(r"^[A-Za-z\s]+$", warna):
                raise ValueError("Warna hanya boleh huruf dan spasi.")

            break
        except ValueError as erorvalue:
            print("Error:", erorvalue)
        except Exception as erorexception:
            print("Kesalahan:", erorexception)

    kendaraan = CekKendaraan(pemilik, merk, tahun, jenis, nopol, warna)
    print("\nData oke.")
    print("Pemilik     :", kendaraan.get_pemilik())
    print("Merk        :", kendaraan.get_merk())
    print("Tahun       :", kendaraan.get_tahun())
    print("Jenis       :", kendaraan.get_jenis())
    print("No Polisi   :", kendaraan.get_nopol())
    print("Warna       :", kendaraan.get_warna())

    if kendaraan.cek_kendaraan_tua():
        print("Catatan: Kendaraan ini termasuk kendaraan tua (lebih dari 10 tahun).")
    else:
        print("Catatan: Kendaraan ini termasuk kendaraan baru (kurang dari 10 tahun).")
        
    simpan(kendaraan.ambildata())

mulai()