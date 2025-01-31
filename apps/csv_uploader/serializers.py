from rest_framework import serializers


class UploadCSVSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate_file(self, value):
        if not value.name.endswith('.csv'):
            raise serializers.ValidationError("only csv files are allowed!")
        return value


class ProductUpdateSerializer(serializers.Serializer):
    new_data = serializers.JSONField()
