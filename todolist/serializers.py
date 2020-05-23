from datetime import date

from rest_framework import serializers

from todolist.models import TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'

    def create(self, validated_data):
        return TodoItem.objects.create(**validated_data)

    def validate(self, data):
        if data.get("done"):
            if not data.get("done_date"):
                data["done_date"] = date.today()
        else:
            if data.get("done_date"):
                raise serializers.ValidationError("You cannot assign done_date if done is False")
        return data
