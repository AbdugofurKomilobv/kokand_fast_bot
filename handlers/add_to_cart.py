from aiogram.types import CallbackQuery
from aiogram import F


from router import router
from loader import db



@router.callback_query(F.data.split(":")[0] == "add_to_cart")
async def add_to_cart(call: CallbackQuery):
    quantity = call.data.split(":")[1]
    product_id = call.data.split(":")[2]
    telegram_id = call.from_user.id
    user = db.get_user(telegram_id=telegram_id)
    user_id = user.get('id')

    db.add_to_cart(user_id=user_id,product_id=product_id,quantity=quantity)

    await call.message.delete()
    await call.message.answer(text="Maxsulot savatchangizga qo'shildi", show_alter = True)