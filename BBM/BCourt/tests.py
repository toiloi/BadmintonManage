from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import io
from BUser.models import User
from .models import Court, Address, San
from .forms import CourtForm, AddressForm, SanForm

# Tạo ảnh hợp lệ cho test
def generate_test_image():
    image = Image.new('RGB', (100, 100), color=(73, 109, 137))  # Ảnh 100x100 px
    img_io = io.BytesIO()
    image.save(img_io, format='JPEG')  # Lưu dưới dạng JPEG
    img_io.seek(0)
    return SimpleUploadedFile("test.jpg", img_io.getvalue(), content_type="image/jpeg")

class CourtManagementTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='toairole3', password='1')
        self.address = Address.objects.create(soNha='123', duong='Main St', phuong='1', quan='A', tinh='B')
        self.court = Court.objects.create(
            maCourt='C001', name='Test Court', address=self.address, price=100, 
            courtManager=self.user, img=generate_test_image()
        )
        self.san = San.objects.create(maSan='S001', numSan=1, court=self.court)

    def test_add_court_view(self):
        self.client.login(username='toairole3', password='1')
        image = generate_test_image()
        response = self.client.post(reverse('r3add_court'), {
            'maCourt': 'C002',
            'name': 'New Court',
            'price': 200,
            'soNha': '456', 'duong': 'Second St', 'phuong': '2', 'quan': 'B', 'tinh': 'C',
            'img': image
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Court.objects.filter(name='New Court').exists())

    def test_manage_court_view(self):
        self.client.login(username='toairole3', password='1')
        response = self.client.get(reverse('r3manage_court'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Court')

    def test_chiTiet_view(self):
        self.client.login(username='toairole3', password='1')
        response = self.client.get(reverse('chiTiet', args=[self.court.maCourt]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Court')

    def test_add_san_view(self):
        self.client.login(username='toairole3', password='1')
        response = self.client.post(reverse('r3add_san', args=[self.court.maCourt]), {
            'maSan': 'S002', 'numSan': 2
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(San.objects.filter(numSan=2).exists())

    def test_delete_court_view(self):
        self.client.login(username='toairole3', password='1')
        response = self.client.post(reverse('delete_court', args=[self.court.maCourt]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Court.objects.filter(maCourt='C001').exists())

    def test_delete_san_view(self):
        self.client.login(username='toairole3', password='1')
        response = self.client.post(reverse('delete_san', args=[self.san.maSan]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(San.objects.filter(maSan='S001').exists())