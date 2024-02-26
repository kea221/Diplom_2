import requests
import allure
from constants import Constants, Endpoints


class TestLogin:
    @allure.title("Можно войти под существующим пользователем")
    def test_login_as_an_existing_user(self, create_user_for_login_and_then_delete_user):
        response = requests.post(f"{Constants.URL}{Endpoints.LOGIN}",
                                 data=create_user_for_login_and_then_delete_user[0],
                                 headers={'Authorization': create_user_for_login_and_then_delete_user[1]})
        assert response.status_code == 200
        assert response.json()["success"] == True

    @allure.title("Нельзя войти с неверным логином(email)")
    def test_login_with_invalid_email_not_completed(self, create_user_for_login_and_then_delete_user):
        payload_fake_user = create_user_for_login_and_then_delete_user[0]
        payload_fake_user["email"] = "shelly_cooper@yandex.ru"
        response = requests.post(f"{Constants.URL}{Endpoints.LOGIN}",
                                 data=payload_fake_user,
                                 headers={'Authorization': create_user_for_login_and_then_delete_user[1]})
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Нельзя войти с неверным паролем")
    def test_login_with_invalid_password_not_completed(self, create_user_for_login_and_then_delete_user):
        payload_fake_user = create_user_for_login_and_then_delete_user[0]
        payload_fake_user["password"] = "12345678"
        response = requests.post(f"{Constants.URL}{Endpoints.LOGIN}",
                                 data=payload_fake_user,
                                 headers={'Authorization': create_user_for_login_and_then_delete_user[1]})
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"
