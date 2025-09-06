lst_nama_siswa = ['Satrio: 90', 'Tio: 79', 'Sat: 96', 'Utomo: 89', 'Tomo: 83', 'Ernesto: 98', 'Nesto: 81'] 

dic_nilai_siswa = { 'Satrio': 90,
               'Tio': 79,
               'Sat': 96,
               'Utomo': 89,
               'Tomo': 83,
               'Ernesto': 98,
               'Nesto': 81}

lst_nama_siswa.append('Momo: 75')
lst_nama_siswa.remove('Tio: 79')
print(lst_nama_siswa)

print(f"Siswa pertama adalah {lst_nama_siswa[0]}")
print(f"Siswa terakhir adalah {lst_nama_siswa[-1]}")
print(f"Tiga siswa terakhir adalah {lst_nama_siswa[-4:-1]}")
