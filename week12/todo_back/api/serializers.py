from rest_framework import serializers
from .models import Task,TaskList

class TaskListSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(required=True)

    def create(self,validated_data):
        li=TaskList(**validated_data)
        li.save()
        return li

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.save()
        return instance


class TaskListSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = TaskList
        fields = ('id', 'name',)


class TaskSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(required=True)
    # task_list=ListSerializer()
    status=serializers.CharField(read_only=True)
    created_at=serializers.DateTimeField(read_only=True)
    due_on=serializers.DateTimeField(read_only=True)
    listik=TaskList()

    def create(self,validated_data):
        li=Task(**validated_data)
        li.task_list=TaskSerializer.listik
        li.save()
        print(TaskSerializer.listik)
        return li

    # def update(self, instance, validated_data):
    #     instance.name=validated_data.get('name',instance.name)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.save()
    #     return instance

