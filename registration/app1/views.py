from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import VideosForm  , CoursesForm
from .models import Videos , Comment , Courses

# Create your views here.

@login_required(login_url='login') # bach doz lay page akhra khasssek login first 
def HomePage(request):
   return render (request,'home.html')

@login_required(login_url='login') 
def AdminPage(request):
    return render(request, 'admin.html')


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)

        if user is not None:
            login(request,user)
            if user.is_staff:
                # Rediriger l'administrateur vers la page admin
                return redirect('admin')
            else:
                # Rediriger l'utilisateur ordinaire vers la page home
                return redirect('courses')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def CoursesPage(request):
     imgg=Courses.objects.all()
     return render(request,"courses.html",{"imgg":imgg})

def Add_CoursesPage(request):
     if request.method == "POST":
       forrm=CoursesForm(data=request.POST,files=request.FILES)
       if forrm.is_valid():
          forrm.save()
          objj=forrm.instance
          return render(request,"add_courses.html",{"objj":objj})
     else:
       forrm=CoursesForm()
     imgg=Courses.objects.all()
     return render(request,"add_courses.html",{"imgg":imgg,"forrm":forrm})
 
def ReadPage(request, courses_id):
    cours = get_object_or_404(Courses, pk=courses_id)
    print(cours.pdf.url)
    return render(request, 'read_cours.html', {'cours': cours})
    
def VideosPage(request):
    img=Videos.objects.all()
    return render(request,"videos.html",{"img":img})
    


def Add_videoPage(request):
    if request.method == "POST":
       form=VideosForm(data=request.POST,files=request.FILES)
       if form.is_valid():
          form.save()
          obj=form.instance
          return render(request,"add_video.html",{"obj":obj})
    else:
       form=VideosForm()
    img=Videos.objects.all()
    return render(request,"add_video.html",{"img":img,"form":form})
   
   
def WatchPage(request, videos_id):
    video = get_object_or_404(Videos, pk=videos_id)
    comments = video.comments.all()
    return render(request, 'watch_video.html', {'video': video, 'comments': comments})

def add_comment(request, videos_id):
    video = get_object_or_404(Videos, pk=videos_id)
    if request.method == 'POST':
        user_name = request.POST['user_name']
        text = request.POST['text']
        Comment.objects.create(video=video, user_name=user_name, text=text)
        return redirect('watch', videos_id=videos_id)  
    return redirect('watch', videos_id=videos_id) 


def IndexPage(request):
    return render (request,'index.html')

def ProjectsPage(request):
    return render (request,'projects.html')

def QuizPage(request):
    return render (request,'quiz.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

