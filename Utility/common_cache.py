class CommonCache:
    email = None

    @staticmethod
    def set_email(email):
        if CommonCache.email is None:
            CommonCache.email = email
        return CommonCache.email
