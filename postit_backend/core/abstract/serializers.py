from rest_framework import serializers

class AbstractSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = ["public_id", "created", "updated"]
        read_only_fields = ["public_id", "created", "updated"]