# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormMixin, DeleteView, UpdateView

from CV.forms import ExperienceForm, EducationForm, AboutForm, SkillsForm, InterestsForm
from CV.models import About, Education, Experience, Skills, Interests


class AboutView(ListView):
    model = About

    def get_queryset(self):
        return About.objects.all()


class AboutUpdateView(LoginRequiredMixin, UpdateView, FormMixin):
    login_url = '/login/'
    redirect_field_name = 'CV/about'
    model = About
    form_class = AboutForm

    def get_context_data(self, **kwargs):
        context = super(AboutUpdateView, self).get_context_data(**kwargs)
        text = About.objects.get(pk=self.kwargs.get('pk')).description
        context['form'] = AboutForm(initial={'form': self.object, 'description': text})
        return context

    success_url = reverse_lazy('about')

class EducationView(ListView):
    model = Education

    def get_queryset(self):
        return Education.objects.all()


class EducationUpdateView(LoginRequiredMixin, UpdateView, FormMixin):
    login_url = '/login/'
    redirect_field_name = 'CV/education_list'

    form_class = EducationForm

    model = Education

    def get_context_data(self, **kwargs):
        context = super(EducationUpdateView, self).get_context_data(**kwargs)
        certificate_description = Education.objects.get(pk=self.kwargs.get('pk')).certificate_description
        certificate_title = Education.objects.get(pk=self.kwargs.get('pk')).certificate_title
        certificate_institute = Education.objects.get(pk=self.kwargs.get('pk')).certificate_institute
        certificate_start_date = Education.objects.get(pk=self.kwargs.get('pk')).certificate_start_date
        certificate_end_date = Education.objects.get(pk=self.kwargs.get('pk')).certificate_end_date
        context['form'] = EducationForm(initial={'form': self.object, 'certificate_title': certificate_title,
                                                 'certificate_description': certificate_description,
                                                 'certificate_start_date': certificate_start_date,
                                                 'certificate_end_date': certificate_end_date,
                                                 'certificate_institute': certificate_institute}, )
        return context

    success_url = reverse_lazy('education')


class EducationDeleteView(LoginRequiredMixin, DeleteView):
    model = Education
    ordering = ['-job_start_date']

    success_url = reverse_lazy('education')


class EducationCreateView(LoginRequiredMixin, CreateView, FormMixin):
    login_url = '/login/'
    redirect_field_name = 'CV/education_list'

    form_class = EducationForm

    model = Education

    def get_context_data(self, **kwargs):
        context = super(EducationCreateView, self).get_context_data(**kwargs)
        context['form'] = EducationForm(initial={'form': self.object})
        return context

    success_url = reverse_lazy('education')


class ExperienceView(ListView):
    model = Experience

    def get_queryset(self):
        return Experience.objects.all()


class ExperienceDeleteView(LoginRequiredMixin, DeleteView):
    model = Experience
    ordering = ['-job_start_date']

    success_url = reverse_lazy('experience')


class ExperienceCreateView(LoginRequiredMixin, CreateView, FormMixin):
    login_url = '/login/'
    redirect_field_name = 'CV/experience_list'

    form_class = ExperienceForm

    model = Experience

    def get_context_data(self, **kwargs):
        context = super(ExperienceCreateView, self).get_context_data(**kwargs)
        context['form'] = ExperienceForm(initial={'form': self.object})
        return context

    success_url = reverse_lazy('experience')


class ExperienceUpdateView(LoginRequiredMixin, UpdateView, FormMixin):
    login_url = '/login/'
    redirect_field_name = 'CV/experience_list'

    form_class = ExperienceForm

    model = Experience

    def get_context_data(self, **kwargs):
        context = super(ExperienceUpdateView, self).get_context_data(**kwargs)
        job_description = Experience.objects.get(pk=self.kwargs.get('pk')).job_description
        job_title = Experience.objects.get(pk=self.kwargs.get('pk')).job_title
        job_company = Experience.objects.get(pk=self.kwargs.get('pk')).job_company
        job_start_date = Experience.objects.get(pk=self.kwargs.get('pk')).job_start_date
        job_end_date = Experience.objects.get(pk=self.kwargs.get('pk')).job_end_date
        context['form'] = ExperienceForm(
            initial={'form': self.object, 'job_description': job_description, 'job_title': job_title,
                     'job_company': job_company, 'job_start_date': job_start_date, 'job_end_date': job_end_date})
        return context

    success_url = reverse_lazy('experience')


class SkillsView(ListView):
    model = Skills

    def get_queryset(self):
        return Skills.objects.all()


class SkillsDeleteView(LoginRequiredMixin, DeleteView):
    model = Skills

    def get_success_url(self):
        return reverse_lazy('skills')


class SkillsUpdateView(LoginRequiredMixin, UpdateView, FormMixin):
    login_url = '/login/'
    redirect_field_name = 'CV/skills'
    model = Skills
    form_class = SkillsForm

    def get_context_data(self, **kwargs):
        context = super(SkillsUpdateView, self).get_context_data(**kwargs)
        text = Skills.objects.get(pk=self.kwargs.get('pk')).skills_text
        context['form'] = SkillsForm(initial={'form': self.object, 'skills_text': text})
        return context

    success_url = reverse_lazy('skills')


class SkillsCreateView(LoginRequiredMixin, CreateView, FormMixin):
    login_url = '/login/'
    redirect_field_name = 'CV/skills'
    model = Skills
    form_class = SkillsForm

    def get_context_data(self, **kwargs):
        context = super(SkillsCreateView, self).get_context_data(**kwargs)
        context['form'] = SkillsForm(initial={'form': self.object})
        return context

    success_url = reverse_lazy('skills')


class InterestsView(ListView):
    model = Interests

    def get_queryset(self):
        return Interests.objects.all()


class InterestsDeleteView(LoginRequiredMixin, DeleteView):
    model = Interests


class InterestsUpdateView(LoginRequiredMixin, UpdateView, FormMixin):
    login_url = '/login/'
    redirect_field_name = 'CV/interests'
    model = Interests
    form_class = InterestsForm

    def get_context_data(self, **kwargs):
        context = super(InterestsUpdateView, self).get_context_data(**kwargs)
        text = Interests.objects.get(pk=self.kwargs.get('pk')).interests_text
        context['form'] = InterestsForm(initial={'form': self.object, 'interests_text': text})
        return context

    success_url = reverse_lazy('interests')


class InterestsCreateView(LoginRequiredMixin, CreateView, FormMixin):
    login_url = '/login/'
    redirect_field_name = 'CV/interests'
    model = Interests
    form_class = InterestsForm

    def get_context_data(self, **kwargs):
        context = super(InterestsCreateView, self).get_context_data(**kwargs)
        context['form'] = InterestsForm(initial={'form': self.object})
        return context

    success_url = reverse_lazy('interests')
