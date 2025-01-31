from apps.csv_uploader.search_indexes import ProductDocument
from elasticsearch_dsl import Search
from elasticsearch_dsl import Q
from typing import List


class ProductSelector:
    def search(self, query: str, field: str) -> List[dict]:
        search_query = Q("match", **{f'data.{field}': query})
        search_results = ProductDocument.search().query(search_query).execute()
        return elastic_result_serializer(search_results)

    def get_by_id(self, id: int) -> ProductDocument:
        query = Q("match", **{'data.Product ID': str(id)})
        product = ProductDocument.search().query(query).execute()
        return product


def elastic_result_serializer(data: Search) -> List[dict]:
    results = [hit for hit in data]
    return results
