from rest_framework import serializers

from apps.domain.models import Attribute
from apps.conditions.models import Condition

from .models import Task, TimeFrame
from .validators import TaskUniqueKeyValidator


class TaskIndexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = (
            'id',
            'key',
            'title',
            'text'
        )


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = (
            'id',
            'uri_prefix',
            'key',
            'comment',
            'title_en',
            'title_de',
            'text_en',
            'text_de',
            'conditions'
        )
        validators = (TaskUniqueKeyValidator(), )


class TimeFrameSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeFrame
        fields = (
            'id',
            'task',
            'start_attribute',
            'end_attribute',
            'days_before',
            'days_after'
        )


class AttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attribute
        fields = (
            'id',
            'path',
            'value_type'
        )


class ConditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Condition
        fields = (
            'id',
            'key'
        )


class ExportSerializer(serializers.ModelSerializer):

    attribute = serializers.CharField(source='attribute.uri')
    conditions = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = (
            'uri',
            'comment',
            'attribute',
            'time_period',
            'title_en',
            'title_de',
            'text_en',
            'text_de',
            'conditions'
        )

    def get_conditions(self, obj):
        return [condition.uri for condition in obj.conditions.all()]
