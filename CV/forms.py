from django import forms

from .models import About, Skills, Interests, Experience, Education


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'

        widgets = {
            'job_title': forms.TextInput(),
            'job_description': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
            'job_company': forms.TextInput(),
            'job_start_date': forms.DateInput(format='%d/%m/%Y'),
            'job_end_date': forms.DateInput(format='%d/%m/%Y'),
        }


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

        widgets = {
            'about': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'

        widgets = {
            'skills': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }


class InterestsForm(forms.ModelForm):

    class Meta:
        model = Interests
        fields = '__all__'

        widgets = {
            'interests': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

        widgets = {
            'certificate_title': forms.TextInput(),
            'certificate_description': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
            'certificate_start_date': forms.DateInput(format='%d/%m/%Y'),
            'certificate_end_date': forms.DateInput(format='%d/%m/%Y'),
            'certificate_institute': forms.TextInput(),
        }
