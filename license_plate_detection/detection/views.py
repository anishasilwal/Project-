# detection/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import UploadedFile
from .forms import UploadFileForm
from .ocr_utils import perform_ocr

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = UploadedFile(file=request.FILES['file'])

            # Placeholder text (replace with actual OCR code later)
            uploaded_file.plate_text = perform_ocr()  # Replace with your placeholder text

            uploaded_file.save()
            
            return JsonResponse({
                'message': 'File uploaded!',
                'license_details': True,
                'plate_text': uploaded_file.plate_text
            })
        else:
            # If form is not valid, return form errors
            return JsonResponse({'message': form.errors}, status=400)
    
    # If not a POST request, return error (though it's unlikely to hit this case)
    return JsonResponse({'message': 'File upload failed!'}, status=400)


def index(request):
    return render(request, 'detection/index.html')

def about(request):
    return render(request, 'detection/about.html')

def contact(request):
    return render(request, 'detection/contact.html')
