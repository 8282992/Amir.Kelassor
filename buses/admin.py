from django.contrib.admin import ModelAdmin , register
from .models import Terminal , Bus


@register (Terminal)
@register (Bus)

class Terminaladmin(ModelAdmin):
    pass

class Busadmin(ModelAdmin):
    pass