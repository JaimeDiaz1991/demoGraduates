"""spice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from ofertas import views
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import obtain_jwt_token


router = SimpleRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'offers_list', views.OfferReadViewSet) # Se usa para mostrar las ofertas y su usuario ya serializado
router.register(r'offers_edit', views.OfferWriteViewSet) # modificar usuarios o agregar, se serializa sin nested para poder agregar por id
router.register(r'favs_user', views.FavsByUserViewSet) # ver la lista de favoritos por usuario ya serializada

router.register(r'users', views.UserViewSet)
#router.register(r'favs', views.FavoriteViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^login/', obtain_jwt_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('ofertas.urls'))
]
