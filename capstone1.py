from datetime import datetime
# Data Stock Awal (Gudang Jeans)

list_barang = [{'kode_barang':'JPKW2005', 'nama_barang': 'Jeans Pendek Wanita', 'harga_barang': 75000, 'jumlah_stock': {'S':20,'M':50,'L':50,'XL':30}, 'lokasi_rak': 'A01', 'tanggal_masuk':''}, 
{'kode_barang':'JPKP2006', 'nama_barang': 'Jeans Pendek Pria', 'harga_barang': 75000, 'jumlah_stock': {'S':30,'M':40,'L':60,'XL':20}, 'lokasi_rak': 'A02', 'tanggal_masuk':''},
{'kode_barang':'JPJW2105', 'nama_barang': 'Jeans Panjang Wanita', 'harga_barang': 120000, 'jumlah_stock': {'S':50,'M':30,'L':35,'XL':50}, 'lokasi_rak': 'A03', 'tanggal_masuk':''},
{'kode_barang':'JPJP2106', 'nama_barang': 'Jeans Panjang Pria', 'harga_barang': 125000, 'jumlah_stock': {'S':40,'M':50,'L':60,'XL':25}, 'lokasi_rak': 'A04', 'tanggal_masuk':''}, 
{'kode_barang':'JPAA2206', 'nama_barang': 'Jeans Anak', 'harga_barang': 130000, 'jumlah_stock': {'S':35,'M':50,'L':50,'XL':65}, 'lokasi_rak': 'A05', 'tanggal_masuk':''}]

# Main menu
def menu_utama():
    menu = input('''
Halo, Selamat Datang di Database Jeans Import Top)
1. Tampil Data Stock Barang
2. Tambah Stok Barang Baru
3. Update Data Stock Barang
4. Hapus Data Stock Barang
5. Barang Keluar/Masuk
6. Keluar Program
Masukan angka Menu yang ingin dijalankan : ''')
    if menu == '1':
        menu_1()
    elif menu == '2':
        menu_2()
    elif menu == '3':
        menu_3()
    elif menu == '4':
        menu_4()
    elif menu == '5':
        menu_5()
    elif menu == '6':
        exit()
    else:
        print("Layanan tidak ada, silahkan input angka lain")
        menu_utama()

# Menu Read
def menu_1():
    menu = input('''
Menampilkan Data Stock Barang
1. Tampilkan Seluruh Data Stok Barang
2. Mencari Data Barang Berdasarkan Kode Barang
3. Kembali ke Menu Awal
Masukkan angka Menu yang ingin dijalankan: ''')
    
    if menu == '1':
        stock()
    elif menu == '2':
        kode = input('masukkan kode barang')
        data = list(filter(lambda i:i if i['kode_barang'] == kode else '',list_barang))
        if len(data)>0:
            stock(data[0]['kode_barang'])
        else:
            print("Data tidak ditemukan")
    elif menu == '3':
        menu_utama()
    else:
        print("Layanan tidak tersedia, silahkan input angka lain")
        menu_1()
    

# Print Stock Barang
def stock(id=0):
    print(f"Kode | Barang | Harga | Stock | Rak")
    if(id == 0):
        for i in list_barang:
            print(f'{i["kode_barang"]} | {i["nama_barang"]:} | {i["harga_barang"]:<5} | {i["jumlah_stock"]} | {i["lokasi_rak"]} | {i["tanggal_masuk"]}')
            print()
    else:
        for i in list_barang:
            if i["kode_barang"] == id:
                print(f'{i["kode_barang"]} | {i["nama_barang"]:} | {i["harga_barang"]:<5} | {i["jumlah_stock"]} | {i["lokasi_rak"]}')
                print()
# Menu Create
def menu_2():
    menu = input('''
Tambah Stock Barang Baru
1. Tambah Stock Barang
2. Kembali ke Menu Awal
Masukkan angka Menu yang ingin dijalankan : ''')
    
    if menu == '1':
        print() 
        tambah_kode = input("Masukkan kode Barang: ").upper()
        try :
            konfirmasi_barang = True
            while konfirmasi_barang :
                tambah_barang = input("Masukkan Nama Barang: ").title()
                if len(tambah_barang) != 0:
                    kata = tambah_barang.split()
                    gabung = ''.join(kata)
                    if gabung.isalpha() == True:
                        konfirmasi_barang = False
                    else: 
                        print("input hanya huruf saja")
                else: 
                    print("Nama Barang Belum diisi, silahkan isi dengan ketentuan")
                
                tambah_harga = int(input("Masukkan Harga: "))
                tambah_stock_s = int(input("Masukkan Stock S: "))
                tambah_stock_m = int(input("Masukkan Stock M: "))
                tambah_stock_l = int(input("Masukkan Stock L: "))
                tambah_stock_xl = int(input("Masukkan Stock XL: "))
                tambah_rak = input("Masukkan Nomor Rak: ").upper()

                list_barang.append({
                    'kode_barang':tambah_kode,
                    'nama_barang':tambah_barang,
                    'harga_barang':tambah_harga,
                    'jumlah_stock':{
                        'S':tambah_stock_s,
                        'M':tambah_stock_m,
                        'L':tambah_stock_l,
                        'XL':tambah_stock_xl,   
                    },
                    'lokasi_rak':tambah_rak,
                    'tanggal_masuk':datetime.now().strftime("%Y-%m-%d")})
                stock()
                menu_2()
        except ValueError:
            print('Masukkan Angka yang Benar')

# Menu Update
def menu_3():
    menu = input('''
Mengupdate Data Barang
1. Mengupdate Data Barang
2. Kembali Ke Menu Awal
Masukkan angka Menu yang ingin dijalankan :''')
    if menu == '1':
        stock()
        kode = input('masukkan kode barang: ')
        data = list(filter(lambda i:i if i['kode_barang'].lower() == kode.lower() else '',list_barang))
        if len(data) > 0:
            print(f"Anda sekarang sedang mengedit {data[0]['nama_barang']}")

            menu_edit = input('''
Kolom apa yang ingin anda lakukan ?
1. Nama Barang
2. Harga Barang
3. Lokasi Rak Barang
4. Kembali ke Menu Awal
Masukkan menu yang ingin dilakukan : ''')
            if menu_edit != '1' and menu_edit != '2' and menu_edit != '3' and menu_edit != '4':
                print("Input tidak valid")
            elif menu_edit == '4':
                menu_3()
            else :
                        if menu_edit == '1' :
                            nama = input("Input nama barang terbaru : ")
                            confirm_nama = True
                            while confirm_nama:
                                confirm = input(f"Apakah yakin ingin mengubah nama barang menjadi {nama} tersebut? (yes/no) : " )
                                if confirm.lower() == 'yes':
                                    confirm_nama = False
                                    index = list_barang.index(data[0])
                                    list_barang[index]['nama_barang'] = nama.title()
                                    print("Data berhasil diubah")
                                    stock(list_barang[index]['kode_barang'])
                                elif confirm.lower() == 'no':
                                    confirm_nama = False
                                else:
                                    print("Input tidak benar, masukkan sesuai ketentuan")
                        elif menu_edit == '2':
                            angka = True
                            while angka:
                                harga = input("Input harga baru barang : ")
                                if harga.isdigit() == True:
                                    confirm_harga = True
                                    while confirm_harga:
                                        confirm = input(f"Apakah yakin ingin mengurangi harga barang menjadi {harga} tersebut? (yes/no) : " )
                                        if confirm.lower() == 'yes':
                                            index = list_barang.index(data[0])
                                            list_barang[index]['harga_barang'] = int(harga)
                                            confirm_harga = False
                                            angka = False
                                            print("Data berhasil diubah")
                                            stock(list_barang[index]['kode_barang'])
                                        elif confirm.lower() == 'no':
                                            confirm_harga = False
                                            angka = False
                                        else:
                                            print("Input tidak benar, masukkan sesuai ketentuan")
                                else :
                                    print("Angka tidak valid, masukkan data yang benar")
                        elif menu_edit == '3':
                            rak = input("Input lokasi rak barang terbaru : ")
                            confirm_nama = True
                            while confirm_rak:
                                confirm = input(f"Apakah yakin ingin mengubah lokasi rak barang ke {rak} tersebut? (yes/no) : " )
                                if confirm.lower() == 'yes':
                                    confirm_rak = False
                                    index = list_barang.index(data[0])
                                    list_barang[index]['lokasi_rak'] = rak.title()
                                    print("Data berhasil diubah")
                                    stock(list_barang[index]['kode_barang'])
                                elif confirm.lower() == 'no':
                                    confirm_rak = False
                                else:
                                    print("Input tidak benar, masukkan sesuai ketentuan")   
        else:
            print("Data tidak ditemukan")
    elif menu == '2':
        menu_utama()
    else:
        print('Layanan Tidak Ada, Silakhkan Pilih Angka Lain')
    menu_3()

def menu_4():
    menu = input('''
Menghapus Data Barang
1. Menghapus Data Barang
2. Kembali Ke Menu Awal
Masukkan angka Menu yang ingin dijalankan :''')
    
    if menu == '1':
        stock()
        kode = input('masukkan kode barang: ')
        data = list(filter(lambda i:i if i['kode_barang'].lower() == kode.lower() else '',list_barang))
        if len(data)>0:
            confirm_hapus = True
            while confirm_hapus:
                confirm = input("Apakah yakin ingin menghapus barang tersebut? (yes/no) : " )
                if confirm.lower() == 'yes':
                    list_barang.remove(data[0])
                    confirm_hapus = False
                    print("Data berhasil dihapus")
                    stock()
                elif confirm.lower() == 'no':
                    confirm_hapus = False
                else:
                    print("Input tidak benar, masukkan sesuai ketentuan")
        else:
            print("Data tidak ditemukan")
    elif menu == '2':
        menu_utama()
    else:
        print('Menu Tidak Ada')
    menu_4()

def menu_5():
    stock()
    kode = input('masukkan kode barang: ')
    data = list(filter(lambda i:i if i['kode_barang'].lower() == kode.lower() else '',list_barang))
    if len(data) > 0:
        print(f"Anda sekarang sedang mengedit {data[0]['nama_barang']}")
        menu_edit = input('''
Apa yang ingin anda lakukan?
1. Menambah Stok Barang
2. Mengurangi Stok Barang
3. Kembali Ke Menu Awal
Masukkan menu yang ingin dilakukan : ''')
        if menu_edit != '1' and menu_edit != '2' and menu_edit != '3':
            print("Input tidak valid")
        elif menu_edit == '3':
            menu_utama()
        else :
            check_ukuran = True
            while check_ukuran:
                ukuran = input('Pilih ukuran barang (S / M / L / XL):')
                if ukuran.lower() in ['s','m','l','xl']:
                    if menu_edit == '1' :
                            angka = True
                            while angka:
                                tambah = input("Input berapa barang masuk : ")
                                if tambah.isdigit() == True:
                                    confirm_tambah = True
                                    while confirm_tambah:
                                        confirm = input("Apakah yakin ingin menambahkankan stok barang tersebut? (yes/no) : " )
                                        if confirm.lower() == 'yes':
                                            data[0]['jumlah_stock'][ukuran.upper()] = data[0]['jumlah_stock'][ukuran.upper()] + int(tambah)
                                            confirm_tambah = False
                                            angka = False
                                            print("Data berhasil diubah")
                                            stock(data[0]['kode_barang'])
                                        elif confirm.lower() == 'no':
                                            confirm_tambah = False
                                            angka = False
                                        else:
                                            print("Input tidak benar, masukkan sesuai ketentuan")
                                else :
                                    print("Angka tidak valid, masukkan data yang benar")
                    else:
                            angka = True
                            while angka:
                                kurang = input("Input berapa barang keluar : ")
                                if kurang.isdigit() == True:
                                    confirm_kurang = True
                                    while confirm_kurang:
                                        confirm = input("Apakah yakin ingin mengurangi stok barang tersebut? (yes/no) : " )
                                        if confirm.lower() == 'yes':
                                            data[0]['jumlah_stock'][ukuran.upper()] = data[0]['jumlah_stock'][ukuran.upper()] - int(kurang)
                                            confirm_kurang = False
                                            angka = False
                                            print("Data berhasil diubah")
                                            stock(data[0]['kode_barang'])
                                        elif confirm.lower() == 'no':
                                            confirm_kurang = False
                                            angka = False
                                        else:
                                            print("Input tidak benar, masukkan sesuai ketentuan")
                                else :
                                    print("Angka tidak valid, masukkan data yang benar")
                    check_ukuran = False
                else:
                        print("ukuran tidak valid")
                

    else:
            print("Data tidak ditemukan")
    menu_5()
    

menu_utama()
            
                 