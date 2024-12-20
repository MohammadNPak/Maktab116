from django import template
import re

register = template.Library()

@register.filter
def highlight(text,query):
    if query:
        pattern = re.compile(re.escape(query),re.IGNORECASE)
        return pattern.sub(lambda p: f'<mark>{p.group(0)}</mark>',text)
    return text