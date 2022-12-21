import requests
from bs4 import BeautifulSoup
from googlesearch import search

def arte_jogo(jogos):
    for jogo in jogos:
        busca = search(f'{jogo} gamefaqs')
        for item in busca:
            if 'gamefaqs.gamespot.com' in item:
                linkgf = item.replace('/faqs', '')
                linkgf = linkgf.replace('/videos', '')
                linkgf = linkgf.replace('/boxes', '')
                linkgf = linkgf.replace('/boxes', '')
                linkgf = linkgf.replace('/reviews', '')
                linkgf = linkgf.replace('/saves', '')
                linkgf = linkgf.replace('/cheats', '')
                linkgf = linkgf.replace('/cheats', '')
                linkgf = linkgf.replace('/answers', '')
                linkgf = linkgf.replace('/stats', '')
                linkgf = linkgf.replace('/playing', '')
                linkgf = linkgf.replace('/credit', '')
                linkgf = linkgf.replace('/data', '')
                break
            else:
                pass
        content = requests.get(f'{linkgf}/boxes', headers=headers).content
        site = BeautifulSoup(content, 'html.parser')
        ol = site.find('ol', class_='list')
        imagem = ol.find('a').find('img')
        imagem = 'https://gamefaqs.gamespot.com' + imagem['src']
        imagem = imagem.replace('thumb.jpg', 'front.jpg')
        print(imagem)