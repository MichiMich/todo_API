from fastapi import APIRouter

router = APIRouter()



@router.get("/")
async def get_users():
    return {"message": "Get Users"}

# because of ther outer / leads us to users

#if we would create a new route like the following, it would lead us to /users/new

# found at: /users/new
@router.get("/new")
async def get_new_users():
      return {"message": "Get New Users"}