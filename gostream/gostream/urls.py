"""gostream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from gostream import settings

from accueil.views import accueil
from equipe.views import equipe
from mention.views import mention
from candidature.views import candidature
from programmation.views import programmation
from partenaire.views import partenaire

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accueil, name = 'accueil'),
    path('programmation/', programmation, name='programmation'),
    path('equipe/', equipe, name='equipe'),
    path('partenaire/', partenaire, name='partenaire'),
    path('candidature/', candidature, name ='candidature'),
    path('mention/', mention, name='mention'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
