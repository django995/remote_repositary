from django import forms

class FeedbackForm(forms.Form):
        Name = forms.CharField(
            label="Enter Your Name",
            widget=forms.TextInput(
                attrs=
                {
                    'placeholder': 'Your Name',
                    'class': 'form-control'
                }
            )
        )
        Rating = forms.IntegerField(
            label="Enter Your Rating",
            widget=forms.NumberInput(
                attrs=
                {
                    'placeholder': 'Your Rating',
                    'class': 'form-control'
                }
            )
        )
        Feedback = forms.CharField(
            label="Enter Your Feedback",
            widget=forms.Textarea(
                attrs=
                {
                    'placeholder': 'Your Feedback',
                    'class': 'form-control'
                }
            )
        )
