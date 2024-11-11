from ast import Pass
from dataclasses import field
from tkinter.tix import COLUMN
from urllib import request
from email.headerregistry import Address
from unicodedata import name
from django.contrib import messages
from tabnanny import check
from django.shortcuts import render
from userapp.models import *
from django.shortcuts import render,redirect,get_object_or_404
from userapp.views import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.db.models import Q
import random
import requests
# Create your views here.


#user login
def user_login(request):
     if request.method=='POST':
         email=request.POST.get('email')
         password=request.POST.get('password')

         try:     
            
            check=userModel.objects.get(email=email,password=password)
            request.session["user_id"]=check.user_id
            return redirect ('user_dashboard')
           
         except: 
             pass
     return render(request,'user/user-login.html')         


#user register
def user_register(request):
    if request.method=='POST' and request.FILES['user_image']:
        user_name=request.POST ['user_name'] 
        email=request.POST['email']       
        password=request.POST['password']
        mobile=request.POST['mobile']
        dob=request.POST['dob']
        location=request.POST['location']
        user_image=request.FILES['user_image']

        user = userModel.objects.create(user_name=user_name,password=password,mobile=mobile,email=email,dob=dob,location=location,user_image=user_image)
        user.save()

        if user:

             messages.info(request,'Successfully Registered.')
             return redirect('user_login')
        else:
             messages.error(request,'Something Wrong, Please try again.')
         
    return render(request,'user/user-register.html')

#dashboard
def user_dashboard(request):
    house=rent_houseModel.objects.count()+sale_houseModel.objects.count()
    land=rent_landModel.objects.count()+sale_landModel.objects.count()
    shop=rent_shopModel.objects.count()+sale_shopModel.objects.count()
    pg=rent_pgModel.objects.count()+sale_pgModel.objects.count()

    return render(request,'user/user-dashboard.html',{'house':house,'land':land,'shop':shop,'pg':pg,})  


def  properties_menu(request):
    house=rent_houseModel.objects.all()
    salehouse=sale_houseModel.objects.all()
    land=rent_landModel.objects.all()
    saleland=sale_landModel.objects.all()
    shop=rent_shopModel.objects.all()
    saleshop=sale_shopModel.objects.all()
    pg=rent_pgModel.objects.all()
    salepg=sale_pgModel.objects.all()
    return render(request,'user/properties-menu.html',{'house':house,'land':land,'shop':shop,'pg':pg,'salehouse':salehouse,'saleland':saleland,'saleshop':saleshop,'salepg':salepg})  


def  property_types(request):
    return render(request,'user/property-types.html') 

def delete_property(request,id):
    house=rent_houseModel.objects.filter(house_id=id)
    salehouse=sale_houseModel.objects.filter(sale_house_id=id)
    land=rent_landModel.objects.filter(land_id=id)
    saleland=sale_landModel.objects.filter(sale_land_id=id)
    shop=rent_shopModel.objects.filter(shop_id=id)
    saleshop=sale_shopModel.objects.filter(sale_shop_id=id)
    pg=rent_pgModel.objects.filter(pg_id=id)
    salepg=sale_pgModel.objects.filter(sale_pg_id=id)
    print(house,)
    house.delete()
    salehouse.delete()
    land.delete()
    saleland.delete()
    shop.delete()
    saleshop.delete()
    pg.delete()
    salepg.delete()
    return redirect("my_properties")

def my_peoperties_status(request):
    user_id=request.session["user_id"]
    house = rent_houseModel.objects.filter(owner_id=user_id)
    print(user_id)
    salehouse = sale_houseModel.objects.filter(owner_id=user_id)
    land =rent_landModel.objects.filter(owner_id=user_id)
    saleland = sale_landModel.objects.filter(owner_id=user_id)
    shop = rent_shopModel.objects.filter(owner_id=user_id)
    saleshop =sale_shopModel.objects.filter(owner_id=user_id)
    pg = rent_pgModel.objects.filter(owner_id=user_id)
    salepg =sale_pgModel.objects.filter(owner_id=user_id)
    
    return render(request,'user/my-properties-status.html',{'house':house,'salehouse':salehouse,'land':land,'saleland':saleland,'shop':shop,'saleshop':saleshop,'pg':pg,'salepg':salepg})

def my_properties(request):
    user_id=request.session["user_id"]
    house=rent_houseModel.objects.filter(owner_id=user_id)
    salehouse=sale_houseModel.objects.filter(owner_id=user_id)
    land=rent_landModel.objects.filter(owner_id=user_id)
    saleland=sale_landModel.objects.filter(owner_id=user_id)
    shop=rent_shopModel.objects.filter(owner_id=user_id)
    saleshop=sale_shopModel.objects.filter(owner_id=user_id)
    pg=rent_pgModel.objects.filter(owner_id=user_id)
    salepg=sale_pgModel.objects.filter(owner_id=user_id)
    return render(request,'user/my-properties.html',{'house':house,'salehouse':salehouse,'land':land,'saleland':saleland,'shop':shop,'saleshop':saleshop,'pg':pg,'salepg':salepg} ) 

def add_properties_rent(request):
    user_id=request.session["user_id"]
    if request.method=='POST' and 'button1' in request.POST and request.FILES['house_image'] and request.FILES['bedroom_image'] and request.FILES['bathroom_image'] and request.FILES['kitchen_image'] and request.FILES['parking_image'] and request.FILES['dining_image']:
           
        hproperty_type=request.POST['hproperty_type']
        hproperty_location=request.POST['hproperty_location'] 
        hprice=request.POST['hprice']            
        hyear_built=request.POST['hyear_built']
        hrooms=request.POST['hrooms']
        hbedrooms=request.POST['hbedrooms']
        hbathrooms=request.POST['hbathrooms']
        hcar_parking=request.POST['hcar_parking']
       
        hsuper_buldup_area=request.POST['hsuper_buldup_area']        
        hcarpet_area=request.POST['hcarpet_area']
        hfurnishing=request.POST['hfurnishing']
        hmaintenance=request.POST['hmaintenance']
        htotal_floors=request.POST['htotal_floors']

       
        hfloor_no=request.POST['hfloor_no']        
        hfacing=request.POST['hfacing']
        hreference=request.POST['hreference']
    
        house_image=request.FILES['house_image']
        bedroom_image=request.FILES['bedroom_image']
        bathroom_image=request.FILES['bathroom_image']
        kitchen_image=request.FILES['kitchen_image']        
        parking_image=request.FILES['parking_image']
        dining_image=request.FILES['dining_image']
        hdescription=request.POST['hdescription']
        hamenities=request.POST['hamenities']
        
        
        properties = rent_houseModel.objects.create(owner_id=user_id,property_type=hproperty_type,car_parking=hcar_parking,property_location=hproperty_location,price=hprice,year_built=hyear_built,rooms=hrooms,bedrooms=hbedrooms,bathrooms=hbathrooms,super_buldup_area=hsuper_buldup_area,
        carpet_area=hcarpet_area,furnishing=hfurnishing,maintenance=hmaintenance,total_floors=htotal_floors,floor_no=hfloor_no,facing=hfacing,reference=hreference,house_image=house_image,bedroom_image=bedroom_image,bathroom_image=bathroom_image,kitchen_image=kitchen_image,parking_image=parking_image,dining_image=dining_image,description=hdescription,amenities=hamenities)
        properties.save()
        messages.info(request,'Successfully Added')
        
    elif request.method=='POST'and 'button2' in request.POST and "land_image" in request.FILES and "land_image1" in request.FILES and "land_image2" in request.FILES and "land_image3" in request.FILES and "land_image4" in request.FILES and "land_image5" in request.FILES: 
        user_id=request.session["user_id"]     
        lproperty_type=request.POST['lproperty_type']
        lproperty_location=request.POST['lproperty_location'] 
        lprice=request.POST['lprice']            
        llength=request.POST['llength']
        lbreadth=request.POST['lbreadth']
        lfacing=request.POST['lfacing']
        land_image=request.FILES['land_image']
        land_image1=request.FILES['land_image1']
        land_image2=request.FILES['land_image2']
        land_image3=request.FILES['land_image3']        
        land_image4=request.FILES['land_image4']
        land_image5=request.FILES['land_image5']
        ldescription=request.POST['ldescription']
        lamenities=request.POST['lamenities']

        
        properties = rent_landModel.objects.create(owner_id=user_id,property_type=lproperty_type,facing=lfacing,property_location=lproperty_location,price=lprice,length=llength,breadth=lbreadth,land_image=land_image,land_image1=land_image1,land_image2=land_image2,land_image5=land_image5,land_image3=land_image3,land_image4=land_image4,description=ldescription,amenities=lamenities)
        properties.save()
        messages.info(request,'Successfully Added')
           
    elif request.method=='POST'and 'button3' in request.POST and "shop_image" in request.FILES and "simage1" in request.FILES and "simage2" in request.FILES and "simage3" in request.FILES and "simage4" in request.FILES and "simage5" in request.FILES:
           
        user_id=request.session["user_id"] 
        sproperty_type=request.POST['sproperty_type']
        project_name=request.POST['project_name'] 
        scar_parking=request.POST['scar_parking']
        sprice=request.POST['sprice']
        sproperty_location=request.POST['sproperty_location'] 
        sfurnishing=request.POST['sfurnishing']            
        sbathrooms=request.POST['sbathrooms']
       
        ssuper_buldup_area=request.POST['ssuper_buldup_area']
        scarpet_area=request.POST['scarpet_area'] 
        smaintenance=request.POST['smaintenance']            
        sfacing=request.POST['sfacing']
        sreference=request.POST['sreference']
       
        shop_image=request.FILES['shop_image']
        simage1=request.FILES['simage1']
        simage2=request.FILES['simage2']
        simage3=request.FILES['simage3']        
        simage4=request.FILES['simage4']
        simage5=request.FILES['simage5']
        sdescription=request.POST['sdescription']
        samenities=request.POST['samenities']

        
        properties = rent_shopModel.objects.create(owner_id=user_id,price=sprice,property_location=sproperty_location,car_parking=scar_parking,project_name=project_name,property_type=sproperty_type,furnishing=sfurnishing,bathrooms=sbathrooms,super_buldup_area=ssuper_buldup_area,carpet_area=scarpet_area,maintenance=smaintenance,facing=sfacing,reference=sreference, shop_image=shop_image,image1=simage1,image2=simage2,image3=simage3,image4=simage4,image5=simage5,description=sdescription,amenities=samenities)
        properties.save()
        messages.info(request,'Successfully Added')

        
    elif request.method=='POST'and 'button4' in request.POST and "pg_image" in request.FILES and "pimage1" in request.FILES and "pimage2" in request.FILES and "pimage3" in request.FILES and "pimage4" in request.FILES and "pimage5" in request.FILES: 
        user_id=request.session["user_id"]     
        psub_type=request.POST['psub_type']
        pproperty_location=request.POST['pproperty_location'] 
        pprice=request.POST['pprice']            
        pfurnishing=request.POST['pfurnishing']
        pmeals=request.POST['pmeals']
       
       
        pg_image=request.FILES['pg_image']
        pimage1=request.FILES['pimage1']
        pimage2=request.FILES['pimage2']
        pimage3=request.FILES['pimage3']        
        pimage4=request.FILES['pimage4']
        pimage5=request.FILES['pimage5']
        pdescription=request.POST['pdescription']
        pamenities=request.POST['pamenities']
       
        properties = rent_pgModel.objects.create(owner_id=user_id,sub_type=psub_type,property_location=pproperty_location,price=pprice,furnishing=pfurnishing,meals=pmeals,pg_image=pg_image,image1=pimage1,image2=pimage2,image3=pimage3,image4=pimage4,image5=pimage5,description=pdescription,amenities=pamenities)
        properties.save() 
        messages.info(request,'Successfully Added')
        return redirect('user_dashboard')
    return render(request,'user/add-properties-rent.html')

#add properties sale
def add_properties_sale(request):
    user_id=request.session["user_id"]
    if request.method=='POST' and 'button1' in request.POST and request.FILES['house_image'] and request.FILES['bedroom_image'] and request.FILES['bathroom_image'] and request.FILES['kitchen_image'] and request.FILES['parking_image'] and request.FILES['dining_image']:
           
        hproperty_type=request.POST['hproperty_type']
        hproperty_location=request.POST['hproperty_location'] 
        hprice=request.POST['hprice']            
        hyear_built=request.POST['hyear_built']
        hrooms=request.POST['hrooms']
        hbedrooms=request.POST['hbedrooms']
        hbathrooms=request.POST['hbathrooms']
       
        hsuper_buldup_area=request.POST['hsuper_buldup_area']        
        hcarpet_area=request.POST['hcarpet_area']
        hfurnishing=request.POST['hfurnishing']
        hmaintenance=request.POST['hmaintenance']
        htotal_floors=request.POST['htotal_floors']

        htotal_floors=request.POST['htotal_floors']
        hfloor_no=request.POST['hfloor_no']        
        hfacing=request.POST['hfacing']
        hreference=request.POST['hreference']
    
        house_image=request.FILES['house_image']
        bedroom_image=request.FILES['bedroom_image']
        bathroom_image=request.FILES['bathroom_image']
        kitchen_image=request.FILES['kitchen_image']        
        parking_image=request.FILES['parking_image']
        dining_image=request.FILES['dining_image']
        hdescription=request.POST['hdescription']
        hamenities=request.POST['hamenities']
       
        properties = sale_houseModel.objects.create(owner_id=user_id,property_type=hproperty_type,property_location=hproperty_location,price=hprice,year_built=hyear_built,rooms=hrooms,bedrooms=hbedrooms,bathrooms=hbathrooms,super_buldup_area=hsuper_buldup_area,carpet_area=hcarpet_area,furnishing=hfurnishing,maintenance=hmaintenance,total_floors=htotal_floors,floor_no=hfloor_no,facing=hfacing,reference=hreference,house_image=house_image,bedroom_image=bedroom_image,bathroom_image=bathroom_image,kitchen_image=kitchen_image,parking_image=parking_image,dining_image=dining_image,description=hdescription,amenities=hamenities)
        properties.save()
        messages.info(request,'Successfully Added')
       
    elif request.method=='POST'and 'button2' in request.POST and "land_image" in request.FILES and "land_image1" in request.FILES and "land_image2" in request.FILES and "land_image3" in request.FILES and "land_image4" in request.FILES and "land_image5" in request.FILES:
        user_id=request.session["user_id"]      
        lproperty_type=request.POST['lproperty_type']
        lproperty_location=request.POST['lproperty_location'] 
        lprice=request.POST['lprice']            
        llength=request.POST['llength']
        lbreadth=request.POST['lbreadth']
        lfacing=request.POST['lfacing']
       
        land_image=request.FILES['land_image']
        land_image1=request.FILES['land_image1']
        land_image2=request.FILES['land_image2']
        land_image3=request.FILES['land_image3']        
        land_image4=request.FILES['land_image4']
        land_image5=request.FILES['land_image5']
        ldescription=request.POST['ldescription']
        lamenities=request.POST['lamenities']

        properties = sale_landModel.objects.create(owner_id=user_id,property_type=lproperty_type,facing=lfacing,property_location=lproperty_location,price=lprice,length=llength,breadth=lbreadth,land_image=land_image,land_image1=land_image1,land_image2=land_image2,land_image5=land_image5,land_image3=land_image3,land_image4=land_image4,description=ldescription,amenities=lamenities)
        properties.save()
        messages.info(request,'Successfully Added')
    elif request.method=='POST'and 'button3' in request.POST and "shop_image" in request.FILES and "simage1" in request.FILES and "simage2" in request.FILES and "simage3" in request.FILES and "simage4" in request.FILES and "simage5" in request.FILES: 
        user_id=request.session["user_id"]
        sproperty_type=request.POST['sproperty_type']
        project_name=request.POST['project_name'] 
        scar_parking=request.POST['scar_parking']           
        sprice=request.POST['sprice']
        sproperty_location=request.POST['sproperty_location'] 
        sfurnishing=request.POST['sfurnishing']            
        sbathrooms=request.POST['sbathrooms']
       
        ssuper_buldup_area=request.POST['ssuper_buldup_area']
        scarpet_area=request.POST['scarpet_area'] 
        smaintenance=request.POST['smaintenance']            
        sfacing=request.POST['sfacing']
        sreference=request.POST['sreference']
       
        shop_image=request.FILES['shop_image']
        simage1=request.FILES['simage1']
        simage2=request.FILES['simage2']
        simage3=request.FILES['simage3']        
        simage4=request.FILES['simage4']
        simage5=request.FILES['simage5']
        sdescription=request.POST['sdescription']
        samenities=request.POST['samenities']

        properties = sale_shopModel.objects.create(owner_id=user_id,car_parking=scar_parking,project_name=project_name,property_type=sproperty_type,price=sprice,property_location=sproperty_location,furnishing=sfurnishing,bathrooms=sbathrooms,super_buldup_area=ssuper_buldup_area,carpet_area=scarpet_area,maintenance=smaintenance,facing=sfacing,reference=sreference, shop_image=shop_image,image1=simage1,image2=simage2,image3=simage3,image4=simage4,image5=simage5,description=sdescription,amenities=samenities)
        properties.save()
        messages.info(request,'Successfully Added')
    elif request.method=='POST'and 'button4' in request.POST and "pg_image" in request.FILES and "pimage1" in request.FILES and "pimage2" in request.FILES and "pimage3" in request.FILES and "pimage4" in request.FILES and "pimage5" in request.FILES:  
        user_id=request.session["user_id"]    
        psub_type=request.POST['psub_type']
        pproperty_location=request.POST['pproperty_location'] 
        pprice=request.POST['pprice']            
        pfurnishing=request.POST['pfurnishing']
        pmeals=request.POST['pmeals']
       
       
        pg_image=request.FILES['pg_image']
        pimage1=request.FILES['pimage1']
        pimage2=request.FILES['pimage2']
        pimage3=request.FILES['pimage3']        
        pimage4=request.FILES['pimage4']
        pimage5=request.FILES['pimage5']
        pdescription=request.POST['pdescription']
        pamenities=request.POST['pamenities']

        properties = sale_pgModel.objects.create(owner_id=user_id,sub_type=psub_type,property_location=pproperty_location,price=pprice,furnishing=pfurnishing,meals=pmeals,pg_image=pg_image,image1=pimage1,image2=pimage2,image3=pimage3,image4=pimage4,image5=pimage5,description=pdescription,amenities=pamenities)
        properties.save() 
        messages.info(request,'Successfully Added')  
        return redirect('user_dashboard')
    return render(request,'user/add-properties-sale.html')

def edit_rent_house(request,id):
    house = rent_houseModel.objects.get(house_id=id) 
    if request.method=='POST' and request.FILES['house_image'] and request.FILES['bedroom_image'] and request.FILES['bathroom_image'] and request.FILES['kitchen_image'] and request.FILES['parking_image'] and request.FILES['dining_image']:
        hproperty_type=request.POST['hproperty_type']
        hproperty_location=request.POST['hproperty_location'] 
        hprice=request.POST['hprice']            
        hyear_built=request.POST['hyear_built']
        hrooms=request.POST['hrooms']
        hbedrooms=request.POST['hbedrooms']
        hbathrooms=request.POST['hbathrooms']
        hcar_parking=request.POST['hcar_parking']
       
        hsuper_buldup_area=request.POST['hsuper_buldup_area']        
        hcarpet_area=request.POST['hcarpet_area']
        hfurnishing=request.POST['hfurnishing']
        hmaintenance=request.POST['hmaintenance']
        htotal_floors=request.POST['htotal_floors']

       
        hfloor_no=request.POST['hfloor_no']        
        hfacing=request.POST['hfacing']
        hreference=request.POST['hreference']
    
        house_image=request.FILES['house_image']
        bedroom_image=request.FILES['bedroom_image']
        bathroom_image=request.FILES['bathroom_image']
        kitchen_image=request.FILES['kitchen_image']        
        parking_image=request.FILES['parking_image']
        dining_image=request.FILES['dining_image']
        hdescription=request.POST['hdescription']
        hamenities=request.POST['hamenities']
              
        obj = get_object_or_404(rent_houseModel,house_id=id)
        obj.property_type = hproperty_type
        obj.property_location = hproperty_location
        obj.price = hprice
        obj.year_built = hyear_built

        obj.rooms = hrooms
        obj.floor_no = hfloor_no
        obj.bedrooms = hbedrooms
        obj.bathrooms = hbathrooms
        obj.car_parking = hcar_parking
        obj.super_buldup_area = hsuper_buldup_area

        obj.carpet_area = hcarpet_area
        obj.furnishing = hfurnishing
        obj.maintenance = hmaintenance
        obj.total_floors = htotal_floors

        obj.facing = hfacing
        obj.reference = hreference
        obj.house_image = house_image
        obj.bedroom_image = bedroom_image
        obj.bathroom_image = bathroom_image
        obj.kitchen_image = kitchen_image
        obj.parking_image = parking_image

        obj.dining_image = dining_image
        obj.description = hdescription
        obj.amenities = hamenities
        obj.save()
        messages.info(request,'Successfully Updated')  
        return redirect('my_properties')
    return render(request,'user/edit-rent-house.html',{'house':house})


def edit_sale_house(request,id):
    salehouse = sale_houseModel.objects.get(sale_house_id=id) 
    if request.method=='POST' and request.FILES['house_image'] and request.FILES['bedroom_image'] and request.FILES['bathroom_image'] and request.FILES['kitchen_image'] and request.FILES['parking_image'] and request.FILES['dining_image']:
        hproperty_type=request.POST['hproperty_type']
        hproperty_location=request.POST['hproperty_location'] 
        hprice=request.POST['hprice']            
        hyear_built=request.POST['hyear_built']
        hrooms=request.POST['hrooms']
        hbedrooms=request.POST['hbedrooms']
        hbathrooms=request.POST['hbathrooms']
        hcar_parking=request.POST['hcar_parking']
       
        hsuper_buldup_area=request.POST['hsuper_buldup_area']        
        hcarpet_area=request.POST['hcarpet_area']
        hfurnishing=request.POST['hfurnishing']
        hmaintenance=request.POST['hmaintenance']
        htotal_floors=request.POST['htotal_floors']

       
        hfloor_no=request.POST['hfloor_no']        
        hfacing=request.POST['hfacing']
        hreference=request.POST['hreference']
    
        house_image=request.FILES['house_image']
        bedroom_image=request.FILES['bedroom_image']
        bathroom_image=request.FILES['bathroom_image']
        kitchen_image=request.FILES['kitchen_image']        
        parking_image=request.FILES['parking_image']
        dining_image=request.FILES['dining_image']
        hdescription=request.POST['hdescription']
        hamenities=request.POST['hamenities']
              
        obj = get_object_or_404(sale_houseModel,sale_house_id=id)
        obj.property_type = hproperty_type
        obj.property_location = hproperty_location
        obj.price = hprice
        obj.year_built = hyear_built

        obj.rooms = hrooms
        obj.floor_no = hfloor_no
        obj.bedrooms = hbedrooms
        obj.bathrooms = hbathrooms
        obj.car_parking = hcar_parking
        obj.super_buldup_area = hsuper_buldup_area

        obj.carpet_area = hcarpet_area
        obj.furnishing = hfurnishing
        obj.maintenance = hmaintenance
        obj.total_floors = htotal_floors

        obj.facing = hfacing
        obj.reference = hreference
        obj.house_image = house_image
        obj.bedroom_image = bedroom_image
        obj.bathroom_image = bathroom_image
        obj.kitchen_image = kitchen_image
        obj.parking_image = parking_image

        obj.dining_image = dining_image
        obj.description = hdescription
        obj.amenities = hamenities
        obj.save()
        messages.info(request,'Successfully Updated')  
        return redirect('my_properties')
    return render(request,'user/edit-sale-house.html',{'salehouse':salehouse})


def edit_rent_land(request,id):
    land = rent_landModel.objects.get(land_id=id) 
    if request.method=='POST'and 'button2' in request.POST and "land_image" in request.FILES and "land_image1" in request.FILES and "land_image2" in request.FILES and "land_image3" in request.FILES and "land_image4" in request.FILES and "land_image5" in request.FILES:     
        lproperty_type=request.POST['lproperty_type']
        lproperty_location=request.POST['lproperty_location'] 
        lprice=request.POST['lprice']            
        llength=request.POST['llength']
        lbreadth=request.POST['lbreadth']
        lfacing=request.POST['lfacing']
        land_image=request.FILES['land_image']
        land_image1=request.FILES['land_image1']
        land_image2=request.FILES['land_image2']
        land_image3=request.FILES['land_image3']        
        land_image4=request.FILES['land_image4']
        land_image5=request.FILES['land_image5']
        ldescription=request.POST['ldescription']
        lamenities=request.POST['lamenities']

              
        obj = get_object_or_404(rent_landModel,land_id=id)
        obj.property_type = lproperty_type
        obj.property_location = lproperty_location
        obj.price = lprice
        obj.length = llength
        obj.facing = lfacing

        obj.breadth = lbreadth
        obj.land_image = land_image
        obj.land_image1 = land_image1
        obj.land_image2 = land_image2
        obj.land_image3 = land_image3
        obj.land_image4 = land_image4

        obj.land_image5 = land_image5
        obj.description = ldescription
        obj.amenities = lamenities
        obj.save()
        messages.info(request,'Successfully Updated')  
        return redirect('my_properties')
    return render(request,'user/edit-rent-land.html',{'land':land})


def edit_sale_land(request,id):
    saleland = sale_landModel.objects.get(sale_land_id=id) 
    if request.method=='POST'and 'button2' in request.POST and "land_image" in request.FILES and "land_image1" in request.FILES and "land_image2" in request.FILES and "land_image3" in request.FILES and "land_image4" in request.FILES and "land_image5" in request.FILES:     
        lproperty_type=request.POST['lproperty_type']
        lproperty_location=request.POST['lproperty_location'] 
        lprice=request.POST['lprice']            
        llength=request.POST['llength']
        lbreadth=request.POST['lbreadth']
        lfacing=request.POST['lfacing']
        land_image=request.FILES['land_image']
        land_image1=request.FILES['land_image1']
        land_image2=request.FILES['land_image2']
        land_image3=request.FILES['land_image3']        
        land_image4=request.FILES['land_image4']
        land_image5=request.FILES['land_image5']
        ldescription=request.POST['ldescription']
        lamenities=request.POST['lamenities']

              
        obj = get_object_or_404(sale_landModel,sale_land_id=id)
        obj.property_type = lproperty_type
        obj.property_location = lproperty_location
        obj.price = lprice
        obj.length = llength
        obj.facing = lfacing

        obj.breadth = lbreadth
        obj.land_image = land_image
        obj.land_image1 = land_image1
        obj.land_image2 = land_image2
        obj.land_image3 = land_image3
        obj.land_image4 = land_image4

        obj.land_image5 = land_image5
        obj.description = ldescription
        obj.amenities = lamenities
        obj.save()
        messages.info(request,'Successfully Updated')  
        return redirect('my_properties')
    return render(request,'user/edit-sale-land.html',{'saleland':saleland})


def edit_rent_shop(request,id):
    shop = rent_shopModel.objects.get(shop_id=id)  
    if request.method=='POST'and 'button3' in request.POST and "shop_image" in request.FILES and "simage1" in request.FILES and "simage2" in request.FILES and "simage3" in request.FILES and "simage4" in request.FILES and "simage5" in request.FILES:
        sproperty_type=request.POST['sproperty_type']
        project_name=request.POST['project_name'] 
        scar_parking=request.POST['scar_parking']
        sprice=request.POST['sprice']
        sproperty_location=request.POST['sproperty_location'] 
        sfurnishing=request.POST['sfurnishing']            
        sbathrooms=request.POST['sbathrooms']
       
        ssuper_buldup_area=request.POST['ssuper_buldup_area']
        scarpet_area=request.POST['scarpet_area'] 
        smaintenance=request.POST['smaintenance']            
        sfacing=request.POST['sfacing']
        sreference=request.POST['sreference']
       
        shop_image=request.FILES['shop_image']
        simage1=request.FILES['simage1']
        simage2=request.FILES['simage2']
        simage3=request.FILES['simage3']        
        simage4=request.FILES['simage4']
        simage5=request.FILES['simage5']
        sdescription=request.POST['sdescription']
        samenities=request.POST['samenities']

        obj = get_object_or_404(rent_shopModel,shop_id=id)
        obj.property_type = sproperty_type
        obj.property_location = sproperty_location
        obj.price = sprice
        obj.bathrooms = sbathrooms
        obj.car_parking = scar_parking
        obj.super_buldup_area = ssuper_buldup_area

        obj.carpet_area = scarpet_area
        obj.furnishing = sfurnishing
        obj.maintenance = smaintenance
        obj.project_name = project_name

        obj.facing = sfacing
        obj.reference = sreference
        obj.shop_image = shop_image
        obj.image1 = simage1
        obj.image2 = simage2
        obj.image3 = simage3
        obj.image4 = simage4
        obj.image5 = simage5
        obj.description = sdescription
        obj.amenities = samenities
      
        obj.save()
        messages.info(request,'Successfully Updated')  
        return redirect('my_properties')
    return render(request,'user/edit-rent-shop.html',{'shop':shop})

def edit_sale_shop(request,id):
    saleshop = sale_shopModel.objects.get(sale_shop_id=id)  
    if request.method=='POST'and 'button3' in request.POST and "shop_image" in request.FILES and "simage1" in request.FILES and "simage2" in request.FILES and "simage3" in request.FILES and "simage4" in request.FILES and "simage5" in request.FILES:
        sproperty_type=request.POST['sproperty_type']
        project_name=request.POST['project_name'] 
        scar_parking=request.POST['scar_parking']
        sprice=request.POST['sprice']
        sproperty_location=request.POST['sproperty_location'] 
        sfurnishing=request.POST['sfurnishing']            
        sbathrooms=request.POST['sbathrooms']
       
        ssuper_buldup_area=request.POST['ssuper_buldup_area']
        scarpet_area=request.POST['scarpet_area'] 
        smaintenance=request.POST['smaintenance']            
        sfacing=request.POST['sfacing']
        sreference=request.POST['sreference']
       
        shop_image=request.FILES['shop_image']
        simage1=request.FILES['simage1']
        simage2=request.FILES['simage2']
        simage3=request.FILES['simage3']        
        simage4=request.FILES['simage4']
        simage5=request.FILES['simage5']
        sdescription=request.POST['sdescription']
        samenities=request.POST['samenities']

        obj = get_object_or_404(sale_shopModel,sale_shop_id=id)
        obj.property_type = sproperty_type
        obj.property_location = sproperty_location
        obj.price = sprice
        obj.bathrooms = sbathrooms
        obj.car_parking = scar_parking
        obj.super_buldup_area = ssuper_buldup_area

        obj.carpet_area = scarpet_area
        obj.furnishing = sfurnishing
        obj.maintenance = smaintenance
        obj.project_name = project_name

        obj.facing = sfacing
        obj.reference = sreference
        obj.shop_image = shop_image
        obj.image1 = simage1
        obj.image2 = simage2
        obj.image3 = simage3
        obj.image4 = simage4
        obj.image5 = simage5
        obj.description = sdescription
        obj.amenities = samenities
      
        obj.save()
        messages.info(request,'Successfully Updated')  
        return redirect('my_properties')
    return render(request,'user/edit-sale-shop.html',{'saleshop':saleshop})


def edit_rent_pg(request,id):
    pg = rent_pgModel.objects.get(pg_id=id) 
    if request.method=='POST'and 'button4' in request.POST and "pg_image" in request.FILES and "pimage1" in request.FILES and "pimage2" in request.FILES and "pimage3" in request.FILES and "pimage4" in request.FILES and "pimage5" in request.FILES: 
        psub_type=request.POST['psub_type']
        pproperty_location=request.POST['pproperty_location'] 
        pprice=request.POST['pprice']            
        pfurnishing=request.POST['pfurnishing']
        pmeals=request.POST['pmeals']
       
       
        pg_image=request.FILES['pg_image']
        pimage1=request.FILES['pimage1']
        pimage2=request.FILES['pimage2']
        pimage3=request.FILES['pimage3']        
        pimage4=request.FILES['pimage4']
        pimage5=request.FILES['pimage5']
        pdescription=request.POST['pdescription']
        pamenities=request.POST['pamenities']

        obj = get_object_or_404(rent_pgModel,pg_id=id)
        obj.sub_type = psub_type
        obj.property_location = pproperty_location
        obj.price = pprice
        obj.meals = pmeals
        obj.furnishing = pfurnishing
        
        obj.pg_image = pg_image
        obj.image1 = pimage1
        obj.image2 = pimage2
        obj.image3 = pimage3
        obj.image4 = pimage4
        obj.image5 = pimage5
        obj.description = pdescription
        obj.amenities = pamenities
      
        obj.save()
        messages.info(request,'Successfully Updated')  
        return redirect('my_properties')
    return render(request,'user/edit-rent-pg.html',{'pg':pg}) 


def edit_sale_pg(request,id):
    salepg = sale_pgModel.objects.get(sale_pg_id=id) 
    if request.method=='POST'and 'button4' in request.POST and "pg_image" in request.FILES and "pimage1" in request.FILES and "pimage2" in request.FILES and "pimage3" in request.FILES and "pimage4" in request.FILES and "pimage5" in request.FILES: 
        psub_type=request.POST['psub_type']
        pproperty_location=request.POST['pproperty_location'] 
        pprice=request.POST['pprice']            
        pfurnishing=request.POST['pfurnishing']
        pmeals=request.POST['pmeals']
       
       
        pg_image=request.FILES['pg_image']
        pimage1=request.FILES['pimage1']
        pimage2=request.FILES['pimage2']
        pimage3=request.FILES['pimage3']        
        pimage4=request.FILES['pimage4']
        pimage5=request.FILES['pimage5']
        pdescription=request.POST['pdescription']
        pamenities=request.POST['pamenities']

        obj = get_object_or_404(sale_pgModel,sale_pg_id=id)
        obj.sub_type = psub_type
        obj.property_location = pproperty_location
        obj.price = pprice
        obj.meals = pmeals
        obj.furnishing = pfurnishing
      
        obj.pg_image = pg_image
        obj.image1 = pimage1
        obj.image2 = pimage2
        obj.image3 = pimage3
        obj.image4 = pimage4
        obj.image5 = pimage5
        obj.description = pdescription
        obj.amenities = pamenities
      
        obj.save()
        messages.info(request,'Successfully Updated')  
        return redirect('my_properties')
    return render(request,'user/edit-sale-pg.html',{'salepg':salepg}) 
       

def  property_details(request,id):
    user=request.session["user_id"]
    property=rent_houseModel.objects.get(house_id=id)
    print("gggggggggggggggggggggggg")
    house_id=property.house_id
    owner_id=property.owner_id
    
  
    ownerdata=userModel.objects.get(user_id=owner_id)
    print(house_id)
    print(owner_id)
    user_details=userModel.objects.get(user_id=user)
    

    if request.method=='POST':
        user_name=request.POST['user_name']
        print(user_name)
        email=request.POST['email']
        print(email)
        mobile=request.POST['mobile']
        print(mobile)
        message=request.POST['message']
        appointment = house_bookingModel.objects.create(user_id=user,owner_id=owner_id,house_id=house_id,user_name=user_name,mobile=mobile,email=email,message=message)
        appointment.save()

        
        # otp = random.randint(1111,9999)
        url = "https://www.fast2sms.com/dev/bulkV2"
            # create a dictionary
        my_data = {
                # Your default Sender ID
                'sender_id': 'FSTSMS',            
                # Put your message here!
                'message': '''Welcome to HomeLife, You'r property has been booked. ''',             
                'language': 'english',
                'route': 'p',            
                # You can send sms to multiple numbers
                # separated by comma.
                'numbers': ownerdata.mobile,   
            }
            # create a dictionary
        headers = {
                'authorization': 'dj4i8WDyNGRfSxCV0Hz7FKtIOA29hPLXTUpE5quwZ6snlrYeoQv7zVYsdDJrbQAS5PW0IujioMXO3xUC',
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache"
            }
            # make a post request
        response = requests.request("POST",
                                        url,
                                        data = my_data,
                                        headers = headers)
            # print the send message
        print(response.text)

        messages.info(request,'Thanks for booking... we will contact you soon')
        return redirect('home')
    return render(request,'user/property-details.html',{'user':user_details,'property':property,'data':ownerdata})  

def  sale_property_details(request,id):
    user=request.session["user_id"]
    salehouse=sale_houseModel.objects.get(sale_house_id=id)
    sale_house_id=salehouse.sale_house_id
    owner_id=salehouse.owner_id
    ownerdata=userModel.objects.get(user_id=owner_id)
    user_details=userModel.objects.get(user_id=user)
    

    if request.method=='POST':
        user_name=request.POST['user_name']
        print(user_name)
        email=request.POST['email']
        print(email)
        mobile=request.POST['mobile']
        message=request.POST['message']
        appointment = salehouse_bookingModel.objects.create(user_id=user,owner_id=owner_id,sale_house_id=sale_house_id,user_name=user_name,mobile=mobile,email=email,message=message)
        appointment.save()

       # otp = random.randint(1111,9999)
        url = "https://www.fast2sms.com/dev/bulkV2"
            # create a dictionary
        my_data = {
                # Your default Sender ID
                'sender_id': 'FSTSMS',            
                # Put your message here!
                'message': '''Welcome to HomeLife, You'r property has been booked. ''',             
                'language': 'english',
                'route': 'p',            
                # You can send sms to multiple numbers
                # separated by comma.
                'numbers': ownerdata.mobile,   
            }
            # create a dictionary
        headers = {
                'authorization': 'dj4i8WDyNGRfSxCV0Hz7FKtIOA29hPLXTUpE5quwZ6snlrYeoQv7zVYsdDJrbQAS5PW0IujioMXO3xUC',
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache"
            }
            # make a post request
        response = requests.request("POST",
                                        url,
                                        data = my_data,
                                        headers = headers)
            # print the send message
        print(response.text)
 

        messages.info(request,'Thanks for booking... we will contact you soon')
        return redirect('home')
    return render(request,'user/sale-property-details.html',{'user':user_details,'salehouse':salehouse,'data':ownerdata})


def  rent_land_details(request,id):
    user=request.session["user_id"]
    property=rent_landModel.objects.get(land_id=id)
    land_id=property.land_id
    owner_id=property.owner_id
    ownerdata=userModel.objects.get(user_id=owner_id)
    user_details=userModel.objects.get(user_id=user)

    if request.method=='POST':
        user_name=request.POST['user_name']
        print(user_name)
        email=request.POST['email']
        print(email)
        mobile=request.POST['mobile']
        message=request.POST['message']
        appointment = land_bookingModel.objects.create(user_id=user,owner_id=owner_id,land_id=land_id,user_name=user_name,mobile=mobile,email=email,message=message)
        appointment.save()

       # otp = random.randint(1111,9999)
        url = "https://www.fast2sms.com/dev/bulkV2"
            # create a dictionary
        my_data = {
                # Your default Sender ID
                'sender_id': 'FSTSMS',            
                # Put your message here!
                'message': '''Welcome to HomeLife, You'r property has been booked. ''',             
                'language': 'english',
                'route': 'p',            
                # You can send sms to multiple numbers
                # separated by comma.
                'numbers': ownerdata.mobile,   
            }
            # create a dictionary
        headers = {
                'authorization': 'dj4i8WDyNGRfSxCV0Hz7FKtIOA29hPLXTUpE5quwZ6snlrYeoQv7zVYsdDJrbQAS5PW0IujioMXO3xUC',
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache"
            }
            # make a post request
        response = requests.request("POST",
                                        url,
                                        data = my_data,
                                        headers = headers)
            # print the send message
        print(response.text)


        messages.info(request,'Thanks for booking... we will contact you soon')
        return redirect('home')
    return render(request,'user/rent-land-details.html',{'property':property,'user':user_details,'data':ownerdata})

def  sale_land_details(request,id):
    user=request.session["user_id"]
    property=sale_landModel.objects.get(sale_land_id=id)
    sale_land_id=property.sale_land_id
    owner_id=property.owner_id
    ownerdata=userModel.objects.get(user_id=owner_id)
    user_details=userModel.objects.get(user_id=user)
    if request.method=='POST':
        user_name=request.POST['user_name']
        print(user_name)
        email=request.POST['email']
        print(email)
        mobile=request.POST['mobile']
        message=request.POST['message']
        appointment = saleland_bookingModel.objects.create(user_id=user,owner_id=owner_id,sale_land_id=sale_land_id,user_name=user_name,mobile=mobile,email=email,message=message)
        appointment.save()

      # otp = random.randint(1111,9999)
        url = "https://www.fast2sms.com/dev/bulkV2"
            # create a dictionary
        my_data = {
                # Your default Sender ID
                'sender_id': 'FSTSMS',            
                # Put your message here!
                'message': '''Welcome to HomeLife, You'r property has been booked. ''',             
                'language': 'english',
                'route': 'p',            
                # You can send sms to multiple numbers
                # separated by comma.
                'numbers': ownerdata.mobile,   
            }
            # create a dictionary
        headers = {
                'authorization': 'dj4i8WDyNGRfSxCV0Hz7FKtIOA29hPLXTUpE5quwZ6snlrYeoQv7zVYsdDJrbQAS5PW0IujioMXO3xUC',
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache"
            }
            # make a post request
        response = requests.request("POST",
                                        url,
                                        data = my_data,
                                        headers = headers)
            # print the send message
        print(response.text)


        messages.info(request,'Thanks for booking... we will contact you soon')
        return redirect('home')
    return render(request,'user/sale-land-details.html',{'property':property,'user':user_details,'data':ownerdata})


def  rent_shop_details(request,id):
    user=request.session["user_id"]
    property=rent_shopModel.objects.get(shop_id=id)
    shop_id=property.shop_id
    owner_id=property.owner_id
    ownerdata=userModel.objects.get(user_id=owner_id)
    user_details=userModel.objects.get(user_id=user)

    if request.method=='POST':
        user_name=request.POST['user_name']
        print(user_name)
        email=request.POST['email']
        print(email)
        mobile=request.POST['mobile']
        message=request.POST['message']
        appointment = shop_bookingModel.objects.create(user_id=user,owner_id=owner_id,shop_id=shop_id,user_name=user_name,mobile=mobile,email=email,message=message)
        appointment.save()

       # otp = random.randint(1111,9999)
        url = "https://www.fast2sms.com/dev/bulkV2"
            # create a dictionary
        my_data = {
                # Your default Sender ID
                'sender_id': 'FSTSMS',            
                # Put your message here!
                'message': '''Welcome to HomeLife, You'r property has been booked. ''',             
                'language': 'english',
                'route': 'p',            
                # You can send sms to multiple numbers
                # separated by comma.
                'numbers': ownerdata.mobile,   
            }
            # create a dictionary
        headers = {
                'authorization': 'dj4i8WDyNGRfSxCV0Hz7FKtIOA29hPLXTUpE5quwZ6snlrYeoQv7zVYsdDJrbQAS5PW0IujioMXO3xUC',
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache"
            }
            # make a post request
        response = requests.request("POST",
                                        url,
                                        data = my_data,
                                        headers = headers)
            # print the send message
        print(response.text)


        messages.info(request,'Thanks for booking... we will contact you soon')
        return redirect('home') 
    return render(request,'user/rent-shop-details.html',{'property':property,'user':user_details,'data':ownerdata})


def  sale_shop_details(request,id):
    user=request.session["user_id"]
    property=sale_shopModel.objects.get(sale_shop_id=id)
    sale_shop_id=property.sale_shop_id
    owner_id=property.owner_id
    ownerdata=userModel.objects.get(user_id=owner_id)
    user_details=userModel.objects.get(user_id=user)

    if request.method=='POST':
        user_name=request.POST['user_name']
        print(user_name)
        email=request.POST['email']
        print(email)
        mobile=request.POST['mobile']
        message=request.POST['message']
        appointment = saleshop_bookingModel.objects.create(user_id=user,owner_id=owner_id,sale_shop_id=sale_shop_id,user_name=user_name,mobile=mobile,email=email,message=message)
        appointment.save()

       # otp = random.randint(1111,9999)
        url = "https://www.fast2sms.com/dev/bulkV2"
            # create a dictionary
        my_data = {
                # Your default Sender ID
                'sender_id': 'FSTSMS',            
                # Put your message here!
                'message': '''Welcome to HomeLife, You'r property has been booked. ''',             
                'language': 'english',
                'route': 'p',            
                # You can send sms to multiple numbers
                # separated by comma.
                'numbers': ownerdata.mobile,   
            }
            # create a dictionary
        headers = {
                'authorization': 'dj4i8WDyNGRfSxCV0Hz7FKtIOA29hPLXTUpE5quwZ6snlrYeoQv7zVYsdDJrbQAS5PW0IujioMXO3xUC',
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache"
            }
            # make a post request
        response = requests.request("POST",
                                        url,
                                        data = my_data,
                                        headers = headers)
            # print the send message
        print(response.text)


        messages.info(request,'Thanks for booking... we will contact you soon')
        return redirect('home')
    return render(request,'user/sale-shop-details.html',{'property':property,'user':user_details,'data':ownerdata})


def  rent_pg_details(request,id):
    user=request.session["user_id"]
    property=rent_pgModel.objects.get(pg_id=id)
    pg_id=property.pg_id
    owner_id=property.owner_id
    ownerdata=userModel.objects.get(user_id=owner_id)
    user_details=userModel.objects.get(user_id=user)

    if request.method=='POST':
        user_name=request.POST['user_name']
        print(user_name)
        email=request.POST['email']
        print(email)
        mobile=request.POST['mobile']
        message=request.POST['message']
        appointment = pg_bookingModel.objects.create(user_id=user,owner_id=owner_id,pg_id=pg_id,user_name=user_name,mobile=mobile,email=email,message=message)
        appointment.save()

       # otp = random.randint(1111,9999)
        url = "https://www.fast2sms.com/dev/bulkV2"
            # create a dictionary
        my_data = {
                # Your default Sender ID
                'sender_id': 'FSTSMS',            
                # Put your message here!
                'message': '''Welcome to HomeLife, You'r property has been booked. ''',             
                'language': 'english',
                'route': 'p',            
                # You can send sms to multiple numbers
                # separated by comma.
                'numbers': ownerdata.mobile,   
            }
            # create a dictionary
        headers = {
                'authorization': 'dj4i8WDyNGRfSxCV0Hz7FKtIOA29hPLXTUpE5quwZ6snlrYeoQv7zVYsdDJrbQAS5PW0IujioMXO3xUC',
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache"
            }
            # make a post request
        response = requests.request("POST",
                                        url,
                                        data = my_data,
                                        headers = headers)
            # print the send message
        print(response.text)
 

        messages.info(request,'Thanks for booking... we will contact you soon')
        return redirect('home')

    return render(request,'user/rent-pg-details.html',{'property':property,'user':user_details,'data':ownerdata})

def  sale_pg_details(request,id):
    user=request.session["user_id"]
    property=sale_pgModel.objects.get(sale_pg_id=id)
    sale_pg_id=property.sale_pg_id
    owner_id=property.owner_id
    ownerdata=userModel.objects.get(user_id=owner_id)
    user_details=userModel.objects.get(user_id=user)

    if request.method=='POST':
        user_name=request.POST['user_name']
        print(user_name)
        email=request.POST['email']
        print(email)
        mobile=request.POST['mobile']
        message=request.POST['message']
        appointment = salepg_bookingModel.objects.create(user_id=user,owner_id=owner_id,sale_pg_id=sale_pg_id,user_name=user_name,mobile=mobile,email=email,message=message)
        appointment.save()

       # otp = random.randint(1111,9999)
        url = "https://www.fast2sms.com/dev/bulkV2"
            # create a dictionary
        my_data = {
                # Your default Sender ID
                'sender_id': 'FSTSMS',            
                # Put your message here!
                'message': '''Welcome to HomeLife, You'r property has been booked. ''',             
                'language': 'english',
                'route': 'p',            
                # You can send sms to multiple numbers
                # separated by comma.
                'numbers': ownerdata.mobile,   
            }
            # create a dictionary
        headers = {
                'authorization': 'dj4i8WDyNGRfSxCV0Hz7FKtIOA29hPLXTUpE5quwZ6snlrYeoQv7zVYsdDJrbQAS5PW0IujioMXO3xUC',
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache"
            }
            # make a post request
        response = requests.request("POST",
                                        url,
                                        data = my_data,
                                        headers = headers)
            # print the send message
        print(response.text)


        messages.info(request,'Thanks for booking... we will contact you soon')
        return redirect('home')
    return render(request,'user/sale-pg-details.html',{'property':property,'user':user_details,'data':ownerdata})





def rent_houses(request):
    data=rent_houseModel.objects.all()
    return render(request,'user/rent-houses.html',{'data':data,})
def sale_houses(request):
    data=sale_houseModel.objects.all()
    # user=request.session["user_id"]
    # data=rent_houseModel.objects.filter(user=user)
    return render(request,'user/sale-houses.html',{'data':data} )    

def rent_lands(request):
    data=rent_landModel.objects.all()
    return render(request,'user/rent-lands.html',{'data':data,})

def sale_lands(request):
    data=sale_landModel.objects.all()
    return render(request,'user/sale-lands.html',{'data':data,})

def rent_shops(request):
    data=rent_shopModel.objects.all()
    return render(request,'user/rent-shops.html',{'data':data,})

def sale_shops(request):
    data=sale_shopModel.objects.all()
    return render(request,'user/sale-shops.html',{'data':data,})

def rent_pg(request):
    data=rent_pgModel.objects.all()
    return render(request,'user/rent-pg.html',{'data':data,})

def sale_pg(request):
    data=sale_pgModel.objects.all()
    return render(request,'user/sale-pg.html',{'data':data,})



def appointment(request):
    user_id=request.session["user_id"]
    house=house_bookingModel.objects.filter(owner_id=user_id)
    salehouse=salehouse_bookingModel.objects.filter(owner_id=user_id)
    land=land_bookingModel.objects.filter(owner_id=user_id)
    saleland=saleland_bookingModel.objects.filter(owner_id=user_id)
    shop=shop_bookingModel.objects.filter(owner_id=user_id)
    saleshop=saleshop_bookingModel.objects.filter(owner_id=user_id)
    pg=pg_bookingModel.objects.filter(owner_id=user_id)
    salepg=salepg_bookingModel.objects.filter(owner_id=user_id)
    return render(request,'user/appointment.html',{'house':house,'salehouse':salehouse,'land':land,'saleland':saleland,'shop':shop,'saleshop':saleshop,'pg':pg,'salepg':salepg,})  


def profile(request):
    user=request.session["user_id"]
    data = userModel.objects.get(user_id=user)
    obj = get_object_or_404(userModel,user_id=user)
    if request.method=='POST':
        print('ftttyy')
        user_name=request.POST['user_name']
        print(user_name)
        email=request.POST['email']
        mobile=request.POST['mobile']
        location=request.POST['location']
        dob = request.POST['dob']
        print('ddddddddddddddddddddd')
        if len(request.FILES) != 0:
            print("ggggggggggggggggggggggggggggggg")
            user_image = request.FILES['user_image']
            obj.user_name = user_name
            obj.mobile = mobile
            obj.email = email
            obj.location =location
            obj.dob = dob
            obj.user_image = user_image
            obj.save(update_fields=['user_name','mobile','email','location','user_image','dob'])
            obj.save()

   
        else:
            obj.user_name = user_name
            obj.mobile = mobile
            obj.email = email
            obj.location =location
            obj.dob = dob
            obj.save(update_fields=['user_name','mobile','email','location','dob'])
            obj.save()
       

          
  

   
    return render(request,'user/profile.html',{'data': data})
   

def edit_profile(request,id):
    edit = userModel.objects.get(user_id=id)  
    if request.method=='POST' and "user_image" in request.FILES:
        user_name=request.POST['user_name']
        mobile=request.POST['mobile']
        email=request.POST['email'] 
        dob=request.POST['dob']
        location=request.POST['location']
        user_image=request.FILES['user_image']       
        obj = get_object_or_404(userModel,user_id=id)
        obj.user_name = user_name
        obj.mobile = mobile
        obj.email = email
        obj.dob = dob
        obj.location =location
        obj.user_image = user_image
        obj.save()
        return redirect('profile')
    return render(request,'user/edit-profile.html', {'data':edit})
     

def feedback(request):
    user_id=request.session['user_id']
    print(user_id)
    if request.method=='POST':
        print('hghghggh')
        feedback_type=request.POST['feedback_type']
        feedback=request.POST['feedback']
        print(user_id)
        user_details=userModel.objects.get(user_id=user_id)
        user_name=user_details.user_name
        print(user_name)
        user_image=user_details.user_image
        email=user_details.email
        print(email)

        feedback = feedbackModel.objects.create(user_name=user_name,email=email,feedback=feedback,user_image=user_image,feedback_type=feedback_type)
        feedback.save()
        messages.info(request,"Thank you for your feedback")
    return render(request,'user/feedback.html')

        