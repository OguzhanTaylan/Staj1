R1Bot.
Anlayabildiğim Komutlar:/Stajyerler
/Yaskawa
/Haberler
"""
  
  return update.message.reply_text(message)

 
def getBook(update, content):
    try:
        name = update.message.text.lower().split()
        requested_book = '%20'.join(name[1:])

        r = requests.get("https://tr.b-ok.as/s/"+requested_book)

        soup = BeautifulSoup(r.content, "lxml")

        tablo = soup.find('div', {'id': 'searchResultBox'})
        books = tablo.find_all('div', {'class': 'resItemBox resItemBoxBooks exactMatch'})

        message = str()
        for book in books[:5]:
            book_name = book.find('h3').text
            link = book.find('a').get('href')
            full_link = "https://tr.b-ok.as/"+link

            message += book_name+"\n"+full_link+"\n"
    
        update.message.reply_text(message)
    except:
        error_text = "Ama hangi kitap yahu!?🤔 \nKitap ararken '/Kitap Bul kitap adi' şeklinde ve kitap ismi belirtirken Türkçe karakter kullanmadığında beni çok mutlu edersin😉."

        update.message.reply_text(error_text)


def get_news(update,context):

     r = requests.get("https://www.haberler.com/son-dakika/")
     soup= BeautifulSoup(r.content,"lxml")
     news = soup.find_all('div',attrs={'class':"hblnBox"})
     for new in news [:3]:
       time = new.find("div",attrs={'class':'hblnTime'}).text
       title = new.find('span',attrs={'class':"hblnContent"}).text
       link = new.find('a').get('href')
       my_news= "Time:{}\n{}\nhttps://www.haberler.com/son-dakika".format(time,title)
  
       return update.message.reply_text(my_news)

def yaskawa_news(update,context):


  r = requests.get("https://www.yaskawa.com.tr/header-meta/news-events")


  soup= BeautifulSoup(r.content,"lxml")


  news = soup.find_all('div',attrs={'class':"col-12 col-md-6 col-lg-6 mb-4 card-wrapper"})

  for new in news [:3]:
       title = new.find("div",attrs={'class':'card-body'}).text
       link = new.find('a').get('href')
       message2="{}\nhttps://www.yaskawa.com.tr{}\n".format(title,link)       

       return update.message.reply_text(message2)

def getWeather(update,content):
    try:
        city = update.message.text.split()[1].lower()

        r = requests.get("https://www.hurriyet.com.tr/hava-durumu/"+city+"/")
        soup = BeautifulSoup(r.content, "lxml")

        others = soup.find('div', {'class':'swiper-container'})
        others_date = others.find_all('div', {'class':'col-3 swiper-slide'})

        info=str()
        for od in others_date:
            date = od.find('div', {'class':'content-card-date'}).text
            cond = od.find('div', {'class':'content-card-condition'}).text
            temp = od.find('div', {'class':'content-card-temp'}).text

            info += date+"\n"+cond+"  "+temp+"\n\n"

        update.message.reply_text(info)
    except:
        error_text = "Ama hangi şehir? 🤔 \nHava durumunu merak ettiğinde '/HavaDurumu sehir' şeklinde ve şehir ismi belirtirken Türkçe karakter kullanmadığında beni çok mutlu edersin😉."

        update.message.reply_text(error_text)       

def getCurrencies(update, content):
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")

    r = requests.get("https://kur.doviz.com")
    soup = BeautifulSoup(r.content, "lxml")
    currencies = soup.find_all('div', attrs={'class': 'item'})
    currency_text = str()

    for currency in currencies:
        currency1 = currency.find('a')
        currency_name = currency1.find('span', attrs={'class': 'name'}).text
        currency_value = currency1.find('span', attrs={'class': 'value'}).text

        currency_text += currency_name + " : " + currency_value+"\n"

    update.message.reply_text(d1+"\n"+currency_text)