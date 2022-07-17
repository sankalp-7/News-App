from statistics import mode
from django.shortcuts import render
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from. import models
# Create your views here.
def home(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"} #using google bot for handling user requests
    url = "https://www.theonion.com/"
    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    news=soup.find_all('article',{"class":"js_post_item"})

    for article in news:
        try:
            #scraping links,images,titles from the onion webpage
            tags=article.find('a',href=True)
            links=tags['href']
            image_src = str(article.find('img')['srcset']).split(" ")[-2]
            print(image_src)
            titles=tags['title']
            #storing the collected information in the article model
            headline=models.article()
            headline.title=titles
            headline.image=image_src 
            headline.url=links
            headline.save()
        except:
            pass
    
    obj=models.article.objects.all()
    return render(request,'news/home.html',{'object_list':obj})
