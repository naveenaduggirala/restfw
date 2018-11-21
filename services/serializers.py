from rest_framework import serializers
from accounts.models import Product



#serializers are used in serializing and deserializing the model instance 
#in json format,serializing means object to json form(get request),deserializing means 
#json to object(post)

class ProductSerializers(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=False, allow_blank=True, max_length=100)
	code = serializers.CharField(required=False, allow_blank=True, max_length=100)

	def validate_name(self,value):
		if len(value) < 2:
			raise serializers.ValidationError("Invalid name")


class CustomorSerializers(serializers.Serializer):
	name = serializers.CharField(max_length=100)
	code = serializers.CharField(max_length=100)
	qualification = serializers.CharField(max_length=100)