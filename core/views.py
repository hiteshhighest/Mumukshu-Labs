from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        user_email = request.POST.get('email')
        interests = request.POST.get('interests')

        subject = f"🚀 Mumukshu Labs Join Request: {full_name}"
        body = f"New Join Request!\n\nName: {full_name}\nEmail: {user_email}\nInterests: {interests}"

        try:
            send_mail(
                subject=subject,
                message=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.NOTIFICATION_EMAIL],
                fail_silently=False,
            )
            messages.success(request, "Application sent! Welcome to Mumukshu Labs.")
        except Exception as e:
            messages.error(request, f"Submission error: {e}")

        return redirect('home')

    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_message = request.POST.get('message')

        subject = f"💬 Contact Message from {name}"
        body = f"New message from Mumukshu Labs website:\n\nName: {name}\nEmail: {user_email}\nMessage:\n{user_message}"

        try:
            send_mail(
                subject=subject,
                message=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.NOTIFICATION_EMAIL],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent!")
        except Exception as e:
            messages.error(request, f"Error sending message: {e}")

        return redirect('contact')

    return render(request, 'core/contact.html')