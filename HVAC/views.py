from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Chiller
from libs.EPprocessing import chiller
from django.core.files.storage import FileSystemStorage
# Create your views here.

class ChillerList(ListView):
    template_name = 'hvac/chiller_list.html'
    context_object_name = 'chiller_list'
    model = Chiller

class ChillerDetail(DetailView):
    template_name = 'hvac/chiller_detail.html'
    model = Chiller

    def plot_capfunc(self,context):
        temp=context['object'].capfunc
        print (temp.c1)
        xrange=[temp.min_x,temp.max_x]
        yrange = [temp.min_y, temp.max_y]
        gsize=0.1
        cList=[temp.c1,temp.c2,temp.c3,temp.c4,temp.c5,temp.c6]
        xlabel="Chilled Water Leaving Temp[C]"
        ylabel = "Condenser Fluid Entering Temp[C]"
        title = "Capacity Function of Temperature"
        #need to solve signal problem first
        #chiller.visBiquadratic(xrange, yrange, gsize, cList, xlabel, ylabel, title)


    #implement logic to visualize
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        self.plot_capfunc(context)

def idf_import(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'hvac/idf_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'hvac/idf_upload.html')