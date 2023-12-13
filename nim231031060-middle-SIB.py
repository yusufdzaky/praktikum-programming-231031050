'''
Misalkan anda diberikan tugas untuk membuat program struk pembelian pada kasir di perusahaan alat-alat komputer. Pilih 5 barang Alat Komputer dengan harga masing-masing barang kemudian buatkan program dan ouputnya seperti berikut.

- Buat list data perusahaan
mdata = [PT. XYZ Komputer,
        JL. BALAIKOTA NO.1,
        Kota Parepare,
        Nama lengkap,
        mahasiswa@.ac.id,
        Nama kasir,
        25 Oktober 2023]
(NOTED: ubah Nama Lengkap, e-mail, Nama Kasir, Tanggal-Bulan-Tahun Lahir)

- Buat Nested list untuk 5 barang:

djual = [['B3301','B3302','B3303','B3304','B3305'],
        ['Barang1','Barang2','Barang3','Barang4','Barang5'],
        [15,5,75,3,10],
        [3,3,3,3,3]]
(NOTED: ubah nama barang dan harga barang sesuai keinginan)

- Hasil Runing
                                 PT. XYZ KOMPUTER
                          JL. BALAIKOTA NO.2 KOTA PAREPARE
                             e-Mail: mahasiswa@ith.ac.id


MANAJER           : Nama Lengkap
KASIR             : Nama Kasir
Tanggal Pembelian : 25 Oktober 2023
|-|--   13    --|--       19      --|--     15    --|--  8 --|--    14    --| 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
No. Kode Barang |    Nama Barang    |   H. Satuan   | Jumlah |     Total    |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1   B3301       | Barang1           |      Rp15000,-|    3   |     Rp45000,-|
2   B3302       | Barang2           |       Rp5000,-|    3   |     Rp15000,-|
3   B3303       | Barang3           |      Rp50000,-|    3   |    Rp150000,-|
4   B3304       | Barang4           |       Rp3000,-|    3   |     Rp15000,-|
5   B3305       | Barang5           |      Rp10000,-|    3   |     Rp30000,-|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                    SUBTOTAL:           15   |    Rp245000,-|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|-----------------------------------77--------------------------------------|
Summary:
Harga tertinggi adalah    : Rp50000,-  (B3303 - Barang3)
Harga terendah  adalah    : Rp3000,-   (B3304 - Barang4)
Harga rata-rata pembelian : Rp ,-
                                                   Parepare, 25 Oktober 2023
                                          



                                                         NAMA LENGKAP      
                                                         ------------
                                                            MANAJER

'''

# Write your code in below!

print('''
Nama\t\t: Muh Alif
NIM\t\t: 231031060
Kelas\t\t: Sistem Informasi B''')
print()

#Answer in below
mdata = ['PT. XYZ Komputer',
        'JL. BALAIKOTA NO.2',
        'KOTA PAREPARE',
       ' Muh Alif',
       ' muhalif1788@gmail.com',
        ' Jejes',
        ' 25 Juni 2024']

djual = [['B3301','B3302','B3303','B3304','B3305'],
        ['Monitor','Mouse','Key board','Flashdish','USB'],
        [90,30,70,20,10],
        [3,3,3,3,3]]
print(mdata[0].center(77))
print((mdata[1]+mdata[2]).center(77))
print(mdata[4].center(77))
print('\n')

print(f'MANEGER          :{mdata[3]}')
print(f'KASIR            :{mdata[5]}')
print(f'Tanggal Pembelian:{mdata[6]}')
r =1000
print('-'*77)
print('No.'+'|'+'Kode Barang'.center(13)+'|'+'Nama Barang'.center(19)+'|'+'H.Satuan'.center(15)+'|'+'Jumlah'.center(8)+'|'+'Total'.center(14)+'|')
print('1.'+'|'+djual[0][0].ljust(13)+'|'+djual[1][0].ljust(19)+'|'+f'Rp{djual[2][0]*r},-'.rjust(15)+'|'+'3'.center(8)+'|'+f'Rp{3*r*djual[3][0]},-'.rjust(14)+'|')
print('2.'+'|'+djual[0][1].ljust(13)+'|'+djual[1][1].ljust(19)+'|'+f'Rp{djual[2][1]*r},-'.rjust(15)+'|'+'3'.center(8)+'|'+f'Rp{3*r*djual[3][1]},-'.rjust(14)+'|')
print('3.'+'|'+djual[0][2].ljust(13)+'|'+djual[1][2].ljust(19)+'|'+f'Rp{djual[2][2]*r},-'.rjust(15)+'|'+'3'.center(8)+'|'+f'Rp{3*r*djual[3][2]},-'.rjust(14)+'|')
print('4.'+'|'+djual[0][3].ljust(13)+'|'+djual[1][3].ljust(19)+'|'+f'Rp{djual[2][3]*r},-'.rjust(15)+'|'+'3'.center(8)+'|'+f'Rp{3*r*djual[3][3]},-'.rjust(14)+'|')
print('5.'+'|'+djual[0][4].ljust(13)+'|'+djual[1][4].ljust(19)+'|'+f'Rp{djual[2][4]*r},-'.rjust(15)+'|'+'3'.center(8)+'|'+f'Rp{3*r*djual[3][4]},-'.rjust(14)+'|')
print('-'*77)
print(f'Subtotal = Rp{3*r*sum(djual[2])},-'.rjust(77))
print(f'Summary:
      Harga Tertinggi Adalah :Rp{max}(djual)')