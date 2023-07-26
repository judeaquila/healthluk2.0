from django.shortcuts import render, redirect
from .forms import WaitlistForm
from .models import Waitlist

# Landing page
def index(request):
    form = WaitlistForm()
    if request.method == 'POST':
        form = WaitlistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success-page')
    context = {'form':form}
    return render(request, 'main/index.html', context)

# Success page
def success(request):
    return render(request, 'main/thanks.html')