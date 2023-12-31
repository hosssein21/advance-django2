from rest_framework.test import APIClient
from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestPostApi:
    
    def test_get_post_response_200(self):
        client=APIClient()
        url = reverse('blog:api-v1:posts')
        response =client.get(url)
        assert response.status_code ==200

