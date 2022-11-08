from django import forms
from .models import Applicant, Contact, Newsletter

class ApplicantForm(forms.ModelForm):
    #test = forms.CharField(max_length=30, widget=forms.Textarea(attrs={"class":"mt-5", "placeholder":"Test"}))
    class Meta:
        model = Applicant
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].label = "Ваше имя"
        self.fields["email"].label = "Ваша электронная почта"
        self.fields["location"].label = "Ваше местоположение"
        self.fields["comment"].label = "Комментарий"

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].label = "Ваше имя"
        self.fields["email"].label = "Ваша электронная почта"
        self.fields["location"].label = "Ваше местоположение"
        self.fields["message"].label = "Ваше сообщение"

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"