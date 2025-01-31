from django.db import models


class Product(models.Model):
    data = models.JSONField(default=dict)

    def __str__(self):
        return str(self.data)

    def save(self, *args, **kwargs):
        from .search_indexes import ProductDocument
        super().save(*args, **kwargs)  # ابتدا شی را در دیتابیس ذخیره کن

        # سپس در Elasticsearch ایندکس کن
        product_document = ProductDocument(
            meta={'id': self.id},  # تنظیم شناسه ایندکس
            data=self.data  # داده‌ها
        )
        product_document.save()
