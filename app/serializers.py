from rest_framework import serializers
from app import models


class TagSerializer(serializers.ModelSerializer):
    tag = serializers.CharField(validators=[])

    def to_internal_value(self, data):
        obj = models.Tag.objects.get_or_create(name=data.lower())[0]
        return obj

    def to_representation(self, obj):
        return obj.name

    class Meta:
        model = models.Tag
        fields = ('tag',)
        validators = []


class NoteSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=False, validators=[], required=False, allow_null=True)
    additional_tags = TagSerializer(many=True, required=False, allow_null=True, validators=[])
    title = serializers.CharField()
    
    class Meta:
        model = models.Note
        fields = (
            'tag',
            'title',
            'additional_tags',
        )
        validators = []


