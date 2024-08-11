from django.contrib import admin
from .models import Client, Service, Testimonial, ContactMessage, TeamMember, Project, Faq
# Register your models here.

admin.site.register(Project)
admin.site.register(Service)
admin.site.register(TeamMember)
admin.site.register(Client)
admin.site.register(Testimonial)
admin.site.register(ContactMessage)
admin.site.register(Faq)