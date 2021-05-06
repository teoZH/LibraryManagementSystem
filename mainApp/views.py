from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required
import os
from library_system.settings import BASE_DIR
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.base import ContextMixin
from django.views.generic.edit import FormView
from .mixins import PaginatorMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView


def remove_picture(p):
    actual = os.path.join(BASE_DIR, *p.split('/'))
    print(actual)
    if os.path.exists(actual):
        os.remove(actual)
    else:
        print('not exist')
    return


# Create your views here.


def index(request):
    return render(request, 'main.html')


class CatalogView(View, ContextMixin, PaginatorMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page_obj = None
        self.pages = 3

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        books = Book.objects.all()
        self.objects = books
        self.page_obj = self.paginate(request)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(page_obj=self.page_obj)
        return render(request, 'catalog.html', context)


@method_decorator(login_required, 'dispatch')
class CreateBookView(FormView):
    template_name = 'create.html'
    form_class = BookForm
    success_url = '/catalog/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            book = form.save(commit=False)
            book.book_owner = request.user
            book.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


@method_decorator(login_required, 'dispatch')
class DetailBookView(DetailView):
    model = Book
    template_name = 'details.html'


@method_decorator(login_required, name='dispatch')
class UpdateBookView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'edit.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        old_image = self.object.image.url
        form = self.get_form()
        if form.is_valid():
            remove_picture(old_image)
            self.success_url = f'/details/{kwargs["pk"]}/{kwargs["book_title"]}/'
            return self.form_valid(form)
        else:

            return self.form_invalid(form)


@login_required
def delete(request, book_id, book_title):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return redirect('catalog')
