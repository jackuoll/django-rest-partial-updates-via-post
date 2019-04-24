from .models import Test
from rest_framework import serializers


class XSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = [x.name for x in Test._meta.fields]

    def validate_methods(self, value):
        # validation runs on the initial data, so if the user didn't POST/PUT this field, the original value from the
        # object is taken. if the original object is new, the field is blank/null depending on the field settings
        # if this is not a partial update and this field is required/not supplied, it will throw a normal required error
        if value == "alterme":
            value = "ok, altered"
        elif not value:
            value = "this is impossible!"
        return value
