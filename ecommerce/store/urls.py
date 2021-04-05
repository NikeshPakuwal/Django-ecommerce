from django.urls import path
from . import views, categoryViews, authenticateViews, productViews
from django.contrib.auth import views as auth_views
from .productViews import AddProduct, productAjaxDataTable, productContent
from .categoryViews import AddSubCategory, subcategoryAjaxDataTable, subcategoryContent, categoryAjaxDataTable, categoryContent


urlpatterns = [

    #client side view (store url)
    path('', views.store, name = 'front_view'),

    #admin panel controls
    path('admin/auth/user/', authenticateViews.AdminUserList, name = 'auth_user'),
    path('admin/auth/user/<int:id>/change/', authenticateViews.AdminUser, name = 'auth_view'),
    path('admin/user/delete', authenticateViews.user_delete, name = 'user_delete'),

    #registration url
    path('registration/', authenticateViews.register, name = 'registration'),

    #login url
    path('login/', authenticateViews.loginPage, name = 'login'),

    #cart url
    path('cart/', views.cart, name = 'cart'),

    #dashboard url
    path('dashboard/', views.adminHome, name='dashboard'),
    
    # category url
    path('category/create', categoryViews.AddCategory, name='category'),

    #category datatable url
    path('category/datatable', categoryAjaxDataTable.as_view(), name="CategoryDatatable"),
    path('category/list', categoryContent.as_view(), name="CategoryContent"),

    #category ajax delete
    path('delete/category', categoryViews.category_delete, name="category_delete"),

    #category data view
    path('category/view/<slug:slug>/', categoryViews.category_view, name="categoryView"),

    #category update
    path('category/edit/<int:id>', categoryViews.category_update, name = "category_update"),

    #subcategory url
    path('subCategory/create', categoryViews.AddSubCategory, name = 'subCategory'),

    #subcategory datatable url
    path('subCategory/datatable', subcategoryAjaxDataTable .as_view(), name="subCategoryDatatable"),
    path('subCategory/list', subcategoryContent.as_view(), name="subCategoryContent"),

    #subcategory ajax delete
    path('delete/subcategory', categoryViews.subcategory_delete, name="subcategory_delete"),

    #subcategory data view
    path('subCategory/view/<slug:slug>/', categoryViews.subcategory_view, name="subcategoryView"),

    #subcategory update
    path('subCategory/edit/<int:id>', categoryViews.subcategory_update, name = "subcategory_update"),

    #product url
    path('product/create', AddProduct.as_view(), name = 'product'),

    #product datatable url
    path('product/datatable', productAjaxDataTable .as_view(), name="ProductDatatable"),
    path('product/list', productContent.as_view(), name="ProductContent"),

    #productcategory ajax delete
    path('delete/product', productViews.product_delete, name="product_delete"),

    #product data view
    path('product/view/<slug:slug>/', productViews.product_view, name="productView"),

    #product update
    path('product/edit/<int:id>', productViews.product_update, name = "product_update"),

    #load subcategory according to category in product table
    path('ajax/load_subcategory/', productViews.load_subcategory, name='ajax_load_subcategory'),

]
