from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import DataPointForm
from .models import DataPoint

def index(request):
    if request.method == 'POST':
        form = DataPointForm(request.POST)
        if form.is_valid():
            form.save()
            # Run the compression recommendation algorithm here
            return redirect('dashboard')
    else:
        form = DataPointForm()
    return render(request, 'recommender/index.html', {'form': form})

def dashboard(request):
    # Retrieve data and generate recommendations
    data_points = DataPoint.objects.all()
    # Your recommendation algorithm goes here
    return render(request, 'recommender/dashboard.html', {'data_points': data_points})
