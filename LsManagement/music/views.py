from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Album ,SongTypes, User
import cgi
import operator

# Create your views here.
def index(request):
	all_albums = Album.objects.all()
	#all_albums = Album.objects.raw('select * from music_album')
	#cursor.execute("select * from ls_hero_testride_enquiry")
	context = {
		'all_albums' : all_albums,
	}
	return render(request,'music/index.html',context)

def addAlbum(request):
	context = {
		'text' : 'Add Music Album',
	}
	return render(request,'music/addAlbum.html',context)

def signUp(request):
	context = {
		'text' : 'Add Music Album',
	}
	return render(request,'login/index.html',context)

def signIn(request):
	context = {
		'text' : 'Add Music Album',
	}
	return render(request,'login/signIn.html',context)



def registerUsers(request):

	# form = cgi.FieldStorage()
	# artist =  form.getvalue('artist')
	user = User()
	formValue = request.POST
	user.userName = formValue.get('userName').strip()
	user.mobile = formValue.get('mobile').strip()
	user.email = formValue.get('email').strip()
	user.city = formValue.get('city').strip()
	user.state = formValue.get('state').strip()
	user.address = formValue.get('address').strip()
	user.password = formValue.get('password').strip()
	if user.userName and user.mobile and user.email and user.city:
		user.save()
	else:
		return HttpResponse("Please fill all the fields")
	
	#return HttpResponse("Data saved successfully.")
	context = {
		'text' : 'Data saved successfully.',
	}
	return render(request,'login/signIn.html',context)
	#return render(request,'music/addAlbum.html',context)


def addMusicAlbum(request):

	# form = cgi.FieldStorage()
	# artist =  form.getvalue('artist')
	album = Album()
	formValue = request.POST

	album.artist = formValue.get('artist').strip()
	album.album_title = formValue.get('title').strip()
	album.genre = formValue.get('genre').strip()
	album.album_logo = formValue.get('logo').strip()
	if album.artist and album.album_title and album.genre and album.album_logo:
		album.save()
	else:
		return HttpResponse("Please fill all the fields")
	
	return HttpResponse("Data saved successfully.")
	#return render(request,'music/addAlbum.html',context)


def detail(request,album_id):
	try:
		album = Album.objects.get(pk=album_id)
		all_types = SongTypes.objects.all()
		#return HttpResponse(all_types)
	except:
		raise Http404("Album does not exist")
	return render(request,'music/detail.html',{'album': album, 'all_types' : all_types})


def showForm(request):
	try:
		data="hello world"
		name="Prakash Sahu"
		return render(request,'music/showForm.html',{'text':data, 'name':name})
	except:
		raise Http404("page does not exist")


def showCount(request):
	try:
		textval = request.GET['textarea']
		wordList = textval.split();
		length = len(wordList)
		print(wordList)
		worddict = {}
		for word in wordList:
			if word in worddict:
				worddict[word] += 1
			else:
				worddict[word] = 1
		sorted_list = sorted(worddict.items(), key = operator.itemgetter(1), reverse=True)
		#reverse is used to make asc or desc order
		#sorted function is used to sort the dictionary
		return render(request,'music/showDetail.html',{'text':textval, 'worddict':sorted_list, 'length':length})
		
	except:
		raise Http404("Album does not exist")