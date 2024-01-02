import requests
import json
from stockx import searchx
from goat import searchG
#from stadiumgoods import searchsg

def stockx(query):
    # search for item
    item = searchx(query)

    # item searched for
    print(item['title'],',',item['colorway'],',',item['styleId'],',','$',item['market']['lowestAsk'],',','https://stockx.com/' + item['urlKey'])

def goat(query):   
    # search for item
    itemg = searchG(query)

    # format of output
    print(itemg['value'],',',itemg['data']['color'],',',itemg['data']['sku'],', $',itemg['data']['lowest_price_cents']/100,',','https://www.goat.com/sneakers/' + itemg['data']['slug'])

def stadiumgoods(query):
    item = searchsg(query)

    print(item['shortDescription'])

def compare(query):
    # search both platforms
    itemX = searchx(query)
    itemG = searchG(query)

    # grab prices
    gPrice = int(itemG['data']['lowest_price_cents']/100)
    xPrice = int(itemX['market']['lowestAsk'])

    # compare prices
    if(gPrice < xPrice):
        print("GOAT has the lowest price of $", int(itemG['data']['lowest_price_cents']/100))
        print(itemG['value'],',',itemG['data']['color'],',',itemG['data']['sku'],'$',itemG['data']['lowest_price_cents']/100,',','https://www.goat.com/sneakers/' + itemG['data']['slug'])
    elif(gPrice > xPrice):
        print("StockX has the lowest price of $", int(itemX['market']['lowestAsk']))
        print(itemX['title'],',',itemX['colorway'],',',itemX['styleId'],',','$',itemX['market']['lowestAsk'],',','https://stockx.com/' + itemX['urlKey'])
    else:
        print("Both platforms have the same price of $", int(itemX['market']['lowestAsk']))
        print("GOAT:",itemG['value'],',',itemG['data']['color'],',',itemG['data']['sku'],'$',itemG['data']['lowest_price_cents']/100,',','https://www.goat.com/sneakers/' + itemG['data']['slug'])
        print("StockX:",itemX['title'],',',itemX['colorway'],',',itemX['styleId'],',','$',itemX['market']['lowestAsk'],',','https://stockx.com/' + itemX['urlKey'])

# ask user what platform to search
print("Enter 1 to search GOAT, 2 to search StockX, or 3 to search by lowest price: ")
key = int(input())

# ask user what item to search for
print("Enter the item you would like to search for: ")
query = input()

# format of output
print("Title , Main Color , SKU , Current Price , URL")

# search platfrom for item
match key:
    case 1:
        goat(query)
    case 2:
        stockx(query)
    case 3:
        compare(query)