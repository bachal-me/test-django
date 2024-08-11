from django.shortcuts import render, redirect
from .models import Service, Testimonial, ContactMessage, TeamMember, Project, Faq, Client
# Create your views here.

def home(request):
    testimonials = Testimonial.objects.all()
    projects = Project.objects.all()
    services = Service.objects.all()
    clients = Client.objects.all()
    faqs = Faq.objects.all()
    members = TeamMember.objects.all()
    context = {"clients":clients, "testimonials":testimonials, "services":services, "projects":projects, "members":members, "faqs":faqs}
    return render(request, 'base/index.html', context)

def template(request):
    services = Service.objects.all()
    return render(request, 'base/base.html', context={"services":services})

def projects(request): 
    projects = Project.objects.all()
    return render(request, 'base/case_studies.html', context={'projects':projects})

def caseStudy(request, title):
    case_study = Project.objects.all()
    project = ""
    for item in case_study:
        if item.slug_url == title:
            project = item
            break
    return render(request, 'base/case_study_view.html', context={"project":project})


def testimonials(request):
    testimonials = Testimonial.objects.all()
    context = {"testimonials":testimonials}
    return render(request, 'base/testimonials.html', context)

def services(request, service):
    services = Service.objects.all()
    projects = Project.objects.all()
    service_data = ""
    for item in services:
        if item.slug_url == service:
            service_data = item
            break
    context = {"service":service_data, 'projects':projects}
    return render(request, 'base/services.html', context)

def contact(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        region = request.POST.get("region")
        company = request.POST.get("company")
        message = request.POST.get("message")

        contact_data = ContactMessage.objects.create(firstname=firstname, lastname=lastname, email=email, phone=phone, region=region, company=company, message=message)
        contact_data.save()
        return redirect('contact')

    return render(request, 'base/contact.html')