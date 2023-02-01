from django.forms import ModelForm

from todo_app.models import Task, Comment, Tag, Task

class TaskForm(ModelForm):
    '''Pull the 'description' column rom the Task model into a form'''
    class Meta: 
        model = Task
        fields = ['description']

class TagForm(ModelForm):
    '''When the user is trying to tag a Task object, use this form to 
        a) Create a new Tag with the given name if one does not exist, or
        b) Get the existing Tag with the given name if one does, then
        c) Connect the new or existing Tag to the given Task
    '''
    class Meta:
        model = Tag
        fields = ['name']

    def save(self, task, *args, **kwargs):
        tag_name = self.data['name']

        try:
            tag = Tag.objects.get(name=tag_name)
        except Tag.DoesNotExist:
            tag = Tag.objects.create(name=tag_name)  

        task.tags.add(tag) 
class CommentForm(ModelForm):
    
    class Meta:
        model = Comment
        fields = ['body']
    def __init__(self, *args,**kwargs):
        task = kwargs.pop('task_object')
        super().__init__(*args,**kwargs)
        self.instance.task = task