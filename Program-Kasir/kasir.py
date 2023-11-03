# Program kasir

print()
print('## NPM    : 2210010460   ##')
print('## NAMA   : ABDURRAHIM   ##')
print('## KELAS  : TI 1D BJB    ##')
print('## PROGRAM PYTHON KASIR  ##')
print()


nama = [''] * 10
harga = [0] * 10
jumlah = [0] * 10
total = [0] * 10
diskon = [0.0] * 10

jumlahBarang = int(input('Berapa Banyak Jumlah Barang Yang Ingin Anda Beli? = '))

potongan = 0.0
totalKeseluruhan = 0.0

for i in range(1, jumlahBarang + 1):
    print(f'Data Ke- {i}')
    nama[i] = input('Nama Barang    : ')
    harga[i] = int(input('Harga Barang   : '))
    jumlah[i] = int(input('Jumlah Barang  : '))

    total[i] = harga[i] * jumlah[i]
    if total[i] >= 500000:
        diskon[i] = 5/100 * total[i]
    potongan += diskon[i]
    totalKeseluruhan += total[i]

print('+-------------------------------------------------+')
print('| NO |  NAMA  |  HARGA  | JUMLAH | DISKON | TOTAL |')
print('+-------------------------------------------------+')

for i in range(1, jumlahBarang + 1):
    print(f'| {i:2} | {nama[i]:6} | {harga[i]:6} | {jumlah[i]:6} | {diskon[i]:6.0f} | {total[i] - diskon[i]:6.0f} |')

print('+-------------------------------------------------+')
print(f'| Total potonganongan      : Rp. {potongan:5.0f}')
print(f'| Total Keseluruhan   : Rp. {totalKeseluruhan - potongan:5.0f}')

bayar = float(input('| Pembayaran Anda     : Rp. '))
kembali = bayar - totalKeseluruhan + potongan

print(f'| Kembalian Anda      : Rp. {kembali:5.0f}')
print('+-------------------------------------------------')
print()
print('===============Opsi Pembayaran===============')
print('1. Cash')
print('2. GoPay')

bil = int(input('Metode Pembayaran : '))

if bil == 1:
    print('==========Cash==========')
    print(f'| Total Pembayaran   : Rp. {totalKeseluruhan - potongan:5.0f}')
    print(f'| Terbayar           : Rp. {bayar:5.0f}')
    print(f'| Kembalian          : Rp. {kembali:5.0f}')
elif bil == 2:
    print('==========GoPay==========')
    print('Promo Cashback Pembayaran GoPay')
    print('| Cashback         : Rp. 2000')
    print(f'| Total Pembayaran : Rp. {totalKeseluruhan - potongan:5.0f}')
    print(f'| Terbayar         : Rp. {bayar:5.0f}')
    print(f'| Kembalian        : Rp. {2000 + kembali:5.0f}')

print()
print('Terima Kasih')
print('============')
