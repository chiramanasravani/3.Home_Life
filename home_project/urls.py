"""home_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from ast import If
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from adminapp import views as adminapp_views
from userapp import views as userapp_views
from mainapp import views as mainapp_views
urlpatterns = [
    path('admin/', admin.site.urls),


#admin

    path('admin_login',adminapp_views.admin_login,name='admin_login'),

    path('admin_dashboard', adminapp_views.admin_dashboard,name='admin_dashboard'),

    path('admin_view_users', adminapp_views.admin_view_users,name='admin_view_users'),

    path('admin_view_properties', adminapp_views.admin_view_properties,name='admin_view_properties'), 
    
    path('admin_view_bookings',adminapp_views.admin_view_bookings,name='admin_view_bookings'),

    path('admin_view_feedbacks',adminapp_views.admin_view_feedbacks,name='admin_view_feedbacks'),


    path('accept_renthouse/<int:id>/',adminapp_views.accept_renthouse,name='accept_renthouse'),

    path('reject_renthouse/<int:id>/',adminapp_views.reject_renthouse,name='reject_renthouse'),
    
    path('accept_salehouse/<int:id>/',adminapp_views.accept_salehouse,name='accept_salehouse'),

    path('reject_salehouse/<int:id>/',adminapp_views.accept_salehouse,name='accept_salehouse'),

    path('accept_rentland/<int:id>/',adminapp_views.accept_rentland,name='accept_rentland'),

    path('reject_rentland/<int:id>/',adminapp_views.reject_rentland,name='reject_rentland'),

    path('accept_saleland/<int:id>/',adminapp_views.accept_saleland,name='accept_saleland'),

    path('reject_saleland/<int:id>/',adminapp_views.reject_saleland,name='reject_saleland'),

    path('accept_rentshop/<int:id>/',adminapp_views.accept_rentshop,name='accept_rentshop'),

    path('reject_rentshop/<int:id>/',adminapp_views.reject_rentshop,name='reject_rentshop'),
    
    path('accept_saleshop/<int:id>/',adminapp_views.accept_saleshop,name='accept_saleshop'),

    path('reject_saleshop/<int:id>/',adminapp_views.reject_saleshop,name='reject_saleshop'),

    path('accept_rentpg/<int:id>/',adminapp_views.accept_rentpg,name='accept_rentpg'),

    path('reject_rentpg/<int:id>/',adminapp_views.reject_rentpg,name='reject_rentpg'),
    
    path('accept_salepg/<int:id>/',adminapp_views.accept_salepg,name='accept_salepg'),

    path('reject_salepg/<int:id>/',adminapp_views.reject_salepg,name='reject_salepg'),

 #user

    path('user_login',userapp_views.user_login,name='user_login'),
    path('user_register', userapp_views.user_register,name='user_register'),
    path('user_dashboard', userapp_views.user_dashboard,name='user_dashboard'),
    path('properties_menu', userapp_views.properties_menu,name='properties_menu'), 
    path('property_types',userapp_views.property_types,name='property_types'),


    path('property_details/<int:id>/',userapp_views.property_details,name='property_details'),
    path('sale_property_details/<int:id>/',userapp_views.sale_property_details,name='sale_property_details'),

    path('rent_land_details/<int:id>/',userapp_views.rent_land_details,name='rent_land_details'),
    path('sale_land_details/<int:id>/',userapp_views.sale_land_details,name='sale_land_details'),

    path('rent_shop_details/<int:id>/',userapp_views.rent_shop_details,name='rent_shop_details'),
    path('sale_shop_details/<int:id>/',userapp_views.sale_shop_details,name='sale_shop_details'),

    path('rent_pg_details/<int:id>/',userapp_views.rent_pg_details,name='rent_pg_details'),
    path('sale_pg_details/<int:id>/',userapp_views.sale_pg_details,name='sale_pg_details'),

   

# edit
    path('edit_rent_house/<int:id>/',userapp_views.edit_rent_house,name='edit_rent_house'),
    path('edit_sale_house/<int:id>/',userapp_views.edit_sale_house,name='edit_sale_house'),

    path('edit_rent_land/<int:id>/',userapp_views.edit_rent_land,name='edit_rent_land'),
    path('edit_sale_land/<int:id>/',userapp_views.edit_sale_land,name='edit_sale_land'),

    path('edit_rent_shop/<int:id>/',userapp_views.edit_rent_shop,name='edit_rent_shop'),
    path('edit_sale_shop/<int:id>/',userapp_views.edit_sale_shop,name='edit_sale_shop'),

    path('edit_rent_pg/<int:id>/',userapp_views.edit_rent_pg,name='edit_rent_pg'),
    path('edit_sale_pg/<int:id>/',userapp_views.edit_sale_pg,name='edit_sale_pg'),

    

    path('add_properties_rent', userapp_views.add_properties_rent,name='add_properties_rent'),

    path('add_properties_sale', userapp_views.add_properties_sale,name='add_properties_sale'),




    path('rent_houses',userapp_views.rent_houses,name='rent_houses'),
    path('sale_houses',userapp_views.sale_houses,name='sale_houses'),
   
    path('rent_lands',userapp_views.rent_lands,name='rent_lands'),
    path('sale_lands',userapp_views.sale_lands,name='sale_lands'),

    path('rent_shops',userapp_views.rent_shops,name='rent_shops'),
    path('sale_shops',userapp_views.sale_shops,name='sale_shops'),
   
    path('rent_pg',userapp_views.rent_pg,name='rent_pg'),
    path('sale_pg',userapp_views.sale_pg,name='sale_pg'),
   


    path('appointment',userapp_views.appointment,name='appointment'),
    path('my_properties',userapp_views.my_properties,name='my_properties'),
    path('my_properties_status',userapp_views.my_peoperties_status,name='my_properties_status'),
    path('delete_property/<int:id>/',userapp_views.delete_property,name='delete_property'),
    path('profile',userapp_views.profile,name='profile'),
    path('edit_profile/<int:id>/',userapp_views.edit_profile,name='edit_profile'),
    path('feedback',userapp_views.feedback,name='feedback'),
    

  
# mainapp

    path('',mainapp_views.home,name='home'),
    path('about', mainapp_views.about,name='about'),
    path('contact',mainapp_views.contact,name='contact'),
   

   
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
       

