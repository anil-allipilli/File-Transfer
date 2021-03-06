"""filetransfer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt import views as jwt_views
from accounts.viewsets import MyUserViewSet
from products.viewsets import (
    ProductViewset,
    ProductFileViewset,
    MyProductsViewset,
    SharedProductsViewset,
)
from products.views import create_product
from django.views.generic import TemplateView

router = DefaultRouter()

router.register("accounts", MyUserViewSet, basename="accounts")
router.register("products", ProductViewset, basename="products")
router.register("productfiles", ProductFileViewset, basename="product_files")
urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("createproduct/", create_product, name="createproduct"),
    path("myproducts/", MyProductsViewset.as_view({"get": "list"}), name="myproducts"),
    path(
        "sharedproducts/",
        SharedProductsViewset.as_view({"get": "list"}),
        name="sharedproducts",
    ),
    # path("myproducts/", my_products, name="myproducts"),
    path("api/", include(router.urls)),
    # path("", TemplateView.as_view(template_name="index.html")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns.append(
    re_path(r"^", TemplateView.as_view(template_name="index.html")),
)
