from django.db import models
from .utils import get_current_timestamp, get_current_timestamp_id, get_readable_timestamp
# Create your models here.

class Tasks:
    id: int
    name: str
    description: str

    def __init__(self, name, description):
        self.id = get_current_timestamp_id()
        self.name = name
        self.description = description
        self.is_done = False
        self.created_at = get_current_timestamp()
        self.ended_at = None

    def mark_as_done(self):
        self.is_done = True
        self.ended_at = get_current_timestamp()

    def __str__(self):
        return f"""
    <h3>{self.name}</h3>
    <h4>id: {self.id}</h4>
    <p>{self.description}</p>
    <p>is done: {self.is_done}</p>
    <p>created at: {get_readable_timestamp(self.created_at)}</p>
    <p>ended at: {get_readable_timestamp(self.ended_at) if self.ended_at else "not ended"}</p>
    """

tasks = [
    Tasks('first task', 'description task 1'),
    Tasks('second task', 'description task 2'),
    Tasks('third task', 'description task 3'),
    Tasks('fourth task', 'description task 4'),
]


