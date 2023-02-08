from django.contrib import admin
from .models import Registration
from .models import Winnings
from .models import matchschedule
from .models import sliderimg
# Register your models here.

admin.site.register(Registration)

admin.site.register(Winnings)

admin.site.register(matchschedule)

admin.site.register(sliderimg)