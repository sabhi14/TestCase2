from rest_framework import serializers

class AccounSerializers(serializers.ModelSerializer):
        class Meta:
                model = AccountDetails
                fields = ['account_id','account_name','time_updated']