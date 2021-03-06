from slim.support.peewee import PeeweeView

from app import app
from model.example import Example


@app.route.view('example', 'Example API')
class ExampleView(PeeweeView):
    model = Example
