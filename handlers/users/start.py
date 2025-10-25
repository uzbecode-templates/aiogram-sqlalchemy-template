from aiogram import types
from database.models import Users
from database.orm import ORMbase
from database.db import get_session

async def start_handler(message: types.Message):
    async for session in get_session():
        UsersModel = ORMbase(Users, session)
        user = await UsersModel.get(user_id=message.from_user.id)

        if not user:
            await UsersModel.create(
                user_id=message.from_user.id,
                fullname=message.from_user.full_name,
                username=message.from_user.username
            )
            await message.answer("Your profile saved to database successfully!")
        else:
            await message.answer("You are already exist on database.")

async def delete_me(message: types.Message):
    async for session in get_session():
        UsersModel = ORMbase(Users, session)
        user = await UsersModel.get(user_id=message.from_user.id)

        if user:
            await UsersModel.delete(
                user_id=message.from_user.id,
            )
            await message.answer("Your profile deleted successfully!")
        else:
            await message.answer("Your profile not found.")
