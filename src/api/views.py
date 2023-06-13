from django.http import JsonResponse
from blog.models import Post
from .forms import PostForm

def save_form_data(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            
            # Save the data in the Post model
            post = Post(title=title, text=text)
            post.save()

            response = {"message": "Form data saved successfully"}
            return JsonResponse(response)
        else:
            response = {"error": "Form submission failed."}
            return JsonResponse(response, status=400)
    else:
        response = {"error": "Invalid request method."}
        return JsonResponse(response, status=405)
