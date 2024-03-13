from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def profile(self):
        profile = Profile.objects.get(user=self)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000)
    bio = models.CharField(max_length=100)
    image = models.ImageField(upload_to="user_images", default="default.jpg")
    verified = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.full_name == "" or self.full_name == None:
            self.full_name = self.user.username
        super(Profile, self).save(*args, **kwargs)



def create_user_profile(sender,instance,created,**kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()



class ChatMessage(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    sender= models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender")
    reciever= models.ForeignKey(User,on_delete=models.CASCADE,related_name="reciever")

    message = models.CharField(max_length=1000)
    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)


    class Meta: 
        ordering = ["date"]
        verbose_name_plural = "Message"


    def _str__(self):
        return f"from {self.sender} to {self.reciever}"
    

    @property
    def sender_profile(self):
        sender_profile = Profile.objects.get(user=self.sender)

        return sender_profile

    @property
    def reciever_profile(self):
        reciever_profile = Profile.objects.get(user=self.reciever)
        
        return reciever_profile