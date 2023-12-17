import dj_rest_auth.serializers


class LoginSerializer(dj_rest_auth.serializers.LoginSerializer):
    username = None