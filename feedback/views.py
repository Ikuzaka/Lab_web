from django.shortcuts import render, redirect
from .forms import FeedbackForm
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html', context={'form': form})