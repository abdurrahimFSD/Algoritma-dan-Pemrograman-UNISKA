# 2210010460
# Abdurrahim

print()
print ('Program Kalkulator Sederhana')
print ('****************************')
print()
print('## NPM    : 2210010460   ##')
print('## NAMA   : ABDURRAHIM   ##')
print('## KELAS  : TI 2D BJB    ##')
print('## PROGRAM PYTHON KASIR  ##')
print()

print ('Pilihan Operasi : ')
print ('1. Penjumlahan')
print ('2. Pengurangan')
print ('3. Perkalian')
print ('4. Pembagian')

pilihanOperasi = int(input('Masukkan Pilihan Operasi (1/2/3/4) : '))

angka1 = int(input('Masukkan Angka pertama : '))
angka2 = int(input('Masukkan Angka kedua   : '))

match pilihanOperasi:
    case 1:
        hasil = angka1 + angka2
        print(f'Hasil dari {angka1} + {angka2} = {hasil}')

    case 2:
        hasil = angka1 - angka2
        print(f'Hasil dari {angka1} - {angka2} = {hasil}')

    case 3:
        hasil = angka1 * angka2
        print(f'Hasil dari {angka1} * {angka2} = {hasil}')

    case 4:
        if angka2 == 0:
            print ('Error : Angka kedua tidak boleh nol')
        else:
            hasil = angka1 / angka2
            print(f'Hasil dari {angka1} / {angka2} = {hasil}')

    case _:
        print('Error : No pilihan operasi yang dimasukkan salah')
