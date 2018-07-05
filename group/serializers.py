from rest_framework import serializers
from group.models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('groupIndex','groupName','essIndex24','essIndex5','apType','active')