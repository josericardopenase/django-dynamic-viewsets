from django.shortcuts import render
from rest_framework import viewsets
from abc import ABC

# Create your views here.

class DynamicViewSet(viewsets.ModelViewSet, ABC):

    """

        DynamicViewSet():

        View set that aggregate a action_fields dict which
        contains the fields of the serializer per action type.


    """
    
    action_fields = {}

    def get_serializer_class(self):

        """

        get_serializer_class()

        We create the serializer using a concrete fields.

        """

        try:

            serializer =  lambda serializer, fields : lambda *args, **kwargs : serializer(fields = fields, *args, **kwargs)

            if('all' in self.action_fields):
                return serializer(self.serializer_class, self.action_fields['all'])
            else:
                return serializer(self.serializer_class, self.action_fields[self.action])

        except:
            return self.serializer_class
