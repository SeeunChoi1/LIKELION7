from django.db import models
from django.utils import timezone

# Create your models here.
Book_Rate = (
    (5, '5'),
    (4, '4'),
    (3, '3'),
    (2, '2'),
    (1, '1'),
)

# def get_image_path(instance, filename):
#     return os.path.join('picture', str(instance.id), filename)

# def photo_url(self):
#     if self.photo and hasattr(self.photo, 'url'):
#         return self.photo.url
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    price = models.PositiveIntegerField(default=0)
    star_rate = models.IntegerField(choices=Book_Rate, default=1)
    picture = models.FileField(null=True, default='#')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    id_user = models.CharField(max_length=200, default=0)