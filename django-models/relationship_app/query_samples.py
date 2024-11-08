from relationship_app.models import Author, Book, Library, Librarian

# 1. List all books in a library
try:
    library_name = "Library Name"
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()

    print(f"Books in {library_name}:")
    for book in books_in_library:
        print(book.title)
except Library.DoesNotExist:
    print(f"Error: Library '{library_name}' does not exist.")

# 2. Query all books by a specific author
try:
    author_name = "Author Name"
    author = Author.objects.get(name=author_name)
    books_by_author = author.books.all()  # Related name defined in the ForeignKey

    print(f"\nBooks by {author_name}:")
    for book in books_by_author:
        print(book.title)
except Author.DoesNotExist:
    print(f"Error: Author '{author_name}' does not exist.")

# 3. Retrieve the librarian for a library
try:
    library_name = "Library Name"
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # OneToOneField with related_name

    print(f"\nLibrarian of {library_name}: {librarian.name}")
except Library.DoesNotExist:
    print(f"Error: Library '{library_name}' does not exist.")
except Librarian.DoesNotExist:
    print(f"Error: No librarian found for the library '{library_name}'.")
