from django.shortcuts import render

# Create your views here.
class storeviews:
    def store(request):
        return render(request=request, template_name='store.html') 