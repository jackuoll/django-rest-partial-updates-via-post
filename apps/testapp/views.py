from rest_framework import viewsets
from .models import Test
from .serializers import XSerializer


class XViewSet(viewsets.ModelViewSet):
    """this is some docstring to explain what's different about this than a normal ModelViewSet"""
    queryset = Test.objects.all()
    serializer_class = XSerializer

    def get_object(self):
        """This is overridden to get the object from request.data.subscriber_key, when posting to the root X endpoint,
        which is not default DRF behaviour"""
        try:
            # this allows detail view, PUT/PATCH/DELETE to work, although currently not implemented
            obj = super(XViewSet, self).get_object()
        except AssertionError:
            try:
                # if subscriber key not in url, get it from POST. currently always the case.
                obj = self.queryset.get(pk=self.request.data['subscriber_key'])
            except Test.DoesNotExist:
                return None

        self.check_object_permissions(self.request, obj)
        return obj

    def create(self, request):
        """Override create so that we create a new object when one is not found, and do a partial update when the object
        is found."""
        if not self.get_object():
            return super(XViewSet, self).create(request)
        return self.partial_update(request, pk=request.data['subscriber_key'])
