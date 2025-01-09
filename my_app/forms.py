from django import forms
from .models import Blog, Author

class BlogForm(forms.ModelForm):
   author = forms.ModelChoiceField(
       queryset=Author.objects.all(),
       empty_label="Select an author",
    #    widget=forms.Select(attrs={
    #        'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm'
    #        })
   )

   class Meta:
       model = Blog
       fields = ['title', 'content', 'author']
    #    widgets = {
    #        'title': forms.TextInput(attrs={
    #            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm'
    #            }),
    #        'content': forms.Textarea(attrs={
    #            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm h-32'
    #            }),
    #     #    'published_date': forms.DateTimeInput(attrs={
    #     #        'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm',
    #     #        'type': 'datetime-local'
    #     #    }),
    #    }

