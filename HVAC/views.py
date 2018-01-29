from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Chiller
from libs.EPprocessing import chiller
from libs.EPprocessing.parseidf import parseIDF
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
        parse(myfile)

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        uploaded_file_url = fs.url(filename)
        return render(request, 'hvac/idf_import.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'hvac/idf_import.html')

def parse(idf):
    objects = ['Chiller:Electric:EIR', 'Curve:Biquadratic', 'Curve:Quadratic']
    attrbiquad = ["Name", "Coefficient1_Constant", "Coefficient2_x", "Coefficient3_x2", "Coefficient4_y",
                  "Coefficient5_y2", "Coefficient6_xy"]
    attrquad = ["Name", "Coefficient1_Constant", "Coefficient2_x", "Coefficient3_x2"]
    parsed = parseIDF(idf)
    print (parsed)
    parsed.readobjs(objects)
