from django.db import models

# Create your models here.
Book_Rate = (
    (5, '5'),
    (4, '4'),
    (3, '3'),
    (2, '2'),
    (1, '1'),
)

def get_image_path(instance, filename):
    return os.path.join('profile_image', str(instance.id), filename)
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    price = models.PositiveIntegerField(default=0)
    star_rate = models.IntegerField(choices=Book_Rate, default=1)
    # picture = models.ImageField(upload_to='profile_image', blank=True, null=True)

    def __str__(self):
        return self.title