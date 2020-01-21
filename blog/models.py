from django.db import models

# Create a blog model
#title
#pub_date
#body
#image

class Blog(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image =models.ImageField(upload_to='images/')
# add the blog app to the settings

# Create a migration


# MIGRATE


#Add to the Admin
