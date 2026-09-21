from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    """Дополнительная информация о пользователе."""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="Пользователь",
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Телефон",
    )
    address = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="Адрес доставки",
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата рождения",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return f"Профиль {self.user.username}"

class Category(models.Model):
    """Категория блюд: пицца, суши, напитки."""

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название",
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="URL-идентификатор",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активна",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Dish(models.Model):
    """Блюдо в каталоге."""

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="dishes",
        verbose_name="Категория",
    )
    name = models.CharField(
        max_length=200,
        verbose_name="Название",
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name="URL-идентификатор",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
    )
    image = models.ImageField(
        upload_to="dishes/",
        blank=True,
        null=True,
        verbose_name="Фото",
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name="Доступно",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Создано",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Обновлено",
    )

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["slug"]),
        ]

    def __str__(self):
        return self.name


class Courier(models.Model):
    """Курьер — отдельная роль пользователя."""

    TRANSPORT_CHOICES = [
        ("foot", "Пешком"),
        ("bike", "Велосипед"),
        ("car", "Автомобиль"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="courier",
        verbose_name="Пользователь",
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Рабочий телефон",
    )
    transport = models.CharField(
        max_length=10,
        choices=TRANSPORT_CHOICES,
        default="bike",
        verbose_name="Транспорт",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Работает",
    )
    hired_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата найма",
    )

    class Meta:
        verbose_name = "Курьер"
        verbose_name_plural = "Курьеры"

    def __str__(self):
        return f"Курьер {self.user.get_full_name() or self.user.username}"
