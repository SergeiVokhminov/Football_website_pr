from django.db import models


class Blog(models.Model):
    """Поля для модели блога."""

    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите заголовок блога"
    )
    content = models.TextField(
        verbose_name="Содержание блога",
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to="photo/blog/",
        verbose_name="Превью",
        help_text="Загрузите превью блога",
        null=True,
        blank=True,
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата обновления")
    publication_sign = models.BooleanField(verbose_name="Признак публикации")
    views = models.IntegerField(verbose_name="Количество просмотров", default=0)

    def __str__(self):
        """Метод для строкового представления объекта Blog."""

        return f"{self.title}"

    class Meta:
        """Мета-информация модели Blog>."""

        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["created_at"]
