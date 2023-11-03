print()
print('## NPM  : 2210010460 ##')
print('## NAMA : ABDURRAHIM ##')
print('## Program Python Diskon Potongan Harga ##')
print('==========================================')

totalBelanja = float(input('Total Belanja : Rp.'))

if 150000 <= totalBelanja <= 500000:
    hargaAkhir = totalBelanja - (0.1 * totalBelanja)
    print('Selamat, anda mendapatkan diskon 10%')
elif 550000 <= totalBelanja <= 1000000:
    hargaAkhir = totalBelanja - (0.15 * totalBelanja)
    print('Selamat, anda mendapatkan diskon 15%')
elif totalBelanja >= 1000000:
    hargaAkhir = totalBelanja - (0.2 * totalBelanja)
    print('Selamat, anda mendapatkan diskon 20%')
else:
    hargaAkhir = totalBelanja

print(f'Total bayar : {hargaAkhir}')
