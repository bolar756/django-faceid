from django.shortcuts import render, redirect
from .models import ProgrammingQuestion
from django.http import HttpResponseBadRequest,HttpResponse
from .models import ProgrammingQuestion  # Assuming your model is in the same app
from django.contrib.auth.decorators import login_required
import csv
import random
# Create your views here.

def home(request):
    if request.user.is_authenticated:
       return render(request, 'exam.html')
    else:
        return render(request, 'index.html')

@login_required(login_url='login')    
def exam(request):
        return HttpResponseBadRequest('Method Not Allowed: Only POST requests accepted')

@login_required(login_url='login')    
def programming(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('Method Not Allowed: Only POST requests accepted')
    if not request.FILES:
        return render(request, 'upload_form.html', {'error': 'No file uploaded'})
    csv_file = request.FILES['csv_file']
    if not csv_file.name.endswith('.csv'):
        return HttpResponseBadRequest('Invalid file format: Only CSV files allowed')
    try:
        question_objects = []
        reader = csv.reader(csv_file.read().decode('utf-8').splitlines(), delimiter=',')
        next(reader, None)  # Skip header row
        for row in reader:
            if len(row) != 4:  # Check for expected number of columns
                raise ValueError('Invalid CSV format: Row must have 4 columns (question, answer, difficulty, tags)')
            question_objects.append(ProgrammingQuestion(
                question_text=row[0],
                answer_text=row[1],
                difficulty_level=row[2] if row[2] else 'hard',  # Default difficulty if not provided
                tags=row[3] if row[3] else '',  # Empty string for blank tags
            ))
        ProgrammingQuestion.objects.bulk_create(question_objects)
        return redirect('home')  # Redirect to success page
    except (csv.Error, ValueError) as e:
        return HttpResponseBadRequest(f'Error processing CSV: {e}')

@login_required(login_url='login')    
def rex(request):
    return render(request, 'upload.html')

@login_required(login_url='login')    
def  Exam_setter(request):
    if request.method =="POST":
         mathematics = request.POST['Mathematics']
         biology = request.POST['biology']
         English = request.POST['english']
         Programing = request.POST['programming']
         ceer =ProgrammingQuestion.objects.all()
         context={
             'science':ceer,
             'biology':biology,
             'english':English,
             "program":Programing,
             'math':mathematics,
         }
    return  render(request,'exams.html',context )