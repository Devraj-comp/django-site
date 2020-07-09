"""first_project URL Configuration

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
from django.urls import path
from django.contrib.auth import views as auth_views
from product.views import home_screen_view
from django.conf.urls.static import static
from django.conf import settings
#from pages.views import home_view,contact_view
#from product.views import product_detail_view,product_create_view,dynamic_lookup_view,home_screen_view,product_delete_view,product_list_view
#from .views import ArticleListView,ArticleDetailView
#app_name='article'
from account.views import registration_view,logout_view,login_view,account_view
urlpatterns = [
    #path('',home_view, name='home'),
    # path('contact/',contact_view),
    # path('product/',product_detail_view),
     path('',home_screen_view,name='home'),
    # path('create/',product_create_view),
     path('register/',registration_view,name='register'),
     path('logout/',logout_view,name='logout'),
     path('login/',login_view,name='login'),
     path('account/',account_view,name='account'),
     path('admin/', admin.site.urls)

 
    #path('product/',product_list_view,name='product-list'),
 #   path('',ArticleListView.as_view(),name='article-list'),
  #  path('<int:pk/',ArticleDetailView.as_view(),name='article-detail')

    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


