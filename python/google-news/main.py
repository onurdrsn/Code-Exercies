from GoogleNews import GoogleNews

gNews = GoogleNews(lang = 'tr', period = '7d')
gNews.search("Turkey")

for i in gNews.result():
    print("****************SON DAKİKA HABERLER****************")
    print("Başlik:", i['title'], "\n")
    print("Zaman:", i['date'], "\n")
    print("Açiklama:", i['desc'], "\n")
    print("Link:", i['link'])
    print("--------------------------------------------------\n")
    