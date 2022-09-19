import json
data = None
with open('mahasiswa.json','r+') as datafile:
    data = json.load(datafile)

    jml_mahasiswa = int(input("Masukkan jumlah mahasiswa baru : "))
    for i in range(0,jml_mahasiswa):
        nama_mahasiswa = input("Masukkan nama Anda : ")
        jml_prestasi = int(input("Masukkan Jumlah hobi : "))
        hobi = list()
        hitung = 1
        for isi in range(0,jml_prestasi):
            isi_hobi = input("Masukkan Hobi ke-%d : "%(hitung))
            hobi.append(isi_hobi)
            hitung += 1
        prestasi_mahasiswa = input("Masukkan Prestasi Anda : ")
        isi = {nama_mahasiswa:[
            {"Biodata" : {
                "Hobi" : hobi,
                "Prestasi": prestasi_mahasiswa
            }}]}
        print("==== Data berhasil ditambahkan ====")
        data.update(isi)
        datafile.seek(0)
        json.dump(data,datafile,indent=4)