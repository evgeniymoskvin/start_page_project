from django.shortcuts import render
from django.views import View

from .models import LinksModel


class IndexMainPage(View):
    """
    Главная страница
    """

    def get(self, request):
        # Получаем ссылки из базы, сортируем по номеру порядковому
        links = LinksModel.objects.get_queryset().order_by('number')
        count_none = 9 - links.count()  # Получаем количество пустых ячеек
        none_list = [i for i in range(count_none)]  # Генерируем список для цикла на фронте
        content = {
            'links': links,
            'none_list': none_list,
        }
        return render(request, 'start_page_app/index.html', content)
