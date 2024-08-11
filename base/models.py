from django.db import models
from django.utils import timezone

class Client(models.Model):
    image = models.ImageField(upload_to='clients')
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="clients")
    
    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=100)
    headline = models.CharField(max_length=500)
    description = models.JSONField()
    key_features = models.JSONField()
    features = models.JSONField()
    image = models.ImageField(upload_to='services')

    @property
    def slug_url(self):
        self.url = ""
        for char in self.title:
            if char == " " or char == "/":
                char = "-"
            self.url += char
        return self.url.lower()

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    message = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.client.name
    
class ContactMessage(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    message = models.TextField(max_length=50)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f" {self.firstname} {self.lastname}"
    
class TeamMember(models.Model):
    name = models.CharField(max_length=50)
    works_as = models.CharField(max_length=50)
    image = models.ImageField(upload_to='team', default='team/defualt.png')
    facebook_link = models.CharField(null=True, blank=True, max_length=500)
    instagram_link = models.CharField(null=True, blank=True, max_length=500)
    whatsapp_link = models.CharField(null=True, blank=True, max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=50)
    about_client = models.CharField(max_length=500)
    description = models.JSONField()
    problem = models.JSONField()
    solution = models.JSONField()
    challenges = models.JSONField()
    technologies = models.JSONField(default=list)
    services = models.ManyToManyField(Service)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='projects', default='projects/defualt.png')
    date_posted = models.DateTimeField(default=timezone.now)
    
    @property
    def slug_url(self):
        self.url = ""
        for char in self.title:
            if char == " ":
                char = "-"
            self.url += char
        return self.url.lower()
    
    def __str__(self):
        return self.title
    
class Faq(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField(max_length=2000)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question

    
    