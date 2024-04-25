import requests
from bs4 import BeautifulSoup
from telegram import Bot
import asyncio

#Buscar promoções

def get_promocoes(siteUrl):
    response = requests.get(siteUrl)
    soup = BeautifulSoup(response.text, 'html.parser')


    #Econtrar e extrair links
    links = soup.find_all('a', class_='sc-8932d6e-10 kjShTR productLink')
    return [f"www.kabum.com.br{link['href']}" for link in links]



#Enviar links Telegram
async def enviar_links_telegram(links, TOKEN, CHAT_ID):
    bot = Bot(token=TOKEN) 
    for link in links:
        await bot.send_message(chat_id=CHAT_ID, text=link)


siteUrl = "https://www.kabum.com.br/"
TOKEN = "6944893922:AAF5Naf5lyINh_p33ODQee7T1Q82fLsBI2E"
CHAT_ID = "-1002056341491"


async def main():
    # Buscar Promoção
    links_promocionais = get_promocoes(siteUrl)
    await enviar_links_telegram(links_promocionais, TOKEN, CHAT_ID)

if __name__ == "__main__":
    asyncio.run(main())


    






    