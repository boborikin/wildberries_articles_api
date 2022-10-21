from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from asgiref.sync import async_to_sync
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FileUploadParser
from .parser import PlainTextParser
from .schemas import UploadXLSXViewSchema, GetArticleInformationViewSchema
from .services import get_article_information_from_int, get_articles_information_from_xlsx_file


class UploadXLSXView(APIView):

    parser_classes = [MultiPartParser, FileUploadParser]

    @async_to_sync
    @swagger_auto_schema(**UploadXLSXViewSchema)
    async def post(self, request, filename, format=None):
        try:
            articles = await get_articles_information_from_xlsx_file(request.data['file'])
        except:
            return Response({"success": False, "message": "Неверные данныe."})
        return Response(articles)


class GetArticleInformationView(APIView):

    parser_classes = [PlainTextParser]

    @async_to_sync
    @swagger_auto_schema(**GetArticleInformationViewSchema)
    async def post(self, request):
        try:
            article_information = await get_article_information_from_int(int(request.data))
        except:
            return Response({"success": False, "message": "Неверные данные."})
        return Response(article_information)
