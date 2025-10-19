from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import CommentForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.all().order_by('-created')

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = CommentForm()

    return render(request, 'library/book_detail.html', {
        'book': book,
        'comments': comments,
        'form': form
    })
