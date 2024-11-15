# advanced_features_and_security/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Article
from .models import Book  # Ensure that you have a Book model in models.py

@permission_required('bookshelf.view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@permission_required('bookshelf.view_book', raise_exception=True)
def books(request):
    # This could be another view related to a specific book functionality
    return render(request, 'books.html')

@permission_required('advanced_features_and_security.can_create', raise_exception=True)
def create_article(request):
    if request.method == 'POST':
        # Code to create article
        pass
    return render(request, 'create_article.html')

@permission_required('advanced_features_and_security.can_edit', raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        # Code to edit article
        pass
    return render(request, 'edit_article.html', {'article': article})

@permission_required('advanced_features_and_security.can_delete', raise_exception=True)
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'confirm_delete.html', {'article': article})
