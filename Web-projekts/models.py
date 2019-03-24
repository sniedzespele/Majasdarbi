from smartninja_nosql.odm import Model


class User(Model):
    def __init__(self, name, email, password=None, session_token=None, **kwargs):
        self.name = name
        self.email = email
        self.password = password
        self.session_token = session_token
        super().__init__(**kwargs)


class Article(Model):
    def __init__(self, title, content, main_image=None, **kwargs):
        self.title = title
        self.content = content
        self.main_image = main_image
        super().__init__(**kwargs)
