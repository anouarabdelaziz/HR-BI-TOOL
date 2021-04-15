from django.shortcuts import render
import os, fitz
from django.shortcuts import render, redirect
from .models import *

from .forms import RecruitForm, ApplyFrom,  skillsFrom
from .rect import evaluate
from django.core.files.storage import FileSystemStorage

import numpy as np
def home(request):  
    
    applies = Apply.objects.all()
    data_date = []
    
    for applie in applies:
         data_date.append( applie.date_created)
    data_date = str(data_date)
    data_date = [2019, 2020, 2019, 2020,2019, 2021]
    cnt = ['django', 'pyhton', 'javascripts', 'html', 'machine learning', 'optimization', 'supply chain']
    context = {'cnt' : cnt, 'data_date' : data_date}    
    return render(request, 'home.html', context)

def consult(request):  
    dirs = 'media/media/pdfs'
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base_dir, dirs)
    d = [f for f in os.listdir(f"{path}")]
    sample = []
    for name in d:
        doc = fitz.open(f'{base_dir}/{dirs}/{name}')
        text = ''
        for page in doc:
            text = text + str(page.getText())
        tx = " ".join(text.split('\n'))
        sample.append(tx.lower())

    skills_ = Recruit.objects.get(name='data scientist')
    liste_ = skills_.comp_set.all()
    my_values = [item.name for item in liste_]
    val = [item.importance for item in liste_]
    rank = evaluate(sample, my_values)

    weights = [0.8, 0.6, 0.4, 0.3]
    gscores = []
    for item, val in rank.items():
        scores = []
        for key in val:
            scores.append(val[key])
        j = 0
        for i in range(len(weights)):
            j+= scores[i]*weights[i]

        gscores.append(j)

    applies = Apply.objects.all()
    j = []
    for applie in applies:
        j.append(applie.experience) 
    for i in range(len(j)):
        gscores[i] = gscores[i] + (int(j[i])/10)
    gscores  = np.array(gscores)
    cnt = ['django', 'pyhton', 'javascripts', 'html', 'machine learning', 'optimization', 'supply chain']
    context = {'cnt' : cnt, 'applies' : applies}
    return render(request, 'es.html', context)

def submit(request):
    if request.method == 'POST':
        form = ApplyFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('submit')
    else:
        form = ApplyFrom()
        
    return render(request, 'submit.html', {'form':form})

def recruit(request):
    
    jobs = Recruit.objects.all()

    if request.method =='POST':
        form = RecruitForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/')
    else:
        form = RecruitForm()
    context = {'form' : form, 'jobs' : jobs}
    return render(request, 'recruit.html', context)
   
def skills(request, pk):
    # job = Recruit.objects.get(id=pk)
    # skills, created = Comp.objects.get_or_create(recruit = job)

    job = Recruit.objects.only('id').get(id=pk)

    if request.method == 'POST': 
        form = skillsFrom(request.POST, instance = job)
        print(request.POST)
        obj = Comp.objects.create(name = request.POST['name'],  recruit=job, importance = request.POST['importance'] )
        # if form.is_valid():
        #     form.save()

    else:
        form = skillsFrom(initial = {'recruit' : job.Description})
    context = {}
    context = {'form' : form}
    return render(request, 'skills.html', context)


