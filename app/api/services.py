from .models import Product
from .wildberries_services import get_information_about_article, get_information_by_articles
from asgiref.sync import sync_to_async
from django.forms.models import model_to_dict
from .xlsx_services import get_articles_from_xslx_file


async def get_article_information_from_int(article: int) -> dict[Product]:
    """
    Получение информации об артикуле путем
    запроса к сайту Wildberries (или) базе данных.
     """
    fields = ["article", "brand", "title"]
    try:
        result = await sync_to_async(Product.objects.get, thread_sensitive=True)(article=article)
    except:
        info = await get_information_about_article(article)
        return model_to_dict(await sync_to_async(Product.objects.create, thread_sensitive=True)(**info))
    return model_to_dict(result, fields=fields)


async def get_articles_information_from_xlsx_file(xlsx_file_obj: bytes) -> list[dict]:
    """Получение артикулов из xlsx файла и возвращение информации о них."""
    fields = ["article", "brand", "title"]
    articles_information = []
    not_in_db = []
    articles = get_articles_from_xslx_file(xlsx_file_obj)
    for article in articles:
        try:
            articles_information.append(model_to_dict(await sync_to_async(Product.objects.get, thread_sensitive=True)(article=article), fields=fields))
        except:
            not_in_db.append(article)
    if not_in_db:
        items = await get_information_by_articles(not_in_db)
        for item in items:
            articles_information.append(model_to_dict(await sync_to_async(Product.objects.create, thread_sensitive=True)(**item)))
    return articles_information
