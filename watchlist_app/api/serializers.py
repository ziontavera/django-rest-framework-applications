from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ['watchlist', ]


class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.site_name')

    class Meta:
        model = WatchList

        fields = "__all__"  # have access to all attributes

        # fields = ['id', 'title', ] - filtered attributes

        # exclude = ['is_active'] - excluded attributes

    # # field-level validation
    # def validate_title(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Title too short")
    #     else:
    #         return value

    # # object-level validation
    # def validate(self, data):
    #     if data['title'] == data['description']:
    #         raise serializers.ValidationError(
    #             "Title and description should be different")
    #     else:
    #         return data

    # def title_length(title):
    #     if len(title) < 2:
    #         raise serializers.ValidationError("Title too short")

    # class MovieSerializer(serializers.Serializer):
    #     id = serializers.IntegerField(read_only=True)
    #     title = serializers.CharField()
    #     description = serializers.CharField()
    #     is_active = serializers.BooleanField()

    #     # field-level validation
    #     def validate_title(self, title):
    #         if len(title) < 2:
    #             raise serializers.ValidationError("Title too short")
    #         else:
    #             return title

    #     # object-level validation
    #     def validate(self, data):
    #         if data['title'] == data['description']:
    #             raise serializers.ValidationError(
    #                 "Title and description should be different")
    #         else:
    #             return data

    #     def create(self, validated_data):
    #         return Movie.objects.create(**validated_data)

    #     def update(self, instance, validated_data):
    #         instance.title = validated_data.get('title', instance.title)
    #         instance.description = validated_data.get(
    #             'description', instance.description)
    #         instance.is_active = validated_data.get(
    #             'is_active', instance.is_active)
    #         instance.save()
    #         return instance


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = ['id', 'site_name', 'description', 'website', 'watchlist']
