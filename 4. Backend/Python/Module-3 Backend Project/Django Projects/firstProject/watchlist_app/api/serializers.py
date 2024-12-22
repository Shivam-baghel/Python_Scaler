from rest_framework import serializers
from watchlist_app.models import WatchList


class WatchlistSerializer(serializers.ModelSerializer):
# model serializer class already has the create and update functions.
# no need to write them again.

    #This is custom field
    len_names = serializers.SerializerMethodField()
    
    class Meta:
        model = WatchList
        fields = "__all__"
        # fields = ['id', 'name', 'description']
        # exclude = ['active']
      
    # what are custom len_names field will do.  
    def get_len_names(self, object):
        
        return len(object.title)
        
    # object level validation
    def validate(self, data):
        
        if data['title'] == data['storyline']:
            raise serializers.ValidationError(" title and stroyline should be different.")
        else:
            return data
       
    # field level validation. In field level validation we provide field name too.
    # as you can see below but for object level(which is above) we have not done so.
    def validate_title(self, data):
        
        if len(data) < 2:
            raise serializers.ValidationError("title is too short !!")
        else:
            return data
        
        

# class MovieSerializer(serializers.Serializer):
    
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
    
#     def create(self, validate_data):
        
#         return Movie.objects.create(**validate_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance
#         # return super().update(instance, validated_data)
    
#     # object level validation
#     def validate(self, data):
        
#         if data['name'] == data['description']:
#             raise serializers.ValidationError(" Name and Description should be different.")
#         else:
#             return data
       
#     # field level validation. In field level validation we provide field name too.
#     # as you can see below but for object level we have not done so.
#     def validate_name(self, data):
        
#         if len(data) < 2:
#             raise serializers.ValidationError("Name is too short !!")
#         else:
#             return data