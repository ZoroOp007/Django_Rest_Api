from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "title",
            "amount",
            "transaction_type",
        ]

        # In big projects instead of mentioning all the fields we can just write 
        #
        # fields = '__all__'
        # exclude = ['transaction_type','amount']
        #
        #
