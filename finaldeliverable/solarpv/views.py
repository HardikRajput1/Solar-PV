from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Client, Location, Product, TestStandard, Certificate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'solarpv/index.html')

def hindex(request):
    return render(request, 'solarpv/index.html')
                                

                                # Register Page 



def showRegister(request):
    args = {}
    clients = Client.objects.all()
    args['clients'] = clients
    return render(request, 'solarpv/forms/register_user.html', args)

def showLogin(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = User.objects.get(email=email, password=password)
            if user.choose_user == 'staff' or user.choose_user == 'Staff':
                return redirect('admin/')
            else:
                return redirect('/')
        except:
            messages.info(request, 'Invalid Credentials! Sorry')
            return redirect('login')
        
    else:
        return render(request, 'solarpv/forms/login_user.html')



def storeRegister(request):
    username=request.POST['username']
    company=Client.objects.get(id=request.POST['company'])
    first=request.POST['first']
    middle=request.POST['middle']
    last=request.POST['last']
    job=request.POST['job']
    email=request.POST['email']
    office=request.POST['office']
    cell=request.POST['cell']
    prefix=request.POST['prefix']
    password=request.POST['password']
    choose_user=request.POST['choose_user']
    user = User(userid=username,clientid=company, first=first, middle=middle, last=last, job=job, email=email, office=office, cell=cell, prefix=prefix, password=password, choose_user=choose_user)
    user.save()
    print('User created!')            
    return redirect('/')


        
                                

                                #Client Page
def showClient(request):
    return render(request, 'solarpv/forms/client.html')

def storeClient(request):
    clientname=request.POST['clientname']
    clienttype=request.POST['clienttype']
    client = Client(clientname=clientname,clienttype=clienttype)
    client.save()
    return redirect('/')

                                #Location Page
def showLocation(request):
    args = {}
    clients = Client.objects.all()
    args['clients'] = clients
    return render(request, 'solarpv/forms/location.html', args)

def storeLocation(request):
    clientid=Client.objects.get(id=request.POST['clientid'])
    add=request.POST['add']
    city=request.POST['city']
    state=request.POST['state']
    pincode=request.POST['pincode']
    mobile=request.POST['mobile']
    fax=request.POST['fax']
    location = Location(clientid=clientid, add=add, city=city, state=state, pincode=pincode, mobile=mobile, fax=fax)
    location.save()
    return redirect('/')


                                # Product Page
def showProduct(request):
    return render(request, 'solarpv/forms/product.html')

def storeProduct(request):
    modelnum=request.POST['modelnum']
    mname=request.POST['mname']
    celltech=request.POST['celltech']
    cellmanu=request.POST['cellmanu']
    cellnum=request.POST['cellnum']
    cellseries=request.POST['cellseries']
    cellstring=request.POST['cellstring']
    diodenum=request.POST['diodenum']
    prolen=request.POST['prolen']
    prowid=request.POST['prowid']
    prowei=request.POST['prowei']
    superstrate=request.POST['superstrate']
    product = Product(modelnum=modelnum, mname=mname, celltech=celltech, cellmanu=cellmanu, cellnum=cellnum, cellseries=cellseries, cellstring=cellstring, diodenum=diodenum, prolen=prolen, prowid=prowid, prowei=prowei, superstrate=superstrate)
    product.save()
    return redirect('/')



                                # Test Standard Page
def showTestStandard(request):
    return render(request, 'solarpv/forms/test_standard.html')

def storeTestStandard(request):
    stdname=request.POST['stdname']
    describe=request.POST['describe']
    pubdate=request.POST['pubdate']
    test_standard = TestStandard(stdname=stdname, describe=describe, pubdate=pubdate)
    test_standard.save()
    return redirect('/')




                                # Certificate Page
def showCertificate(request):
    args = {}
    locate = Location.objects.all()
    tsid= TestStandard.objects.all()
    modelnum = Product.objects.all()
    user = User.objects.all()
    args['locate'] = locate
    args['tsid'] = tsid
    args['modelnum'] = modelnum
    args['user'] = user
    return render(request, 'solarpv/forms/certificate.html', args)

def storeCertificate(request):
    user=User.objects.get(id=request.POST['user'])
    locate=Location.objects.get(id=request.POST['locate'])
    tsid=TestStandard.objects.get(id=request.POST['tsid'])
    productid=Product.objects.get(id=request.POST['productid'])
    reportnum = request.POST['reportnum']
    certissue=request.POST['certissue']
    certificate = Certificate(userid=user, locationid=locate, reportnum=reportnum, stdid=tsid, modelnum=productid, certissue=certissue)
    certificate.save()
    return redirect('/')


def showTestingnCertification(request):
    return render(request, 'solarpv/testingncertification.html')