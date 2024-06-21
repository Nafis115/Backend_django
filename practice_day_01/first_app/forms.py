from django import forms
from first_app.models import Goods

class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = '__all__'
