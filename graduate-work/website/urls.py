"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, register_converter

from client.views import index_view, LogoutView, cart_view, section_view, product_view
from client.converters import SectionConverter, ProductIDConverter


register_converter(SectionConverter, 'section')
register_converter(ProductIDConverter, 'product_id')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cart/', cart_view, name='cart'),
    path('<section:section>/', section_view, name='section'),
    path('product/<product_id:id>/', product_view, name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
