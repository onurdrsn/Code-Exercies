from prettytable import PrettyTable
mytable=PrettyTable(["Öğrencinin Adı","Öğrencinin Soyadı", "Sınıf", "Numara", "Bölüm", "Yüzde"])
mytable.add_row(["Mehmet", "Durmuş", "12-C", "15000", "Veri Tabanı", "90%"])
mytable.add_row(["Ali", "Kaya", "12-C", "15600", "Veri Tabanı", "90%"])
mytable.add_row(["Ahmet", "Duran", "12-C", "10000", "Veri Tabanı", "90%"])
mytable.add_row(["Yasin", "Yıldız", "12-C", "15500", "Veri Tabanı", "90%"])
mytable.add_row(["Muhammet", "Yılmaz", "12-C", "15010", "Veri Tabanı", "60%"])
mytable.add_row(["Zeynep", "Yıldırım", "12-C", "17200", "Veri Tabanı", "87%"])
print(mytable)