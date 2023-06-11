from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import json
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer




def post_list_view(request):
    user_id = request.user.id

    try:
        posts = Post.objects.filter(user_id=user_id)
        post_texts = {post.id: post.text for post in posts}  # Map post IDs to their texts
    except Post.DoesNotExist:
        posts = None
        post_texts = {}

    # Check if the request wants to download the PDF
    if request.GET.get('download_pdf'):
        post_id = request.GET.get('post_id')  # Get the post ID from the request

        # Check if the post ID is valid and in the post_texts dictionary
        if post_id and int(post_id) in post_texts:
            # Generate the PDF using the specific post's text
            text = post_texts[int(post_id)]

            data = json.loads(text)

            # Access the 'content' key and print its value

            content = data['content']

            # Create a BytesIO buffer to hold the PDF
            buffer = BytesIO()

            # Create the PDF document
            document = SimpleDocTemplate(buffer, pagesize=letter)

            # Define a paragraph style with center alignment
            styles = getSampleStyleSheet()
            left_style = ParagraphStyle(name='left', parent=styles['Normal'], alignment=0)

            # Create a paragraph with centered style
            paragraph = Paragraph(content, left_style)

            # Build the document with the paragraph
            document.build([paragraph])

            # Get the PDF content from the buffer
            pdf_content = buffer.getvalue()

            # Close the buffer
            buffer.close()

            # Create the HTTP response with PDF content
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{post_id}.pdf"'
            response.write(pdf_content)

            return response

    return render(request, 'pdf/post_list.html', {'posts': posts})