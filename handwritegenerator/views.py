from django.shortcuts import render
from handwritegenerator.models import UploadTxt

context = {}
def index(request):
    return render(request,'index.html')

def txt_upload(request):
	try:
		txt = UploadTxt()
		txt.text = request.FILES['txtfile']
		txt.save()
	except Exception as ex:
		print(ex)
	txt = UploadTxt.objects.latest('id')
	txt.save()
	context['contents'] = open(txt.text.url,'r').read()
	return render(request,'index.html',context)

def txtgenerator(request):
    pass