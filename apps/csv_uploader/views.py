from .serializers import UploadCSVSerializer, ProductUpdateSerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .selector import ProductSelector
from rest_framework import status
from .services import ProductCRUD
import threading


class UploadCSV(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        request=UploadCSVSerializer,
        responses={201: OpenApiResponse(description="CSV file successfully uploaded")},
    )
    def post(self, request):
        data = UploadCSVSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        csv_file = data.validated_data['file']
        p_crud = ProductCRUD()
        threading.Thread(target=p_crud.create_product, args=csv_file)
        return Response({"message": "Products created successfully"}, status=status.HTTP_201_CREATED)


class ProductDelete(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, id):
        p_crud = ProductCRUD()
        threading.Thread(target=p_crud.delete_product_by_id, args=(id,)).start()
        return Response({'message': f'Product with {id} deleted!'}, status=status.HTTP_204_NO_CONTENT)


class ProductUpdate(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(request=ProductUpdateSerializer)
    def put(self, request, id):
        data = ProductUpdateSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        new_data = data.validated_data['new_data']
        p_crud = ProductCRUD()
        product = p_crud.update_product(id, new_data)
        return Response((product.id, product.data), status=status.HTTP_202_ACCEPTED)


class ProductDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        p_crud = ProductSelector()
        product = p_crud.get_by_id(id)
        results = [hit for hit in product]
        return Response(results, status=status.HTTP_200_OK)


class Search(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "q",
                str,
                description="The search query string for filtering products.",
                required=False,
            ),
            OpenApiParameter(
                "field",
                str,
                description="The field to search in, default is 'Name'.",
                required=False,
            ),
        ],
        responses={200: "Search results returned successfully."},
    )
    def get(self, request):
        query = request.GET.get('q', '')
        field = request.GET.get('field', 'Name')

        if not query:
            return Response({"error": "Query parameter 'q' is required"}, status=status.HTTP_400_BAD_REQUEST)

        p_selector = ProductSelector()
        results = p_selector.search(query, field)
        return Response({"results": results}, status=status.HTTP_200_OK)
