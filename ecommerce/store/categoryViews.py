from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms  import ecommerceSubCategory, ecommerceCategory
from .models import SubCategory, Category
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
from django.views.generic import ListView
from datatables_view.views import DatatablesView
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


#sub category view
def AddSubCategory(request):
    # check if the request is post
    if request.method == 'POST':
        details = ecommerceSubCategory(request.POST)
        if details.is_valid():
            post = details.save(commit=False)
            post.save()
            messages.success(request, 'Added Suceessfully...')
            return redirect('/subCategory/create')
        else:
            return render(request, "admin/category/sub_category.html", {'form': details})
    else:
        form = ecommerceSubCategory(None)
        return render(request, 'admin/category/sub_category.html', {'form': form})

#sub category datatable
class subcategoryAjaxDataTable(DatatablesView):
    model = SubCategory
    title = 'SubCategory Datatable'
    column_defs = [
        {
            'name' : 'title',
        },
        {
            'name' : 'slug'
        },
        {
            'name': 'action',
            'searchable': False,
            'orderable': False
        }
    ]

    def customize_row(self, row, obj):
        row['action'] = '<a class="delete-button" cid="%s"><i class="fas fa-trash-alt"></i></a> &nbsp <a class="view-button" href="view/%s"><i class="far fa-eye"></i></a> &nbsp <a class="update-button" href="edit/%s"><i class="far fa-edit"></i></a>' % (
            obj.id,
            obj.slug,
            obj.id,
        )

#sub category datatable view
@method_decorator(login_required(login_url='login'), name="dispatch")
class subcategoryContent(ListView):
    model = SubCategory
    template_name = 'admin/category/subcategory_list.html'
    ordering = ['-id']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

#subcategory ajax delete
def subcategory_delete(request):
    id = request.POST.get('id')
    news = SubCategory.objects.get(pk = id)
    news.delete()
    return JsonResponse({'success' : 'true'});

#subcategory data view
def subcategory_view(request, slug):
    if request.method == "GET":
        subcategory = SubCategory.objects.get(slug = slug)
    return render(request, "admin/category/subcategory_view.html", {'subcategory': subcategory})

#subcategory update
def subcategory_update(request, id = 0):
    if request.method == "GET":
        if id == 0:
            subcat = ecommerceSubCategory()
        else:
            subcategory = SubCategory.objects.get(pk = id)
            subcat = ecommerceSubCategory(instance=subcategory)
        return render(request, 'admin/category/sub_category.html', {'subcat': subcat})
    else:
        if id == 0:
            subcat = ecommerceSubCategory(request.POST)
        else:
            subcategory = SubCategory.objects.get(pk = id)
            subcat = ecommerceSubCategory(request.POST, instance = subcategory)
        if subcat.is_valid():
            subcat.save()
            messages.success(request, 'Updated Sucessfully...')
        return redirect('/subCategory/create')





#category view
@login_required(login_url='login')
def AddCategory(request):
    if request.method == "POST":
        form = ecommerceCategory(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            messages.success(request, 'Added Suceessfully...')
            return redirect('/category/create')
    else:
        form = ecommerceCategory()
    return render(request, 'admin/category/category.html', {'form': form})
    
    
#category datatable
class categoryAjaxDataTable(DatatablesView):
    model = Category
    title = 'Category Datatable'
    column_defs = [
        {
            'name' : 'title',
        },
        {
            'name' : 'meta_title',
        },
        {
            'name' : 'summary',
        },
        
        
        {
            'name': 'action',
            'searchable': False,
            'orderable': False
        }
    ]
    def customize_row(self, row, obj):
        row['image'] ='<img src="/media/%s" width="100"> ' % (obj.image,)
        row['action'] = '<a class="delete-button" cid="%s"><i class="fas fa-trash-alt"></i></a> &nbsp <a class="view-button" href="view/%s"><i class="far fa-eye"></i></a> &nbsp <a class="update-button" href="edit/%s"><i class="far fa-edit"></i></a>' % (
            obj.id,
            obj.slug,
            obj.id,
        ),

#category datatable view
@method_decorator(login_required(login_url='login'), name="dispatch")
class categoryContent(ListView):
    model = Category
    template_name = 'admin/category/category_list.html'
    ordering = ['-id']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

#category ajax delete
def category_delete(request):
    id = request.POST.get('id')
    news = Category.objects.get(pk = id)
    news.delete()
    return JsonResponse({'success' : 'true'});

#category data view
def category_view(request, slug):
    if request.method == "GET":
        category = Category.objects.get(slug = slug)
    return render(request, "admin/category/category_view.html", {'category': category})

#category update
def category_update(request, id = 0):
    if request.method == "GET":
        if id == 0:
            cat = ecommerceCategory()
        else:
            category = Category.objects.get(pk = id)
            cat = ecommerceCategory(instance=category)
        return render(request, 'admin/category/category.html', {'cat': cat})
    else:
        if id == 0:
            cat = ecommerceCategory(request.POST)
        else:
            category = Category.objects.get(pk = id)
            cat = ecommerceCategory(request.POST, instance = category)
        if cat.is_valid():
            cat.save()
            messages.success(request, 'Updated Sucessfully...')
        return redirect('/category/create')
