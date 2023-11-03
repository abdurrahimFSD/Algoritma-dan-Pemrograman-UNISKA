# 2210010460 | Abdurrahim | TI 2D BJB

print()
print('Program Toko Alat Tulis')
print('**********************')
print()
print('## NPM    : 2210010460   ##')
print('## NAMA   : ABDURRAHIM   ##')
print('## KELAS  : TI 2D BJB    ##')
print('## PROGRAM PYTHON TOKO ALAT TULIS  ##')
print()

print('Pilihan Barang')
print('=============> 1. Pensil')
print('               2. Pulpen')
print('               3. Penghapus')
print('               4. Penggaris')
print('               5. Spidol\n')

pilihanBarang = int(input('Pilih No barang yang ingin dibeli: '))

potonganAwal = 0
potonganTambahan = 0
hadiah = ''

match pilihanBarang:
    case 1:
        hargaBarang = 45000
        print(f'Harga pensil per kotak = {hargaBarang}\n')
        pembelian = int(input('Masukkan berapa kotak yang ingin anda beli = '))
        if pembelian < 10:
            potonganAwal = 0
        elif 10 < pembelian <= 30:
            potonganAwal = 0.05
        elif pembelian > 30:
            potonganAwal = 0.05
            hadiah = '1 Kotak Penghapus'
    case 2:
        hargaBarang = 30000
        print(f'Harga Pulpen per kotak = {hargaBarang}\n')
        pembelian = int(input('Masukkan berapa kotak yang ingin anda beli = '))
        if pembelian < 10:
            potonganAwal = 0
        elif 10 < pembelian <= 25:
            potonganAwal = 0.08
        elif pembelian > 25:
            potonganAwal = 0.08
            potonganTambahan = 0.02
    case 3:
        hargaBarang = 28000
        print(f'Harga Penghapus per kotak = {hargaBarang}\n')
        pembelian = int(input('Masukkan berapa kotak yang ingin anda beli = '))
        if pembelian < 10:
            potonganAwal = 0
        elif 10 < pembelian <= 25:
            potonganAwal = 0.03
        elif pembelian > 25:
            potonganAwal = 0.03
            potonganTambahan = 0.05
    case 4:
        hargaBarang = 20000
        print(f'Harga Penggaris per kotak = {hargaBarang}\n')
        pembelian = int(input('Masukkan berapa kotak yang ingin anda beli = '))
        if pembelian < 10:
            potonganAwal = 0
        elif 10 < pembelian <= 25:
            potonganAwal = 0.03
        elif pembelian > 25:
            potonganAwal = 0.03
            potonganTambahan = 0.05
    case 5:
        hargaBarang = 40000
        print(f'Harga Spidol per kotak = {hargaBarang}\n')
        pembelian = int(input('Masukkan berapa kotak yang ingin anda beli = '))
        if pembelian < 10:
            potonganAwal = 0
        elif 10 < pembelian <= 20:
            potonganAwal = 0.1
        elif pembelian > 20:
            potonganAwal = 0.1
            potonganTambahan = 0.03
            hadiah = '1 buah penghapus papan tulis'
    case _:
        print('Pilihan tidak tersedia')
        exit()

totalBelanja = pembelian * hargaBarang
totalDiskon = totalBelanja * potonganAwal
totalDiskonTambahan = totalBelanja * potonganTambahan
totalBayar = totalBelanja - totalDiskon
totalBayarDiskonAwal = totalBelanja - (totalBelanja * potonganAwal)
totalBayarDiskonTambahan = totalBayarDiskonAwal - (totalBayarDiskonAwal * potonganTambahan)

print(f'\nTotal Belanja Anda : {totalBelanja}')

if potonganAwal != 0:
    print(f'Selamat anda mendapatkan diskon : {int(potonganAwal * 100)}%')

    if potonganTambahan != 0:
        print(f'Total bayar anda : {totalBayarDiskonAwal}')
        print(f'Anda juga mendapatkan tambahan diskon sebesar : {int(potonganTambahan * 100)}%')
        print(f'Jadi total bayar anda hanya : {totalBayarDiskonTambahan}')
    else:
        if pilihanBarang == 2:
            print(f'Diskon sebesar : {totalDiskon}')
        print(f'Jadi total bayar anda : {totalBayar}')

else:
    print(f'Jadi total bayar anda : {totalBelanja}')

if hadiah != '':
    print(f'Anda juga mendapatkan hadiah {hadiah}')




