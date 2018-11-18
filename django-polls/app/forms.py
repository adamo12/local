from django import forms

from .models import Topic, Entry, Client, Server, Instance

class TopicForm(forms.ModelForm):
	class Meta:
	
		model = Topic
		fields = ['text']
		labels = {'text':''}
	

class EntryForm(forms.ModelForm):
	class Meta:
	
		model = Entry
		fields = ['text']
		labels = {'text':''}
		widgets = {'text': forms.Textarea(attrs={'rows': 1, 'cols': 80})}

class ClientForm(forms.ModelForm):
    class Meta:
	
        model = Client
        fields = ['text']
        labels = {'text':''}
		
class ServerForm(forms.ModelForm):
    class Meta:
	
        model = Server
        fields = ['text', 'ip', 'port', 'username', 'password', 'check_memory', 'check_disk', 'check_cpu', 'check_users', 'check_was', 'check_instance1', 'check_instance2', 'check_instance3', 'check_instance4', 'check_instance5', 'check_instance6', 'check_instance7', 'check_instance8', 'check_instance9', 'check_instance10' ]
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'rows': 1, 'cols': 60}), 'password': forms.PasswordInput()}
		
class InstForm(forms.ModelForm):
    class Meta:
        model = Instance
        fields = ['text', 'pid', 'status']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'rows': 1, 'cols': 80})}
        
		
		
		