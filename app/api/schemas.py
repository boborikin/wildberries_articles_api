from drf_yasg import openapi

UploadXLSXViewSchema = dict(
    operation_id='Get articles information from xlsx file',
    manual_parameters=[
        openapi.Parameter('file', openapi.IN_FORM, type=openapi.TYPE_FILE, description='XLSX document to be uploaded',
                          required=True)
    ]
)

GetArticleInformationViewSchema = dict(
    operation_id='Get article and return information',
    request_body=openapi.Schema(
        type=openapi.TYPE_INTEGER,
    )
)
