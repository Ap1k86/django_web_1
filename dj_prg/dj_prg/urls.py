"""dj_prg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path
from dj_app import views

# --- 1. Объяснение создания маршрута --- :
# EN - path ('admin/', admin.site.urls)
# RU - ФункцияСозданияМаршрута(URL, МетодОбработкиURL, ИмяМаршрута)

# --- 2. Объяснение ДИНАМИЧЕСКОЙ части в маршруте ---
# PATH: Динамическое место в URL - <int:product_id> <ТипДанных:ИмяПеременной>
# Возможные типы данных: str, int, slug, uuid, path
# Пример: path('products/<int:product_id>/<str:name>', ...)

# RE_PATH: Динамическое место в URL - (?P<product_id>\d+) (?P<ИмяПеременной>\ТипДанных)
# Возможные типы данных: "d+" - (INT), "D+" - (STR)
# Пример: re_path(r'^products/(?P<product_id>\d+)/(?P<name>\D+)', ...)

# --- 3. Передача данных может быть 2-умя способами: ---
# 1. Передача ДАННЫХ через интернет-адрес - http://127.0.0.1:8000/products/8/Samsung
#    Данные будут находиться: В аргументах метода обработки URL
# 2. Передача ДАННЫХ по строке запроса - http://127.0.0.1:8000/products?product_id=3&name=Igor
#    Данные будут находиться: В первом аргументе "request" метода обработки URL - request.GET.get()

# Маршруты URl нашего сайта
urlpatterns = [
    # --- СТАТИЧЕСКИЕ маршруты ---
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),  # Маршрут: Главная
    path('about', views.about, name="about"),  # Маршрут: О себе
    path("contact/", views.contact, name="contact"),
    path('tags', TemplateView.as_view(template_name="tags.html", extra_context={"age": 19,
                                                                                'lst': ["Анна", "Ганна", "Ванна"]}),
         name="tags"),  # Маршрут Jinja2
    path('hello', TemplateView.as_view(template_name="hello.html", extra_context={})),
    # --- ДИНАМИЧЕСКИЕ маршруты (По интернет-адресу) ---
    path('products/<int:product_id>/<str:name>', views.products_1, name="products_1"),  # Маршрут: Продукт
    # re_path(r'^products/(?P<product_id>\d+)/(?P<name>\D+)', views.products, name="products"),  # Маршрут:

    # --- Статично-Динамические маршруты ---
    path('products', views.products_2, name="products_2"),  # Маршрут: Продукт
    path('products/<int:product_id>', views.products_3, name="products_3"),  # Маршрут: Продукт
]
