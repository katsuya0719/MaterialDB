from django.shortcuts import render,render_to_response
from django.urls import reverse_lazy
from django.http import HttpResponse,Http404
from django.db import transaction
from django.views.generic import ListView,DetailView,TemplateView,CreateView
from .models import Chiller,CapacityFunction,EIRofTemp,EIRofPLR
from libs.EPprocessing import chiller
from libs.EPprocessing.parseidf import parseIDF
from django.core.files.storage import FileSystemStorage
from django.core.files.images import ImageFile
from io import BytesIO
import matplotlib as mpl
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import plotly
plotly.tools.set_credentials_file(username='obakatsu', api_key='nK5JWwdD7LGUH5lx1wkz')
import plotly.offline as opy
import plotly.graph_objs as go
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ChillerSerializer,CapSerializer,EIRTSerializer,PLRSerializer
from .forms import CapInline,EIRInline,PLRInline
# Create your views here.

class ChillerCreate(CreateView):
    model=Chiller
    fields = ['title','manufacturer','capacity', 'cop', 'cost','chwtemp', 'conwtemp', 'condenser', 'flowmode', 'chwfr', 'conwfr', 'minplr', 'maxplr','optimumplr', 'minunloadratio','url']
    success_url=reverse_lazy('hvac:list')
    template_name = 'hvac/chiller_create.html'

    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        if self.request.POST:
            data['capfunc']=CapInline(self.request.POST)
            data['eirfunc'] = EIRInline(self.request.POST)
            data['plrfunc'] = PLRInline(self.request.POST)
        else:
            data['capfunc'] = CapInline()
            data['eirfunc'] = EIRInline()
            data['plrfunc'] = PLRInline()

        print (data)
        return data

    def form_valid(self,form):
        context=self.get_context_data()
        print (context)
        capfunc=context['capfunc']
        eirfunc=context['eirfunc']
        plrfunc = context['plrfunc']
        with transaction.atomic():
            self.object=form.save()
            if capfunc.is_valid():
                capfunc.instance=self.object
                capfunc.save()
            if eirfunc.is_valid():
                eirfunc.instance=self.object
                eirfunc.save()
            if plrfunc.is_valid():
                plrfunc.instance=self.object
                plrfunc.save()
        return super().form_valid(form)

def Graph(request):
    if request.method == "GET":
        return render_to_response('hvac/graph.html')

class ChillerData(APIView):
    def get_object(self,pk):
        try:
            return Chiller.objects.get(pk=pk)

        except Chiller.DoesNotExist:
            raise Http404

    def get(self, request,pk, format=None):
        c=self.get_object(pk)
        serializer = ChillerSerializer(c)
        print (serializer)
        return Response(serializer.data)

class ChartData(APIView):
    # you can these two variables down the road to enhance security, but for now just leave them blank
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        capacity = []
        cop = []
        id=[]

        water=0
        air=0
        evaporate=0
        for c in Chiller.objects.all():
            capacity.append(c.capacity)
            cop.append(c.cop)
            id.append(c.id)

            if c.condenser=="WaterCooled":
                water+=1
            elif c.condenser=="AirCooled":
                air+=1
            else:
                evaporate+=1

        print (water,air,evaporate)

        data = {
            "capacity": capacity,
            "cop": cop,
            'id':id
        }

        return Response(data)



class ChillerList(ListView):
    template_name = 'hvac/chiller_list.html'
    context_object_name = 'chiller_list'
    model = Chiller

class ChillerDetail(DetailView):
    template_name = 'hvac/chiller_detail.html'
    model = Chiller

"""
    def plot_capfunc(self,context):
        temp=context['object'].capacityfunction
        print (temp)
        print (context['object'].cop)
        #print (temp.c1)
        xrange=[temp.min_x,temp.max_x]
        yrange = [temp.min_y, temp.max_y]
        gsize=0.1
        cList=[temp.c1,temp.c2,temp.c3,temp.c4,temp.c5,temp.c6]
        xlabel="Chilled Water Leaving Temp[C]"
        ylabel = "Condenser Fluid Entering Temp[C]"
        title = "Capacity Function of Temperature"
        #need to solve signal problem first
        plt=chiller.visBiquadratic(xrange, yrange, gsize, cList, xlabel, ylabel, title)
        #response=HttpResponse(content_type="image/jpeg")
        figure=BytesIO()
        plt.savefig(figure,format="png")
        content_file=ImageFile(figure)
        print (content_file)
        return content_file


    #implement logic to visualize
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context["cap"]=self.plot_capfunc(context)

        return context

"""

class uploadView(TemplateView):
    template_name = "hvac/upload.html"


def heatmap(request):
    if request.method == "GET":
        return render_to_response('hvac/heatmap.html')

    elif request.method == "POST":
        domain = request.POST['domain'].split()
        eqn = request.POST['equation']
        domain = range(int(domain[0]), int(domain[1]))
        y = [eval(eqn) for x in domain]
        title = 'y = ' + eqn

        plot = figure(title=title, x_axis_label='X-Axis', y_axis_label='Y- Axis', plot_width=400, plot_height=400)
        plot.line(domain, y, legend='f(x)', line_width=2)
        script, div = components(plot)
        print (plot)

        return render_to_response('hvac/heatmap.html', {'script': script, 'div': div})


    else:
        pass


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
    attrchiller = ["Name", "Reference_Capacity", "Reference_COP", "Reference_Leaving_Chilled_Water_Temperature", "Reference_Entering_Condenser_Fluid_Temperature",
                  "Reference_Chilled_Water_Flow_Rate", "Reference_Condenser_Fluid_Flow_Rate","Cooling_Capacity_Function_of_Temperature_Curve_Name","Electric_Input_to_Cooling_Output_Ratio_Function_of_Temperature_Curve_Name",
                  "Electric_Input_to_Cooling_Output_Ratio_Function_of_Part_Load_Ratio_Curve_Name","Minimum_Part_Load_Ratio","Maximum_Part_Load_Ratio","Optimum_Part_Load_Ratio","Minimum_Unloading_Ratio",
                   "Condenser_Type","Chiller_Flow_Mode"]
    attrbiquad = ["Name", "Coefficient1_Constant", "Coefficient2_x", "Coefficient3_x2", "Coefficient4_y",
                  "Coefficient5_y2", "Coefficient6_xy","Minimum_Value_of_x","Maximum_Value_of_x","Minimum_Value_of_y","Maximum_Value_of_y"]
    attrquad = ["Name", "Coefficient1_Constant", "Coefficient2_x", "Coefficient3_x2","Minimum_Value_of_x","Maximum_Value_of_x"]
    parsed = parseIDF(idf)
    parsed.readobjs(objects)
    chillers=parsed.readattrs(0, attrchiller)
    biquadratic = parsed.readattrs(1, attrbiquad)
    quadratic = parsed.readattrs(2, attrquad)
    for c in chillers:
        #print (c[0])

        chiller_db=Chiller(title=c[0],capacity=int(c[1]),cop=float(c[2]),chwtemp=float(c[3]),conwtemp=float(c[4]),chwfr=float(c[5]),conwfr=float(c[6]),minplr=float(c[10]),maxplr=float(c[11]),optimumplr=float(c[12]),minunloadratio=float(c[13]),condenser=c[14],flowmode=c[15])
        chiller_db.save()
        capfunc=c[7]
        eiroftemp=c[8]
        eirofplr=c[9]
        for b in biquadratic:
            #print (b[0])
            if b[0]==capfunc:
                cf_db=CapacityFunction(chiller=chiller_db,name=b[0],c1=b[1],c2=b[2],c3=b[3],c4=b[4],c5=b[5],c6=b[6],min_x=b[7],max_x=b[8],min_y=b[9],max_y=b[10])
                cf_db.save()
            elif b[0]==eiroftemp:
                et_db=EIRofTemp(chiller=chiller_db,name=b[0],c1=b[1],c2=b[2],c3=b[3],c4=b[4],c5=b[5],c6=b[6],min_x=b[7],max_x=b[8],min_y=b[9],max_y=b[10])
                et_db.save()

        for q in quadratic:
            print (q[0])
            if q[0]==eirofplr:
                print (q[0],eirofplr)
                ep_db=EIRofPLR(chiller=chiller_db,name=q[0],c1=q[1],c2=q[2],c3=q[3],min_x=q[4],max_x=q[5])
                ep_db.save()
