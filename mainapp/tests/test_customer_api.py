from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient

from mainapp.models.customer import Customer
from mainapp.permissions import create_permissions, MainAppPermissions

CUSTOMER_LIST_URL = reverse("mainapp:customers")
TEST_USER_DATA = {"username": "testuser", "password": "testpassword"}


class CustomerAPITest(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(**TEST_USER_DATA)

        # create permissions and assign to user
        permissions_dict = create_permissions(MainAppPermissions.choices)
        self.user.user_permissions.add(
            permissions_dict.get(MainAppPermissions.CUSTOMER_ADMIN.value)
        )
        # check if user really has the permissions
        self.assertTrue(
            self.user.has_perm(
                MainAppPermissions.get_fullname(MainAppPermissions.CUSTOMER_ADMIN)
            )
        )

    def test_get_customer_list_success(self):
        """
        Ensure we can get customers list with correct credentials
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(CUSTOMER_LIST_URL, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)
