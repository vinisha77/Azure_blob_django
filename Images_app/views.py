from django.shortcuts import render, redirect
from django.http import HttpResponse
from .azure_storage import upload_file_to_azure, list_files_in_azure_container, download_file_from_azure


def home(request):
    return render(request, 'Images_app/index.html')

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        upload_file_to_azure(uploaded_file)
        return redirect('upload_success') 
        #return redirect('image_list')
    return render(request, 'Images_app/upload.html')

def download_file(request, filename):
    file_content = download_file_from_azure(filename)
    response = HttpResponse(file_content, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response

def list_images(request):
    images = list_files_in_azure_container()
    return render(request, 'Images_app/image_list.html', {'images': images})

def upload_success(request):
    return render(request, 'Images_app/upload_success.html')



