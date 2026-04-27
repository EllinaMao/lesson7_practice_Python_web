from django.core.serializers.json import DjangoJSONEncoder

from .models import Tasks


'''вручную собираем весь объект в словарь, который может быть сериализован в json'''

class TaskSerializer(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, Tasks):
            result = {}
            result["id"] = o.id
            result["name"] = o.name
            result["description"] = o.description
            result["is_done"] = o.is_done
            result["created_at"] = o.created_at
            result["ended_at"] = o.ended_at
            return result
                 
        return super().default(o)
