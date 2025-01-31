from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl.fields import Object
from django_elasticsearch_dsl import Document
from .models import Product


@registry.register_document
class ProductDocument(Document):
    data = Object()

    class Index:
        name = "products"
        settings = {'number_of_shards': 1, 'number_of_replicas': 1}

    class Django:
        model = Product
        fields = []
