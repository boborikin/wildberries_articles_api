from aiohttp import ClientSession
from .pydantic_models import Product
import asyncio


async def _get_article(article: int, session: ClientSession):
    """Внутренняя асинхронная функция, получающая информацию о товаре."""
    async with session.get(f"https://card.wb.ru/cards/detail?nm={article}", ssl=False) as response:
        data = await response.json(encoding="UTF-8", content_type="text/plain")
        model = Product(**data["data"])
        return dict(model.product[0])


async def get_information_by_articles(articles: list[int]):
    """Функция для получения информации по артикулам."""
    async with ClientSession() as session:
        tasks = []
        for article in articles:
            task = asyncio.create_task(_get_article(article, session))
            tasks.append(task)
        return await asyncio.gather(*tasks, return_exceptions=True)


async def get_information_about_article(article: int) -> dict[Product]:
    """Получение информации об одном артикуле."""
    async with ClientSession() as session:
        async with session.get(f"https://card.wb.ru/cards/detail?nm={article}", ssl=False) as resp:
            data = await resp.json(encoding="UTF-8", content_type="text/plain")
            model = Product(**data["data"])
            return dict(model.product[0])
