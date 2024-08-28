from mongoengine import Document, StringField
import bcrypt

class User(Document):
    username = StringField(min_length=4, required=True, unique=True)
    password = StringField(required=True)

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('$2b$'):
            self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return super(User, self).save(*args, **kwargs)
