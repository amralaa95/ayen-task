import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import DocumentForm
from .models import Document
from .files_factory.factory_file import FactoryFile

import logging
logger = logging.getLogger(__name__)


@login_required(login_url='login/')
def home(request):
    user_documents = Document.objects.filter(user=request.user)
    if request.method == 'GET':
        return render(request, 'home.html', {'query': '', 'results': user_documents})
    else:
        search_term = request.POST.get('search_term')
        results = []
        for document in user_documents:
            logger.info(f'search on file {document.document.url}')
            if search_term in document.title:
                results.append(document)
            else:
                try:
                    file_extension = os.path.splitext(document.document.path)[1]
                    file_obj = FactoryFile.create_file_class(file_extension)
                    if file_obj.search(document.document.path, search_term):
                        results.append(document)
                except Exception as e:
                    logger.error(f"Error in file {document.document.url}: {e}")
                
        return render(request, 'home.html', {'query':search_term, 'results': results})

    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required(login_url='login/')
def form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {
        'form': form
    })
