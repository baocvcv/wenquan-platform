""" Serializers for Paper Record """
from rest_framework import serializers

# from backend.models import QuestionRecord
from backend.models import PaperRecord
from backend.models import Paper

class PaperRecordSerializer(serializers.ModelSerializer):
    "Serializer for PaperRecord"
    paper_id = serializers.IntegerField(source="paper.id")
    paper_name = serializers.CharField(source="paper.title")
    is_active = serializers.BooleanField(default=True)
    record_time = serializers.DateTimeField(read_only=True)
    time_left = serializers.IntegerField(read_only=True)
    paper_total_points = serializers.IntegerField(source="paper.total_point")
    user_total_points = serializers.IntegerField(read_only=True)
    need_judging = serializers.BooleanField(read_only=True)
    owner = serializers.IntegerField(source="user.id")

    def create(self, validated_data):
        " Creat paper record "
        paper = Paper.objects.get(id=validated_data['paper_id'])
        paper_record = PaperRecord(
            paper=paper,
            is_timed=validated_data['is_timed'],
            time_left=paper.time_limit,
            need_judging=paper.have_brief_ans,
        )
        paper_record.save()
        return paper_record

    def to_representation(self, instance):
        """Add points"""
        instance.update_time()
        instance.judge()
        ret = super().to_representation(instance)
        return ret

    class Meta:
        model = PaperRecord
        fields = [
            "id",
            "paper_id",
            "paper_name",
            "record_time",
            "is_timed",
            "is_active",
            "time_left",
            "paper_total_points",
            "user_total_points",
            "need_judging",
            "owner",
        ]
