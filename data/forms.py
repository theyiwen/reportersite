from django.forms import ModelForm
from django import forms
from data.models import Day, Sleep, HappyLog, UnhappyLog, Exercise, FoodScore, HappyScore, TestModel
from django.forms.models import modelformset_factory

class DayForm(ModelForm):
	class Meta:
		model = Day

class SleepForm(ModelForm):
	class Meta:
		model = Sleep
		exclude = ('date','day',)
	
	def clean(self):
	    cleaned_data = super(SleepForm, self).clean()
	    if cleaned_data.get('time_slept') == None or cleaned_data.get('time_awake') == None:
	        raise forms.ValidationError("Sleep not saved")
	    return cleaned_data

class FoodForm(ModelForm):
	class Meta:
		model = FoodScore
		exclude = ('date','day',)
	
	def clean(self):
	    cleaned_data = super(FoodForm, self).clean()
	    if cleaned_data.get('g_score') == None and cleaned_data.get('p_score') == None:
	        raise forms.ValidationError('Food not saved')
	    return cleaned_data

class ExerciseForm(ModelForm):
	class Meta:
		model = Exercise
		exclude = ('date','day',)
		
class HSForm(ModelForm):
	class Meta:
		model = HappyScore
		exclude = ('date','day',)
	
	def clean(self):
	    cleaned_data = super(HSForm, self).clean()
	    if cleaned_data.get('score') == None:
	        raise forms.ValidationError("HS not saved")
	    return cleaned_data

class HappyForm(ModelForm):
	class Meta:
		model = HappyLog
		exclude = ('date','day',)

class UnhappyForm(ModelForm):
	class Meta:
		model = UnhappyLog
		exclude = ('date','day',)
		
class TestForm(ModelForm):
	class Meta:
		model = TestModel
		exclude = ('day',)