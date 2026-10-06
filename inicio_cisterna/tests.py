from django.test import TestCase
from django.urls import reverse


class InicioCisternaTests(TestCase):
    def test_homepage_contains_project_title_and_theme_cards(self):
        response = self.client.get(reverse('inicio_cisterna:inicio'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Benjamin Cisterna')
        self.assertContains(response, 'Temas')
        self.assertContains(response, 'Tema 1')
        self.assertContains(response, 'Tema 2')

    def test_topic_details_show_descriptions_and_two_images(self):
        expected_topics = {
            'tema-1': 'Imágenes de Civilization VI y Minecraft.',
            'tema-2': 'Imágenes de Pink Floyd y Soundgarden.',
        }

        for topic_slug, expected_description in expected_topics.items():
            with self.subTest(topic=topic_slug):
                response = self.client.get(
                    reverse('inicio_cisterna:tema_detalle', args=[topic_slug])
                )

                self.assertEqual(response.status_code, 200)
                self.assertContains(response, expected_description)
                self.assertEqual(len(response.context['tema']['imagenes']), 2)

    def test_unknown_topic_returns_404(self):
        response = self.client.get(
            reverse('inicio_cisterna:tema_detalle', args=['tema-inexistente'])
        )

        self.assertEqual(response.status_code, 404)
