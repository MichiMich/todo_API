from tokenize import Number, String
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# define class with id, title, description, all strings
class Todo(BaseModel):
    id : str
    title : str
    description : str

todoList = []

def get_index_of_id(id: str):
    for i in range(0,len(todoList),1):
        if todoList[i].id == id:
            return i
    return -1

# Get all To-Do objects
@router.get("/")
async def get_all():
    # we should show all list data
    return todoList

# Get To-Do object by id
@router.get("/{id}")
async def get_by_id(id: str):
    #check if exists, otherwise throw 404 error
    index = get_index_of_id(id)
    if index != -1:
        return todoList[index]
    # element not found in list
    raise HTTPException(status_code=404, detail="id not found")


# create new todo object
@router.put("/")
async def create_new(todo: Todo):
    # add todo to list
    todoList.append(todo)
    #show added object
    return todo

# Update existing To-Do object
@router.put("/{todo_id}")
async def update_existing(todo_id: str, todo: Todo):
    # update element if existent
    index = get_index_of_id(todo_id)
    if index != -1:
        todoList[index] = todo
        return todo
    #show added data
    raise HTTPException(status_code=404, detail="given id does not exist")


# Delete existing To-Do object
@router.delete("/{todo_id}")
async def delete_existing(todo_id: str):
    # delete element if existent
    index = get_index_of_id(todo_id)
    if index != -1:
        todoList.pop(index)
        return "element successfully deleted"
    # element not found in list
    raise HTTPException(status_code=404, detail="given id does not exist")


# create new object, id needs to be provided
# @router.put("/{todo_id}")
# async def create_todo(todo_id: int, todo: Todo):
#     if todo_id in todoList:
#         return {"error": "id already exists, try updating it"}
#     # add todo to list
#     todoList[todo_id] = todo
#     #show added data
#     return todoList[todo_id]


