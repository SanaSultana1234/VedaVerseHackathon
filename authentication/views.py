from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as loginUser, logout as logoutUser
from hackathon2 import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str as force_text
from . tokens import generate_token

# Create your views here.
def home(request):
    return render(request, "authentication/home.html")


def register(request):
    if request.method=="POST":
        username = request.POST['username']
        fname = request.POST['fname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        address = request.POST['address']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists! Please try with another one.")
            return redirect("home")
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered")
            return redirect("home")
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 characters")
            return redirect("home")

        if pass1!=pass2:
            messages.error(request, "Passwords did not match")
            return redirect("home")
        
        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric")
            return redirect("home")

        myuser = User.objects.create_user(username, email, password=pass1)
        myuser.first_name=fname

        myuser.is_active = False

        myuser.save()

        messages.success(request, "Your account has been successfully created.\nWe have sent you a confirmation email. Please confirm it in order to Activate your account.")

        subject = "Welcome to LEARNIVERSE!"
        message = "Hello" + myuser.first_name + "!\nAt LEARNIVERSE - You can LEARN anything!✨✨✨\n\nOur vision is to revolutionize education by using Virtual Reality (VR)👽and Augmented Reality (AR)👾 to create engaging and immersive learning experiences that are accessible to all children.\n\nThrough AR, students can input voice commands or text to visualize 3D models, aiding comprehension of abstract or complex subjects, while VR provides immersive simulations to explore intricate topics, offering an engaging alternative to traditional methods.\n\nThe platform also features gamified assessments to reinforce knowledge retention through interactive quizzes, thereby making learning more accessible and enjoyable for all learners, including those with special needs.🤩\n\n"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        current_site = get_current_site(request)
        email_subject = "Confirm your email @ LEARNIVERSE!"
        message2 = render_to_string('email_confirmation.html', {
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject, 
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()
        return redirect('login')

    return render(request, "authentication/register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        print(f"Username: {username}, Password: {pass1}")

        user = authenticate(request, username=username, password=pass1)
        print(user)
        if user is not None: 
            loginUser(request, user)
            fname = user.first_name
            return render(request, "authentication/learn.html", {'fname': fname})
        else:
            messages.error(request, "Bad credentials")
            return redirect("home")
    return render(request, "authentication/login.html")

def learn(request):
    return render(request, "authentication/learn.html")
     
def game(request):
    return render(request, "authentication/index.html")

def about(request):
    return render(request, "authentication/about.html")



def logout(request):
    logoutUser(request)
    messages.success(request, "Logged out Successfully")
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid=force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser=None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active=True
        myuser.save()
        loginUser(request, myuser)
        fname = myuser.first_name
        return render(request, "authentication/learn.html", {'fname': fname})
    else:
        return render(request, 'activation_failed.html')