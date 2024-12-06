from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm, BookForm, LibraryForm
def base_view(request):
    return render(request,"testapp/base.html")
def student_management(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_management')
    else:
        form = StudentForm()
    return render(request, 'testapp/student.html', {'form': form, 'students': students})

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_management')  # Redirect to the main page after saving
    else:
        form = StudentForm(instance=student)
    return render(request, 'testapp/edit_student.html', {'form': form, 'student': student})


# Delete student
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('student_management')  # Use the correct name here


# Book Views
def book_view(request):
    books = Book.objects.all()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')
    else:
        form = BookForm()
    return render(request, 'testapp/book.html', {'form': form, 'books': books})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book')
    else:
        form = BookForm(instance=book)
    return render(request, 'testapp/edit_book.html', {'form': form})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book')


# Library Views

from django.shortcuts import render, redirect
from .forms import LibraryForm
from .models import Library, Student, Book

from django.shortcuts import render, redirect
from .models import Library, Student, Book
from .forms import LibraryForm

def library_view(request):
    records = Library.objects.all()
    issued_books = {record.book.id: record.student.name for record in records}  # Create a dictionary of issued books

    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        form = LibraryForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            try:
                # Save the form data and create a new Library record
                form.save()
                return redirect('library')  # Redirect to the library page to see updated records
            except Exception as e:
                # If there's an error saving, show an error message
                form.add_error(None, f"Error saving record: {str(e)}")
        else:
            # Print form errors for debugging
            print("Form errors:", form.errors)  # Debug print
    else:
        form = LibraryForm()

    # Pass the form, records, issued_books, students, and books to the template
    context = {
        'form': form,
        'records': records,
        'issued_books': issued_books,  # Pass issued books to the context
        'students': Student.objects.all(),
        'books': Book.objects.all(),
    }
    return render(request, 'testapp/library.html', context)

def edit_library(request, pk):
    record = get_object_or_404(Library, pk=pk)
    if request.method == 'POST':
        form = LibraryForm(request.POST, instance=record)
        if form.is_valid():
            try:
                form.save()
                return redirect('library')
            except Exception as e:
                form.add_error(None, f"Error updating record: {str(e)}")
        else:
            print("Form errors:", form.errors)  # Debug print
    else:
        form = LibraryForm(instance=record)
    return render(request, 'testapp/edit_library.html', {'form': form})

def delete_library(request, pk):
    record = get_object_or_404(Library, pk=pk)
    record.delete()
    return redirect('library')

