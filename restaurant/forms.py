from django.forms import ModelForm
from .models import Booking

# Add loading form data in the booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"