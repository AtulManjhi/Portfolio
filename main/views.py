from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    name = 'Atul Kumar Manjhi'
    occup = 'Student'
    addr = 'Kadma, Khunti, Jharkhand - 835210'
    email = 'atulmanjhi05@gmail.com'
    about_me = """ 
    I am pursuing my master\'s degree in Computer Application from Birla Institute of Technology, Mesra. I\'m a Computer Application graduate from St. Xavier\'s College, Ranchi and I enjoy the challenge of working with different types of people and coming up with solutions to difficult problems.
    """
    context = {
        "Name": name,
        "Occup": occup,
        "Address": addr,
        "Email": email,
        "About_Me": about_me,
    }
    
    if request.method == 'POST':
        senders_name = request.POST.get('senders_name')
        senders_email = request.POST.get('senders_email')
        subject = request.POST.get('subject')
        message = request.POST.get('content')
        message_to_be_sent = '''
        Hello Atul,
        {} sent you a message from your Portfolio website.
        
        Name: {}
        Email: {}
        Subject: {}

        Message: {}
        '''.format(senders_name,senders_name,senders_email,subject,message)
       # send_mail("New message from Portfolio.",
       # message_to_be_sent,
       # settings.EMAIL_HOST_USER,
       # ['atulmanjhi05@gmail.com'],
       # fail_silently=False,
       # auth_user=settings.EMAIL_HOST_USER,
       # auth_password='India@Cric123')

        try:
            send_mail("New message form Portfolio.",
            message,
            settings.EMAIL_HOST_USER,
            ['atulmanjhi05@gmail.com'],
            fail_silently=False)
            return render(request,'main/thanks.html')
        except:
            return render(request, 'main/error.html')

    return render(request, 'main/index.html', context)
