from django.http import Http404
from django.shortcuts import render
from rest_framework import status,viewsets
from reciepe.serializers import recipeserializer,userserializer,reviewserializer
from reciepe.models import recipe
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from reciepe.models import recipe,review




@api_view(['GET','POST'])
def create(request):

    if (request.method=='GET'):
        r=recipe.objects.all()
        rev=recipeserializer(r,many=True)
        return Response(rev.data)

    if(request.method=='POST'):
        rev=recipeserializer(data=request.data)
        return Response(rev.data,status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_400_BAD_REQUEST)


#Using viewset

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = recipe.objects.all()
    serializer_class = recipeserializer


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = userserializer

class user_logout(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self,request):
        self.request.user.auth_token.delete()
        return Response({"message":"logout successful"},status=status.HTTP_200_OK)

class create_rev(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self,request):
        s=review.objects.all()
        stu=reviewserializer(s,many=True)
        return Response(stu.data)


    def post(self,request):
        r=reviewserializer(data=request.data)
        if(r.is_valid()):
            r.save()
            return Response(r.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class detail_rev(APIView):
    # permission_classes = [IsAuthenticated]

    def get_object(self,pk):
        try:
            return recipe.objects.get(pk=pk)
        except:
            raise Http404

    def get(self,request,pk):
        r=self.get_object(pk)
        rev=review.objects.filter(recipe_name=r)
        revdet=reviewserializer(rev,many=True)
        return Response(revdet.data)


class cuisinefilter(APIView):
    def get(self, request):
        query = self.request.query_params.get('cuisine')
        recipes = recipe.objects.filter(cuisine=query)
        r = recipeserializer(recipes, many=True)
        return Response(r.data)


# filter based on meal type

class mealfilter(APIView):
    def get(self, request):
        query = self.request.query_params.get('meal_type')
        recipes = recipe.objects.filter(meal_type=query)
        r = recipeserializer(recipes, many=True)
        return Response(r.data)



# filter based on ingredients

class ingredientFilter(APIView):
    def get(self, request):
        query = self.request.query_params.get('ingredients')
        recipes = recipe.objects.filter(ingredients=query)
        r = recipeserializer(recipes, many=True)
        return Response(r.data)