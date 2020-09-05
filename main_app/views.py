from django.shortcuts import render, redirect
from .models import Dog, Toy, Photo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'dogcollector2'


# View Functions

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    toys_dog_doesnt_have = Toy.objects.exclude(id__in=dog.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'dogs/detail.html', {
        'dog': dog,
        'feeding_form': feeding_form,
        'toys': toys_dog_doesnt_have
    })

def add_photo(request, dog_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, dog_id=dog_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', dog_id=dog_id)

# Class-Based Views

class DogCreate(CreateView):
    model = Dog
    fields = ['name', 'breed', 'description', 'age']

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'

class ToyList(ListView):
    model = Toy

class ToyDetailView(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = '__all__'

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'
    
def add_feeding(request, dog_id):
    form = FeedingForm(request.POST)

    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.dog_id = dog_id
        new_feeding.save()

    return redirect('detail', dog_id=dog_id)

def assoc_toy(request, dog_id, toy_id):
    Dog.objects.get(id=dog_id).toys.add(toy_id)
    return redirect('detail', dog_id=dog_id)

def remove_toy(request, dog_id, toy_id):
    Dog.objects.get(id=dog_id).toys.remove(toy_id)
    return redirect('detail', dog_id=dog_id)
    