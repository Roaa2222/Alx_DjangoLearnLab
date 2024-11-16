# bookshelf/forms.py
from django import forms
from .models import Book  # Import your model if you need a ModelForm

class ExampleForm(forms.Form):
    # Replace these fields with the ones relevant to your use case
    title = forms.CharField(max_length=100, required=True)
    author = forms.CharField(max_length=100, required=True)
    published_date = forms.DateField(required=False)

class BookSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)

# In views.py, validate the form
def search_books(request):
    form = BookSearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['search']
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})
