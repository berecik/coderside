from rest_framework import serializers
from snippets.models import Snippet, Edition, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = serializers.ALL_FIELDS


class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = serializers.ALL_FIELDS