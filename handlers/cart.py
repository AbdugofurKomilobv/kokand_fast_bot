from aiogram.types import Message
from aiogram import F

from router import router
from loader import db

from keyboards.inline.cart import generate_cart_menu


@router.message(F.text == "🛒 Savatcha")
async def cart(message:Message):
    telegram_id = message.from_user.id
    user = db.get_user(telegram_id=telegram_id)
    user_id = user.get("id")
    orders = db.get_cart_product(user_id=user_id)

    text = "<b>🛒 Sizning savachangizda</b>\n\n"
    conter = 0
    final_prise = 0

    for order in orders:
        conter += 1
        tottal_price = f"Umumiy narx: {order.get('total_price'):,.2f}".replace(",", " ")
        final_prise += order.get("total_price")
        product = db.get_product(product_id=order.get("product_id"))



        text += f"<b>{conter} -----------------------</b>\n"
        text += f"<b>Maxsulot: {product.get('name')}</b>\n "
        text += f"<b>Soni: {order.get('quantity')}</b>\n\n "
        text += f"<b>{tottal_price} so'm</b>\n\n"
    final_prise = f"<b>{final_prise:,.2f}</b>".replace(",", " ")
    text += f"<b>Savtcha narxi {final_prise} so'm</b>"

    if len(orders) > 0:
     await message.answer(text=text,parse_mode="HTML" ,reply_markup=generate_cart_menu())

    else:
       await message.answer(text="🛒 Savatchangiz bo'sh")
