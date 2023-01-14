# pip install prettytable

from prettytable import PrettyTable
mytable=PrettyTable(["Öğrencinin Adi","Öğrencinin Soyadi", "Sinif", "Numara", "Bölüm", "Yüzde"])
mytable.add_row(["Mehmet", "Durmuş", "12-C", "15000", "Veri Tabani", "90%"])
mytable.add_row(["Ali", "Kaya", "12-C", "15600", "Veri Tabani", "90%"])
mytable.add_row(["Ahmet", "Duran", "12-C", "10000", "Veri Tabani", "90%"])
mytable.add_row(["Yasin", "Yildiz", "12-C", "15500", "Veri Tabani", "90%"])
mytable.add_row(["Muhammet", "Yilmaz", "12-C", "15010", "Veri Tabani", "60%"])
mytable.add_row(["Zeynep", "Yildirim", "12-C", "17200", "Veri Tabani", "87%"])
print(mytable)