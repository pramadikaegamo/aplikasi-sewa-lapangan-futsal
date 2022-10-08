import csv
import os.path
from os import path

data_baru = []
diperbaharui = {}
file_csv = "database.csv"

# Sub program menu utama


def menu():
    print("\n============= Menu Booking Lapangan Futsal =============")
    print("1. Informasi lapangan")
    print("2. Daftar harga")
    print("3. Sewa lapangan")
    print("4. Lihat semua data booking")
    print("5. Hapus data booking (jika sudah bermain & lunas)")
    print("6. Keluar")
    print("======================================================\n")

# Sub Program menu 1 (Informasi lapangan)


def informasi_lapangan():
    print("\n========== PENYEWAAN LAPANGAN FUTSAL LIPRAM ==========")
    print("Waktu Buka\t: 08.00 - 23.00 WIB")
    print("Alamat\t\t: Jl. Suka Coding Blok Z No.99 Rt.001 Rw.01\n\t\t Nusa Selatan, Angkasa Timur, Indonesia")
    print("Instagram\t: LIPRAM_CENTER_SPORT")
    print("Contact Person\t: 081193311911")
    print("======================================================")
    input("\nPress enter to continue...")

# Sub Program menu 2 (Daftar harga)


def daftar_harga():
    print("\n\t\t\tHARGA SEWA LAPANG FUTSAL")
    print("------------------------------------------------------------------------")
    print("     JAM\tSENIN\t SELASA\t RABU\t KAMIS\t JUM'AT\t SABTU\t MINGGU")
    print("------------------------------------------------------------------------")
    print("08.00 - 15.00\t75.000\t 75.000\t 75.000\t 75.000\t 75.000\t125.000\t125.000")
    print("15.00 - 16.00\t100.000\t100.000\t100.000\t100.000\t100.000\t125.000\t125.000")
    print("16.00 - 22.00\t125.000\t125.000\t125.000\t125.000\t125.000\t165.000\t165.000")
    print("22.00 - 23.00\t100.000\t100.000\t100.000\t100.000\t100.000\t100.000\t100.000")
    print("------------------------------------------------------------------------")
    input("\nPress enter to continue...")

# Sub program menu 3 (Sewa lapangan)


def penyewaan():
    print("\n\t\tLAPANGAN FUTSAL LIPRAM")
    print("======================================================")
    nama_pemesan = input("INPUT NAMA PEMESAN\t: ")
    hari = input("INPUT HARI\t\t: ")
    tanggal = int(input("INPUT TANGGAL SEWA\t: "))
    jam_mulai = int(input("INPUT JAM MULAI\t\t: "))
    jam_selesai = int(input("INPUT JAM SELESAI\t: "))
    lapang = input("INPUT LAPANGAN (1/2/3)\t: ")
    metode_pembayaran = input("INPUT METODE PEMBAYARAN (dp/lunas)\t: ")
    print("======================================================")
    if metode_pembayaran == "dp":
        if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis" or hari == "jumat":
            if jam_mulai == 8 or jam_mulai == 9 or jam_mulai == 10 or jam_mulai == 11 or jam_mulai == 12 or jam_mulai == 13 or jam_mulai == 14:
                tagihan = 75000
                print("TOTAL BAYAR\t:", tagihan)
                uang_bayar = int(input("UANG BAYAR\t: "))
                tagihan -= uang_bayar
                print("SISA BAYAR\t:", tagihan)
                simpan_data_baru = {"NAMA PENYEWA\t": nama_pemesan, "HARI\t\t": hari, "TANGGAL\t\t": tanggal, "MULAI JAM\t": jam_mulai,
                                    "SELESAI JAM\t": jam_selesai, "LAPANGAN KE\t": lapang, "JENIS PEMBAYARAN": metode_pembayaran, "SISA BAYAR\t": tagihan, "KEMBALIAN\t": 0}
                diperbaharui.update(simpan_data_baru)
                data_baru.append(diperbaharui.copy())
                print("======================================================")
            elif jam_mulai == 15:
                tagihan = 100000
                print("TOTAL BAYAR\t:", tagihan)
                uang_bayar = int(input("UANG BAYAR\t: "))
                tagihan -= uang_bayar
                print("SISA BAYAR\t:", tagihan)
                simpan_data_baru = {"NAMA PENYEWA\t": nama_pemesan, "HARI\t\t": hari, "TANGGAL\t\t": tanggal, "MULAI JAM\t": jam_mulai,
                                    "SELESAI JAM\t": jam_selesai, "LAPANGAN KE\t": lapang, "JENIS PEMBAYARAN": metode_pembayaran, "SISA BAYAR\t": tagihan, "KEMBALIAN\t": 0}
                diperbaharui.update(simpan_data_baru)
                data_baru.append(diperbaharui.copy())
                print("======================================================")
            elif jam_mulai == 16 or jam_mulai == 17 or jam_mulai == 18 or jam_mulai == 19 or jam_mulai == 20 or jam_mulai == 21:
                tagihan = 125000
                print("TOTAL BAYAR\t:", tagihan)
                uang_bayar = int(input("UANG BAYAR\t: "))
                tagihan -= uang_bayar
                print("SISA BAYAR\t:", tagihan)
                simpan_data_baru = {"NAMA PENYEWA\t": nama_pemesan, "HARI\t\t": hari, "TANGGAL\t\t": tanggal, "MULAI JAM\t": jam_mulai,
                                    "SELESAI JAM\t": jam_selesai, "LAPANGAN KE\t": lapang, "JENIS PEMBAYARAN": metode_pembayaran, "SISA BAYAR\t": tagihan, "KEMBALIAN\t": 0}
                diperbaharui.update(simpan_data_baru)
                data_baru.append(diperbaharui.copy())
                print("======================================================")
            elif jam_mulai == 22:
                tagihan = 100000
                print("TOTAL BAYAR\t:", tagihan)
                uang_bayar = int(input("UANG BAYAR\t: "))
                tagihan -= uang_bayar
                print("SISA BAYAR\t:", tagihan)
                simpan_data_baru = {"NAMA PENYEWA\t": nama_pemesan, "HARI\t\t": hari, "TANGGAL\t\t": tanggal, "MULAI JAM\t": jam_mulai,
                                    "SELESAI JAM\t": jam_selesai, "LAPANGAN KE\t": lapang, "JENIS PEMBAYARAN": metode_pembayaran, "SISA BAYAR\t": tagihan, "KEMBALIAN\t": 0}
                diperbaharui.update(simpan_data_baru)
                data_baru.append(diperbaharui.copy())
                print("======================================================")
        elif hari == "sabtu" or hari == "minggu":
            if jam_mulai == 8 or jam_mulai == 9 or jam_mulai == 10 or jam_mulai == 11 or jam_mulai == 12 or jam_mulai == 13 or jam_mulai == 14 or jam_mulai == 15:
                tagihan = 125000
                print("TOTAL BAYAR\t:", tagihan)
                uang_bayar = int(input("UANG BAYAR\t: "))
                tagihan -= uang_bayar
                print("SISA BAYAR\t:", tagihan)
                simpan_data_baru = {"NAMA PENYEWA\t": nama_pemesan, "HARI\t\t": hari, "TANGGAL\t\t": tanggal, "MULAI JAM\t": jam_mulai,
                                    "SELESAI JAM\t": jam_selesai, "LAPANGAN KE\t": lapang, "JENIS PEMBAYARAN": metode_pembayaran, "SISA BAYAR\t": tagihan, "KEMBALIAN\t": 0}
                diperbaharui.update(simpan_data_baru)
                data_baru.append(diperbaharui.copy())
                print("======================================================")
            elif jam_mulai == 16 or jam_mulai == 17 or jam_mulai == 18 or jam_mulai == 19 or jam_mulai == 20 or jam_mulai == 21:
                tagihan = 165000
                print("TOTAL BAYAR\t:", tagihan)
                uang_bayar = int(input("UANG BAYAR\t: "))
                tagihan -= uang_bayar
                print("SISA BAYAR\t:", tagihan)
                simpan_data_baru = {"NAMA PENYEWA\t": nama_pemesan, "HARI\t\t": hari, "TANGGAL\t\t": tanggal, "MULAI JAM\t": jam_mulai,
                                    "SELESAI JAM\t": jam_selesai, "LAPANGAN KE\t": lapang, "JENIS PEMBAYARAN": metode_pembayaran, "SISA BAYAR\t": tagihan, "KEMBALIAN\t": 0}
                diperbaharui.update(simpan_data_baru)
                data_baru.append(diperbaharui.copy())
                print("======================================================")
            elif jam_mulai == 22:
                tagihan = 100000
                print("TOTAL BAYAR\t:", tagihan)
                uang_bayar = int(input("UANG BAYAR\t: "))
                tagihan -= uang_bayar
                print("SISA BAYAR\t:", tagihan)
                simpan_data_baru = {"NAMA PENYEWA\t": nama_pemesan, "HARI\t\t": hari, "TANGGAL\t\t": tanggal, "MULAI JAM\t": jam_mulai,
                                    "SELESAI JAM\t": jam_selesai, "LAPANGAN KE\t": lapang, "JENIS PEMBAYARAN": metode_pembayaran, "SISA BAYAR\t": tagihan, "KEMBALIAN\t": 0}
                diperbaharui.update(simpan_data_baru)
                data_baru.append(diperbaharui.copy())
                print("======================================================")
    elif metode_pembayaran == "lunas":
        if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis" or hari == "jumat":
            if jam_mulai == 8 or jam_mulai == 9 or jam_mulai == 10 or jam_mulai == 11 or jam_mulai == 12 or jam_mulai == 13 or jam_mulai == 14:
                tagihan = 75000
                print("TOTAL BAYAR\t:", tagihan)
                uang_bayar = int(input("UANG BAYAR\t: "))
                uang_bayar -= tagihan
                print("UANG KEMBALI\t:", uang_bayar)
                simpan_data_baru = {"NAMA PENYEWA\t": nama_pemesan, "HARI\t\t": hari, "TANGGAL\t\t": tanggal, "MULAI JAM\t": jam_mulai,
                                    "SELESAI JAM\t": jam_selesai, "LAPANGAN KE\t": lapang, "JENIS PEMBAYARAN": metode_pembayaran, "SISA BAYAR\t": 0, "KEMBALIAN\t": uang_bayar}
                diperbaharui.update(simpan_data_baru)
                data_baru.append(diperbaharui.copy())
                print("======================================================")
            elif jam_mulai == 15:
                tagihan = 100000
                print("TOTAL BAYAR\t:", tagihan)
                uang_bayar = int(input("UANG BAYAR\t: "))
                uang_bayar -= tagihan
                print("UANG KEMBALI\t:", uang_bayar)
                simpan_data_baru = {"NAMA PENYEWA\t": nama_pemesan, "HARI\t\t": hari, "TANGGAL\t\t": tanggal, "MULAI JAM\t": jam_mulai,
                                    "SELESAI JAM\t": jam_selesai, "LAPANGAN KE\t": lapang, "JENIS PEMBAYARAN": metode_pembayaran, "SISA BAYAR\t": 0, "KEMBALIAN\t": uang_bayar}
                diperbaharui.update(simpan_data_baru)
                data_baru.append(diperbaharui.copy())
                print("======================================================")
            elif jam_mulai == 16 or jam_mulai == 17 or jam_mulai == 18 or jam_mulai == 19 or jam_mulai == 20 or jam_mulai == 21:
                tagihan = 125000
                print("TOTAL BAYAR\t:", tagihan)
                uang_bayar = int(input("UANG BAYAR\t: "))
                uang_bayar -= tagihan
                print("UANG KEMBALI\t:", uang_bayar)
                simpan_data_baru = {"NAMA PENYEWA\t": nama_pemesan, "HARI\t\t": hari, "TANGGAL\t\t": tanggal, "MULAI JAM\t": jam_mulai,
                                    "SELESAI JAM\t": jam_selesai, "LAPANGAN KE\t": lapang, "JENIS PEMBAYARAN": metode_pembayaran, "SISA BAYAR\t": 0, "KEMBALIAN\t": uang_bayar}
                diperbaharui.update(simpan_data_baru)
                data_baru.append(diperbaharui.copy())
                print("======================================================")
            elif jam_mulai == 22:
                tagihan = 100000
                print("TOTAL BAYAR\t:", tagihan)
                uang_bayar = int(input("UANG BAYAR\t: "))
                uang_bayar -= tagihan
                print("UANG KEMBALI\t:", uang_bayar)
                simpan_data_baru = {"NAMA PENYEWA\t": nama_pemesan, "HARI\t\t": hari, "TANGGAL\t\t": tanggal, "MULAI JAM\t": jam_mulai,
                                    "SELESAI JAM\t": jam_selesai, "LAPANGAN KE\t": lapang, "JENIS PEMBAYARAN": metode_pembayaran, "SISA BAYAR\t": 0, "KEMBALIAN\t": uang_bayar}
                diperbaharui.update(simpan_data_baru)
                data_baru.append(diperbaharui.copy())
                print("======================================================")
        elif hari == "sabtu" or hari == "minggu":
            if jam_mulai == 8 or jam_mulai == 9 or jam_mulai == 10 or jam_mulai == 11 or jam_mulai == 12 or jam_mulai == 13 or jam_mulai == 14 or jam_mulai == 15:
                tagihan = 125000
                print("TOTAL BAYAR\t:", tagihan)
                uang_bayar = int(input("UANG BAYAR\t: "))
                uang_bayar -= tagihan
                print("UANG KEMBALI\t:", uang_bayar)
                simpan_data_baru = {"NAMA PENYEWA\t": nama_pemesan, "HARI\t\t": hari, "TANGGAL\t\t": tanggal, "MULAI JAM\t": jam_mulai,
                                    "SELESAI JAM\t": jam_selesai, "LAPANGAN KE\t": lapang, "JENIS PEMBAYARAN": metode_pembayaran, "SISA BAYAR\t": 0, "KEMBALIAN\t": uang_bayar}
                diperbaharui.update(simpan_data_baru)
                data_baru.append(diperbaharui.copy())
                print("======================================================")
            elif jam_mulai == 16 or jam_mulai == 17 or jam_mulai == 18 or jam_mulai == 19 or jam_mulai == 20 or jam_mulai == 21:
                tagihan = 165000
                print("TOTAL BAYAR\t:", tagihan)
                uang_bayar = int(input("UANG BAYAR\t: "))
                uang_bayar -= tagihan
                print("UANG KEMBALI\t:", uang_bayar)
                simpan_data_baru = {"NAMA PENYEWA\t": nama_pemesan, "HARI\t\t": hari, "TANGGAL\t\t": tanggal, "MULAI JAM\t": jam_mulai,
                                    "SELESAI JAM\t": jam_selesai, "LAPANGAN KE\t": lapang, "JENIS PEMBAYARAN": metode_pembayaran, "SISA BAYAR\t": 0, "KEMBALIAN\t": uang_bayar}
                diperbaharui.update(simpan_data_baru)
                data_baru.append(diperbaharui.copy())
                print("======================================================")
            elif jam_mulai == 22:
                tagihan = 100000
                print("TOTAL BAYAR\t:", tagihan)
                uang_bayar = int(input("UANG BAYAR\t: "))
                uang_bayar -= tagihan
                print("UANG KEMBALI\t:", uang_bayar)
                simpan_data_baru = {"NAMA PENYEWA\t": nama_pemesan, "HARI\t\t": hari, "TANGGAL\t\t": tanggal, "MULAI JAM\t": jam_mulai,
                                    "SELESAI JAM\t": jam_selesai, "LAPANGAN KE\t": lapang, "JENIS PEMBAYARAN": metode_pembayaran, "SISA BAYAR\t": 0, "KEMBALIAN\t": uang_bayar}
                diperbaharui.update(simpan_data_baru)
                data_baru.append(diperbaharui.copy())
                print("======================================================")

# Sub Program menu 4 (Lihat semua data booking)


def yang_booking(banyak, booking):
    print("======================================================")
    for i in range(banyak):
        print("\nID ", str(i + 1))
        for key, value in booking[i].items():
            print(key, ":", value)
    print("======================================================")
    input("press enter to continue...")

# Sub Program pengecekan


def mengecek(banyak, nama):
    nilai = 0
    for i in range(banyak):
        if nama == data_baru[i]["NAMA PENYEWA\t"]:
            nilai = 1
    return nilai

# Sub Program menu 5 (Hapus data booking)


def hapus():
    nama_pemesan = input("\nMasukan nama pemyewa yang akan di hapus : ")
    i = 0
    for diperbaharui in data_baru:
        if nama_pemesan == data_baru[i]["NAMA PENYEWA\t"]:
            del data_baru[i]
        i += 1


# Menulis csv
def menulis_csv():
    keys = data_baru[0].keys()
    with open(file_csv, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data_baru)

# Membaca csv


def membaca_csv():
    with open(file_csv) as f:
        a = [{k: v for k, v in row.items()}
             for row in csv.DictReader(f, skipinitialspace=True)]
    return a

# Mengecek file csv


def mengecek_csv():
    cekAda = path.exists(file_csv)
    return cekAda

# Menhapus file csv


def mengahapus_csv():
    with open(file_csv, mode="w") as csv_file:
        fieldnames = ["NAMA PENYEWA\t", "HARI\t\t", "TANGGAL\t\t", "MULAI JAM\t",
                      "SELESAI JAM\t", "LAPANGAN KE\t", "JENIS PEMBAYARAN", "SISA BAYAR\t", "KEMBALIAN\t"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i in data_baru:
            writer.writerow({"NAMA PENYEWA\t": i["NAMA PENYEWA\t"], "HARI\t\t": i["HARI\t\t"], "TANGGAL\t\t": i["TANGGAL\t\t"], "MULAI JAM\t": i["MULAI JAM\t"], "SELESAI JAM\t": i["SELESAI JAM\t"],
                            "LAPANGAN KE\t": i["LAPANGAN KE\t"], "JENIS PEMBAYARAN": i["JENIS PEMBAYARAN"], "SISA BAYAR\t": i["SISA BAYAR\t"], "KEMBALIAN\t": i["KEMBALIAN\t"]})
    print("\nData sudah terhapus!")


# Main
if __name__ == "__main__":
    looping = True

    while looping:
        menu()
        pilihan = int(input("MASUKAN PILIHAN MENU\t: "))
        if pilihan == 1:
            informasi_lapangan()
        elif pilihan == 2:
            daftar_harga()
        elif pilihan == 3:
            cek = mengecek_csv()
            if cek == True:
                data_baru = membaca_csv()
                penyewaan()
                menulis_csv()
            else:
                penyewaan()
                menulis_csv()
        elif pilihan == 4:
            cek = mengecek_csv()
            if cek == True:
                data_baru = membaca_csv()
                yang_booking(len(data_baru), data_baru)
        elif pilihan == 5:
            cek = mengecek_csv()
            if cek == True:
                data_baru = membaca_csv()
                hapus()
                mengahapus_csv()
        elif pilihan == 6:
            looping = False
        else:
            print("\nPILIHAN MENU YANG ANDA MASUKAN SALAH (Masukan 1 - 6)")
            input("\nPress enter to continue...")
