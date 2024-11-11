
from django.db import models



# user register
class userModel(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(help_text='user_name',max_length=50)
    email=models.CharField(help_text=' email', max_length=50)
    password=models.CharField(help_text='password', max_length=50)
    mobile=models.BigIntegerField(help_text='mobile')
    location=models.CharField(help_text='location', max_length=200)
    dob=models.DateField(help_text='dob')
    user_image=models.ImageField(upload_to='user_image')
    reg_date=models.DateField(auto_now_add=True)

    class Meta:
        db_table='user_details'


# feedback start      
class feedbackModel(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    user_name=models.CharField(help_text='user_name',max_length=50, null=True)
    email=models.EmailField(help_text='email', max_length=50)
    feedback_type=models.CharField(help_text='feedback_type', max_length=50)
    feedback=models.TextField(help_text='feedback', max_length=350)
    user_image=models.ImageField(upload_to='user_image', null=True)
   
    feedback_date=models.DateField(auto_now_add=True)
    
    class Meta:
        db_table='user_feedback'

    feedback_id=models.AutoField(primary_key=True)
    user_name=models.CharField(help_text='user_name',max_length=50, null=True)
    email=models.EmailField(help_text='email', max_length=50)
    feedback_type=models.CharField(help_text='feedback_type', max_length=50)
    feedback=models.TextField(help_text='feedback', max_length=350)
    user_image=models.ImageField(upload_to='user_image', null=True)
   
    feedback_date=models.DateField(auto_now_add=True)
    
    class Meta:
        db_table='user_feedback'

#properties start
class rent_houseModel(models.Model):
    house_id=models.AutoField(primary_key=True)
    owner_id=models.IntegerField(null=True)
   
    property_type=models.TextField(help_text='property_type',max_length=100)
    property_location=models.CharField(help_text='property_location', max_length=250)
    price=models.CharField(help_text='price',max_length=50)
    year_built=models.DateField(help_text='year_built')
    rooms=models.CharField(help_text='rooms', max_length=10) 
    bedrooms=models.CharField(help_text='bedrooms',max_length=100)
    bathrooms=models.CharField(help_text='bathrooms', max_length=50)
    car_parking=models.CharField(help_text='car_parking',max_length=50,null=True)
    super_buldup_area=models.CharField(help_text='super_buldup_area',max_length=50)
    carpet_area=models.CharField(help_text='carpet_area',max_length=50)
    furnishing=models.CharField(help_text='furnishing',max_length=50)
    maintenance=models.CharField(help_text='maintenance',max_length=50)
    total_floors=models.CharField(help_text='total_floors',max_length=50)
    floor_no=models.CharField(help_text='floor_no',max_length=50)
    facing=models.TextField(help_text='facing',max_length=100)
    reference=models.TextField(help_text='reference',max_length=100)
    house_image=models.ImageField(upload_to='logo/images/')
    bedroom_image=models.ImageField(upload_to='logo/images/')
    bathroom_image=models.ImageField(upload_to='logo/images/')
    kitchen_image=models.ImageField(upload_to='logo/images/')
    parking_image=models.ImageField(upload_to='logo/images/')
    dining_image=models.ImageField(upload_to='logo/images/') 
    description=models.TextField(help_text='description',max_length=200)
    amenities=models.TextField(help_text='amenities',max_length=100)
    status=models.CharField(max_length=50,default='pending',null="True")
    uploded_date=models.DateField(auto_now_add=True)

    class Meta:
         db_table='property_rent_houses' 
 

#landmodel
class rent_landModel(models.Model):
    land_id=models.AutoField(primary_key=True)
    owner_id=models.IntegerField(null=True)
    property_type=models.TextField(help_text='property_type',max_length=100)
    property_location=models.CharField(help_text='property_location', max_length=250)
    price=models.CharField(help_text='price',max_length=50)
    facing=models.CharField(help_text='price',max_length=50,null=True)
    length=models.CharField(help_text='length',max_length=50)
    breadth=models.CharField(help_text='breadth', max_length=10) 
   
    land_image=models.ImageField(upload_to='land/images/')
    land_image1=models.ImageField(upload_to='land/images/')
    land_image2=models.ImageField(upload_to='land/images/')
    land_image3=models.ImageField(upload_to='land/images/')
    land_image4=models.ImageField(upload_to='land/images/')
    land_image5=models.ImageField(upload_to='land/images/') 
    description=models.TextField(help_text='description',max_length=200)
    amenities=models.TextField(help_text='amenities',max_length=100)
    status=models.CharField(max_length=50,default='pending',null="True")
    uploded_date=models.DateField(auto_now_add=True)

    class Meta:
         db_table='property_rent_lands'

#shop model
class rent_shopModel(models.Model):
    shop_id=models.AutoField(primary_key=True)
    owner_id=models.IntegerField(null=True)
    property_type=models.CharField(help_text='property_type',max_length=100,null=True)
    project_name=models.CharField(help_text='project_name',max_length=100,null=True)
    price=models.CharField(help_text='price',max_length=100)
    property_location=models.CharField(help_text='property_location',max_length=100,null=True)
    furnishing=models.CharField(help_text='furnishing',max_length=100)
    bathrooms=models.CharField(help_text='bathrooms',max_length=100)
    car_parking=models.CharField(help_text='car_parking',max_length=50,null=True)
    super_buldup_area=models.CharField(help_text='super_buldup_area',max_length=100,null=True)
    carpet_area=models.CharField(help_text='carpet_area',max_length=100,null=True)
    maintenance=models.CharField(help_text='maintenance',max_length=100)

    facing=models.CharField(help_text='facing',max_length=100)
    reference=models.CharField(help_text='reference',max_length=100)
    shop_image=models.ImageField(upload_to='shop/images/')
    image1=models.ImageField(upload_to='shop/images/')
    image2=models.ImageField(upload_to='shop/images/')
    image3=models.ImageField(upload_to='shop/images/')
    image4=models.ImageField(upload_to='shop/images/')
    image5=models.ImageField(upload_to='shop/images/') 
    description=models.TextField(help_text='description',max_length=200,null=True)
    amenities=models.TextField(help_text='amenities',max_length=100,null=True)
    status=models.CharField(max_length=50,default='pending',null="True")
    uploded_date=models.DateField(auto_now_add=True)

    class Meta:
         db_table='property_rent_shops'


#pg Model
class rent_pgModel(models.Model):
    pg_id=models.AutoField(primary_key=True)
    owner_id=models.IntegerField(null=True)
    sub_type=models.CharField(help_text='property_type',max_length=100)
    property_location=models.CharField(help_text='property_location', max_length=250)
    price=models.CharField(help_text='price',max_length=50)
    meals=models.CharField(help_text='meals',max_length=50,null=True)
    furnishing=models.CharField(help_text='furnishing',max_length=50)
   
    car_parking=models.CharField(help_text='car_parking',max_length=50,null=True)
    pg_image=models.ImageField(upload_to='pg/images/',null=True)
    image1=models.ImageField(upload_to='pg/images/')
    image2=models.ImageField(upload_to='pg/images/')
    image3=models.ImageField(upload_to='pg/images/')
    image4=models.ImageField(upload_to='pg/images/')
    image5=models.ImageField(upload_to='pg/images/') 
    description=models.TextField(help_text='description',max_length=200)
    amenities=models.TextField(help_text='amenities',max_length=100)
    status=models.CharField(max_length=50,default='pending',null="True")
    uploded_date=models.DateField(auto_now_add=True)

    class Meta:
         db_table='property_rent_pg&hostel'


#sale properties starts

class sale_houseModel(models.Model):
    sale_house_id=models.AutoField(primary_key=True)
    owner_id=models.IntegerField(null=True)
    property_type=models.TextField(help_text='property_type',max_length=100)
    property_location=models.CharField(help_text='property_location', max_length=250)
    price=models.CharField(help_text='price',max_length=50)
   
    year_built=models.DateField(help_text='year_built')
    rooms=models.CharField(help_text='rooms', max_length=10) 
    bedrooms=models.CharField(help_text='bedrooms',max_length=100)
    bathrooms=models.CharField(help_text='bathrooms', max_length=50)
    car_parking=models.CharField(help_text='car_parking', max_length=50,null=True)
    super_buldup_area=models.CharField(help_text='super_buldup_area',max_length=50)
    carpet_area=models.CharField(help_text='carpet_area',max_length=50)
    furnishing=models.CharField(help_text='furnishing',max_length=50)
    maintenance=models.CharField(help_text='maintenance',max_length=50)
    total_floors=models.CharField(help_text='total_floors',max_length=50)
    floor_no=models.CharField(help_text='floor_no',max_length=50)
    facing=models.TextField(help_text='facing',max_length=100)
    reference=models.TextField(help_text='reference',max_length=100)
    house_image=models.ImageField(upload_to='logo/images/')
    bedroom_image=models.ImageField(upload_to='logo/images/')
    bathroom_image=models.ImageField(upload_to='logo/images/')
    kitchen_image=models.ImageField(upload_to='logo/images/')
    parking_image=models.ImageField(upload_to='logo/images/')
    dining_image=models.ImageField(upload_to='logo/images/') 
    description=models.TextField(help_text='description',max_length=200)
    amenities=models.TextField(help_text='amenities',max_length=100)
    status=models.CharField(max_length=50,default='pending',null="True")
    uploded_date=models.DateField(auto_now_add=True)

    class Meta:
         db_table='property_sale_houses' 
 

#landmodel
class sale_landModel(models.Model):
    sale_land_id=models.AutoField(primary_key=True)
    owner_id=models.IntegerField(null=True)
    property_type=models.TextField(help_text='property_type',max_length=100)
    property_location=models.CharField(help_text='property_location', max_length=250)
    price=models.CharField(help_text='price',max_length=50)
    length=models.CharField(help_text='length',max_length=50)
    breadth=models.CharField(help_text='breadth', max_length=10) 
    facing=models.CharField(help_text='price',max_length=50,null=True)
    land_image=models.ImageField(upload_to='land/images/')
    land_image1=models.ImageField(upload_to='land/images/')
    land_image2=models.ImageField(upload_to='land/images/')
    land_image3=models.ImageField(upload_to='land/images/')
    land_image4=models.ImageField(upload_to='land/images/')
    land_image5=models.ImageField(upload_to='land/images/') 
    description=models.TextField(help_text='description',max_length=200)
    amenities=models.TextField(help_text='amenities',max_length=100)
    status=models.CharField(max_length=50,default='pending',null="True")
    uploded_date=models.DateField(auto_now_add=True)

    class Meta:
         db_table='property_sale_lands'

#shopmodel
class sale_shopModel(models.Model):
    sale_shop_id=models.AutoField(primary_key=True)
    owner_id=models.IntegerField(null=True)
    property_type=models.CharField(help_text='property_type',max_length=100,null=True)
    project_name=models.CharField(help_text='project_name',max_length=100,null=True)
    price=models.CharField(help_text='price',max_length=100)
    property_location=models.CharField(help_text='property_location',max_length=100,null=True)
    furnishing=models.CharField(help_text='furnishing',max_length=100)
    bathrooms=models.CharField(help_text='bathrooms',max_length=100)
    car_parking=models.CharField(help_text='car_parking', max_length=50,null=True)
    super_buldup_area=models.CharField(help_text='super_buldup_area',max_length=100,null=True)
    carpet_area=models.CharField(help_text='carpet_area',max_length=100,null=True)
    maintenance=models.CharField(help_text='maintenance',max_length=100)

    facing=models.CharField(help_text='facing',max_length=100)
    reference=models.CharField(help_text='reference',max_length=100)
    shop_image=models.ImageField(upload_to='shop/images/')
    image1=models.ImageField(upload_to='shop/images/')
    image2=models.ImageField(upload_to='shop/images/')
    image3=models.ImageField(upload_to='shop/images/')
    image4=models.ImageField(upload_to='shop/images/')
    image5=models.ImageField(upload_to='shop/images/') 
    description=models.TextField(help_text='description',max_length=200,null=True)
    amenities=models.TextField(help_text='amenities',max_length=100,null=True)
    status=models.CharField(max_length=50,default='pending',null="True")
    uploded_date=models.DateField(auto_now_add=True)

    class Meta:
         db_table='property_sale_shops'


#pg Model
class sale_pgModel(models.Model):
    sale_pg_id=models.AutoField(primary_key=True)
    owner_id=models.IntegerField(null=True)
    sub_type=models.CharField(help_text='property_type',max_length=100)
    property_location=models.CharField(help_text='property_location', max_length=250)
    price=models.CharField(help_text='price',max_length=50)
    meals=models.CharField(help_text='meals',max_length=50,null=True)
    furnishing=models.CharField(help_text='furnishing',max_length=50)
    car_parking=models.CharField(help_text='car_parking',max_length=50,null=True)
    pg_image=models.ImageField(upload_to='pg/images/',null=True)
    image1=models.ImageField(upload_to='pg/images/')
    image2=models.ImageField(upload_to='pg/images/')
    image3=models.ImageField(upload_to='pg/images/')
    image4=models.ImageField(upload_to='pg/images/')
    image5=models.ImageField(upload_to='pg/images/') 
    description=models.TextField(help_text='description',max_length=200)
    amenities=models.TextField(help_text='amenities',max_length=100)
    status=models.CharField(max_length=50,default='pending',null="True")
    uploded_date=models.DateField(auto_now_add=True)

    class Meta:
         db_table='property_sale_pg&hostel' 
  

class house_bookingModel(models.Model):
      house_booking_id=models.AutoField(primary_key=True)
      user_id=models.IntegerField()
      owner_id=models.IntegerField()
      house_id=models.IntegerField()
      user_name=models.CharField(help_text='user_name',max_length=50)
      email=models.EmailField(help_text='email',max_length=50)
      mobile=models.BigIntegerField(help_text='mobile')
      message=models.CharField(help_text='message',max_length=200)
      booking_date=models.DateField(auto_now_add=True)

      class Meta:
          db_table='house_booking_details'


class salehouse_bookingModel(models.Model):
      salehouse_booking_id=models.AutoField(primary_key=True)
      user_id=models.IntegerField()
      owner_id=models.IntegerField()
      sale_house_id=models.IntegerField()
      user_name=models.CharField(help_text='user_name',max_length=50)
      email=models.EmailField(help_text='email',max_length=50)
      mobile=models.BigIntegerField(help_text='mobile')
      message=models.CharField(help_text='message',max_length=200)
      booking_date=models.DateField(auto_now_add=True)

      class Meta:
          db_table='salehouse_booking_details' 

class land_bookingModel(models.Model):
      land_booking_id=models.AutoField(primary_key=True)
      user_id=models.IntegerField()
      owner_id=models.IntegerField()
      land_id=models.IntegerField()
      user_name=models.CharField(help_text='user_name',max_length=50)
      email=models.EmailField(help_text='email',max_length=50)
      mobile=models.BigIntegerField(help_text='mobile')
      message=models.CharField(help_text='message',max_length=200)
      booking_date=models.DateField(auto_now_add=True)

      class Meta:
          db_table='land_booking_details'


class saleland_bookingModel(models.Model):
      saleland_booking_id=models.AutoField(primary_key=True)
      user_id=models.IntegerField()
      owner_id=models.IntegerField()
      sale_land_id=models.IntegerField()
      user_name=models.CharField(help_text='user_name',max_length=50)
      email=models.EmailField(help_text='email',max_length=50)
      mobile=models.BigIntegerField(help_text='mobile')
      message=models.CharField(help_text='message',max_length=200)
      booking_date=models.DateField(auto_now_add=True)

      class Meta:
          db_table='saleland_booking_details' 


class shop_bookingModel(models.Model):
      shop_booking_id=models.AutoField(primary_key=True)
      user_id=models.IntegerField()
      owner_id=models.IntegerField()
      shop_id=models.IntegerField()
      user_name=models.CharField(help_text='user_name',max_length=50)
      email=models.EmailField(help_text='email',max_length=50)
      mobile=models.BigIntegerField(help_text='mobile')
      message=models.CharField(help_text='message',max_length=200)
      booking_date=models.DateField(auto_now_add=True)

      class Meta:
          db_table='shop_booking_details'  

class saleshop_bookingModel(models.Model):
      saleshop_booking_id=models.AutoField(primary_key=True)
      user_id=models.IntegerField()
      owner_id=models.IntegerField()
      sale_shop_id=models.IntegerField()
      user_name=models.CharField(help_text='user_name',max_length=50)
      email=models.EmailField(help_text='email',max_length=50)
      mobile=models.BigIntegerField(help_text='mobile')
      message=models.CharField(help_text='message',max_length=200)
      booking_date=models.DateField(auto_now_add=True)

      class Meta:
          db_table='saleshop_booking_details'       



class pg_bookingModel(models.Model):
      pg_booking_id=models.AutoField(primary_key=True)
      user_id=models.IntegerField()
      owner_id=models.IntegerField()
      pg_id=models.IntegerField()
      user_name=models.CharField(help_text='user_name',max_length=50)
      email=models.EmailField(help_text='email',max_length=50)
      mobile=models.BigIntegerField(help_text='mobile')
      message=models.CharField(help_text='message',max_length=200)
      booking_date=models.DateField(auto_now_add=True)

      class Meta:
          db_table='pg_booking_details'   


class salepg_bookingModel(models.Model):
      salepg_booking_id=models.AutoField(primary_key=True)
      user_id=models.IntegerField()
      owner_id=models.IntegerField()
      sale_pg_id=models.IntegerField()
      user_name=models.CharField(help_text='user_name',max_length=50)
      email=models.EmailField(help_text='email',max_length=50)
      mobile=models.BigIntegerField(help_text='mobile')
      message=models.CharField(help_text='message',max_length=200)
      booking_date=models.DateField(auto_now_add=True)

      class Meta:
          db_table='salepg_booking_details'                                            