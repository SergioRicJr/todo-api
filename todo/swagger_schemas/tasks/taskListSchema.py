from drf_yasg import openapi

taskListSchema = openapi.Schema(
    title="Succesfull schema",
    type=openapi.TYPE_OBJECT,
    properties={
        "detail": openapi.Schema(type=openapi.TYPE_STRING),
        "object": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                    "title": openapi.Schema(type=openapi.TYPE_STRING),
                    "description": openapi.Schema(type=openapi.TYPE_STRING),
                    "due_date": openapi.Schema(type=openapi.TYPE_STRING),
                    "completed": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                    "user": openapi.Schema(type=openapi.TYPE_INTEGER),
                    "task_type": openapi.Schema(type=openapi.TYPE_INTEGER)
                }
            )
        )
    }
)