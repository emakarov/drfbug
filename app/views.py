from django.shortcuts import render
from rest_framework import mixins, status
from app import serializers
from app import models
from rest_framework.viewsets import GenericViewSet

class NoteViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin):
    serializer_class = serializers.NoteSerializer
    queryset = models.Note.objects.all()

    def get_queryset(self):
        return models.Note.objects.all()

    def update(self, instance, validated_data):
        tag = validated_data.pop('tag')
        add_tags = validated_data.pop('additional_tags')
        instance.tag = tag
        instance.save()
        instance.additional_tags.clear()
        instance.additional_tags.add(*add_tags)
