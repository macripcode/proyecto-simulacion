from django import forms


class InputForm(forms.Form):

	numero_retadores = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'input_numero_retadores', 'class':'validate'}), min_value=0)
	tiempo_llegadas = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'input_tiempo_llegadas', 'class':'validate'}), min_value=0)
	desviacion_tiempo = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'input_desviacion_tiempo', 'class':'validate'}), min_value=0)
	numero_reinas = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'input_numero_reinas', 'class':'validate'}), min_value=1)
   
