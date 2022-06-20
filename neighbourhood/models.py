from pickle import FALSE
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_photo = CloudinaryField("Profile Image")
#     bio = models.TextField(max_length=300)
#     location = models.CharField(max_length = 40)
#     email = models.EmailField(max_length=200)
#     contact = models.CharField(max_length=100, blank=True)

#     def save_profile(self):
#         self.save()
    
#     def update_profile(self):
#         self.save()

#     def delete_profile(self):
#         self.delete()

#     @classmethod
#     def filter_by_id(cls, id):
#         profile = Profile.objects.filter(user=id).first()
#         return profile

#     def __str__(self):
#         return self.user.username

class Location(models.Model):
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

class Neighbourhood(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    location = models.ForeignKey(Location, on_delete = models.CASCADE,null = True)
    occupants = models.IntegerField(default=0)

    def save_neighbourhood(self):
        self.save()

    def __str__(self):
        return self.name

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    def update_neighbourhood(self):
        self.save()

    def update_occupants(self):
        self.occupants += 1
        self.save()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE,related_name = 'profile')
    profile_photo = CloudinaryField("Profile Image")
    bio = models.TextField(max_length=300)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE,related_name='neighbourhood',default= 1)
    location = models.ForeignKey(Location,related_name='location', on_delete = models.CASCADE,null=True)
    email = models.EmailField(max_length=60, blank=True)
    contact = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username

class Business(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name = 'business_user')
    name =models.CharField(max_length=60)
    description = models.CharField(max_length = 150,null=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE,null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE,related_name = 'business_neighbourhood',null=True)
    email =models.EmailField(max_length=60, blank=True)

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls,search_term):
        business = Business.objects.get(name__icontains=search_term)
        return business

    def update_business(self):
        self.save()

class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=60)
    post=models.TextField()
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete = models.CASCADE,default= 1)
    posted=models.DateTimeField(auto_now_add=True) 
    

    def __str__(self):
        return self.title


class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True)
    comment=models.CharField(max_length=255)
    posted=models.DateTimeField(auto_now_add=True) 

    @classmethod
    def get_comments(cls):
        comments = cls.objects.all()
        return comments

    def save_commment(self):
        self.save()

        
