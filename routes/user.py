from fastapi import APIRouter, HTTPException, status
from models.user import User
from config.db import get_db
from bson import ObjectId
from schemas.user import userEntity, usersEntity

user = APIRouter()


@user.get('/')
async def find_all_users():
    db = get_db()
    return usersEntity(db.user.find())


@user.get('/{id}')
async def find_one_user(id: str):
    db = get_db()
    user_data = db.user.find_one({"_id": ObjectId(id)})
    if user_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return userEntity(user_data)


@user.post('/register', status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    db = get_db()
    existing_user = db.user.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    db.user.insert_one(dict(user))
    return userEntity(db.user.find_one({"email": user.email}))


@user.put('/{id}')
async def update_user(id: str, user: User):
    db = get_db()
    updated_user = db.user.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(user)}
    )
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return userEntity(db.user.find_one({"_id": ObjectId(id)}))


@user.delete('/{id}')
async def delete_user(id: str):
    db = get_db()
    deleted_user = db.user.find_one_and_delete({"_id": ObjectId(id)})
    if deleted_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return userEntity(deleted_user)
