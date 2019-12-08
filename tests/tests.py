import pytest
from django.core.exceptions import ValidationError
from django.test import TestCase

# Create your tests here.
from tests.models import Goods


@pytest.mark.django_db
def test_create_model():
    model = Goods(name='test').save()
    assert Goods.objects.count() == 1


def test_validation_correct():
    with pytest.raises(ValidationError):
        model = Goods(name='a' * 256)
        model.full_clean()
