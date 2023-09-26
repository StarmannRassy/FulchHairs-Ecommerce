#from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
class TokenGenerator(PasswordResetTokenGenerator):
    #def _make_hash_value(self, user: AbstractBaseUser, timestamp: int) -> str:
        #return super()._make_hash_value(user, timestamp)
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.pk)+six.text_type(timestamp)+six.text_type(user.is_active))
    
generate_token=TokenGenerator()