from django import forms
import csv
from .models import Glass
import io

class UploadFileForm(forms.Form):
	data_file = forms.FileField()

	def clean_data_file(self):
		f=self.cleaned_data['data_file']
		if f:
			ext=f.name.split('.')[-1]
			if ext != 'csv':
				raise forms.ValidationError('File Type not Supproted')
		return f

	def process_data(self):
		print (self.cleaned_data['data_file'].file)
		f=io.TextIOWrapper(self.cleaned_data['data_file'].file)
		reader=csv.DictReader(f)

		for data in reader:
			#data=data.split(',')
			tmp=Glass.objects.create()
			#print data
			tmp.title=data['ProductName']
			tmp.manufacturer=data['Manufacturer']
			tmp.thickness=data['Thickness']
			tmp.tsol=data['Tsol']
			tmp.rsol1 = data['Rsol1']
			tmp.rsol2 = data['Rsol2']
			tmp.tvis = data['Tvis']
			tmp.rvis1 = data['Rvis1']
			tmp.rvis2 = data['Rvis2']
			tmp.emis1 = data['emis1']
			tmp.emis2 = data['emis2']
			tmp.conductivity = data['Conductivity']
			tmp.tvis2 = data['Tvis2']
			tmp.tsol2 = data['Tsol2']
			tmp.save()

	#class Meta:
	#	model = Glass

