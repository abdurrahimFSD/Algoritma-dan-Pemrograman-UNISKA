print()
print('Program Menghitung Gaji Karyawan')
print('================================')
print()
print('## NPM    : 2210010460   ##')
print('## NAMA   : ABDURRAHIM   ##')
print('## KELAS  : TI 2D BJB    ##')
print()

masaKerja = int(input('Masukkan Masa Kerja (angka) : '))
gajiPokok = int(input('Masukkan Gaji Pokok (angka) : '))
statusPegawai = str(input('Masukkan Status Pegawai (tetap / tidak) : '))
statusKeluarga = str(input('Masukkan Status Keluarga (berkeluarga / tidak ) : '))

if masaKerja > 5:
    bonus = 0.15 * gajiPokok
else:
    bonus = 0

if statusPegawai == 'tetap':
    uangTransport = 50000
else:
    uangTransport = 0

if statusKeluarga == 'berkeluarga':
    tunjangan = 0.1 * gajiPokok
else:
    tunjangan = 0

gajiBersih = gajiPokok + bonus + tunjangan + uangTransport

print('Gaji bersih karyawan adalah: Rp.', gajiBersih )

