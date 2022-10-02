
from .models import  *
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import CustomUser as User

class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = '__all__'
        
class token_serial(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'

class group_serial(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields ='__all__'


class groupmembers_serial(serializers.ModelSerializer):
    class Meta:
        model = GroupMember
        fields ='__all__'

# data =''
# class serial(self,serializers.ModelSerializer,data):
#     class Meta:
#         model = self.data
#         fields = '__all__'

# def serial(dataname,*args, **kwargs):
#     class gserial(serializers.ModelSerializer):
#         class Meta:
#             model = data
#             fields ='__all__'



class feelings_serial(serializers.ModelSerializer):
    class Meta:
        model = Feelings
        fields = '__all__'


class backpost_serial(serializers.ModelSerializer):
    class Meta:
        model = BackPost
        fields = '__all__'



class post_serial(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'



class postmedia_serial(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = '__all__'




class page_serial(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'



class story_serial(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'
        
        
class postuser_serial(serializers.ModelSerializer):
    class Meta:
        model  = PostUser
        fields = '__all__'
        
        

        
class postcomment_serial(serializers.ModelSerializer):
    class Meta:
        model  = PostComment
        fields = '__all__'
        
        
        

class postlike_serial(serializers.ModelSerializer):
    class Meta:
        model  = PostLike
        fields = '__all__'
        

class profile_serial(serializers.ModelSerializer):
    class Meta:
        model  = Profile
        fields = '__all__'
        
        
        
class addfriend_serial(serializers.ModelSerializer):
    class Meta:
        model  = AddFriend
        fields = '__all__'
        
        
        

        
class mchatsms_serial(serializers.ModelSerializer):
    class Meta:
        model  = MChatSms
        fields = '__all__'
        
    
        
class blockuser_sereial(serializers.ModelSerializer):
    class Meta:
        model  = Blockuser
        fields = '__all__'
        
        
    