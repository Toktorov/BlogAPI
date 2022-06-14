from rest_framework.test import APITestCase
from apps.posts.models import Post
from django.urls import reverse
from rest_framework import status


class PostTests(APITestCase):

    def setUp(self):
        post = Post.objects.create(
            title='Test title',
            description='Test description',
        )

    def test_get_list_of_post(self):
        url = reverse('posts-list')
        responce = self.client.get(url)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)

    def test_get_detail_of_post(self):
        post = Post.objects.first()
        url = reverse('posts-detail', kwargs={'pk': post.id})
        responce = self.client.get(url)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
