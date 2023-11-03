print()
print('Program Nilai Mahasiswa')
print('=======================')
print()
print('## NPM    : 2210010460   ##')
print('## NAMA   : ABDURRAHIM   ##')
print('## KELAS  : TI 2D BJB    ##')
print()

class StaticArray:

    def __init__ (self, n):
        self.data = [None] * n

    def get_at(self, i):
        if not (0 <= i < len(self.data)): raise IndexError
        return self.data[i]

    def set_at(self, i, x):
        if not (0 <= i < len(self.data)): raise IndexError
        self.data[i] = x

array1 = StaticArray(20)
array2 = StaticArray(20)
array3 = StaticArray(20)
array4 = StaticArray(20)
rerata = StaticArray(20)

n = int(input('Masukkan Jumlah Data Mahasisiwa : '))
print()
for k in range(n):
    print('ENTRY NILAI UJIAN MAHASISWA')
    print('---------------------------')
    nama = input('Masukkan Nama : ')
    array1.set_at(k, (nama))
    tugas = float(input('Masukkan Nilai Tugas : '))
    array2.set_at(k , (tugas))
    uts = float(input('Masukkan Nilai UTS : '))
    array3.set_at(k, (uts))
    uas = float(input('Masukkan Nilai UAS : '))
    array4.set_at(k, (uas))
    print()
    rerata.set_at(k, ((0.30 * array2.get_at(k))) + ((0.30 * array3.get_at(k)))+ ((0.40 * array4.get_at(k))))

    print('LAPORAN UJIAN MAHASISWA')
    print('-----------------------')
    print('No', '\t', 'Nama', '\t', 'Tugas', '\t', 'UTS', '\t', 'UAS', '\t', 'Nilai Akhir')
    for i in range(n):
        print(i, '\t', array1.get_at(i), '\t', array2.get_at(i), '\t', array3.get_at(i), '\t', array4.get_at(i), '\t', rerata.get_at(i), end='\n')




   
