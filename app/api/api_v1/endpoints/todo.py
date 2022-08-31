from tokenize import Number, String
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# define class with id, title, description, all strings
class Todo(BaseModel):
    id : str
    title : str
    description : str

harry = Todo(id="1", title="Harry", description="dirty harray")

todoList = []


@router.get("/")
async def get_todo():
    # we should show all todo data
    return todoList



@router.get("/{id}")
async def get_todo_with_id(id: str):
    #check if exists, otherwise throw 404 error
    for i in range(0,len(todoList),1):
        if todoList[i].id == id:
            return todoList[i]
    # element not found in list
    raise HTTPException(status_code=404, detail="id not found")


# create new todo element
@router.put("/")
async def create_todo(todo: Todo):
    # add todo to list
    todoList.append(todo)
    #show added data
    return todo


# create new object, id needs to be provided
# @router.put("/{todo_id}")
# async def create_todo(todo_id: int, todo: Todo):
#     if todo_id in todoList:
#         return {"error": "id already exists, try updating it"}
#     # add todo to list
#     todoList[todo_id] = todo
#     #show added data
#     return todoList[todo_id]


