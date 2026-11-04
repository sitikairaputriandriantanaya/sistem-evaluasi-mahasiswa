jumlah_mahasiswa = int(input("Jumlah mahasiswa (5-10): "))

if jumlah_mahasiswa >= 5 and jumlah_mahasiswa <= 10:
    total_nilai = 0

    for i in range(1, jumlah_mahasiswa + 1):
        nilai = float(input("Masukkan nilai mahasiswa " + str(i) + ": "))
        total_nilai += nilai

    rata_rata = total_nilai / jumlah_mahasiswa

    print("Nilai rata-rata:", rata_rata)

else:
    print("Jumlah mahasiswa harus 5 sampai 10!")