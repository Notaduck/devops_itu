from django.db import models

class User(models.Model):
	user_id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=50)
	email = models.EmailField()
	pw_hash = models.CharField(max_length=100)

class Follower(models.Model):
	who =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_who')
	whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_whom')

class Message(models.Model):
	message_id = models.AutoField(primary_key=True)
	author_id = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.CharField(max_length=280)
	pub_date = models.DateField(auto_now_add=True)
	flagged = models.IntegerField(null=True)




