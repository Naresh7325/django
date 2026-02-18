from django import forms
from .models import Service

#employee form
#modelForm -->it will create form using model fileds
class servicesform(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__' #[name,age,salary,joiningDate,post]
