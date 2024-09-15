from django.shortcuts import render, get_object_or_404
from .models import News_post


def index(request):
    main_news = News_post.objects.all().order_by('-pub_date')[:2]  # Первые 2 новости для карусели
    latest_news = News_post.objects.all().order_by('-pub_date')[2:5]  # Следующие 3 новости для списка
    popular_articles = News_post.objects.all().order_by('-views')[:3]  # 3 самых популярных статьи

    return render(request, 'news/index.html', {
        'main_news': main_news,
        'latest_news': latest_news,
        'popular_articles': popular_articles,
    })


def news_page(request, news_id):
    news_post = get_object_or_404(News_post, id=news_id)
    news_post.views += 1
    news_post.save()
    return render(request, 'news/news.html', {'news_post': news_post})


def about(request):
    return render(request, 'news/about.html')