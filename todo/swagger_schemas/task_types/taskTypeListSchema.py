from drf_yasg import openapi

taskListSchema = openapi.Schema(
    title="Succesfull schema",
    type=openapi.TYPE_OBJECT,
    properties={
        "detail": openapi.Schema(type=openapi.TYPE_STRING),
        "object": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                    "name": openapi.Schema(type=openapi.TYPE_STRING),
                    "description": openapi.Schema(type=openapi.TYPE_STRING),
                    "user": openapi.Schema(type=openapi.TYPE_INTEGER)
                }
            )
        )
    }
)