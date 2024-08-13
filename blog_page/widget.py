


from django import forms
from django.templatetags.static import static

class MoodWidget(forms.Widget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, renderer=None):
        mood_images = [
            static('blog_page/images/crying.png'),
            static('blog_page/images/sad.png'),
            static('blog_page/images/neutral.png'),
            static('blog_page/images/smiling.png'),
            static('blog_page/images/lovely.png')
        ]
        
        html = '<div class="mood-selector">'
        for i, img in enumerate(mood_images):
            checked = 'checked' if str(i+1) == str(value) else ''
            html += f'<img src="{img}" data-value="{i+1}" class="mood-image {checked}" onclick="selectMood(this)" />'
        html += f'<input type="hidden" name="{name}" value="{value}" />'
        html += '</div>'
        
        return html

    class Media:
        css = {
            'all': ('blog_page/css/styles.css',),  # Correct path to your CSS file
        }
        js = ('blog_page/js/mood_widget.js',)  # Correct path to your JS file
