
from django.shortcuts import get_object_or_404, redirect, render
from userapp.models import *
from mainapp.models import *
from adminapp.models import *
from django.db.models import Q
# Create your views here.

#admin
def admin_login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        if email=='cloud' and password=='cloud':
            return redirect('admin_dashboard')
        elif email=='admin@gmail.com' and password=='admin':
            return redirect('admin_dashboard')
    return render(request,'user/admin-login.html')
   

def admin_dashboard(request):
    users=userModel.objects.count()
    feedbacks=feedbackModel.objects.count()
    house=rent_houseModel.objects.count()+sale_houseModel.objects.count()+rent_landModel.objects.count()+sale_landModel.objects.count()+rent_shopModel.objects.count()+sale_shopModel.objects.count()+rent_pgModel.objects.count()+sale_pgModel.objects.count()
   
    bookings=house_bookingModel.objects.count()+salehouse_bookingModel.objects.count()+land_bookingModel.objects.count()+saleland_bookingModel.objects.count()+pg_bookingModel.objects.count()+salepg_bookingModel.objects.count()+shop_bookingModel.objects.count()+saleshop_bookingModel.objects.count()

    return render(request,'admin/admin-dashboard.html',{'users':users,'feedbacks':feedbacks,'house':house,'bookings':bookings})


def admin_view_users(request):
    data=userModel.objects.all()

    if request.method=='POST':
         search=request.POST.get('search')
         data=userModel.objects.filter(Q(user_id__icontains=search) | Q(user_name__icontains=search) | Q(user_id__icontains=search) | Q(email__icontains=search) | Q(mobile__icontains=search) | Q(location__icontains=search) | Q(reg_date__icontains=search))
        
    return render(request,'admin/admin-view-users.html',{'data':data})        


def admin_view_properties(request):
    house=rent_houseModel.objects.all().order_by("-uploded_date")
    salehouse=sale_houseModel.objects.all().order_by("-uploded_date")
    land=rent_landModel.objects.all().order_by("-uploded_date")
    saleland=sale_landModel.objects.all().order_by("-uploded_date")
    shop=rent_shopModel.objects.all().order_by("-uploded_date")
    saleshop=sale_shopModel.objects.all().order_by("-uploded_date")
    pg=rent_pgModel.objects.all().order_by("-uploded_date")
    salepg=sale_pgModel.objects.all().order_by("-uploded_date")
    if request.method=="POST" :
        print("okkk")
        search=request.POST.get('search')
        house=rent_houseModel.objects.filter(Q(house_id__icontains=search) | Q(owner_id__icontains=search) | Q(property_type__icontains=search) )
         
        salehouse=sale_houseModel.objects.filter(Q(sale_house_id__icontains=search) | Q(owner_id__icontains=search) | Q(property_type__icontains=search) )

        land=rent_landModel.objects.filter(Q(land_id__icontains=search) | Q(owner_id__icontains=search) | Q(property_type__icontains=search) )

        saleland=sale_landModel.objects.filter(Q(sale_land_id__icontains=search) | Q(owner_id__icontains=search) | Q(property_type__icontains=search) )

        shop=rent_shopModel.objects.filter(Q(shop_id__icontains=search) | Q(owner_id__icontains=search) | Q(property_type__icontains=search) )

        saleshop=sale_shopModel.objects.filter(Q(sale_shop_id__icontains=search) | Q(owner_id__icontains=search) | Q(property_type__icontains=search) )

        pg=rent_pgModel.objects.filter(Q(pg_id__icontains=search) | Q(owner_id__icontains=search) | Q(sub_type__icontains=search) )

        salepg=sale_pgModel.objects.filter(Q(sale_pg_id__icontains=search) | Q(owner_id__icontains=search) | Q(sub_type__icontains=search) )

    return render(request,'admin/admin-view-properties.html',{'house':house,'salehouse':salehouse,'land':land,'saleland':saleland,'shop':shop,'saleshop':saleshop,'pg':pg,'salepg':salepg})        



def admin_view_bookings(request):
   house=house_bookingModel.objects.all().order_by("-booking_date")
   salehouse=salehouse_bookingModel.objects.all().order_by("-booking_date")
   land=land_bookingModel.objects.all().order_by("-booking_date")
   saleland=saleland_bookingModel.objects.all().order_by("-booking_date")
   shop=shop_bookingModel.objects.all().order_by("-booking_date")
   saleshop=saleshop_bookingModel.objects.all().order_by("-booking_date")
   pg=pg_bookingModel.objects.all().order_by("-booking_date")
   salepg=salepg_bookingModel.objects.all().order_by("-booking_date")
   
   if request.method=='POST':
       search=request.POST.get('search')
       house = house_bookingModel.objects.filter(Q(house_booking_id__icontains=search) | Q(user_id__icontains=search) | Q(owner_id__icontains=search) | Q(house_id__icontains=search) )
       
       salehouse = salehouse_bookingModel.objects.filter(Q(salehouse_booking_id__icontains=search) | Q(user_id__icontains=search) | Q(owner_id__icontains=search) | Q(sale_house_id__icontains=search) )


       land = land_bookingModel.objects.filter(Q(land_booking_id__icontains=search) | Q(user_id__icontains=search) | Q(owner_id__icontains=search) | Q(land_id__icontains=search))
       
       saleland = saleland_bookingModel.objects.filter(Q(saleland_booking_id__icontains=search) | Q(user_id__icontains=search) | Q(owner_id__icontains=search) | Q(sale_land_id__icontains=search))

       shop = shop_bookingModel.objects.filter(Q(shop_booking_id__icontains=search) | Q(user_id__icontains=search) | Q(owner_id__icontains=search) | Q(shop_id__icontains=search))
       
       saleshop = saleshop_bookingModel.objects.filter(Q(saleshop_booking_id__icontains=search) | Q(user_id__icontains=search) | Q(owner_id__icontains=search) | Q(sale_shop_id__icontains=search))

       pg = pg_bookingModel.objects.filter(Q(pg_booking_id__icontains=search) | Q(user_id__icontains=search) | Q(owner_id__icontains=search) | Q(pg_id__icontains=search))
       
       salepg = salepg_bookingModel.objects.filter(Q(salepg_booking_id__icontains=search) | Q(user_id__icontains=search) | Q(owner_id__icontains=search) | Q(sale_pg_id__icontains=search) )

   return render(request,'admin/admin-view-bookings.html',{'house':house,'salehouse':salehouse,'land':land,'saleland':saleland,'shop':shop,'saleshop':saleshop,'pg':pg,'salepg':salepg}) 




def accept_renthouse(request,id):
    accept=get_object_or_404(rent_houseModel,house_id=id)
    accept.status='Accepted'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('admin_view_properties')

def accept_salehouse(request,id):
    accept=get_object_or_404(sale_houseModel,sale_house_id=id)
    accept.status='Accepted'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('admin_view_properties')    

def accept_rentland(request,id):
    accept=get_object_or_404(rent_landModel,land_id=id)
    accept.status='Accepted'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('admin_view_properties')    

def accept_saleland(request,id):
    accept=get_object_or_404(sale_landModel,sale_land_id=id)
    accept.status='Accepted'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('admin_view_properties')    

def accept_rentshop(request,id):
    accept=get_object_or_404(rent_shopModel,shop_id=id)
    accept.status='Accepted'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('admin_view_properties')

def accept_saleshop(request,id):
    accept=get_object_or_404(sale_shopModel,sale_shop_id=id)
    accept.status='Accepted'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('admin_view_properties')    

def accept_rentpg(request,id):
    accept=get_object_or_404(rent_pgModel,pg_id=id)
    accept.status='Accepted'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('admin_view_properties')    

def accept_salepg(request,id):
    accept=get_object_or_404(sale_pgModel,sale_pg_id=id)
    accept.status='Accepted'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('admin_view_properties')    

def reject_renthouse(request,id):
    reject=get_object_or_404(rent_houseModel,house_id=id)
    reject.status='Rejected'
    reject.save(update_fields=['status'])
    reject.save()
    return redirect('admin_view_properties')

def reject_salehouse(request,id):
    accept=get_object_or_404(sale_houseModel,sale_house_id=id)
    accept.status='Rejected'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('admin_view_properties')    

def reject_rentland(request,id):
    accept=get_object_or_404(rent_landModel,land_id=id)
    accept.status='Rejected'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('admin_view_properties')    

def reject_saleland(request,id):
    accept=get_object_or_404(sale_landModel,sale_land_id=id)
    accept.status='Rejected'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('admin_view_properties')    

def reject_rentshop(request,id):
    accept=get_object_or_404(rent_shopModel,shop_id=id)
    accept.status='Rejected'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('admin_view_properties')    

def reject_saleshop(request,id):
    accept=get_object_or_404(sale_shopModel,sale_shop_id=id)
    accept.status='Rejected'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('admin_view_properties')    
   

def reject_rentpg(request,id):
    accept=get_object_or_404(rent_pgModel,pg_id=id)
    accept.status='Rejected'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('admin_view_properties')    

def reject_salepg(request,id):
    accept=get_object_or_404(sale_pgModel,sale_pg_id=id)
    accept.status='Rejected'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('admin_view_properties')    



def admin_view_feedbacks(request):
    feedback= feedbackModel.objects.all().order_by("-feedback_date")

    if request.method=='POST':
         search=request.POST.get('search')
         feedback=feedbackModel.objects.filter(Q(user_name__icontains=search) | Q(feedback__icontains=search) | Q(feedback_date__icontains=search))
    return render(request,'admin/admin-view-feedback.html',{'feedback':feedback})
