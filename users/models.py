from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Check if image exists and handle resizing
        if self.image and hasattr(self.image, 'path') and os.path.isfile(self.image.path):
            img = Image.open(self.image.path)

            # Resize image if needed
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
        else:
            # Handle case where image file is missing
            print(f"Image file not found at {self.image.path}")
