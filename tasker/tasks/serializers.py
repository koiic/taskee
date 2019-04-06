from rest_framework_mongoengine import serializers
from tasker.tasks.models import Task

class TaskSerializers(serializers.DocumentSerializer):

    class Meta:
        model = Task
        fields = '__all__'



