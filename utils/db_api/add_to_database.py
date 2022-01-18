import asyncio

from utils.db_api.database_gino import on_startup
from utils.db_api.db_commands import add_item


async def add_items():
    await add_item(
        name="ASUS",
        category_name="Электроника",
        category_code="Electronics",
        subcategory_name="Компьютеры",
        subcategory_code="PCs",
        price=90000,
        photo="-"
    )
    await add_item(
        name="DELL",
        category_name="Электроника",
        category_code="Electronics",
        subcategory_name="Компьютеры",
        subcategory_code="PCs",
        price=30000,
        photo="-"
    )

    await add_item(
        name="Apple",
        category_name="Электроника",
        category_code="Electronics",
        subcategory_name="Компьютеры",
        subcategory_code="PCs",
        price=200000,
        photo="-"
    )
    await add_item(
        name="HP",
        category_name="Электроника",
        category_code="Electronics",
        subcategory_name="Компьютеры",
        subcategory_code="PCs",
        price=25000,
        photo="-"
    )
    await add_item(
        name="Huawei",
        category_name="Электроника",
        category_code="Electronics",
        subcategory_name="Компьютеры",
        subcategory_code="PCs",
        price=40000,
        photo="-"
    )

    await add_item(
        name="Xiaomi",
        category_name="Электроника",
        category_code="Electronics",
        subcategory_name="Компьютеры",
        subcategory_code="PCs",
        price=75000,
        photo="-"
    )

    await add_item(
        name="Xiaomi",
        category_name="Электроника",
        category_code="Electronics",
        subcategory_name="Смартфоны",
        subcategory_code="Phones",
        price=30000,
        photo="-"
    )
    await add_item(
        name="Samsung",
        category_name="Электроника",
        category_code="Electronics",
        subcategory_name="Смартфоны",
        subcategory_code="Phones",
        price=55000,
        photo="-"
    )
    await add_item(
        name="Huawei",
        category_name="Электроника",
        category_code="Electronics",
        subcategory_name="Смартфоны",
        subcategory_code="Phones",
        price=70000,
        photo="-"
    )
    await add_item(
        name="Apple",
        category_name="Электроника",
        category_code="Electronics",
        subcategory_name="Смартфоны",
        subcategory_code="Phones",
        price=85000,
        photo="-"
    )
    await add_item(
        name="Nothing",
        category_name="Электроника",
        category_code="Electronics",
        subcategory_name="Смартфоны",
        subcategory_code="Phones",
        price=55000,
        photo="-"
    )
    await add_item(
        name="Nokia",
        category_name="Электроника",
        category_code="Electronics",
        subcategory_name="Смартфоны",
        subcategory_code="Phones",
        price=7000,
        photo="-"
    )
    await add_item(
        name="Канал_1",
        category_name="Услуги рекламы",
        category_code="Ads",
        subcategory_name="Реклама на Youtube",
        subcategory_code="Youtube",
        price=4000,
        photo="-"
    )
    await add_item(
        name="Канал_2",
        category_name="Услуги рекламы",
        category_code="Ads",
        subcategory_name="Реклама на Youtube",
        subcategory_code="Youtube",
        price=9000,
        photo="-"
    )
    await add_item(
        name="Канал_3",
        category_name="Услуги рекламы",
        category_code="Ads",
        subcategory_name="Реклама в Instagram",
        subcategory_code="Instagram",
        price=3000,
        photo="-"
    )
    await add_item(
        name="Канал_4",
        category_name="Услуги рекламы",
        category_code="Ads",
        subcategory_name="Реклама в Instagram",
        subcategory_code="Instagram",
        price=10000,
        photo="-"
    )
    await add_item(
        name="Канал_5",
        category_name="Услуги рекламы",
        category_code="Ads",
        subcategory_name="Реклама на Youtube",
        subcategory_code="Youtube",
        price=50000,
        photo="-"
    )
    await add_item(
        name="Канал_6",
        category_name="Услуги рекламы",
        category_code="Ads",
        subcategory_name="Реклама на Youtube",
        subcategory_code="Youtube",
        price=10000,
        photo="-"
    )
    await add_item(
        name="Канал_7",
        category_name="Услуги рекламы",
        category_code="Ads",
        subcategory_name="Реклама в Instagram",
        subcategory_code="Instagram",
        price=20000,
        photo="-"
    )
    await add_item(
        name="Канал_8",
        category_name="Услуги рекламы",
        category_code="Ads",
        subcategory_name="Реклама в Instagram",
        subcategory_code="Instagram",
        price=15000,
        photo="-"
    )

# loop = asyncio.get_event_loop()
# loop.run_until_complete(on_startup())
# loop.run_until_complete(add_items())