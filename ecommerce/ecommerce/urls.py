"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from ecom import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from ecom.views import  SearchResultsView




urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),

    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('logout/', views.userlogout, name='logout'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('cart', views.cart_view,name='cart'),
    path('add-to-cart/<int:pk>', views.add_to_cart_view,name='add-to-cart'),
    path('remove-from-cart/<int:pk>', views.remove_from_cart_view,name='remove-from-cart'),
    path('products/<int:id>/', views.productdetail, name='productdetail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    # path('accounts/', include('django.contrib.auth.urls')),



    path('category/<id>/', views.catogorylist, name='category'),
    # path('category/<int:id>/', views.CategoryView, name='categoryid'),







    path('reg', views.reg, name='reg'),
    path('login/', views.user_login, name='login'),


     path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),

    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
