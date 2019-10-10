from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    class Meta:
        permissions = (("self_edif","Let user edit selfopsts"),("can_delete","Can delete posts"))
    post_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100)
    post_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField("datapablished")
    def publish(self):
        self.pub_date = timezone.now()

    def __str__(self):
        return self.post_text


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date = models.DateTimeField("date") #auto_now_add=True (Replace this when recreate db)

    def publish(self):
        self.date = timezone.now()
    def __str__(self):
        return self.text

