from django.core.paginator import Paginator


def get_page_number(request):
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    return page_number


class PaginatorMixin:
    def __init__(self, *args, **kwargs):
        self.__objects = None
        self.paginator = None
        self.pages = None

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, value):
        self.__objects = value
        if self.pages is None:
            raise Exception('Improperly configured. Please set self.pages to integer `self.pages=1` ')
        self.paginator = Paginator(self.__objects, self.pages)

    def paginate(self, request):
        page_number = get_page_number(request)
        page_obj = self.paginator.get_page(page_number)
        return page_obj
