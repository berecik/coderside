from django.shortcuts import render


def all_bands(request):
    return render(request=request, template_name='band/all_bands.html')


def band(request, band_id):
    return render(request=request, template_name='band/band.html')
