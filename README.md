# Partial updates via POST with Django Rest Framework
Simple DRF ModelViewSet that allows partial updates via POST to the root endpoint of the viewset.

In this example we have a viewset `testapp.views.XViewSet`, which uses the serializer `testapp.serializers.XSerializer` and a queryset utilizing `testapp.models.Test`.

If we POST to http://127.0.0.1:8000/testapp/x/users we get the following behaviour:

* No primary key supplied: exception (can be handled in XViewSet.get_object())
* Primary key (`subscriber_key`) supplied and nothing else:
  * PKey exists in DB: Partial update, nothing changes.
  * PKey doesn't exist: Normal validation errors about required fields.
* Primary key supplied with only `direct` field:
  * PKey exists in DB: Partial update, only updating the `direct` field.
  * PKey doesn't exist: Normal validation error for field `methods`
* Primary key supplied with only `methods` field:
  * PKey exists in DB: Partial update, only updating the `methods` field and altering the value saved to DB by the `validate_methods` field.
  * PKey doesn't exist: Normal validation error for the field `direct`  
  
Note: actually PUT/PATCH to `/users/[subscriber_key]` don't work completely as expected since subscriber_key is a required field and must be in the data. Most likely not too difficult to fix but I'm done. At least the `/users/[subscriber_key]` endpoint form does correctly populate this data.
