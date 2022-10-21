from pydantic import BaseModel, Field


class Subject(BaseModel):
    """Модель, описывающая необходимые поля о продукте."""
    article: int = Field(alias="id")
    brand: str
    title: str = Field(alias="name")


class Product(BaseModel):
    """Модель, описывающая информацию о продукте."""
    product: list[Subject] = Field(alias="products")
