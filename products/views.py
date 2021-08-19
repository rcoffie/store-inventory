from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url=('accounts:login'))
def home(request):
  products = Product.objects.all().order_by('-id')
  context = {'products':products}
  return render(request,'products/index.html',context)



@login_required(login_url=('accounts:login'))
def product_detail(request,id):
  product = Product.objects.get(id=id) 
  context = {'product':product}
  
  return render(request,'products/product_detail.html',context)



@login_required(login_url=('accounts:login'))
def issue_item(request, pk):
    issued_item = Product.objects.get(id = pk)
    sales_form = SaleForm(request.POST)  

    if request.method == 'POST':     
        if sales_form.is_valid():
            new_sale = sales_form.save(commit=False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price   
            new_sale.save()
            #To keep track of the stock remaining after sales
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()

            return redirect('products:receipt') 

    return render (request, 'products/issue_item.html',
     {
    'sales_form': sales_form,
    })

@login_required(login_url=('accounts:login'))
def add_to_stock(request, pk):
    issued_item = Product.objects.get(id = pk)
    form = AddForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
           #To add to the remaining stock quantity is reducing
            added_quantity = int(request.POST['received_quantity'])
            issued_item.total_quantity += added_quantity
            issued_item.save()
            return redirect('home')

    return render (request, 'products/add_to_stock.html', {'form': form})
  
  
  
@login_required(login_url=('accounts:login'))  
def receipt(request): 
    sales = Sale.objects.all().order_by('-id')
    return render(request, 
    'products/receipt.html', 
    {'sales': sales,
    })
    
    
    
@login_required(login_url=('accounts:login'))
def receipt_detail(request, id):
  sale = Sale.objects.get(id=id)
  context = {'sale':sale}
  
  return render(request,'products/receipt_detail.html',context)



@login_required(login_url=('accounts:login'))    
def all_sales(request):
    sales = Sale.objects.all()
    total  = sum([items.amount_received for items in sales])
    change = sum([items.get_change() for items in sales])
    net = total - change
    return render(request, 'products/all_sales.html',
     {
     'sales': sales, 
     'total': total,
     'change': change, 
     'net': net,
      })
    
    
    
  

