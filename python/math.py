from matplotlib import pyplot as plt
kişiler = ['Messi', 'Ronaldo', 'Neymar']
score = [87, 89, 88]
plt.bar(kişiler, score, color = 'red')
plt.title('Skor')
plt.xlabel('Oyuncular')
plt.ylabel('Oynama Yüzdeleri')
plt.show()