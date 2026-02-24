from django.db import models

# Create your models here.
# the class promotions has many to many relationship with product
# 
class Promotion(models.Model):
      description = models.TextField()
      discount = models.FloatField()
 #products
      # 
      # #
class Collection(models.Model):
     title = models.CharField(max_length=255)
     featured_product = models.ForeignKey('product',on_delete=models.SET_NULL, null=True,related_name='+')
     # why in the featured_product we set product as string its 
     # its because django can not create the reverse relationship as the collection has alredy implemented in product as parent class
     # this is for resolving reverse relationship of entities

#class of product table
class Product(models.Model):
     slug = models.SlugField()
     SKU = models.CharField(max_length=10, primary_key=True)
     title = models.CharField(max_length=255)
     description = models.TextField()
     unit_price = models.DecimalField(max_digits=6,decimal_places=2)
     invetory = models.IntegerField()
     last_update = models.DateTimeField(auto_now_add=True)
     collections =models.ForeignKey(Collection,on_delete=models.PROTECT)
     promotions = models.ManyToManyField(Promotion)#related_name='products')
 #customer class with choices implementation 
class Customer(models.Model):
      MEMBERSHIP_BROZE = 'B'
      MEMBERSHIP_SILVER = 'S'
      MEMBERSHIP_GOLD = 'G'
      MEMBERSHIP_CHOICE = [
      (MEMBERSHIP_BROZE ,'broze'), 
      (MEMBERSHIP_BROZE , 'silver'),
      (MEMBERSHIP_BROZE ,'gold')
      ]
      first_name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255)
      email = models.EmailField(unique=True)
      phone = models.CharField(max_length=255)
      birthday_date = models.DateField(null=True)
      membership = models.CharField(max_length=1,
                                    choices=MEMBERSHIP_CHOICE, default=MEMBERSHIP_BROZE)

class Meta:
      db_table = 'store_customers'
      indexes = [
            models.Index(fields =['last_name','first_name'])
      ]
#class order
class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETED ='C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
    (PAYMENT_STATUS_PENDING,'pending'),
    (PAYMENT_STATUS_COMPLETED,'completed'),
    (PAYMENT_STATUS_FAILED ,'failed')]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1,choices=PAYMENT_STATUS_CHOICES,default=PAYMENT_STATUS_PENDING)
    #the orderItem class has implemented as one to many relationships as that one order
    # has many order iterms 
class OrderItem(models.Model):
     order=models.ForeignKey(Order,on_delete=models.PROTECT)
     product = models.ForeignKey(Product,on_delete=models.PROTECT)
     quantity = models.PositiveSmallIntegerField()
     unit_price = models.DecimalField(max_digits=6,decimal_places=2)  
    #how to implement one to one relationship entities
    # take a look that the customer has adress and one customer has one adress
    # 
    # 
     
class Address(models.Model):
      street = models.CharField(max_length=255)
      city = models.CharField(max_length=255)
      customer = models.OneToOneField(Customer,on_delete= models.CASCADE,primary_key=True)
      # in case of one to many relationship      
      # we add the adress as the attribute to the customer class
      # and we replace oneTooneField with foreignkey also we delete primary_key in adress class  
class Cart(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
# class cartItems is child class from cart class and therefore 
class CartItems(models.Model):
         cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
         product = models.ForeignKey(Product,on_delete= models.CASCADE)
         quantity = models.PositiveSmallIntegerField() 