from tokenize import Comment, group
from urllib import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import models
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser , IsAuthenticated ,  BasePermission
from rest_framework.decorators import authentication_classes , permission_classes
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from random import randint
from .models import CustomUser as User
from .serial import *
# Create your views here.
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.timezone import now
import json
from django.forms import DateField
import random




# email backend

from chirp.settings import email_backend
from django.core.mail import send_mail

# basic functions


# pagination 
from chirp.pagination import CustomPageNumberPagination
from rest_framework.generics import ListAPIView


# swagger 
from rest_framework.generics import GenericAPIView


from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
status.HTTP_403_FORBIDDEN

from django.shortcuts import render





def mutable(request):
    request.data._mutable =True



@api_view()
def index(request):
    return Response('Respnse is Here')

@api_view(['GET','POST'])
def signup(request):
    if request.method == "GET":
        return Response({
            "message":"Please sign up first",
            "status":status.HTTP_100_CONTINUE
        })
    if request.method == "POST":
        dataa = request.data 
        request.POST._mutable = True
        global user_email , user_name , user_pass1,user_pass2,user_otp , user_dob ,user_fname,user_lname
        user_name = dataa['user_name']
        user_email = dataa['user_email']
        user_pass1 = dataa['user_pass1']
        user_pass2 = dataa['user_pass2']
        user_dob   = dataa['user_dob']
        user_fname  = dataa['user_fname']
        user_lname  = dataa['user_lname']


        try:
            user = User.objects.get(username=user_name)
            if user is not None:
                return Response({'message':'User already exit','status':status.HTTP_403_FORBIDDEN})
        except User.DoesNotExist:
            pass
        # SUser = authenticate(username=User.objects.get(email=SEmail),password=SPass)
        try:
            userr = User.objects.get(email=user_email)
            if userr is not None:
                return Response({'message':'Email already exit','status':status.HTTP_403_FORBIDDEN})
        except User.DoesNotExist:
            pass


        if user_pass1 != user_pass2:
            return Response({
            "message":"Please insert the Mathced password",
            "status":status.HTTP_404_NOT_FOUND
        })
        user_otp = randint(1000,9999)
        print(user_otp)
        text = f"The code for subscription is {user_otp}"
        send_mail('SignUp', text , email_backend, [user_email],fail_silently=False)
        return Response({
            "message":"We just malid you a OTP",
            "status":status.HTTP_100_CONTINUE
        })

@api_view(['GET','POST'])
def otp(request):
    if request.method == "GET":
        return Response({
            "message":"Please insert the otp",
            "status":status.HTTP_100_CONTINUE
        })    

    if request.method == "POST":
        dataa = request.data 
        request.POST._mutable = True
        code = int(dataa['code'])
        if code != user_otp:
            return Response({
                "message":"OTP is not right",
                "status":status.HTTP_404_NOT_FOUND
            })
        user = User.objects.create_user(
            username=user_name,
            password=user_pass1,
            email= user_email,
            dob = user_dob,
            first_name = user_fname,
            last_name = user_lname
            )
        user.save()
        getuser = User.objects.get(username=user_name)
        print(getuser.id)
        userid = int(getuser.id)
        # profileobj = Profile.objects.create(
        #     profile_user = userid
        # ) 
        # profileobj.save()
        profileobj = Profile.objects.create(
            profile_user_id = userid
            # when relational model have keyword "profile_user"
            # tehn we use "profile_user_id"
        )
        profileobj.save()
        
        text = f"You have sign up successfully"
        send_mail('SignUp', text , email_backend, [user_email],fail_silently=False)
        return Response({
            "message":"You have signed Up successfully",
            "status":status.HTTP_100_CONTINUE
        })    


@api_view(['GET','POST'])
def forget_pass(request):
    if request.method == 'POST':
        dataa = request.data 
        request.POST._mutable = True
        global forget_email , forget_otp
        forget_email = dataa['forget_email']
        forget_otp = randint(1000,9999)
        print(forget_otp)
        # 
        
        text = f"You Forget otp is {forget_otp}"
        send_mail('SignUp', text , email_backend, [forget_email],fail_silently=False)
        return Response({
            "message":"we just mailed you a otp",
            "status":status.HTTP_100_CONTINUE
        })
    if request.method == "GET":
        return Response({
            "message":"Please Insert the email to continoue",
            "status":status.HTTP_100_CONTINUE
        })


@api_view(['GET','POST'])
def forget_otp(request):
    if request.method == "GET":
        return Response({
            "message":"Please insert the otp and the passwords",
            "status":status.HTTP_100_CONTINUE
        })

    if request.method == "POST":
        dataa = request.data 
        request.POST._mutable = True
        code = int(dataa['code'])
        if code != forget_otp:
            return Response({
                "message":"OTP is not right",
                "status":status.HTTP_404_NOT_FOUND
            })
        f_pass1 = dataa['f_pass1']
        f_pass2 = dataa['f_pass2']
        if f_pass1 != f_pass2:
            return Response({'message':'Passwords not match','status':status.HTTP_406_NOT_ACCEPTABLE})
        f_user = User.objects.get(email=forget_email)
        f_user.set_password(f_pass1)
        f_user.save()
        text = f"You password updated succefuly"
        send_mail('SignUp', text , email_backend, [forget_email],fail_silently=False)
        return Response({
            "message":"Your password updated successfuly",
            "status":status.HTTP_100_CONTINUE
        })    


@api_view(['POST','GET'])
def sign_in(request):
    if request.method == "GET":
        return Response("Momin Iqbal is here")

    if request.method == "POST":

        dataa = request.data 
        signin_email = dataa['signin_email']
        signin_pass = dataa['signin_pass']
        
        
        try:
            try:
                user = authenticate(username=User.objects.get(email=signin_email),password=signin_pass)
            except:
                user = authenticate(username=signin_email,password=signin_pass)
        except User.DoesNotExist:
            return Response({'message':'Email or Username not corect','status':status.HTTP_404_NOT_FOUND})
        print(user)
        if user is None:
            return Response({'message':'Email or Password not corect','status':status.HTTP_404_NOT_FOUND})


        refresh = RefreshToken.for_user(user)

        return Response({
            'message':'User founded',
            'status':status.HTTP_200_OK,
            'data':{
                'username':str(user),
                'user email':signin_email,
                
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                }
            })


@api_view(['GET','POST'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def group_api(request):
    if request.method == 'GET':
        snippet = Group.objects.all()
        serialize  = group_serial( snippet , many = True)
        # serialize  = serial( snippet ,dataname=Group, many = True)
        
        return Response({
            'message':'Please Insert the goup',
            'status':status.HTTP_200_OK,
            'data':serialize.data
            })
        return Response(serialize.data)
    if request.method == 'POST':
        dataa = request.data
        mutable(request)
        request.data._mutable()
        serialize = group_serial(data=dataa)
        if serialize.is_valid():
            serialize.save()
            return Response({
                "messsage":"Group is saved is saved in database",
                "status":status.HTTP_200_OK,
                "data":serialize.data
                })




@api_view(['GET','DELETE','PUT'])
def group_api_id(request,id):
    try :
        snippet = Group.objects.get(group_id=id)
    except Group.DoesNotExist:
        return Response({'message':'Group not found','status':status.HTTP_404_NOT_FOUND})
    if request.method == "GET":
        snippet = Group.objects.filter(group_id=id)
        serialize = group_serial(snippet,many=True)
        return Response({"message":"Get Method","staus":status.HTTP_200_OK,"data":serialize.data})

    if request.method == "DELETE":
        snippet.delete()
        return Response({"message":"Deleted"})

    if request.method == "PUT":
        dataa = request.data
        mutable(request)
        key = dataa.keys()
        for k in key:
            setattr(snippet,k,dataa[k])
            # snippet.save()
        serialize = group_serial(snippet)
        return Response({"data":serialize.data})




# for all groups that are any where
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def group_all_api(request):
    if request.method == 'GET':
        objs = list(Group.objects.all())
        snippet = random.sample(objs,len(objs))
        # snippet = Group.objects.all()
        serialize  = group_serial( snippet , many = True)
        
        return Response({
            'message':'Please Insert the goup',
            'status':status.HTTP_200_OK,
            'data':serialize.data
            })

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def group_create_api(request):
    if request.method == 'POST':
        dataa = request.data
        mutable(request)
        dataa['group_creater'] = request.user.id
        dataa['group_created'] = now()
        dataa['group_admin'] = json.dumps({"admin":[f"{request.user.id}"]})
        serialize = group_serial(data=dataa)
        print(dataa)
        print(serialize)
        if serialize.is_valid():
            serialize.save()
            return Response({
                "messsage":"Group is saved is saved in database",
                "status":status.HTTP_200_OK,
                "data":serialize.data,
                'Creater':f'{request.user.id}'
                })
        return Response('not updated')



@api_view(['GET','DELETE','PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def group_update_id(request,id):
    user = request.user 
     
    try :
        snippet = Group.objects.filter(group_id=id)
    except Group.DoesNotExist:
        return Response({'message':'Group not found','status':status.HTTP_404_NOT_FOUND})
    
    snippet = Group.objects.filter(group_id=id)
    # print(snippet.group_creater)
    serialize = group_serial(snippet,many= True)
    # print(serialize.data['group_creater'])
    if request.user.id != serialize.data[0]['group_creater']:
        return Response({"message":"you have no access to do this"})
    if request.method == "GET":
        snippet = Group.objects.filter(group_id=id)
        serialize = group_serial(snippet,many=True)
        return Response({"message":"Get Method","staus":status.HTTP_200_OK,"data":serialize.data})

    if request.method == "DELETE":
        snippet.delete()
        return Response({"message":"Deleted"})

    # if request.method == "PUT":

    #     dataa = request.data
    #     print('----------')
    #     print(dataa)
    #     mutable(request)
    #     key = dataa.keys()
    #     print(key)
    #     for k in key:
    #         print(k)
    #         setattr(snippet,k,dataa[k])
    #         snippet.save()
    #     serialize = group_serial(snippet)
    #     return Response({"message":"The data is updated","status":status.HTTP_201_CREATED,"data":serialize.data})





# still not working
    if request.method == "PUT":
        snippet = Group.objects.get(group_id=id)
        dataa = request.data
        key = dataa.keys()
        print(dataa)
        for k in key:
            setattr(snippet,k,dataa[k])
            snippet.save()
        serialize = group_serial(snippet)
        return Response({"data":serialize.data})




@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def feelings_all_api(request):
    if request.method == 'GET':
        snippet = Feelings.objects.all()
        serialize  = feelings_serial( snippet , many = True)
        return Response({'message':'All feeelings are here','status':status.HTTP_200_OK,'data':serialize.data})



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def feelings_create_api(request):
    if request.method == 'POST':
        dataa = request.data
        print(dataa)
        serialize = feelings_serial(data=dataa)
        
        if serialize.is_valid():
            serialize.save()
            return Response({"messsage":"Added your feelings","status":status.HTTP_200_OK,"data":serialize.data})
        return Response('not updated')



@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def backpost_all_api(request):
    if request.method == 'GET':
        snippet = BackPost.objects.all()
        serialize  = backpost_serial( snippet , many = True)
        return Response({'message':'All post backgrouds are here are here','status':status.HTTP_200_OK,'data':serialize.data})



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def backpost_create_api(request):
    if request.method == 'POST':
        dataa = request.data
        serialize = backpost_serial(data=dataa)
        if serialize.is_valid():
            serialize.save()
            return Response({"messsage":"Added your backgroud post","status":status.HTTP_200_OK,"data":serialize.data})
        return Response('not Added')




@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def post_all_api(request):
    if request.method == 'GET':
        snippet = Post.objects.all()
        serialize  = post_serial( snippet , many = True)
        return Response({'message':'All post are here','status':status.HTTP_200_OK,'data':serialize.data})
    


@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def post_api(request):
    if request.method == 'GET':
        snippet = Post.objects.all()
        serialize  = post_serial( snippet , many = True)
        return Response({'message':'All post are here','status':status.HTTP_200_OK,'data':serialize.data})
    
    
    if request.method == 'POST':
        dataa = request.data
        mutable(request)
        serialize = post_serial(data=dataa)
        if serialize.is_valid():
            serialize.save()
            return Response({"messsage":"Group is saved is saved in database","status":status.HTTP_200_OK,"data":serialize.data})



@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def page_api(request):
    if request.method == 'GET':
        snippet = Page.objects.all()
        
        serialize  = page_serial( snippet , many = True)
        # snippet = PostUser.objects.all()
        # serialize = postuser_serial(snippet,many= True)
        return Response({'message':'All pages are here','status':status.HTTP_200_OK,'data':serialize.data})
    
    
    if request.method == 'POST':
        dataa = request.data
        mutable(request)  
        print(dataa)
        serialize = page_serial(data=dataa)
        # dataa['page_creater'] = request.user.id
        print(request.user.id) 
        print(type(request.user.id))
        dataa['page_creater'] = int(request.user.id)
        # dataa['page_like_count'] = int(dataa['page_like_count'])
        dataa['page_time_stamp'] = now()
        dataa['page_modified'] = now()
        print(dataa)
        if serialize.is_valid():
            serialize.save()
            return Response({"messsage":"Paged is saved in database","status":status.HTTP_200_OK,"data":serialize.data})
        return Response("dummmy respnse is here")


@api_view(['GET','DELETE','PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def page_api_id(request,id):
    try :
        snippet = Page.objects.get(page_username=id)
    except Page.DoesNotExist:
        return Response({'message':'Page not found','status':status.HTTP_404_NOT_FOUND})
    if request.method == "GET":
        snippet = Page.objects.filter(page_username=id)
        serialize = page_serial(snippet,many=True)
        return Response({"message":"Page is here","staus":status.HTTP_200_OK,"data":serialize.data})

    if request.method == "DELETE":
        snippet.delete()
        return Response({"message":"Deleted"})

    if request.method == "PUT":
        dataa = request.data
        mutable(request)
        key = dataa.keys()
        for k in key:
            setattr(snippet,k,dataa[k])
        serialize = page_serial(snippet)
        return Response({"data":serialize.data})





@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def story_api(request):
    if request.method == 'GET':
        snippet = Story.objects.all()
        serialize  = story_serial( snippet , many = True)
        return Response({'message':'All stories are here','status':status.HTTP_200_OK,'data':serialize.data})
    
    
    if request.method == 'POST':
        dataa = request.data
        mutable(request)  
        print(dataa)
        serialize = story_serial(data=dataa)
        # print(request.user.id) 
        # print(type(request.user.id))
        dataa['story_user'] = int(request.user.id)
        # dataa['page_like_count'] = int(dataa['page_like_count'])
        # dataa['page_time_stamp'] = now()
        # dataa['page_modified'] = now()
        dataa['story_time_stamp'] = now()
        print(dataa)
        if serialize.is_valid():
            serialize.save()
            return Response({"messsage":"Story is saved in database","status":status.HTTP_200_OK,"data":serialize.data})
        return Response("dummmy response is here")





@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def group_share(request,id):
    if request.method == 'PUT':
        snippet = Group.objects.filter(group_id = id)
        serialize = group_serial(data=snippet)
        print(serialize.data)
        return Response('Put method for group share')








# pagination as class based vies
class paginat(ListAPIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]
    
    def get(self, request):

        queryset = Group.objects.all()
        serializer_class = group_serial
        
        
        


# class postuser_add():
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
    
#     def get(self,request):
#         snippet = PostUser.objects.all()
#         serialize = postuser_serial(snippet,many = True)
        
#         return Response({'message':'All post are here','status':status.HTTP_200_OK,'data':serialize.data})


@api_view(['POST','GET'])
@authentication_classes([JWTAuthentication])   
@permission_classes([IsAuthenticated])
def postuser_add(request):
    if request.method ==  "GET":
        snippet = PostUser.objects.all()
        serialize = postuser_serial(snippet,many=True)
        # print(serialize.data)
        return Response({'message':'All post will here zara sabar karo are here','status':status.HTTP_200_OK,'data':serialize.data})
    if request.method == "POST":
        dataa = request.data
        # mutable(request)  
        
        # print(dataa)
        serialize = postuser_serial(data=dataa)
        # dataa['story_user'] = int(request.user.id)
        # dataa['story_time_stamp'] = now()
        # print(dataa)
        if serialize.is_valid():
            serialize.save()
            return Response({"messsage":"Post is saved in database","status":status.HTTP_200_OK,"data":serialize.data})
        return Response("dummmy response is here")



@api_view(['GET','DELETE','PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def postuser_id(request,id):
    try :
        snippet = PostUser.objects.get(post_id=id)
    except PostUser.DoesNotExist:
        return Response({'message':'Page not found','status':status.HTTP_404_NOT_FOUND})
    if request.method == "GET":
        snippet = PostUser.objects.filter(post_id=id)
        serialize = postuser_serial(snippet,many=True)
        postuser_id = serialize['postuser_id'].list
        print(postuser_id)
        return Response({"message":"Page is here","staus":status.HTTP_200_OK,"data":serialize.data})

    if request.method == "DELETE":
        snippet.delete()
        return Response({"message":"Deleted"})

    if request.method == "PUT":
        dataa = request.data
        mutable(request)
        key = dataa.keys()
        for k in key:
            setattr(snippet,k,dataa[k])
        serialize = postuser_serial(snippet)
        return Response({"message":"your data is updated","status":status.HTTP_200_OK ,"data":serialize.data})



@api_view(['POST','GET'])
@authentication_classes([JWTAuthentication])   
@permission_classes([IsAuthenticated])
def postcomment_view(request):
    if request.method ==  "GET":
        snippet = PostComment.objects.all()
        serialize = postcomment_serial(snippet,many=True)
        # print(serialize.data)
        return Response({'message':'All post will here zara sabar karo are here','status':status.HTTP_200_OK,'data':serialize.data})


    if request.method == "POST":
        dataa = request.data
        mutable(request)  
        
        # print(dataa)
        serialize = postcomment_serial(data=dataa)
        # dataa['story_user'] = int(request.user.id)
        # dataa['story_time_stamp'] = now()
        print(dataa)
        if serialize.is_valid():
            serialize.save()
            return Response({"messsage":"postcoment is saved in database","status":status.HTTP_200_OK,"data":serialize.data})
        return Response("dummmy response is here")

@api_view(['GET'])
@authentication_classes([JWTAuthentication])   
@permission_classes([IsAuthenticated])
def postcomment_view_id(request,id):
    try :
        snippet = PostUser.objects.get(post_id=id)
    except PostUser.DoesNotExist:
        return Response({'message':'Post user not found not found','status':status.HTTP_404_NOT_FOUND})
    if request.method == "GET":
        snippet = PostComment.objects.filter(comment_post=id)
        serialize = postcomment_serial(snippet,many=True)
        return Response({"message":"Comments of the post","staus":status.HTTP_200_OK,"data":serialize.data})

# likes for the specific view
@api_view(['GET'])
@authentication_classes([JWTAuthentication])   
@permission_classes([IsAuthenticated])
def postcomment_view_id(request,id):
    try :
        snippet = PostUser.objects.get(post_id=id)
    except PostUser.DoesNotExist:
        return Response({'message':'Post user not found not found','status':status.HTTP_404_NOT_FOUND})
    if request.method == "GET":
        snippet = PostLike.objects.filter(like_post=id)
        serialize = postlike_serial(snippet,many=True)
        return Response({"message":"Likes for the post","staus":status.HTTP_200_OK,"data":serialize.data})



@api_view(['POST','GET'])
@authentication_classes([JWTAuthentication])   
@permission_classes([IsAuthenticated])
def postlike_view(request):
    if request.method ==  "GET":
        snippet = PostLike.objects.all()
        serialize = postlike_serial(snippet,many=True)
        # print(serialize.data)
        return Response({'message':'All post will here zara sabar karo are here','status':status.HTTP_200_OK,'data':serialize.data})


    if request.method == "POST":
        dataa = request.data
        # mutable(request)  
        
        # print(dataa)
        serialize = postlike_serial(data=dataa)
        # dataa['story_user'] = int(request.user.id)
        # dataa['story_time_stamp'] = now()
        print(dataa)
        if serialize.is_valid():
            serialize.save()
            return Response({"messsage":"postcoment is saved in database","status":status.HTTP_200_OK,"data":serialize.data})
        return Response("dummmy response is here")
    
    
# till now we are unable to run for loop on the query dict
@api_view(['POST','GET'])
@authentication_classes([JWTAuthentication])   
@permission_classes([IsAuthenticated])
def postuser_view(request):
    if request.method ==  "GET":
        snippet = PostUser.objects.all()
        # snippet = snippet.lists()
        # for key,value in QueryDict(snippet).lists():
        # for key,value in snippet:
        #     print(key)
        for i in snippet:
            print(i)
            # for k in i:

            serialize = postuser_serial(i,many=True)
            print(serialize.data)
        serialize = postuser_serial(snippet,many=True)
        serializeresult = serialize.data
        # print(serializeresult)
        # for i in serializeresult:
        #     print(i)
        #     for k,v in i:
        #         print(k,v)
                
                # print ("%s %s" % (k, value))
        # print(serialize.data)
        return Response({'message':'All post will here zara sabar karo are here','status':status.HTTP_200_OK,'data':serialize.data})


@api_view(['POST','GET'])
@authentication_classes([JWTAuthentication])   
@permission_classes([IsAuthenticated])
def profile_view(request):
    user = request.user
    if request.method ==  "GET":
        snippet = Profile.objects.filter(profile_user=user.id)
        serialize = profile_serial(snippet,many=True)
        # print(serialize.data)
        return Response({'message':'All post will here zara sabar karo are here','status':status.HTTP_200_OK,'data':serialize.data})


    if request.method == "POST":
        dataa = request.data
        serialize = profile_serial(data=dataa)
        # dataa['story_user'] = int(request.user.id)
        # dataa['story_time_stamp'] = now()
        print(dataa)
        if serialize.is_valid():
            serialize.save()
            return Response({"messsage":"postcoment is saved in database","status":status.HTTP_200_OK,"data":serialize.data})
        return Response("dummmy response is here")

 
 
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def profile_update_view(request,id):
    try :
        snippet = Profile.objects.get(profile_id=id)
    except Profile.DoesNotExist:
        return Response({'message':'Profile not found','status':status.HTTP_404_NOT_FOUND})
    serialize = profile_serial(snippet)
    print(type(request.user.id))
    print(type(serialize.data['profile_user']))
    # FOr security that the orignal user can update data
    if request.user.id != serialize.data['profile_user']:
        return Response({"message":"you have no access to do this"})
    
    if request.method == "PUT":
        dataa = request.data
        mutable(request)
        dataa['profile_updated']= now()
        key = dataa.keys()
        for k in key:
            setattr(snippet,k,dataa[k])
            snippet.save()
        serialize = profile_serial(snippet)
        return Response({"data":serialize.data})
     
 
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def profile_view_id(request,id):
    try :
        snippet = Profile.objects.get(profile_id=id)
    except Profile.DoesNotExist:
        return Response({'message':'Profile not found','status':status.HTTP_404_NOT_FOUND})
    
    if request.method == "GET":
        snippet = Profile.objects.filter(profile_id=id)
        serialize = profile_serial(snippet,many=True)
        return Response({"message":"Page is here","staus":status.HTTP_200_OK,"data":serialize.data})

    # if request.method == "PUT":
    #     dataa = request.data
    #     mutable(request)
    #     key = dataa.keys()
    #     # print(key)
    #     for k in key:
    #         print(k)
    #         setattr(snippet,k,dataa[k])
    #         print(k)
    #         print(dataa[k])
    #     serialize = profile_serial(snippet)
        
        
    # if request.method == "PUT":
    #     dataa = request.data
    #     mutable(request)
    #     key = dataa.keys()
    #     for k in key:
    #         setattr(snippet,k,dataa[k])
    #         # snippet.save()
    #     serialize = profile_serial(snippet)
    #     return Response({"data":serialize.data})
        
        
        # return Response({"message":"your data is updated","status":status.HTTP_200_OK ,"data":serialize.data})
    
    
    
    '''remianing the for loop to view the data of the freinds'''
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])    
def friendlist_view(request):
    if request.method == "GET":
        user = request.user
        # print('_________')
        # print(user)
        # print('_________')
        sender = AddFriend.objects.filter(addfreind_sender=user).filter(addfreind_status = "friend")
        for i in sender:
            # print(i)
            # print('_________')
            # print(addfriend_serial(i).data)
            obj_add = addfriend_serial(i)
            print(obj_add['addfreind_reciever'].value)
            print(type(int(obj_add['addfreind_reciever'].value)))
            # friend_id = CustomUser.objects.get(id=obj_add['addfreind_reciever'].value)
            # print(friend_id)
        serialize_sender = addfriend_serial(sender,many=True)
        reciever = AddFriend.objects.filter(addfreind_reciever=user).filter(addfreind_status = "friend")
        serialize_reciever = addfriend_serial(reciever,many=True)
        # print(serialize_reciever.data)
        # print(serialize_sender.data)
        # return Response({'message':"The freind list is here","status":status.HTTP_100_CONTINUE, "data":"no data to display"})        

        return Response({'message':"The freind list is here","status":status.HTTP_100_CONTINUE, "Sender":serialize_sender.data,"reciever":serialize_reciever.data})


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])  
def addfriend_view(request):
    user = request.user
    dataa = request.data
    mutable(request)
    dataa['addfreind_status'] = 'sent'
    dataa['addfreind_created'] = now()
    dataa['addfreind_updated'] = now()
    dataa['addfreind_sender'] = user.id
    print(dataa)
    serialize = addfriend_serial(data=dataa)
    if serialize.is_valid():
        serialize.save()
    return Response({'message':"The freind list is here","status":status.HTTP_100_CONTINUE,"data":serialize.data})

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def accept_request_view(request,id):
    
    try :
        snippet = AddFriend.objects.get(addfriend_id=id)
    except AddFriend.DoesNotExist:
        return Response({'message':'NOt sent the friend request ','status':status.HTTP_404_NOT_FOUND})
    user = request.user
    print(user.id)
    # if request.user.id != 
    serialize = addfriend_serial(snippet)
    if request.user.id != serialize.data['addfreind_reciever']:
        return Response({"message":"you have no access to do this"})
    # snippet = AddFriend.objects.filter(addfriend_id = id)
    # dataa = request.data
    # mutable(request)
    # try:
    #     if user.id != addfr:
    #         print("Not matched")
    # except:
    #     pass
    dataa ={}
    # serialize = addfriend_serial(data=snippet)
    dataa['addfreind_updated'] = now()
    dataa['addfreind_status'] = 'friend'
       
    key = dataa.keys()
    for k in key:
        setattr(snippet,k,dataa[k])
        snippet.save()
    serialize = addfriend_serial(snippet)

    consrvation = MChat(
        # mchat_user1 = serialize['addfreind_reciever'].value,
        # mchat_user2 = serialize['addfreind_sender'].value,
        mchat_user1 = CustomUser.objects.get(id=serialize['addfreind_reciever'].value),
        mchat_user2 = CustomUser.objects.get(id=serialize['addfreind_sender'].value),
        mchat_nickname_1 = "No Name",
        mchat_nickname_2 = "No Name",
        
    )
    consrvation.save()
    return Response({"data":serialize.data})
    return Response("hello every body")

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def friend_unfriend_view(request,id):
    
    try :
        snippet = AddFriend.objects.get(addfriend_id=id)
    except AddFriend.DoesNotExist:
        return Response({'message':'NOt sent the friend request ','status':status.HTTP_404_NOT_FOUND})
    user = request.user

    dataa = request.data
    # mutable(request)
    # snippet.delete()
    if request.method == "DELETE":
        snippet.delete()
        return Response({"message":"Deleted"})






@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])  
def blockuser_view(request):
    user = request.user
    dataa = request.data
    mutable(request)
    # dataa['addfreind_status'] = 'sent'
    dataa['blockuser_timestamp'] = now()
    dataa['blockuser_update'] = now()
    dataa['blockuser_blocker'] = user.id
    print(dataa)
    serialize = blockuser_sereial(data=dataa)
    if serialize.is_valid():
        serialize.save()
        return Response({'message':"You block this user","status":status.HTTP_100_CONTINUE,"data":serialize.data})



@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def block_unblock_view(request,id):
    
    try :
        snippet = Blockuser.objects.get(blockuser_id=id)
    except Blockuser.DoesNotExist:
        return Response({'message':'not found ','status':status.HTTP_404_NOT_FOUND})
    user = request.user

    dataa = request.data
    # mutable(request)
    # snippet.delete()
    if request.method == "DELETE":
        snippet.delete()
        return Response({"message":"Deleted"})








'''Group '''

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def group_all_view(request):
    user = request.user
    snipppet = Group.objects.all()
    serialize = group_serial(snipppet,many=True)
    return Response({'message':"The Groups are  here","status":status.HTTP_100_CONTINUE, "data":serialize.data})


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def group_add_view(request):
    user = request.user
    dataa = request.data
    mutable(request)
    dataa['group_creater']=user.id
    # dataa['group_created'] = now()
    # dataa['group_updated'] = now()
    serialize = group_serial(data=dataa)
    if serialize.is_valid():
        serialize.save()
        return Response({'message':"The Groups are  here","status":status.HTTP_100_CONTINUE, "data":serialize.data})


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def group_put_view(request,id):

    try :
        snippet = Group.objects.get(group_id=id)
    except Group.DoesNotExist:
        return Response({'message':'Group not found ','status':status.HTTP_404_NOT_FOUND})
    user = request.user
    dataa = request.data
    mutable(request)
    # try:
    #     if user.id != snippet['addfreind_reciever']:
    #         print("not matched")
    # except:
    #     pass
    dataa['group_updated'] = now()
    key = dataa.keys()
    for k in key:
        setattr(snippet,k,dataa[k])
        snippet.save()
    serialize = group_serial(snippet)
    return Response({"data":serialize.data})


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def group_members_with_group_view(request,username):
    user = request.user
    try :
        snippet = Group.objects.get(group_username=username)
    except Group.DoesNotExist:
        return Response({'message':'Group not found ','status':status.HTTP_404_NOT_FOUND})
    snipppet = Group.objects.get(group_username=username)
    
    serialize = group_serial(snipppet)
    # print(type(serialize['group_id'].value))
    members = GroupMember.objects.filter(gmember_group=serialize['group_id'].value)
    serialize_members = groupmembers_serial(members,many=True)
    return Response({'message':"The Groups are  here","status":status.HTTP_100_CONTINUE, "data":{"group":serialize.data,"members":serialize_members.data}})

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def group_members_all_view(request,id):
    user = request.user
    try :
        snippet = Group.objects.get(group_id=id)
    except Group.DoesNotExist:
        return Response({'message':'Group not found ','status':status.HTTP_404_NOT_FOUND})
    # snipppet = Group.objects.get(group_id=id)
    
    # serialize = group_serial(snipppet)
    # print(type(serialize['group_id'].value))
    members = GroupMember.objects.filter(gmember_group=id)
    serialize_members = groupmembers_serial(members,many=True)
    return Response({'message':"The Groups are  here","status":status.HTTP_100_CONTINUE, "data":serialize_members.data})


            # obj_add = addfriend_serial(i)
            # print(obj_add['addfreind_reciever'].value)
            # print(type(int(obj_add['addfreind_reciever'].value)))
            
            

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def group_member_join_view(request):
    user = request.user
    dataa = request.data
    mutable(request)
    dataa['gmember_user']=user.id
    # dataa['gmember_isadmin']= False
    # dataa['gmember_created'] = now()
    # dataa['gmember_updated'] = now()
    serialize = groupmembers_serial(data=dataa)
    if serialize.is_valid():
        serialize.save()
        return Response({'message':"The group is created","status":status.HTTP_100_CONTINUE, "data":serialize.data})



# @api_view(['DELETE'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
# def group_member_delete_view(request,id):
#     dataa=






# For messenger chat



@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def messenger_sms_view(request):
    user = request.user
    snipppet = MChatSms.objects.all()
    serialize = mchatsms_serial(snipppet,many=True)
    return Response({'message':"All messages are here","status":status.HTTP_100_CONTINUE, "data":serialize.data})


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def messenger_sms_delete_view(request,id):
    
    try :
        snippet = MChatSms.objects.get(sms_id=id)
    except MChatSms.DoesNotExist:
        return Response({'message':'Message not found','status':status.HTTP_404_NOT_FOUND})
    user = request.user

    # dataa = request.data
    # mutable(request)
    # snippet.delete()
    if request.method == "DELETE":
        snippet.delete()
        return Response({"message":"Deleted"})
