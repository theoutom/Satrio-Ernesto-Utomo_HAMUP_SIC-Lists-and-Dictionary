# Membuat list untuk nama siswa
lst_nama_siswa = ['Satrio', 'Tio', 'Sat', 'Utomo', 'Tomo', 'Ernesto', 'Nesto'] 

# Membuat dictionary nilai siswa dengan key nama siswa, dan value nilai siswa
dict_nilai_siswa = { 'Satrio': 90,
               'Tio': 79,
               'Sat': 96,
               'Utomo': 89,
               'Tomo': 83,
               'Ernesto': 98,
               'Nesto': 81}

'''Mengoperasikan list'''
# Menambahkan siswa 'Momo' ke dalam list
lst_nama_siswa.append('Momo')

# Menghapus siswa 'Tio' dari list
lst_nama_siswa.remove('Tio')

# Mencetak list untuk mengecek data terbaru
print(lst_nama_siswa)

# Mencetak siswa dari index 0 (pertama dalam list)
print(f"Siswa pertama adalah {lst_nama_siswa[0]}")

# Mencetak siswa dari index -1 (terakhir dalam list)
print(f"Siswa terakhir adalah {lst_nama_siswa[-1]}")

# Mencetak siswa dari index ke -3 sampai -1 (3 Siswa terakhir dalam list)
print(f"Tiga siswa terakhir adalah {lst_nama_siswa[-4:-1]}")

'''Mengoperasikan dictionary'''
# Mengganti value dari key 'Satrio' ke 99
dict_nilai_siswa['Satrio'] = 99
print(dict_nilai_siswa) # Mencetak Dictionary terbaru

# Menghapus key dan value dari 'Tio'
dict_nilai_siswa.pop('Tio')
print(dict_nilai_siswa)

# Mengganti key 'Tomo' ke key 'Hamup'
dict_nilai_siswa['Hamup'] = dict_nilai_siswa.pop('Hamup')
print(dict_nilai_siswa)