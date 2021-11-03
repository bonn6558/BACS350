from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


# class AdminTests(SimpleTestCase):

    def test_admin_page_status_code(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)

    def test_login_view(self):
        response = self.client.get('/accounts/login')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, '/accounts/login/')

        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'theme.html')

    # def test_logout_view(self):
    #     response = self.client.get('/accounts/logout/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/')