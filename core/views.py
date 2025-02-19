from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from authentication.utils import check_and_deduct_credits  # Import credit system
from .models import Document
import os
import pytesseract
from PIL import Image
import PyPDF2
from django.shortcuts import render



@csrf_exempt
@login_required

def upload_document(request):
    """
    Handles document upload.
    Checks authentication, deducts credits, and saves the file.
    """
    if request.method == "POST" and request.FILES.get("file"):
        if not check_and_deduct_credits(request.user):
            return JsonResponse({"message": "Insufficient credits"}, status=400)

        file = request.FILES["file"]
        allowed_types = ["application/pdf", "image/png", "image/jpeg", "text/plain"]
        
        if file.content_type not in allowed_types:
            return JsonResponse({"message": "Invalid file type"}, status=400)

        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        doc = Document.objects.create(user=request.user, file=filename)

        return JsonResponse({"message": "File uploaded successfully", "document_id": doc.id}, status=201)

    return JsonResponse({"message": "Invalid request"}, status=400)

@login_required
def list_documents(request):
    """
    Lists all documents uploaded by the user.
    """
    docs = Document.objects.filter(user=request.user).values("id", "file", "uploaded_at")
    return JsonResponse({"documents": list(docs)}, safe=False)

@login_required
def extract_text(request, document_id):
    """
    Extracts text from the uploaded document.
    Supports PDF, PNG, and JPG.
    """
    try:
        doc = Document.objects.get(id=document_id, user=request.user)
        file_path = doc.file.path
        extracted_text = ""

        if file_path.endswith(".pdf"):
            with open(file_path, "rb") as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                extracted_text = "".join([page.extract_text() or "" for page in reader.pages])

        elif file_path.endswith((".png", ".jpg", ".jpeg")):
            image = Image.open(file_path)
            extracted_text = pytesseract.image_to_string(image)

        elif file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as txt_file:
                extracted_text = txt_file.read()

        return JsonResponse({"text": extracted_text})

    except Document.DoesNotExist:
        return JsonResponse({"message": "Document not found"}, status=404)
    except Exception as e:
        return JsonResponse({"message": f"Error extracting text: {str(e)}"}, status=500)

from django.shortcuts import render
from .models import Document 

def home(request):
    return render(request, 'home.html')


def register(request):
    return render(request, 'register.html')



