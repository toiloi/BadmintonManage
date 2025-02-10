from django.http import HttpResponse # type: ignore
from django.template import loader # type: ignore
def app(request):
    template= loader.get_template('myfirst.html')
    return HttpResponse(template.render())