from django.db import models


class Universe(models.Model):
    name = models.CharField(max_length=40)

    def __repr__(self):
        return f'<Universe[{self.id}]>'
