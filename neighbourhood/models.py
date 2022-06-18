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

class Neighbourhood(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    # location = models.ForeignKey(Location, on_delete = models.CASCADE,null = True)
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
    first_name = models.CharField(max_length = 50,null=True)
    last_name = models.CharField(max_length = 50,null=True)
    bio = models.TextField(max_length=300)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    # location = models.ForeignKey(Location,on_delete = models.CASCADE,null=True)
    email = models.EmailField(max_length=60, blank=True)
    contact = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username
        
