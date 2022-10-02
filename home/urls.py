from django.urls import path , include
from . import views


urlpatterns = [
    path('index/',views.index),


    
    # group

    path('group/',views.group_api),
    path('group/<int:id>',views.group_api_id),
    path('group/all/',views.group_all_api),
    path('group/create/',views.group_create_api),
    path('group/update/<int:id>',views.group_update_id),


    # group share
    path('group/share/<int:id>',views.group_share),

    # feeelings

    path('feelings/all/',views.feelings_all_api),
    path('admin/feelings/create/',views.feelings_create_api),

    # post background

    path('backpost/all/',views.backpost_all_api),
    path('admin/backpost/create/',views.backpost_create_api),

    # post

    path('post/all/',views.post_api),


    # page
    path('page/all/',views.page_api),
    path('page/post/',views.page_api),
    path('page/update/<str:id>',views.page_api_id),
    path('page/delete/<str:id>',views.page_api_id),
    path('page/get/<str:id>',views.page_api_id),
    

    # story
    path('story/all/',views.story_api),
    path('story/post/',views.story_api),

    path('paginat/',views.paginat.as_view()),
    
    
    
# all workable apis are here

    # registrationn
    path('signup/',views.signup),
    path('otp/',views.otp),
    path('forgetpass/',views.forget_pass),
    path('forgetotp/',views.forget_otp),
    path('signin/',views.sign_in),
    
    # postuser
    path('post/allposts/',views.postuser_add),
    path('post/update/<int:id>',views.postuser_id),
    path('post/comments/all/',views.postcomment_view),
    path('post/like/all/',views.postlike_view),
    path('post/postview/',views.postuser_view),
    
    path('post/comments/<int:id>/',views.postcomment_view_id),
    
    path('post/likes/<int:id>/',views.postcomment_view_id),
    
    # profile
    path("profile/all/",views.profile_view),
    path("profile/get/<int:id>/",views.profile_view_id),
    path("profile/update/<int:id>/",views.profile_update_view),    
    
    # addfriend 
    path("friendlist/all/",views.friendlist_view),
    path("friendlist/sent/",views.addfriend_view),
    path("friendlist/accept/<int:id>",views.accept_request_view),
    path("friendlist/unfriend/<int:id>",views.friend_unfriend_view),
    
    
    # block user
    
    path("block/blockuser/",views.blockuser_view),
    path("block/unblock/<int:id>/",views.block_unblock_view),
    
    # group
    path("group/allgroups/",views.group_all_view),
    path("group/addgroup/",views.group_add_view),
    path("group/putgroup/<int:id>/",views.group_put_view),
    path("group/member/all/<int:id>/",views.group_members_all_view),
    path("group/members/<str:username>/",views.group_members_with_group_view),
    path("group/member/join/",views.group_member_join_view),


    # messenger 
    path("messenger/sms/all/",views.messenger_sms_view),
    path("messenger/sms/delete/<int:id>/",views.messenger_sms_delete_view),
]   