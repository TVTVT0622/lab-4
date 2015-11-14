# Create your views here.
from django.shortcuts import render_to_response
from book.models import Author,Book
		
def index(req):
	return render_to_response('index.html',{'title':'mybook'}) 	 

def search(req):
	auname = req.GET['author_name']
	authorid = Author.objects.get(name = auname)
	books = authorid.book_set.all()
	return render_to_response('search.html',{'books':books})

def show_book(req):
	books = Book.objects.all()
	return render_to_response('show_book.html',{'books':books})

def show_author(req):
	authors = Author.objects.all()
	return render_to_response('show_author.html',{'authors':authors})

def detail(req):
	isbn = req.GET['isbn']
	books = Book.objects.get(isbn = isbn)
	return render_to_response('detail.html',{'book':books})

def delete(req):
	isbn = req.GET['isbn']
	Book.objects.get(isbn = isbn).delete()
	return render_to_response('index.html',{})
