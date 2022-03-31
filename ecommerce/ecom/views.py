from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .models import Category, Contact, User, Product
from .forms import ContactForm, UserForm, LoginForm, ProductForm
from django.contrib import auth
from django.contrib.auth import authenticate, forms, login, logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import ListView



from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from django.views.generic import ListView







# Create your views here.





# def CategoryView(request, id):
#     img = Product.objects.get(pk = id)
#     if 'product_ids' in request.COOKIES:
#             product_ids = request.COOKIES['product_ids']
#             counter=product_ids.split('|')
#             product_count_in_cart=len(set(counter))
#     else:
#         product_count_in_cart=0
#     return render(request, 'details.html',{'img':img, 'product_count_in_cart':product_count_in_cart })
    
#     # return render(request, 'category.html', {'img':img})
    

def catogorylist(request,id):
    img = Product.objects.filter(category__id=id)
    categories = Category.objects.all()
    print("==========================>", products)
    if 'product_ids' in request.COOKIES:
            product_ids = request.COOKIES['product_ids']
            counter=product_ids.split('|')
            product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
    return render(request, 'category.html',{'img':img, 'categories': categories, 'products':products, 'product_count_in_cart':product_count_in_cart })
    # return render(request,"category.html", {'products':products}) 



class SearchResultsView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products' # by default = object_list

    def get_queryset(self):
        query = self.request.GET.get('search')
        products=Product.objects.filter(Q(name__icontains=query))
        print('---------product----------', products)
        return products



def home(request):
        if request.method == 'GET':
            img = Product.objects.all() 
            categories = Category.objects.all()
            if request.user.is_authenticated:
                if 'product_ids' in request.COOKIES:
                    product_ids = request.COOKIES['product_ids']
                    counter=product_ids.split('|')
                    product_count_in_cart=len(set(counter))
                else:
                    product_count_in_cart=0
                return render(request, 'home.html', {'img':img, 'categories' : categories, 'product_count_in_cart':product_count_in_cart})
            else:
                return render(request, 'home.html', {'img':img, 'categories' : categories})



def contact(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            sb = form.cleaned_data['subject']
            ms = form.cleaned_data['message']
            msg = Contact(name=nm, email=em, subject=sb, message=ms)
            msg.save()
            messages.success(request, 'Congratulations!! Your message is sent successfully.')
            return HttpResponseRedirect('/contact/')

    else:
        form = ContactForm()  
    print('-----fm-------',form)
    return render(request, 'contact.html', {'form':form, 'categories' : categories}) 

def products(request):
    if request.method == 'GET':
        image = Product.objects.all() 
        categories = Category.objects.all()
        paginator = Paginator(image, 3) 
        page_number = request.GET.get('page')
        img = paginator.get_page(page_number)

        if request.user.is_authenticated:
            if 'product_ids' in request.COOKIES:
                product_ids = request.COOKIES['product_ids']
                counter=product_ids.split('|')
                product_count_in_cart=len(set(counter))
            else:
                product_count_in_cart=0
            return render(request, 'products.html', {'img' : img,'categories' : categories, 'product_count_in_cart':product_count_in_cart})
    return render(request, 'products.html', {'img' : img, 'categories' : categories})
    


def about(request):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        if 'product_ids' in request.COOKIES:
            product_ids = request.COOKIES['product_ids']
            counter=product_ids.split('|')
            product_count_in_cart=len(set(counter))
        else:
            product_count_in_cart=0
        return render(request, 'about.html', {'categories' : categories, 'product_count_in_cart':product_count_in_cart})
    return render(request, 'about.html', {'categories': categories})


def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')


def reg(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            un = fm.cleaned_data['username']
            mb = fm.cleaned_data['mobile']
            em = fm.cleaned_data['email']
            p1 = fm.cleaned_data['password']
            cs = fm.cleaned_data['customer']
            ct = fm.cleaned_data['country']
            ad = fm.cleaned_data['address']
            reg = User(name=nm, mobile=mb, email=em, username=un, password=p1, customer=cs ,country=ct, address=ad)
            # user = fm.save(commit=False)
            reg.set_password(p1)
            reg.save()
            messages.success(request, 'Congratulations!! Registrations Successfull.')
            return HttpResponseRedirect('reg')
            
    else:
        fm = UserForm()
    
    return render(request, 'reg.html', {'form':fm,'categories' : categories})


def user_login(request):   
    # if not request.user.is_authenticated:
        categories = Category.objects.all()
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    # return render(request, 'login.html')
                    # return HttpResponseRedirect('/home/')
                    return render(request, 'home.html', {'categories': categories})

        else:
            form = LoginForm()
        return render(request, 'login.html', {'categories' : categories, 'form':form})
    # else:
    #     return render(request, 'login.html')
        # return HttpResponseRedirect('/')




def addproduct(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        fm = ProductForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Upload product succesfully  !!')
            return render(request, 'add_product.html', {'categories' : categories})
            
    else:
        fm = ProductForm()
    # data = User.objects.all()
    return render(request, 'add_product.html', {'form':fm, 'categories' : categories})

    

@login_required(login_url='login')
def cart_view(request):
    categories = Category.objects.all()
    #for cart counter
    
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # fetching product details from db whose id is present in cookie
    products=None
    total=0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_id_in_cart=product_ids.split('|')
            products = Product.objects.all().filter(id__in = product_id_in_cart)

            #for total price shown in cart
            for p in products:
                total=total+p.price
    
    return render(request,'cart.html',{'categories' : categories, 'products':products,'total':total,'product_count_in_cart':product_count_in_cart})




@login_required(login_url='login')
def add_to_cart_view(request,pk):
    categories = Category.objects.all()
    products=Product.objects.all()

    #for cart counter, fetching products ids added by customer from cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    response = render(request, 'home.html',{'categories' : categories, 'products':products,'product_count_in_cart':product_count_in_cart})

    #adding product id to cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids=="1":
            product_ids=str(pk)
        else:
            product_ids=product_ids+"|"+str(pk)
        response.set_cookie('product_ids', product_ids)
    else:
        response.set_cookie('product_ids', pk)

    product = Product.objects.get(id=pk)
    messages.info(request, product.name + ' added to cart successfully!')

    return response

   


def remove_from_cart_view(request,pk):
    categories = Category.objects.all()
    #for counter in cart
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # removing product id from cookie
    total=0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        product_id_in_cart=product_ids.split('|')
        product_id_in_cart=list(set(product_id_in_cart))
        product_id_in_cart.remove(str(pk))
        products= Product.objects.all().filter(id__in = product_id_in_cart)
        #for total price shown in cart after removing product
        for p in products:
            total=total+p.price

        #  for update coookie value after removing product id in cart
        value=""
        for i in range(len(product_id_in_cart)):
            if i==0:
                value=value+product_id_in_cart[0]
            else:
                value=value+"|"+product_id_in_cart[i]
        response = render(request, 'cart.html',{'categories' : categories, 'products':products,'total':total,'product_count_in_cart':product_count_in_cart})
        if value=="":
            response.delete_cookie('product_ids')
        response.set_cookie('product_ids',value)
        return response


def productdetail(request,id):
    categories = Category.objects.all()
    img = Product.objects.get(id = id)
    if 'product_ids' in request.COOKIES:
            product_ids = request.COOKIES['product_ids']
            counter=product_ids.split('|')
            product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
    return render(request, 'details.html',{'categories' : categories, 'img':img, 'product_count_in_cart':product_count_in_cart })
    



def password_reset_request(request):
	if request.method == "POST":
		form = PasswordResetForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [email.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	form = PasswordResetForm()
	return render(request=request, template_name="password_reset.html", context={"form":form})                  