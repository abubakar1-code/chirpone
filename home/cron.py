# from .models import wesy , Feelings
# from random import randint
# from apscheduler.schedulers.background import BackgroundScheduler



# scheduler = BackgroundScheduler()













# def cron_def():
#     # text = str(randint(1111, 9999))
#     obj = wesy.objects.create(text="some text")
#     obj.save()
#     print("acha g chal raha hy ye function")

    
# def emoji_cron():
#     obj = Feelings.objects.create(emoji_emoji="❤️",emoji_name="kuch bhi",emoji_type="kuch bi")
#     obj.save()


# def hi():
#     print('hy i ma here')
#     wesy.objects.create(text="some text")


# from django_cron import CronJobBase, Schedule

# class MyCronJob(CronJobBase):
#     RUN_EVERY_MINS = 2 # every 2 hours

#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     schedule.add_job(print("hello world"))
#     code = 'home.MyCronJob'    # a unique code

#     def do(self):
#         # pass    # do your thing here
#         obj = Feelings.objects.create(emoji_emoji="❤️",emoji_name="kuch bhi",emoji_type="kuch bi")
#         obj.save()