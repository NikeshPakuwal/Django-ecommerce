from django.shortcuts import render, redirect
from .forms  import ecommerceProduct
from .models import Product, SubCategory
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.serializers import serialize
from django.views import View
from django.views.generic import ListView
from datatables_view.views import DatatablesView
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


#product view
@method_decorator(login_required(login_url='login'), name="dispatch")
class AddProduct(View):

    def get(self, request):
        form = ecommerceProduct()
        return render(request, 'admin/product/product.html', {'form': form})

    def post(self, request):
        if request.method == "POST":
            form = ecommerceProduct(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                img_obj = form.instance
                messages.success(request, 'Added Suceessfully...')
                return redirect('/product/create')
        else:
            form = ecommerceProduct()
        return render(request, 'admin/product/product.html', {'form': form})

#product datatable
class productAjaxDataTable(DatatablesView):
    model = Product
    title = 'Product Datatable'
    column_defs = [
        {
            'name' : 'title',
        },
        
        {
            'name' : 'meta_title',
        },
        
        {
            'name' : 'description',
        },
        {
            'name' : 'price',
        },
        {
            'name' : 'stock',
        },
        
        {
            'name': 'action',
            'searchable': False,
            'orderable': False
        }
    ]
    def customize_row(self, row, obj):
        row['image'] ='<img src="/media/%s" width="100"> ' % (
            obj.image,
        ),
        row['action'] = '<a class="delete-button" cid="%s"><i class="fas fa-trash-alt"></i></a> &nbsp <a class="view-button" href="view/%s"><i class="fas fa-eye"></i></a> &nbsp <a class="view-button" href="edit/%s"><i class="far fa-edit"></i></a>' % (
            obj.id,
            obj.slug,
            obj.id,
        ),

#product datatable view
@method_decorator(login_required(login_url='login'), name="dispatch")
class productContent(ListView):
    model = Product
    template_name = 'admin/product/product_list.html'
    ordering = ['-id']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

#category ajax delete
def product_delete(request):
    id = request.POST.get('id')
    news = Product.objects.get(pk = id)
    news.delete()
    return JsonResponse({'success' : 'true'});

#product data view
def product_view(request, slug):
    if request.method == "GET":
        product = Product.objects.get(slug = slug)
    return render(request, "admin/product/product_view.html", {'product': product})

#load subcategory as the particular category is selected
def load_subcategory(request):
    category_id = request.GET.get('category')
    subcat = SubCategory.objects.filter(category_id = category_id).order_by('id')
    return render(request, 'admin/ajax/subcategory_ajax.html', {'subcat': subcat})

#product update
def product_update(request, id = 0):
    if request.method == "GET":
        if id == 0:
            prod = ecommerceProduct()
        else:
            product = Product.objects.get(pk = id)
            prod = ecommerceProduct(instance=product)
        return render(request, 'admin/product/product.html', {'prod': prod})
    else:
        if id == 0:
            prod = ecommerceProduct(request.POST)
        else:
            product = Product.objects.get(pk = id)
            prod = ecommerceProduct(request.POST, instance = product)
        if prod.is_valid():
            prod.save()
            messages.success(request, 'Updated Sucessfully...')
        return redirect('/product/create')