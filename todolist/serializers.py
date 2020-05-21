from datetime import date

from rest_framework import serializers

from todolist.models import TodoItem


class TodoItemSerializer(serializers.Serializer):
    class Meta:
        model = TodoItem
        fields = '__all__'

    def create(self, validated_data):
        return TodoItem.objects.create(**validated_data)

    def validate_done_date(self):
        dd = self.initial_data
        if dd["done"]:
            if not dd["done_date"]:
                dd["done_date"] = date.today()
        else:
            if dd.done_date:
                raise serializers.ValidationError("You cannot assign done_date if done is False")

