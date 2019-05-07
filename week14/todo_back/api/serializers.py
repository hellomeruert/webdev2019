from rest_framework import serializers
from .models import Task,TaskList
from django.contrib.auth.models import User

class ListSerializer(serializers.Serializer):
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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('id','username', 'email',)



# class TaskSerializer2(serializers.ModelSerializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(required=True)
#     status=serializers.CharField(read_only=True)
#     created_at=serializers.DateTimeField(read_only=True)
#     due_on=serializers.DateTimeField(read_only=True)
#     task_list=ListSerializer2(read_only=True)
#     created_by =UserSerializer(read_only=True)
#     class Meta:
#         model= Task
#         fields=('id','name','created_by','status','created_at','due_on','task_list',)
#
#



class TaskSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(required=True)
    status=serializers.CharField(read_only=True)
    created_at=serializers.DateTimeField(read_only=True)
    due_on=serializers.DateTimeField(read_only=True)
    created_by = UserSerializer(read_only=True)
    task_list_id=serializers.IntegerField(write_only=True)

    class Meta:
        model = Task
        fields  = ('id','name','status','created_at','due_on','created_by','task_list_id',)

class TaskSerializer2(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(required=True)
    status=serializers.CharField(read_only=True)
    created_at=serializers.DateTimeField(read_only=True)
    due_on=serializers.DateTimeField(read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields  = ('id','name','status','created_at','due_on','created_by',)


class TaskListSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_by= UserSerializer(read_only=True)
    # tasks = TaskSerializer2(many=True)
    class Meta:
        model = TaskList
        fields = ('id', 'name','created_by',)

    # def create(self, validated_data):
    #     tasks=validated_data.pop('tasks')
    #     list=TaskList.objects.create(**validated_data)
    #     for task in tasks:
    #         Task.objects.create(task_list=list,**task)
    #     return list
