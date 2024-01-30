from rest_framework_simplejwt.views import TokenBlacklistView

class CustomTokenBlacklistView(TokenBlacklistView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        return response