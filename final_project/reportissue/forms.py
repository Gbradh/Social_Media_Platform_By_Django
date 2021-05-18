from django import forms
from reportissue.models import ReportIssue

class ReportForm(forms.ModelForm):
	class Meta:
		model = ReportIssue
		fields = ('name','message')
