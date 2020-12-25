from django import forms


class CreateUrlHashForm(forms.Form):
    """Form to create url hash."""

    url = forms.CharField(label='Url')
    no_of_expiry_clicks = forms.IntegerField(
        label='Expire the link after no of clicks',
        min_value=0
    )
