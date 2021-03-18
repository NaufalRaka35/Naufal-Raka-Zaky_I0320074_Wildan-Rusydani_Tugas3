# Membuat dictionary
dictionary = {'Nama': 'Raka', 'Hobi1': 'Badminton', 'Hobi2': 'Jalan-jalan', 'Hobi3': 'Basket', 'Sosialmedia1': 'ig:@nrakaz_', 'Sosialmedia2': 'linkedin:naufal raka zaky', 'Sosialmedia3': 'twitter:@nrakaz_', 'Lagufav1': 'Dont look back in anger', 'Lagufav2': 'a sky full of stars', 'Lagufav3': 'Ruang Sendiri', 'Makananfav1': 'Nasi goreng', 'Makananfav2': 'Pisang goreng', 'Makananfav3': 'Ayam goreng'}

# Mengganti salah satu hobi dan sosial media
dictionary['Hobi2'] = 'Nongkrong'
dictionary['Sosmed3'] = 'line : @nrakazaky'

# Menghapus 2 makanan
del dictionary['Makananfav3']
del dictionary['Makananfav2']

# Menambah satu hobi
dictionary['Hobi4'] = 'Mendaki gunung'
print (dictionary)