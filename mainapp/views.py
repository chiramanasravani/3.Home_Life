from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from mainapp.models import contactModel
from userapp.models import *
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def home(request):
    feedback= feedbackModel.objects.all()
    house=rent_houseModel.objects.all()
    salehouse=sale_houseModel.objects.all()
    land=rent_landModel.objects.all()
    saleland=sale_landModel.objects.all()
    shop=rent_shopModel.objects.all()
    saleshop=sale_shopModel.objects.all()
    pg=rent_pgModel.objects.all()
    salepg=sale_pgModel.objects.all()
     

    if request.method=='POST':
       print("first button")
       house=request.POST.get('city1')
       location = request.POST.get('property_location')
       print(location)
       property_type = request.POST.get('property_type1')
       print(property_type)
       contract = request.POST.get('contract_type')
     

       data = rent_landModel.objects.filter(Q(property_type__contains='Lands'))
       sale_house_data = rent_houseModel.objects.filter(Q(property_type__contains='Houses & Villas'))
       rent_shop_data = rent_shopModel.objects.filter(Q(property_type__contains='Office'))
       rent_pg_data = rent_pgModel.objects.filter(Q(sub_type__contains='PG'))
      
     
       print(house)
       print(property_type)
       if property_type=='Lands' and contract=='Rent':
           data = rent_landModel.objects.filter(Q(property_type__icontains='Lands'),Q(property_location__icontains=location ))

       elif property_type=='Lands' and contract=='Buy':
           data = sale_landModel.objects.filter(Q(property_type__icontains='Lands'),Q(property_location__icontains=location ))
       
       elif property_type=='Houses' and contract=='Rent':
           data = rent_houseModel.objects.filter(Q(property_type__icontains='house'),Q(property_location__icontains=location ))

       elif property_type=='Houses' and contract=='Buy':
           data = sale_houseModel.objects.filter(Q(property_type__icontains='Houses & Villas') | Q(property_type__icontains='Builder Floors')|Q(property_type__icontains='Apartments') , Q(property_location__icontains=location ))  


       elif property_type=='Offices' and contract=='Rent':
           data = rent_shopModel.objects.filter(Q(property_type__icontains='house'),Q(property_location__icontains=location ))

       elif property_type=='Pg' and contract=='Rent':
           data = rent_pgModel.objects.filter(Q(sub_type__icontains='house'),Q(property_location__icontains=location ))  

       return render(request,'main/index.html',{'house':data,'house':sale_house_data,'house':rent_shop_data,'house':rent_pg_data})
       
    # if request.method=='POST':  
    #    print("second button")   
    #    salehouse = rent_houseModel.objects.filter( Q(property_location__icontains=house))
    #    print(house)
    #    return render(request,'main/index.html',{'salehouse':salehouse,})


     
    print('ggggggggggggggggggggggggggg')
     
    print("gggggggggggggggggggggggg")
    print(house)
    data=house
    return render(request,'main/index.html',{'feedback':feedback,'house':house,'data':data,'salehouse':salehouse,'land':land,'saleland':saleland,'shop':shop,'saleshop':saleshop,'pg':pg,'salepg':salepg})
    

def about(request):
    return render(request,'main/about.html')


def contact(request):
    if request.method == 'POST':
        user_name= request.POST['user_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contactModel.objects.create(user_name=user_name,email=email,subject=subject,message=message)
        messages.info(request,"Thank You")
    return render(request,'main/contact.html')