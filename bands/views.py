from django.shortcuts import render
from .models import Band, Musican, Member
from .serializers import BandSerializer, MemberSerializer, MusicanSerializer
from rest_framework import generics


class BandList(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer


class BandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer


class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MusicanList(generics.ListCreateAPIView):
    queryset = Musican.objects.all()
    serializer_class = MusicanSerializer


class MusicanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musican.objects.all()
    serializer_class = MusicanSerializer


def all_bands(request):

    return render(
        request=request,
        template_name='band/all_bands.html',
        context={"react_on": True}
    )


def band(request, band_id):
    return render(request=request, template_name='band/band.html')
