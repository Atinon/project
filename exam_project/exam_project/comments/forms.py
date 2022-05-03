from django import forms

from exam_project.comments.models import ProfileComments


class CommentsForm(forms.ModelForm):
    def __init__(self, author, receiver, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.author = author
        self.receiver = receiver

    # def __init__(self, author,  *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.author = author

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.receiver = self.receiver
        if commit:
            comment.save()
        return comment

    class Meta:
        model = ProfileComments
        fields = ('comment_text',)
