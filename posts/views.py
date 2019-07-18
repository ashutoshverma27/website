from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Product
from django.utils import timezone

def add(request):
    return  render(request,'posts/add.html')
def added(request):
    #url= "https://amzn.to/2XqPYd1"
    url1=str(request.GET['link'])
    print(url1)
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

    page=requests.get(url1,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    try:
        title1=soup.find('span', {'class' : 'a-size-large'}).get_text().strip()
        price1=soup.find('span', {'class' : 'a-size-medium a-color-price priceBlockBuyingPriceString'}).get_text()
        image1=soup.find('img', {'id' : 'landingImage'})['data-old-hires']
        mrp1=soup.find('span', {'class' : 'priceBlockStrikePriceString a-text-strike'}).get_text()
        saving1=soup.find('td', {'class' : 'a-span12 a-color-price a-size-base priceBlockSavingsString'}).get_text()

        print(title1,price1,image1,mrp1,saving1)

        product=Product()
        product.title=title1
        product.price=price1
        product.image=image1
        product.url=url1
        product.mrp=mrp1
        product.saving=saving1
        product.date=timezone.datetime.now()
        product.save()
    except AttributeError:
        product=Product()
        product.title=title1
        product.price=price1
        product.image=image1
        product.url=url1
        product.date=timezone.datetime.now()
        product.save()
    print('saved')
    return render(request,'posts/added.html')
