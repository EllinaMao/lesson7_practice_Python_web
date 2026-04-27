from django.http import JsonResponse
from .models import Tasks as Task, tasks
from django.http import HttpRequest, HttpResponse
from django.views import View
from http import HTTPStatus
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

from .serializers import TaskSerializer

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    return JsonResponse(
        {
            "message": "welcome to task manager api",
            "endpoints": 
            {
            "get":"/tasks/ - get all tasks",
            "post":"/tasks/add/ - add new task",
            "delete":"/tasks/delete/?id=task_id - delete task by id"
            }
        }, status=HTTPStatus.OK, json_dumps_params={"indent": 4})

@method_decorator(csrf_exempt, name='dispatch')
class TaskView(View):
    
    def get(self, request: HttpRequest) -> HttpResponse:
        if len(tasks) < 0:
            return JsonResponse({"message": "no tasks"}, status=HTTPStatus.NOT_FOUND)
        r = JsonResponse(tasks, encoder=TaskSerializer, safe=False)
        return r

    
    def post(self, request: HttpRequest) -> HttpResponse:
        try:
            data = json.loads(request.body)
            newtask = Task(data.get("name", None), data.get("description", None))

            tasks.append(newtask)
            return JsonResponse(newtask, encoder=TaskSerializer, safe=False, status=HTTPStatus.CREATED)

        except Exception as e:
            return JsonResponse({"message": str(e)}, status=HTTPStatus.BAD_REQUEST)
    
    def delete(self, request: HttpRequest) -> HttpResponse:
        param_id = request.GET.get("id", None)

        if param_id is None:
            return JsonResponse({"message": "id is required"}, status=HTTPStatus.BAD_REQUEST)
        
        for task in tasks:
            if task.id is not None:
                try:
                    id = int(param_id)
                    result = list(filter(lambda t: t.id == id, tasks))
                    if len(result) < 1:
                        return JsonResponse({"message": f"task with id {id} not found"}, status=HTTPStatus.NOT_FOUND)
                    tasks.remove(result[0])
                    return JsonResponse(result[0], encoder=TaskSerializer, safe=False)
                
                except ValueError:
                    return JsonResponse({"message": f"invalid id {param_id}"}, status=HTTPStatus.BAD_REQUEST)

        return JsonResponse({"message": "task not found"}, status=HTTPStatus.NOT_FOUND)