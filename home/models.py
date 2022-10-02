
from email.mime import audio
from unicodedata import name
from django.db import models
import os
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
# from .models import CustomUser as User
from datetime import timedelta

from django.db.models.functions import Now
# import timespan

'''for only delete the data after 24 hours'''
# class MyModel(models.Model):
#     # …
#     timestamp = models.DateTimeField(auto_now_add=True, db_index=True)


# # from datetime import timedelta
# from django.db.models.functions import Now

# MyModel.objects.filter(timestamp__gte=Now()-timespan(days=1))



class CustomUser(AbstractUser):
    phone           = models.CharField(max_length=20,null=True)
    dob             = models.DateField(auto_now=False, auto_now_add=False,null=True)

class Profile(models.Model):
    profile_id                  = models.BigAutoField(primary_key=True)
    profile_user                = models.OneToOneField("CustomUser",  on_delete=models.CASCADE)
    profile_aboutme             = models.TextField(max_length=500,null=True)
    profile_activities          = models.TextField(null=True)
    profile_afflicationcourt    = models.TextField(null=True)
    profile_favoraitbooks       = models.TextField(null=True)
    profile_favoraitmovies      = models.TextField(null=True)
    profile_favoraitmusics      = models.TextField(null=True)
    profile_favoraitquotes      = models.TextField(null=True)
    profile_favoraittvshows     = models.TextField(null=True)
    profile_intrests            = models.TextField(null=True)
    profile_notescourts         = models.TextField(null=True)
    profile_picture             = models.FileField(upload_to="profile_picture",null=True)
    profile_cover               = models.FileField(upload_to="profile_cover",null=True)
    profile_politicalviews      = models.TextField(null=True)
    profile_religion            = models.TextField(null=True)
    profile_schoolcourt         = models.TextField(null=True)
    profile_significantid       = models.TextField(null=True)
    profile_wallcourt           = models.TextField(null=True)
    profile_workplacecourt      = models.TextField(null=True)
    profile_friendscount        = models.IntegerField(max_length=25,default=0)
    profile_groupcount          = models.IntegerField(max_length=10,default=0)
    profile_created             = models.DateTimeField(default=now(),null=True)
    profile_updated             = models.DateTimeField(default=now(),null=True)
    
    
    
class PostUser(models.Model):
    post_id         = models.BigAutoField(primary_key=True)
    post_creater    = models.ForeignKey('CustomUser',on_delete=models.CASCADE)
    post_media      = models.FileField(upload_to="userpostimages")
    post_text       = models.TextField()
    post_created    = models.DateTimeField(default=now())
    post_comments   = models.IntegerField(max_length=20)
    post_reply      = models.IntegerField(max_length=20)
    
    
class PostComment(models.Model):
    comment_id      = models.BigAutoField(primary_key=True)
    comment_post            = models.ForeignKey('PostUser',on_delete=models.CASCADE)
    comment_profile         = models.ForeignKey('CustomUser',on_delete=models.CASCADE)
    comment_text            = models.TextField()
    comment_created         = models.DateTimeField(default=now())    

class PostLike(models.Model):
    like_id                 = models.BigAutoField(primary_key=True)
    like_post               = models.ForeignKey('PostUser',on_delete=models.CASCADE)
    like_profile            = models.ForeignKey('CustomUser',on_delete=models.CASCADE)
    like_created            = models.DateTimeField(default=now())



class AddFriend(models.Model):
    addfriend_id              = models.BigAutoField(primary_key=True)
    addfreind_sender          = models.ForeignKey("CustomUser",on_delete=models.CASCADE,related_name="sender")
    addfreind_reciever        = models.ForeignKey("CustomUser",on_delete=models.CASCADE,related_name="reciever")
    addfreind_status          = models.CharField(max_length=15)
    addfreind_created         = models.DateTimeField(default=now())
    addfreind_updated         = models.DateTimeField(default=now(),null=True)


class Blockuser(models.Model):
    blockuser_id            = models.AutoField(primary_key=True)
    blockuser_blocker       = models.ForeignKey("CustomUser",on_delete=models.CASCADE,related_name="blocker")
    blockuser_blocked       = models.ForeignKey("CustomUser",on_delete=models.CASCADE,related_name="blocked")
    blockuser_timestamp     = models.DateTimeField(default= now())
    blockuser_update        = models.DateTimeField(default=now())


class Group(models.Model):
    group_id            = models.BigAutoField(primary_key=True)
    group_name          = models.TextField()
    group_username      = models.CharField(max_length=40,unique=True)
    group_type          = models.CharField(max_length=20)
    group_creater       = models.ForeignKey('CustomUser',on_delete=models.CASCADE)
    group_back          = models.FileField(upload_to='group_icon')
    group_desc          = models.TextField(null=True)
    group_created       = models.DateTimeField(default=now())
    group_updated       = models.DateTimeField(default=now(),null=True)
    # for delete the file from storage
    def delete(self,using=None,keep_parents= False):
        self.group_back.storage.delete(self.group_back.name)
        super().delete()


class GroupMember(models.Model):
    gmember_id              = models.AutoField(primary_key=True)
    gmember_group           = models.ForeignKey("Group",on_delete=models.CASCADE)
    gmember_user            = models.ForeignKey("CustomUser",on_delete=models.CASCADE)
    gmember_isadmin         = models.BooleanField(default=0)
    # gmember_status          = models.
    gmember_created         = models.DateTimeField(default=now())
    gmember_updated         = models.DateTimeField(default=now())







# messenger chat models


class MchatTheme(models.Model):
    mchattheme_id           = models.AutoField(primary_key=True)
    mchattheme_name         = models.TextField(max_length=20)
    mchattehme_colors       = models.TextField()
    mchattehme_image        = models.FileField(upload_to="chat_theme",null=True)

class MChat(models.Model):
    mchat_id                = models.AutoField(primary_key=True)
    mchat_user1             = models.ForeignKey("CustomUser",on_delete=models.CASCADE,related_name="User1")
    mchat_user2             = models.ForeignKey("CustomUser",on_delete=models.CASCADE,related_name="User2")
    mchat_nickname_1        = models.TextField(max_length=50)
    mchat_nickname_2        = models.TextField(max_length=50)
    mchat_theme             = models.ForeignKey("MChatTheme" ,on_delete=models.CASCADE,default=1)


class MChatSms(models.Model):
    sms_id              = models.AutoField(primary_key=True)
    sms_parent          = models.ForeignKey("self",on_delete=models.DO_NOTHING,null=True)
    sms_text            = models.TextField(max_length=1000,null=True)
    sms_mchat           = models.ForeignKey("MChat",on_delete=models.CASCADE)
    sms_timestamp       = models.DateTimeField(default=now())
    

class MchatMedia(models.Model): 
    mchatmedia_id           = models.AutoField(primary_key=True)
    mchatmedia_sms          = models.ForeignKey("MChatSms",on_delete=models.CASCADE)
    mchatmedia_file         = models.FileField(upload_to='chat_media')



# model for multiple forigen key in table
# class just(models.Model):
#     sr              = models.AutoField(primary_key=True)
#     name    = models.TextField(max_length=50)
#     user1   = models.ForeignKey("CustomUser",on_delete=models.CASCADE,related_name="User1")
#     user2   = models.ForeignKey("CustomUser",on_delete=models.CASCADE,related_name="user2")
    # user1   = models.ForeignKey("CustomUser",on_delete=models.CASCADE)
    # user2   = models.ForeignKey("CustomUser",on_delete=models.CASCADE)

class MchatMedia(models.Model): 
    mchatmedia_id           = models.AutoField(primary_key=True)
    mchatmedia_sms          = models.ForeignKey("MChatSms",on_delete=models.CASCADE)
    mchatmedia_file         = models.FileField(upload_to='chat_media')










# class UserPanel(models.Model):
#     user_id             = models.BigAutoField(primary_key=True)
#     user_ref            = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
#     user_groups         = models.JSONField(default={"groups":[]})
#     user_friends        = 


# class Group(models.Model):
#     group_id            = models.BigAutoField(primary_key=True)
#     group_name          = models.TextField()
#     group_admin         = models.JSONField()
#     group_type          = models.CharField(max_length=20)
#     group_creater       = models.ForeignKey('CustomUser',on_delete=models.CASCADE)
#     group_back          = models.FileField(upload_to='group_icon')
#     group_desc          = models.TextField()
#     group_created       = models.DateTimeField(default=now())

#     # for delete the file from storage
#     def delete(self,using=None,keep_parents= False):
#         self.group_back.storage.delete(self.group_back.name)
#         super().delete()


class Page(models.Model):
    page_id             = models.BigAutoField(primary_key=True),
    page_name           = models.TextField()
    page_web            = models.URLField(max_length = 400,null=True)
    page_desc           = models.TextField(null=True)
    page_phone          = models.CharField(max_length = 30,null=True)
    page_email          = models.EmailField(max_length=150,null=True)
    page_profile        = models.ImageField(upload_to='page_profile',null=True)
    page_cover          = models.ImageField(upload_to='page_cover',null=True)
    page_creater        = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
    page_admin          = models.JSONField()
    page_time_stamp     = models.DateTimeField(default=now())
    page_like_count     = models.IntegerField(max_length=100)
    page_username       = models.CharField(unique=True,null=True,max_length=150)
    page_modified       = models.DateTimeField(default=now())
    
    def delete(self,using=None,keep_parents= False):
        self.page_profile.storage.delete(self.page_profile.name)
        self.page_cover.storage.delete(self.page_cover.name)
        super().delete()
    

class Story(models.Model):
    story_id            = models.BigAutoField(primary_key=True)
    story_user          = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
    story_type          = models.JSONField()
    story_text          = models.TextField(max_length=300)
    story_media         = models.FileField(upload_to='story_media',null=True)
    story_time_stamp    = models.DateTimeField(default=now())
    def delete(self,using=None,keep_parents= False):
        self.story_media.storage.delete(self.story_media.name)
        super().delete()

# Story.objects.filter(story_time_stamp__gte=Now()-timespan(minutes=1)).delete()
# Story.objects.filter(story_time_stamp__gte=Now()-timedelta(days=1)).delete()
# g = Story.objects.filter(story_id=2)
# MyModel.objects.filter(timestamp__gte=Now()-timespan(days=1))

class Feelings(models.Model):
    emoji_id            = models.AutoField(primary_key=True)
    emoji_type          = models.CharField(max_length=40)
    emoji_name          = models.CharField(max_length=30)
    emoji_emoji         = models.CharField(max_length=10)

class BackPost(models.Model):
    back_post_id        = models.AutoField(primary_key=True)
    back_post_img       = models.FileField(upload_to='post_back')


class Post(models.Model):
    post_id             = models.AutoField(primary_key=True)
    post_name           = models.TextField(max_length=300,null=True)
    post_text           = models.TextField(null=True)
    post_creater        = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
    post_backgound      = models.ForeignKey("BackPost", on_delete=models.SET_NULL,null=True)
    post_feelings       = models.ForeignKey("Feelings", on_delete=models.SET_NULL,null=True)
    post_gif            = models.URLField(max_length=400,null=True)
    post_tag_user       = models.JSONField(null=True)
    post_time_stamp     = models.DateTimeField(default=now())
    

class PostMedia(models.Model):
    post_media_id       = models.AutoField(primary_key=True)
    post_media_post     = models.ForeignKey("Post", on_delete=models.CASCADE)
    post_media_media    = models.FileField(upload_to='post_media')
    

# class wesy(models.Model):
#     id = models.AutoField(primary_key=True)
#     text = models.TextField()




