from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.core.mail import send_mail
from .models import Publication
from news.models import Post
from team.models import Member, Former_member

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def skills(request):
    return render(request, 'skills.html', {})

def publications(request):
    queryset = Publication.objects.all()[::-1]
    paginator = Paginator(queryset, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
       paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages) 

    context = {
        # 'object_list': queryset,
        'queryset': paginated_queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'publications.html', context)

def news(request):
    object_list = Post.objects.all()[::-1]
    paginator = Paginator(object_list, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
       paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages) 

    context = {
        # 'object_list': queryset,
        'object_list': paginated_queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'news.html', context)

def booking(request):
    return render(request, 'booking-system.html', {})

def team(request):
    members_list = Member.objects.all()
    former_members_list = Former_member.objects.all()

    context = {
        'member_list': members_list,
        'former_member_list': former_members_list,
    }

    return render(request, 'team.html', context)

def research(request):
    return render(request, 'research.html', {})

def contact(request):
    if request.method == "POST":
        subject = request.POST['user_subject']
        email = request.POST['user_email']    
        message = request.POST['user_message']
        name = request.POST["user_name"]

        send_mail(
            subject,
            f'Email sent via website \nMessage from: {name} \n' + message,
            email,
            ['elber.risouza@gmail.com'],
           
        )

        return render(request, 'contact.html', {'name' : name})   
    else:
        return render(request, 'contact.html', {})
    
from django.shortcuts import render