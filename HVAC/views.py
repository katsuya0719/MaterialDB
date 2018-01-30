from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Chiller,CapacityFunction,EIRofTemp,EIRofPLR
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
    #model = Chiller

    def plot_capfunc(self,context):
        temp=context['object'].CapacityFunction
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
        print (c[0])

        chiller_db=Chiller(title=c[0],capacity=int(c[1]),cop=float(c[2]),chwtemp=float(c[3]),conwtemp=float(c[4]),chwfr=float(c[5]),conwfr=float(c[6]),minplr=float(c[10]),maxplr=float(c[11]),optimumplr=float(c[12]),minunloadratio=float(c[13]),condenser=c[14],flowmode=c[15])
        chiller_db.save()
        capfunc=c[7]
        eiroftemp=c[8]
        eirofplr=c[9]
        for b in biquadratic:
            print (b[0])
            if b[0]==capfunc:
                cf_db=CapacityFunction(chiller=chiller_db,name=b[0],c1=b[1],c2=b[2],c3=b[3],c4=b[4],c5=b[5],c6=b[6],min_x=b[7],max_x=b[8],min_y=b[9],max_y=b[10])
                cf_db.save()
            elif b[0]==eiroftemp:
                et_db=EIRofTemp(chiller=chiller_db,name=b[0],c1=b[1],c2=b[2],c3=b[3],c4=b[4],c5=b[5],c6=b[6],min_x=b[7],max_x=b[8],min_y=b[9],max_y=b[10])
                et_db.save()

        for q in quadratic:
            print (q[0])
            if q[0]==eirofplr:
                ep_db=EIRofPLR(chiller=chiller_db,name=b[0],c1=b[1],c2=b[2],c3=b[3],min_x=b[4],max_x=b[5])
                ep_db.save()
