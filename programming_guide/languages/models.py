from django.db import models


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название языка")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL-адрес")
    description = models.TextField(verbose_name="Описание")
    year_created = models.IntegerField(verbose_name="Год создания")
    main_application = models.CharField(max_length=200, verbose_name="Сфера применения")
    logo = models.ImageField(upload_to='logos/', verbose_name="Логотип")
    is_popular = models.BooleanField(default=False, verbose_name="Популярный язык")

    class Meta:
        verbose_name = "Язык программирования"
        verbose_name_plural = "Языки программирования"
        ordering = ['name']

    def str(self):
        return self.name


from django.db import models

# Create your models here.
