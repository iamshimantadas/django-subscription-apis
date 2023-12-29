from rest_framework import serializers

from core.models import OurTeam

class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = ['id','name','designation','description','profileimg']
    
