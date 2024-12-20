from django import template
import re

register = template.Library()

@register.filter
def highlight(text,query):
    if not query:
        return text
    pattern = re.compile(re.escape(query),re.IGNORECASE)
    return pattern.sub(lambda match:f'<mark>{match.group(0)}</mark>',text)

