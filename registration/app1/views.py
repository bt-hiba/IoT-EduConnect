from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import VideosForm  , CoursesForm , ProjectsForm , UserCreationForm , QuizLevelForm , QuestionsForm , ContactForm
from .models import Videos , Comment , Courses , Projects , QuizLevel , Questions , Contact

# Create your views here.

@login_required(login_url='login') # bach doz lay page akhra khasssek login first 
def HomePage(request):
    if request.method == 'POST':
        foorm = UserCreationForm(request.POST, instance=request.user)
        if foorm.is_valid():
            foorm.save()
            # Redirigez l'utilisateur vers la page de profil après la mise à jour réussie.
            return redirect('home')
    else:
        foorm = UserCreationForm(instance=request.user)
    return render(request, 'home.html', {'foorm': foorm})

@login_required(login_url='login') 
def AdminPage(request):
    user = request.user 
    total_courses = Courses.objects.count()
    total_videos = Videos.objects.count()
    total_projects = Projects.objects.count()
    total_levels = QuizLevel.objects.count()
    users = User.objects.all()
    return render(request, "admin.html", {'user': user, "users": users,'total_courses': total_courses, 'total_videos': total_videos, 'total_projects': total_projects, 'total_levels': total_levels})

def AdCoursesPage(request):
    user = request.user 
    total_courses = Courses.objects.count()
    total_videos = Videos.objects.count()
    total_projects = Projects.objects.count()
    total_levels = QuizLevel.objects.count()
    imgg = Courses.objects.all()
    return render(request, "admin_courses.html", {'user': user,"imgg": imgg, 'total_courses': total_courses, 'total_videos': total_videos, 'total_projects': total_projects, 'total_levels': total_levels})

def AdVideosPage(request):
    user = request.user 
    total_courses = Courses.objects.count()
    total_videos = Videos.objects.count()
    total_projects = Projects.objects.count()
    total_levels = QuizLevel.objects.count()
    img = Videos.objects.all()
    return render(request, "admin_videos.html", {'user': user,"img": img,'total_courses': total_courses, 'total_videos': total_videos, 'total_projects': total_projects, 'total_levels': total_levels})

def AdProjectsPage(request):
    user = request.user 
    total_courses = Courses.objects.count()
    total_videos = Videos.objects.count()
    total_projects = Projects.objects.count()
    total_levels = QuizLevel.objects.count()
    imggg=Projects.objects.all()
    return render(request, "admin_projects.html", { 'user': user,"imggg": imggg, 'total_courses': total_courses, 'total_videos': total_videos, 'total_projects': total_projects, 'total_levels': total_levels})

def AdQuizesPage(request):
    user = request.user 
    total_courses = Courses.objects.count()
    total_videos = Videos.objects.count()
    total_projects = Projects.objects.count()
    total_levels = QuizLevel.objects.count()
    imgggg=QuizLevel.objects.all()
    return render(request,'admin_quizes.html', {'user': user,"imgggg": imgggg,'total_courses': total_courses, 'total_videos': total_videos, 'total_projects': total_projects, 'total_levels': total_levels})

def AdQuestionsPage(request):
    user = request.user 
    total_courses = Courses.objects.count()
    total_videos = Videos.objects.count()
    total_projects = Projects.objects.count()
    total_levels = QuizLevel.objects.count()
    im=Questions.objects.all()
    return render(request,'admin_questions.html', {'user': user,"im": im,'total_courses': total_courses, 'total_videos': total_videos, 'total_projects': total_projects, 'total_levels' : total_levels })



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
                return redirect('admin')
            else:
                return redirect('courses')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('admin')
 

@login_required(login_url='login')
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
 
 
def delete_cours(request, courses_id):
    cours = get_object_or_404(Courses, pk=courses_id)
    cours.delete()
    return redirect('admin_courses')


def EditCoursPage(request, course_id):
    course = get_object_or_404(Courses, id=course_id)
    if request.method == 'POST':
        form = CoursesForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('admin_courses')  
    else:
        form = CoursesForm(instance=course)
    return render(request, 'admin_editcrs.html', {'form': form})
 
 
def ReadPage(request, courses_id):
    cours = get_object_or_404(Courses, pk=courses_id)
    return render(request, 'read_cours.html', {'cours': cours})
 
@login_required(login_url='login')   
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
   
def delete_video(request, videos_id):
    video = get_object_or_404(Videos, pk=videos_id)
    video.delete()
    return redirect('admin_videos')

def EditVideoPage(request, video_id):
    video = get_object_or_404(Videos, id=video_id)
    if request.method == 'POST':
        forrm = VideosForm(request.POST, instance=video)
        if forrm.is_valid():
            forrm.save()
            return redirect('admin_videos')  
    else:
        forrm = VideosForm(instance=video)
    return render(request, 'admin_editvds.html', {'forrm': forrm})
 
 
  
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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})

def HeaderPage(request):
    user = request.user
    return render (request,'header.html',{'user': user})

@login_required(login_url='login')
def ProjectsPage(request):
    imggg=Projects.objects.all()
    return render(request,"projects.html",{"imggg":imggg})


def Add_ProjectsPage(request):
     if request.method == "POST":
       forrrm=ProjectsForm(data=request.POST,files=request.FILES)
       if forrrm.is_valid():
          forrrm.save()
          objjj=forrrm.instance
          return render(request,"add_projects.html",{"objjj":objjj})
     else:
       forrrm=ProjectsForm()
     imggg=Projects.objects.all()
     return render(request,"add_projects.html",{"imggg":imggg,"forrrm":forrrm})
 
def delete_project(request, projects_id):
    project = get_object_or_404(Projects, pk=projects_id)
    project.delete()
    return redirect('admin_projects')
  
def EditProjectPage(request, project_id):
    project = get_object_or_404(Projects, id=project_id)
    if request.method == 'POST':
        forrrm = ProjectsForm(request.POST, instance=project)
        if forrrm.is_valid():
            forrrm.save()
            return redirect('admin_projects')  
    else:
        forrrm = ProjectsForm(instance=project)
    return render(request, 'admin_editpjs.html', {'forrrm': forrrm})
 
 
@login_required(login_url='login')
def QuizPage(request):
    return render (request,'quiz.html')

def SearchBar(request):
    courses = Courses.objects.all()  
    if request.method == "POST":
        searched = request.POST.get('searched')
        if searched:
            courses = Courses.objects.filter(title__icontains=searched)
            return render(request, 'search_bar.html', {"searched": searched, "courses": courses})
    return render(request, 'search_bar.html', {"courses": courses})  


def quiz(request):
    questions = Questions.objects.all()
    score = None

    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            score = form.calculate_score()
    else:
        form = QuizForm(questions=questions)

    return render(request, 'quiz.html', {'form': form, 'score': score})


def start_quiz(request, level_name):
    # Récupérer le niveau de quiz correspondant
    level = QuizLevel.objects.get(level_name=level_name)

    # Récupérer les questions associées à ce niveau de quiz
    questions = Questions.objects.filter(level=level)

    return render(request, 'start_quiz.html', {'level': level, 'questions': questions})

def LevelPage(request):
    imggggg=QuizLevel.objects.all()
    return render(request,"all_quiz.html",{"imggggg":imggggg})

def Add_LevelPage(request):
     if request.method == "POST":
       forrrrrm=QuizLevelForm(data=request.POST,files=request.FILES)
       if forrrrrm.is_valid():
          forrrrrm.save()
          objjjjj=forrrrrm.instance
          return render(request,"add_level.html",{"objjjjj":objjjjj})
     else:
       forrrrrm=QuizLevelForm ()
     imggggg=QuizLevel.objects.all()
     return render(request,"add_level.html",{"imggggg":imggggg,"forrrrrm":forrrrrm})
 
def delete_level(request, levels_id):
    level = get_object_or_404(QuizLevel, pk=levels_id)
    level.delete()
    return redirect('admin_quizes')

def EditLevelPage(request, level_id):
    level = get_object_or_404(QuizLevel, id=level_id)
    if request.method == 'POST':
        forrrmm = QuizLevelForm(request.POST, instance=level)
        if forrrmm.is_valid():
            forrrmm.save()
            return redirect('admin_quizes')  
    else:
        forrrmm = QuizLevelForm(instance=level)
    return render(request, 'admin_editquiz.html', {'forrrmm': forrrmm})


def SearchVd(request):
    videos = Videos.objects.all()  
    if request.method == "POST":
        searchedd = request.POST.get('searchedd')
        if searchedd:
            videos = Videos.objects.filter(title__icontains=searchedd)
            return render(request, 'search_vd.html', {"searchedd": searchedd, "videos": videos})
    return render(request, 'search_vd.html', {"videos": videos})  


def SearchProject(request):
    projects = Projects.objects.all()  
    if request.method == "POST":
        searcheddd = request.POST.get('searcheddd')
        if searcheddd:
            projects = Projects.objects.filter(title__icontains=searcheddd)
            return render(request, 'search_project.html', {"searched": searcheddd, "projects": projects})
    return render(request, 'search_project.html', {"projects": projects})  

def AddQuizPage(request):
     if request.method == "POST":
       forrrrm=QuestionsForm(data=request.POST,files=request.FILES)
       if forrrrm.is_valid():
          forrrrm.save()
          objjjj=forrrrm.instance
          return render(request,"add_quiz.html",{"objjjj":objjjj})
     else:
       forrrrm=QuestionsForm()
     imgggg=Questions.objects.all()
     return render(request,"add_quiz.html",{"imgggg":imgggg,"forrrrm":forrrrm})

def LogoutPage(request):
    logout(request)
    return redirect('index')

