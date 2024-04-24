import requests
from bs4 import BeautifulSoup
from telegram import Bot

#Buscar promoções

def buscarPromocoes(siteUrl):
    response = requests.get(siteUrl)
    soup = BeautifulSoup(response.text, 'html.parser')


    #Econtrar e extrair links
    links = soup.find_all('a', class_='sc-8932d6e-10 kjShTR productLink')
    return print([link['href'] for link in links])



#Enviar links Telegram
async def enviarLinksTelegram(links, token, chatId):
    bot = Bot(token)
    for link in links:
        await bot.send_message(chatId, link)


siteUrl = "https://www.kabum.com.br/"
token = "6944893922:AAF5Naf5lyINh_p330DQee7T1Q82fLsBI2E"
chatId = "buybycodemaia"

#Buscar Promoção
linksPromocionais = buscarPromocoes(siteUrl)

    #Enviar links
async def main():
    await enviarLinksTelegram(linksPromocionais, token, chatId)
    






    