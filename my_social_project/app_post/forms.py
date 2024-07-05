from django import forms


from app_post.models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields=['image','caption']
        