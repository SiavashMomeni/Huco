from django.db import models
from django.conf import settings
import os

from .category import Category

def images_path():
    return os.path.join(settings.BASE_DIR / 'templates' , "images")

class Product(models.Model):
	name = models.CharField(max_length=60)
	price = models.IntegerField(default=0)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	description = models.CharField(
		max_length=250, default='', blank=True, null=True)
	image = models.FilePathField(path=images_path)

	@staticmethod
	def get_products_by_id(ids):
		return Product.objects.filter(id__in=ids)

	@staticmethod
	def get_all_products():
		return Product.objects.all()

	@staticmethod
	def get_all_products_by_categoryid(category_id):
		if category_id:
			return Product.objects.filter(category=category_id)
		else:
			return Product.get_all_products()
