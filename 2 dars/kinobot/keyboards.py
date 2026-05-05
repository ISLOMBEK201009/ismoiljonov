from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

def get_main_menu_kb() -> ReplyKeyboardMarkup:
    """Asosiy menu klaviaturasi"""
    kb = ReplyKeyboardBuilder()

    kb.button(text="🎬 Top kinolar")
    kb.button(text="🆕 Yangi kinolar")
    kb.button(text="📊 Statistika")
    kb.button(text="ℹ️ Ma'lumot")
    kb.adjust(2, 2, 1)
    return kb.as_markup(resize_keyboard=True)

def get_admin_panel_kb() -> InlineKeyboardMarkup:
    """Admin panel klaviaturasi"""
    kb = InlineKeyboardBuilder()
    kb.button(text="➕ Kino qo'shish", callback_data="admin_add_movie")
    kb.button(text="📝 Kino tahrirlash", callback_data="admin_edit_movie")
    kb.button(text="🗑 Kino o'chirish", callback_data="admin_delete_movie")
    kb.button(text="📢 Rassilka", callback_data="admin_broadcast")
    kb.button(text="📊 Statistika", callback_data="admin_stats")
    kb.button(text="🔐 Majburiy obuna", callback_data="admin_fsub")
    kb.adjust(2)
    return kb.as_markup()

def get_back_to_admin_kb() -> InlineKeyboardMarkup:
    """Admin panelga qaytish tugmasi"""
    kb = InlineKeyboardBuilder()
    kb.button(text="⬅️ Ortga", callback_data="admin_panel_back")
    return kb.as_markup()

def get_cancel_kb() -> InlineKeyboardMarkup:
    """Bekor qilish tugmasi"""
    kb = InlineKeyboardBuilder()
    kb.button(text="❌ Bekor qilish", callback_data="cancel")
    return kb.as_markup()

def get_movie_actions_kb(movie_code: int, user_rated: bool = False) -> InlineKeyboardMarkup:
    """Kino uchun amallar klaviaturasi"""
    kb = InlineKeyboardBuilder()
    kb.button(text="⭐️ Baho berish", callback_data=f"rate_{movie_code}")
    if user_rated:
        kb.button(text="📝 Bahoni o'zgartirish", callback_data=f"edit_rate_{movie_code}")
    kb.button(text="📊 Statistika", callback_data=f"movie_stats_{movie_code}")
    kb.button(text="↗️ Ulashish", switch_inline_query=f"code_{movie_code}")
    kb.adjust(2)
    return kb.as_markup()

def get_rating_kb(movie_code: int) -> InlineKeyboardMarkup:
    """Baho berish klaviaturasi"""
    kb = InlineKeyboardBuilder()
    for i in range(1, 6):
        kb.button(text=f"{'⭐️' * i}", callback_data=f"rating_{movie_code}_{i}")
    kb.button(text="❌ Bekor qilish", callback_data="cancel_rating")
    kb.adjust(5, 1)
    return kb.as_markup()

def get_genre_kb() -> InlineKeyboardMarkup:
    """Janr tanlash klaviaturasi"""
    genres = [
        "🎭 Drama", "😂 Komediya", "🔫 Jangari",
        "💕 Romantik", "😱 Qo'rqinchli", "🔬 Fantastika",
        "🎪 Sarguzasht", "🎬 Thriller", "🎨 Multfilm"
    ]
    kb = InlineKeyboardBuilder()
    for genre in genres:
        kb.button(text=genre, callback_data=f"genre_{genre.split()[1]}")
    kb.button(text="⬅️ Ortga", callback_data="back_to_menu")
    kb.adjust(3)
    return kb.as_markup()

def get_pagination_kb(current_page: int, total_pages: int, prefix: str = "page") -> InlineKeyboardMarkup:
    """Pagination klaviaturasi"""
    kb = InlineKeyboardBuilder()
    
    buttons = []
    if current_page > 1:
        buttons.append(InlineKeyboardButton(text="⬅️", callback_data=f"{prefix}_{current_page-1}"))
    
    buttons.append(InlineKeyboardButton(text=f"{current_page}/{total_pages}", callback_data="current_page"))
    
    if current_page < total_pages:
        buttons.append(InlineKeyboardButton(text="➡️", callback_data=f"{prefix}_{current_page+1}"))
    
    kb.row(*buttons)
    return kb.as_markup()

def get_confirmation_kb(action: str) -> InlineKeyboardMarkup:
    """Tasdiqlash klaviaturasi"""
    kb = InlineKeyboardBuilder()
    kb.button(text="✅ Ha", callback_data=f"confirm_{action}")
    kb.button(text="❌ Yo'q", callback_data=f"cancel_{action}")
    kb.adjust(2)
    return kb.as_markup()

def get_broadcast_kb() -> InlineKeyboardMarkup:
    """Rassilka klaviaturasi"""
    kb = InlineKeyboardBuilder()
    kb.button(text="📤 Yuborish", callback_data="broadcast_send")
    kb.button(text="👁 Ko'rib chiqish", callback_data="broadcast_preview")
    kb.button(text="❌ Bekor qilish", callback_data="admin_panel_back")
    kb.adjust(2, 1)
    return kb.as_markup()

def get_quality_kb() -> InlineKeyboardMarkup:
    """Sifat tanlash klaviaturasi"""
    qualities = ["CAM", "HD", "Full HD", "4K"]
    kb = InlineKeyboardBuilder()
    for quality in qualities:
        kb.button(text=quality, callback_data=f"quality_{quality}")
    kb.adjust(2)
    return kb.as_markup()