from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field,HTML,ButtonHolder,Submit

from .models import Profile,City

class ProfileForm(forms.ModelForm):
    select2script = """
                    <script>
                    $('#id_contry').change(function(){
                        const url =$('#profileForm').attr("action");
                        const contryId = $(this).val();

                        $.ajax({
                            url: url,
                            data:{
                                'country_id':countryId
                            },
                            success: function(data){
                                $('#id_city').html(data);
                            }
                        });
                    });
                    </script>
    
                   """
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(Field('name','contry','city',HTML(self.select2script),ButtonHolder(Submit('submit','Submit',css_class='button white'))))
        self.fields['city'].queryset = City.objects.none()
        
        if 'contry' in self.data:

            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except(ValueError,TypeError):
                pass

        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
    
    class Meta:
        model = Profile
        fields = '__all__'