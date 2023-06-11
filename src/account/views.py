from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from blog.models import Post
from django.http import HttpResponse
import json
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph


def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user).order_by('-created_at')[:5]  # Get the last 5 posts

    context = {
        'user': user,
        'posts': posts,
    }

    if request.GET.get('download_pdf'):
        post_id = request.GET.get('post_id')  # Get the post ID from the request

        # Check if the post ID is valid and belongs to the current user
        if post_id and Post.objects.filter(id=post_id, user=user).exists():
            # Get the specific post
            post = Post.objects.get(id=post_id)

            # Added the post's text to the content variable
            content = post.text

            # Create the PDF document
            buffer = BytesIO()
            document = SimpleDocTemplate(buffer, pagesize=letter)
            styles = getSampleStyleSheet()
            left_style = ParagraphStyle(name='left', parent=styles['Normal'], alignment=0)
            paragraph = Paragraph(content, left_style)
            document.build([paragraph])
            pdf_content = buffer.getvalue()
            buffer.close()

            # Return the PDF as a download attachment
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{post_id}.pdf"'
            response.write(pdf_content)

            return response

    return render(request, 'account/profile.html', context)



def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)

    if request.method == 'POST':
        post.delete()
        return redirect('account:profile', username=request.user.username)

    context = {
        'post': post,
    }

    return render(request, 'account/delete_post.html', context)



def preview_pdf(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Generate the PDF content
    content = post.text

    # Create the PDF document
    buffer = BytesIO()
    document = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    left_style = ParagraphStyle(name='left', parent=styles['Normal'], alignment=0)
    paragraph = Paragraph(content, left_style)
    document.build([paragraph])
    pdf_content = buffer.getvalue()
    buffer.close()

    # Return the PDF content in a new tab
    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{post_id}.pdf"'

    return response