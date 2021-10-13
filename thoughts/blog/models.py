from django.db import models

# Create your models here.

class Blog(models.Model):
	id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length = 500)
	body = models.TextField()

	def __str__(self):
		return str(self.title)+"#"+str(self.id)
