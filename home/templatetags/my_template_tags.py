from django.template import library




register = library.Library()




@register.inclusion_tag('home/result.html')
def show_result(queryset):
    return {'objects': queryset}

