"""coderside URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from snippets import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'snippet', views.SnippetViewSet)
router.register(r'edition', views.EditionViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^wiki/', include('waliki.urls')),
    url(r'^utils/', include("utils.urls")),
    # url(r'^bands/', include("bands.urls")),
    url(r'^snippets/', include("snippets.urls")),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('django.contrib.auth.urls')),
    url('', include('social_django.urls', namespace='social')),

]