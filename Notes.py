#API (Application Programming Interface)
#--->Methode used to communicate two systems/applications

#REST API
#--->Rest is a standard or guidelines for building API
#--->Another standard is SOAP

#DjangoRestFramework
#--->It is a package provided by django for building REST API.

#REST API Based application.
#It doesn't consist of frond end coding only consist of back end coding.
#Its response will be pure data except for web page.
#Its frond end coding is done by another applications.
#Data will be shown in JSON format.

#CRUD OPERATIONS(HTTP REQUEST METHODES)
#--->GET--->READ--->TO READ ALL THE RECORDS FROM BACKEND
#--->POST--->CREATE--->TO CREATE A NEW RECORD IN THE BACKEND DB
#--->PUT--->UPDATE--->TO UPDATE A PARTICULAR RECORD IN THE BACKEND DB
#--->DELETE--->DELETE--->TO DELETE A PARTICULAR RECORD IN THE BACKEND DB

#SERIALIZATION
# --->Conversion of django object format into json format

#DE-SERIALIZATION
# --->Conversion of json format into django object format


# --->SERIALIZER AND MODEL SERIALIZER ARE TWO MODULES USED FOR SERIALIZATION
# AND DE-SERIALIZATION


#2 Types of views in api

#1)Function based API view

# @apiview([method='GET'/,'POST'])
# def view(request):
#     pass

#2)class based API view

# class view(APIview)
#     pass

