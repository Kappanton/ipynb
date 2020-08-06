# from bs4 import BeautifulSoup
# from urllib.request import *
#
# url = 'https://pixabay.com/images/search/flat%20lay/?pagi='  # сайт откуда качаем переходим на 2 страницу
#
#
# # чтобы видеть послный адрес с номерами страниц
# # стираем цифру 2 в конце
#
# def get_html(url):
#     req = Request(url)
#     html = urlopen(req).read()
#     return html
#
#
# def main():
#     opener = build_opener()
#     opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
#     install_opener(opener)
#
#     for i in range(1, 5):  # цикл по страницам
#         html = get_html(url + str(i))
#         soup = BeautifulSoup(html, 'html.parser')
#         pic_list = soup.find_all('div', {'class': 'item'})  # тут ищем, где лежит картинка
#         # в этом примере находятся все div с class=item
#         print(pic_list)
#         # for a in pic_list:
#         #     # print(pic_list)
#         #     fa = a.find('a')  # ищем тег a со ссылкой
#         #     # print(fa)
#         #     secondary_html = get_html(
#         #         'https://pixabay.com' + fa['href'])  # переходим по тегу, если путь не полный дописываем его
#         #     secondary_soup = BeautifulSoup(secondary_html, 'html.parser')
#         #     image = secondary_soup.find(itemprop='contentURL')['src']  # находим src картинки
#         #     urlretrieve(image, image[
#         #                        56:])  # скачиваем, если нужно дописываем полный адрес сайта, второй аргумент отвечает за название файла
#         #     print(image[56:], 'скачан')
#
#
# main()

from bs4 import BeautifulSoup
from urllib.request import *

url = 'https://purepng.com/search?q=flower'  # сайт откуда качаем переходим на 2 страницу


# чтобы видеть послный адрес с номерами страниц
# стираем цифру 2 в конце

def get_html(url):
    req = Request(url)
    html = urlopen(req).read()
    return html


def main():
    opener = build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    install_opener(opener)

    for i in range(1, 3):  # цикл по страницам
        html = get_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        pic_list = soup.find_all('div', {'class': 'flex-images btn-block margin-bottom-40 dataResult'})  # тут ищем, где лежит картинка
        # в этом примере находятся все div с class=item
        #print(pic_list)
        for a in pic_list:
            fa = a.find_all('a', {'class': 'item hovercard'}, {'href'})  # ищем тег a со ссылкой
            print(fa)
            #secondary_html = get_html(fa['href'])  # переходим по тегу, если путь не полный дописываем его
            #print(secondary_html)
            # secondary_soup = BeautifulSoup(secondary_html, 'html.parser')
            # #print(secondary_soup)
            # image = secondary_soup.find(itemprop='contentUrl')['src']  # находим src картинки
            # print(image)
            # # urlretrieve(image, image[56:])  # скачиваем, если нужно дописываем полный адрес сайта, второй аргумент отвечает за название файла
            # # print(image[56:], 'скачан')

main()
