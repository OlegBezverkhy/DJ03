from django.db import models

class News_post(models.Model):
    title = models.CharField('Название новости', max_length=100)
    picture = models.ImageField(upload_to='static/img/news_pic/', default='img/default.jpeg')
    author = models.CharField('Автор публикации', max_length=50)
    pub_date = models.DateTimeField('Дата публикации')
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    views = models.PositiveIntegerField(default=0) #Количество просмотров новости

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title