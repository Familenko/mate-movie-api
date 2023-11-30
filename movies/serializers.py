from rest_framework import serializers

from movies.models import Certification, Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=250)
    year = serializers.IntegerField()
    time = serializers.IntegerField()
    imdb = serializers.FloatField()
    votes = serializers.IntegerField()
    meta_score = serializers.FloatField(allow_null=True)
    gross = serializers.FloatField(allow_null=True)
    certification = serializers.PrimaryKeyRelatedField(
        queryset=Certification.objects.all(), many=False
    )
    description = serializers.CharField()

    def create(self, validated_data):
        certification = validated_data.pop("certification")
        movie = Movie.objects.create(**validated_data)
        movie.certification.set(certification)
        return movie

    def update(self, instance, validated_data):
        certification_data = validated_data.pop("certification", [])

        instance.name = validated_data.get("name", instance.name)
        instance.year = validated_data.get("year", instance.year)
        instance.time = validated_data.get("time", instance.time)
        instance.imdb = validated_data.get("imdb", instance.imdb)
        instance.votes = validated_data.get("votes", instance.votes)
        instance.meta_score = validated_data.get("meta_score", instance.meta_score)
        instance.gross = validated_data.get("gross", instance.gross)
        instance.description = validated_data.get("description", instance.description)

        is_partial = self.context["request"].method == "PATCH"
        if certification_data:
            if is_partial:
                instance.certification.add(*certification_data)
            else:
                instance.certification.set(certification_data)
        instance.save()
        return instance
