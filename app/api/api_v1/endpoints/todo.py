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

todoList = [harry]

def get_list_index_of_id(id: str):
    for i in range(0,len(todoList),1):
        if todoList[i].id == id:
            return i
    return -1

print(get_list_index_of_id("1"))
print(get_list_index_of_id("2"))


@router.get("/")
async def get_todo():
    # we should show all list data
    return todoList



@router.get("/{id}")
async def get_todo_with_id(id: str):
    #check if exists, otherwise throw 404 error
    index = get_list_index_of_id(id)
    if index != -1:
        return todoList[index]
    # element not found in list
    raise HTTPException(status_code=404, detail="id not found")


# create new todo element by appending
@router.put("/")
async def create_todo(todo: Todo):
    # add todo to list
    todoList.append(todo)
    #show added data
    return todo





@router.put("/{todo_id}")
async def update_todo(todo_id: str, todo: Todo):
    # update element if existent
    index = get_list_index_of_id(todo_id)
    if index != -1:
        todoList[index] = todo
        return todo
    #show added data
    raise HTTPException(status_code=404, detail="id does not exist")




# create new object, id needs to be provided
# @router.put("/{todo_id}")
# async def create_todo(todo_id: int, todo: Todo):
#     if todo_id in todoList:
#         return {"error": "id already exists, try updating it"}
#     # add todo to list
#     todoList[todo_id] = todo
#     #show added data
#     return todoList[todo_id]


