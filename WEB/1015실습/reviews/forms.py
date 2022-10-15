from django import forms
from .models import Review
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'movie_name', 'grade', )
        labels = {
            'title': '리뷰제목',
            'content': '리뷰내용',
            'movie_name': '영화제목',
            'grade': '평점',
        }

        error_messages = {
            'grade': {
                'min_value':'0점이하는 지정할 수 없습니다.',
                'max_value':'5점을 초과하여 지정할 수 없습니다.'
            }
        }