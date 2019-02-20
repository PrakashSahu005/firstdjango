from django.db import models

# Create your models here.
class Album(models.Model):
	artist = models.CharField(max_length=250)
	album_title = models.CharField(max_length=500)
	genre = models.CharField(max_length=100)
	album_logo = models.CharField(max_length=1000)

class User(models.Model):
	userName = models.CharField(max_length=100)
	mobile = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	address = models.CharField(max_length=500)
	password = models.CharField(max_length=200)
	status = models.CharField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)


class SongTypes(models.Model):
	song_type = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	is_favorite = models.BooleanField(default=False)
	class Meta:
		db_table = "song_types"

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete = models.CASCADE)
	typeId = models.ForeignKey(SongTypes, on_delete = models.CASCADE)
	file_type = models.CharField(max_length=10)
	song_title = models.CharField(max_length=250)