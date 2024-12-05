from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def generate_product_menu(category_id,product_id, quantity = 1):
    builder = InlineKeyboardBuilder()
    
    builder.row(
        InlineKeyboardButton(text="-", callback_data=f"product-action:decrement:{quantity}:{category_id}:{product_id}"),
        InlineKeyboardButton(text=f"{quantity}", callback_data="..."),
        InlineKeyboardButton(text="+", callback_data=f"product-action:increment:{quantity}:{category_id}:{product_id}"),
    )
    builder.row(
        InlineKeyboardButton(text="🛒 Savatchaga qo'shish", callback_data=f"add_to_cart:{quantity}:{product_id}")
    )
    builder.row(
        InlineKeyboardButton(text="👈 Orqaga", callback_data=f"back-to:{category_id}"),
    )

    return builder.as_markup()
