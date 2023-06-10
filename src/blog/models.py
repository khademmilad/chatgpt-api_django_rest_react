from django.db import models
from django.contrib.auth.models import User



def user_directory_path(instance, filename):
    # Get the user ID
    user_id = instance.user.id



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=50)

    def __str__(self):
        return f"Post by {self.user.username}"
    


class PremiumPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=600)
    image = models.ImageField(upload_to=user_directory_path, default='default_image.jpg')

    def __str__(self):
        return f"Premium Post by {self.user.username}"