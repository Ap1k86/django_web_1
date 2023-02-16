# Главный способ! Генерация ответа при помощи шаблона HTML страницы.
from django.shortcuts import render

# Методы позволяющие генерировать ответ.
# Способ №1. Можем явно записать HTML.
from django.http import HttpResponse

# Способ 2. Можно сделать переадресацию на другую страницу
from django.http import HttpResponseRedirect

from datetime import datetime


# Метод: Главная.
def index(request):
    # <a href="СЫЛКУ">НАЗВАНИЕ</a>
    title = "<h2>Главная страница!</h2>"
    btn1 = '<a href="products">Открытие URL (без Передача ДАННЫХ)</a><br>/products'
    btn2 = '<a href="products/8/Nokia">1 способ (Передача ДАННЫХ через интернет-адрес)</a><br>/products/8/Nokia'
    btn3 = '<a href="products?product_id=7&name=Samsung">2 способ (Передача ДАННЫХ по строке запроса)</a><br>/' \
           'products?product_id=7&name=Samsung'
    btn4 = '<a href="products/6?name=Xiaomi">Открытие URL (1 + 2 способ)</a><br>/products/6?name=Xiaomi'

    menu_1 = '<a href="about"> О себе</a><br>'
    menu_2 = '<a href="contact"> Контакты </a><br>'
    menu_3 = '<a href="tags"> Jinja2 Теги </a><br>'
    return HttpResponse(
        f"{menu_1}{menu_2}{menu_3}<br><br><br>{title}<br><br>{btn1}<br><br>{btn2}<br><br>{btn3}<br><br>{btn4}")


# Метод: О себе. /about
def about(request):
    return HttpResponseRedirect("/products")


# Метод: Контакты. /contact
def contact(request):
    number = "(+375 17) 270-13-30"
    email = "info@onliner.by"
    time = str(datetime.now()).split(".")[0].split(" ")[0]
    names = ["Галина", "Катярына", "Анна"]
    context = {
        "phone_number": number,
        "email": email,
        "time": time,
        "names": names
    }
    return render(request, "contact.html", context=context)


# Метод: Продукты (1 Способ - Передача ДАННЫХ через интернет-адрес)
# http://127.0.0.1:8000/products/8/Nokia
def products_1(request, product_id, name):
    return HttpResponse("<h2>Продукт №{}. Название: {}</h2>".format(product_id, name))


# Метод: Продукты (2 Способ - Передача ДАННЫХ по строке запроса)
# http://127.0.0.1:8000/products?product_id=7&name=Samsung
def products_2(request):
    product_id = request.GET.get("product_id", None)
    name = request.GET.get("name", None)
    if product_id is None or name is None:
        return HttpResponse("<h2>Продукт не указан в URL!</h2>")
    else:
        return HttpResponse("<h2>Продукт №{}. Название: {}</h2>".format(product_id, name))


# # Метод: Продукты (1 + 2 Способ)
# /products/6?name=Xiaomi
def products_3(request, product_id):
    name = request.GET.get("name", None)
    return HttpResponse("<h2>Продукт №{}. Название: {}</h2>".format(product_id, name))
