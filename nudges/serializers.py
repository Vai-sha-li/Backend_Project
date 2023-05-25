from rest_framework import serializers
from nudges.models import Nudge

class NudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nudge
        fields = '__all__'
