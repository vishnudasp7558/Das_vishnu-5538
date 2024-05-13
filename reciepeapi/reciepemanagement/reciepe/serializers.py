from rest_framework import serializers
from reciepe.models import recipe,review
from django.contrib.auth.models import User


class recipeserializer(serializers.ModelSerializer):

    class Meta:
        model=recipe
        fields=['id','recipe_name','recipe_ingredients','instructions','cuisine','meal_type']


class userserializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','username','password']

        def create(self,validated_date):
            user=User.objects.create_user(username=validated_date['username'],
                                       password=validated_date['password'])
            user.save()
            return user


class reviewserializer(serializers.ModelSerializer):
    class Meta:
        model=review
        fields=['recipe_name','user','rating','comment']

