from django import forms
from .models import Chiller,CapacityFunction,EIRofTemp,EIRofPLR
from django.forms import widgets
from django.forms import inlineformset_factory

class ChillerForm(forms.ModelForm):

	class Meta:
		model=Chiller
		#fields=['capacity','cop','chwtemp','conwtemp','condenser','flowmode','chwfr','conwfr','minplr','maxplr','optimumplr','minunloadratio']
		#widgets={'ecms':forms.CheckboxSelectMultiple}
		exclude=()

class CapFuncForm(forms.ModelForm):

	class Meta:
		model=CapacityFunction
		fields=['name','c1','c2','c3','c4','c5','c6','min_x','max_x','min_y','max_y']

class EIRFuncForm(forms.ModelForm):

	class Meta:
		model=EIRofTemp
		fields=['name','c1','c2','c3','c4','c5','c6','min_x','max_x','min_y','max_y']

class PLRFuncForm(forms.ModelForm):

	class Meta:
		model=EIRofPLR
		fields=['name','c1','c2','c3','c4','min_x','max_x']

CapInline=inlineformset_factory(Chiller,CapacityFunction,form=CapFuncForm)
EIRInline=inlineformset_factory(Chiller,EIRofTemp,form=EIRFuncForm)
PLRInline=inlineformset_factory(Chiller,EIRofPLR,form=PLRFuncForm)