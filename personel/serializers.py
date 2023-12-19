from rest_framework import serializers
from .models import Personel, Departman
from django.utils import timezone
from django.db.models import Count


class DepartmanSerializer(serializers.ModelSerializer):
    department_employees = serializers.SerializerMethodField()

    class Meta:
        model = Departman
        fields = (
            "id",
            "name",
            "department_employees",
        )

    def get_department_employees(self, obj):
    #    member_count = obj.Personel.values('departman').aggregate(count=Count('id'))
        member_count = obj.Personel.count()
        return member_count

    

class PersonelSerializer(serializers.ModelSerializer):

    emloyee_years = serializers.SerializerMethodField()
   
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()

    class Meta:
        model = Personel
        fields = (
            "first_name",
            "last_name",
            "title",
            "gender",
            "salary",
            "start_date",
            "departman",
            "user",
            "user_id",
            "emloyee_years",
        )

    def get_emloyee_years(self, obj):
        current_time = timezone.now()
        return current_time.year - obj.start_date.year

    