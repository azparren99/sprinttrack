from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import TrainingSession
from .forms import TrainingSessionForm


def home(request):
    return render(request, 'training/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('session_list')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    sessions = TrainingSession.objects.filter(user=request.user)

    total_sessions = sessions.count()
    best_60 = sessions.filter(distance_m=60).order_by('time_seconds').first()
    best_100 = sessions.filter(distance_m=100).order_by('time_seconds').first()
    recent_sessions = sessions.order_by('-date')[:5]

    return render(request, 'training/dashboard.html', {
        'total_sessions': total_sessions,
        'best_60': best_60,
        'best_100': best_100,
        'recent_sessions': recent_sessions,
    })


@login_required
def session_list(request):
    sessions = TrainingSession.objects.filter(user=request.user).order_by('-date')
    return render(request, 'training/session_list.html', {'sessions': sessions})


@login_required
def session_create(request):
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()
            return redirect('session_list')
    else:
        form = TrainingSessionForm()

    return render(request, 'training/session_create.html', {'form': form})


@login_required
def session_edit(request, id):
    session = get_object_or_404(TrainingSession, id=id, user=request.user)

    if request.method == 'POST':
        form = TrainingSessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('session_list')
    else:
        form = TrainingSessionForm(instance=session)

    return render(request, 'training/session_edit.html', {'form': form})


@login_required
def session_delete(request, id):
    session = get_object_or_404(TrainingSession, id=id, user=request.user)

    if request.method == 'POST':
        session.delete()
        return redirect('session_list')

    return render(request, 'training/session_delete.html', {'session': session})