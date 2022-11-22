# Database stok barang dalam gudang
db_stok = [{
        'kode_barang' : 'SG-001',
        'nama_barang' : 'Monitor',
        'merk' : 'Samsung',
        'tipe' : 'LS24-R350',
        'stok' : 4},
    
        {
        'kode_barang' : 'SG-002',
        'nama_barang' : 'AIO PC',
        'merk' : 'Dell',
        'tipe' : 'Optiplex 328',
        'stok' : 5},

        {
        'kode_barang' : 'SG-003',
        'nama_barang' : 'Laptop',
        'merk' : 'Asus',
        'tipe' : 'TUF Dash F15',
        'stok' : 5},

        {
        'kode_barang' : 'SG-004',
        'nama_barang' : 'Printer',
        'merk' : 'Epson',
        'tipe' : 'Deskjet L480',
        'stok' : 10},

        {
        'kode_barang' : 'SG-005',
        'nama_barang' : 'Mouse',
        'merk' : 'Razer',
        'tipe' : 'Death Ader',
        'stok' : 15}
]

# Melihat Database stok barang
def lihatDataBase():
    print('='*35+' STOK BARANG DALAM GUDANG '+'='*35)
    print('| index\t| kode_barang\t| nama_barang \t| merk  \t| tipe \t\t\t | stok\t|')
    for i in range(len(db_stok)):
        print('| {}\t| {}\t| {} \t| {}  \t| {} \t\t | {}\t|'.format(i,db_stok[i]['kode_barang'],
                db_stok[i]['nama_barang'],db_stok[i]['merk'],db_stok[i]['tipe'],db_stok[i]['stok']))

# Fungsi Read dalam Program
def menampilkanStokBarang():
    while True:
        print('''
        ========= Sub Menu View Data Stok Barang =========
            [1] Tampilkan Seluruh Data Stok Barang
            [2] Cari Nama Barang Dalam Data Stok Barang
            [3] Kembali ke Menu Utama
            ''')
        subMenu1 = int(input('\nSilahkan pilih sub menu : '))
        if subMenu1 == 1:
            lihatDataBase()
        elif subMenu1 == 2:
            search = input('Masukkan nama barang yang ingin dicari : ')
            print('| Index\t| kode_barang\t| nama_barang \t| merk  \t| tipe \t\t\t | stok\t|')
            for i in range(len(db_stok)):
                if search.lower() in db_stok[i]['nama_barang'].lower():
                    print('| {}\t| {}\t| {} \t| {}  \t| {} \t\t | {}\t|'.format(i,db_stok[i]['kode_barang'],
                            db_stok[i]['nama_barang'],db_stok[i]['merk'],db_stok[i]['tipe'],db_stok[i]['stok']))
                    break
            else:
                print('Barang tidak ditemukan')
        elif subMenu1 == 3:
            break
        else:
            print('\n\t\tSub Menu Salah')

# Fungsi Create dalam Program
def menambahBarang():
    while True:
        subMenuTB = int(input('''
        ========== Sub Menu Tambah Barang ==========
            [1] Tambah Data Stok Barang Dalam Gudang
            [2] Kembali ke Menu Utama

            Silahkan pilih sub menu : '''))
        if subMenuTB == 1:
            lihatDataBase()
            inputCode = input('\nMasukkan kode barang baru yang ingin diinput : ')
            checkCode1 = [db_stok[i]['kode_barang'] for i in range(len(db_stok))]
            if inputCode in checkCode1:
                print('\nData sudah ada!')
            else:
                print('Silahkan masukkan data barang baru')
                kode_barang_baru = input('Masukkan kode barang sesuai dengan yang pertama diinput : ')
                nama_barang_baru = input('Masukkan nama barang : ')
                merk_barang_baru = input('Masukkan merk barang : ')
                tipe_barang_baru = input('Masukkan tipe barang : ')
                stok_barang_baru = int(input('Masukkan jumlah stok barang : '))
                cek_point1 = input(f'Apakah data yang dimasukkan ingin disimpan?\n {kode_barang_baru},{nama_barang_baru},{merk_barang_baru},{tipe_barang_baru},{stok_barang_baru} \n ya/tidak : ')
                if cek_point1 != 'ya':
                    print('Data tidak disimpan')
                    break
                else:
                    db_stok.append({'kode_barang' : kode_barang_baru,'nama_barang' : nama_barang_baru,'merk' : merk_barang_baru,'tipe' : tipe_barang_baru,'stok' : stok_barang_baru})
                    lihatDataBase()
                    print('\nData stok barang baru telah disimpan')
                    break
        elif subMenuTB == 2:
            break
        else:
            print('\n\t\tSub Menu Salah')

# Fungsi Update dalam Program
def editBarang():
    while True:
        subMenuEB = int(input('''
        ========== Sub Menu Update Barang ==========
            [1] Update Stok Data Barang Dalam Gudang
            [2] Kembali ke Menu Utama

            Silahkan pilih sub menu : '''))
        if subMenuEB == 1:
            lihatDataBase()
            print('\n Kode barang harus sesuai. Diawali dengan SG diikuti dengan dash(-) dan tiga angka contoh : SG-007')
            inputCode = input('\nMasukkan kode barang yang ingin diupdate : ')
            print('| Index\t| kode_barang\t| nama_barang \t| merk  \t| tipe \t\t\t | stok\t|')
            for i in range(len(db_stok)):
                if inputCode.lower() in db_stok[i]['kode_barang'].lower():
                    print('| {}\t| {}\t| {} \t| {}  \t| {} \t\t | {}\t|'.format(i,db_stok[i]['kode_barang'],
                            db_stok[i]['nama_barang'],db_stok[i]['merk'],db_stok[i]['tipe'],db_stok[i]['stok']))
                    updateDB = int(input('''
                    ========= Kolom yang dapat diupdate =========
                        [1] kode_barang
                        [2] nama_barang
                        [3] merk
                        [4] tipe
                        [5] stok
                        [6] Kembali ke menu awal
                        
                        Masukkan angka sesuai pilihan kolom yang ingin diupdate : '''))
                    if updateDB == 1:
                        update_code = input('Masukkan kode barang baru : ')
                        while update_code in range(len(db_stok)):
                            print('Kode barang sudah ada!')
                            update_code = input('Masukkan kode barang baru : ')
                        checkPoint2 = input('Apakah anda yakin ingin mengudpdate data? (ya/tidak) : ')
                        if checkPoint2 != 'ya':
                            break
                        else:
                            db_stok[update_code in range(len(db_stok))]['kode_barang'] = update_code
                            lihatDataBase()
                            print('\nKode barang telah diupdate')
                            break
                    elif updateDB == 2:
                        update_name = input('Masukkan nama barang baru : ')
                        while update_name in range(len(db_stok)):
                            print('Nama barang sudah ada!')
                            update_name = input('Masukkan nama barang baru : ')
                        checkPoint3 = input('Apakah anda yakin ingin mengudpdate data? (ya/tidak) : ')
                        if checkPoint3 != 'ya':
                            break
                        else:
                            db_stok[update_name in range(len(db_stok))]['nama_barang'] = update_name
                            lihatDataBase()
                            print('\nNama barang telah diupdate')
                            break
                    elif updateDB == 3:
                        update_merk = input('Masukkan merk baru : ')
                        while update_merk in range(len(db_stok)):
                            print('Merk sudah ada!')
                            update_name = input('Masukkan merk baru : ')
                        checkPoint4 = input('Apakah anda yakin ingin mengudpdate data? (ya/tidak) : ')
                        if checkPoint4 != 'ya':
                            break
                        else:
                            db_stok[update_merk in range(len(db_stok))]['merk'] = update_merk
                            lihatDataBase()
                            print('\nMerk telah diupdate')
                            break
                    elif updateDB == 4:
                        update_tipe = input('Masukkan tipe baru : ')
                        while update_tipe in range(len(db_stok)):
                            print('Tipe sudah ada!')
                            update_tipe = input('Masukkan tipe baru : ')
                        checkPoint5 = input('Apakah anda yakin ingin mengudpdate data? (ya/tidak) : ')
                        if checkPoint5 != 'ya':
                            break
                        else:
                            db_stok[update_tipe in range(len(db_stok))]['tipe'] = update_tipe
                            lihatDataBase()
                            print('\nTipe telah diupdate')
                            break
                    elif updateDB == 5:
                        update_stok = input('Masukkan stok baru : ')
                        while update_stok in range(len(db_stok)):
                            print('Stok yang dimasukkan sama!')
                            update_stok = input('Masukkan stok baru : ')
                        checkPoint6 = input('Apakah anda yakin ingin mengudpdate data? (ya/tidak) : ')
                        if checkPoint6 != 'ya':
                            break
                        else:
                            db_stok[update_stok in range(len(db_stok))]['stok'] = update_stok
                            lihatDataBase()
                            print('\nStok telah diupdate')
                            break
                    elif updateDB == 6:
                        break
                    else:
                        print('Pilihan salah')
                        break
        elif subMenuEB == 2:
            break
        else:
            print('\n\t\tSub menu salah')      
                          
# Fungis Hapus dalam Program
def hapusBarang():
    while True:
        subMenu3 = int(input('''
        ========== Sub Menu Hapus Barang ==========
            [1] Hapus Stok Data Barang Dalam Gudang
            [2] Kembali ke Menu Utama
        
            Silahkan pilih sub menu : '''))
        if subMenu3 == 1:
            lihatDataBase()
            indeks_hapus = int(input('Masukkan index data stok barang yang ingin dihapus : '))
            if indeks_hapus in range(len(db_stok)):
                cek_hapus = input('Apakah anda yakin akan mengahapus list data?\nya/tidak :')
                if cek_hapus != 'ya':
                    print('List data tidak jadi dihapus')
                    break
                else:
                    del db_stok[indeks_hapus]
                    lihatDataBase()
                    print('List data telah dihapus')
                    break
            else:
                print('Index tidak ditemukan')
                break
        elif subMenu3 == 2:
            break
        else:
            print('\n\t\tSub menu salah')

# Main Menu
def mainMenu():
    while True:
        pilihMenu = input('''
            Data Stok Barang Dalam Gudang Toko Alfabet Komputer
            
            List Menu :
            [1] Menampilkan Data Stok Barang
            [2] Menambah Daftar Barang
            [3] Mengedit Barang Dalam Daftar
            [4] Menghapus Barang
            [5] Exit Program

            Masukkan angka menu yang ingin dijalankan : ''')

        if(pilihMenu == '1'):
            menampilkanStokBarang()
        elif(pilihMenu == '2'):
            menambahBarang()
        elif(pilihMenu == '3'):
            editBarang()
        elif(pilihMenu == '4'):
            hapusBarang()
        elif(pilihMenu == '5'):
            break
        else:
            print('Pilihan menu yang anda masukkan salah')

mainMenu()

