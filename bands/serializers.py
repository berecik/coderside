from rest_framework import serializers
from .models import Band, Musican, Member


class BandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Band
        fields = '__all__'


class MusicanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Musican
        fields = '__all__'


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
