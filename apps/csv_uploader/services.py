from rest_framework.generics import get_object_or_404
from .models import Product
from typing import List
import csv


class ProductCRUD:

    def create_product(self, csv_file: csv) -> None:
        reader = csv.DictReader(
            csv_file.read().decode("utf-8").splitlines())

        for row in reader:
            Product.objects.create(data=row)
        return

    def delete_product_by_id(self, id: str) -> None:
        product = get_object_or_404(Product, id=id)
        product.delete()
        return

    def update_product(self, id: str, data: dict) -> Product:
        product = get_object_or_404(Product, id=id)
        product.data.update(data)
        product.save()
        return product
