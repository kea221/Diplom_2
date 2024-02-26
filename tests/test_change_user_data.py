import requests
import allure
from constants import Constants, Endpoints


class TestChangeUserData:
    @allure.title("Можно изменить логин(email) у авторизованного юзера")
    def test_change_email_of_authorized_user_email_changed(self, create_user_then_delete_user):
        user_data = create_user_then_delete_user[0]
        user_data["email"] = "spock.vulcan@yandex.ru"
        response = requests.patch(f"{Constants.URL}{Endpoints.CHANGE_USER_DATA}",
                                  headers={"Authorization": create_user_then_delete_user[1]},
                                  data=user_data)
        assert response.status_code == 200
        assert response.json()["email"] == user_data[0]

    @allure.title("Можно изменить пароль у авторизованного юзера")
    def test_change_password_of_authorized_user_password_changed(self, create_user_then_delete_user):
        user_data = create_user_then_delete_user[0]
        user_data["password"] = "424242"
        response = requests.patch(f"{Constants.URL}{Endpoints.CHANGE_USER_DATA}",
                                  headers={"Authorization": create_user_then_delete_user[1]},
                                  data=user_data)
        assert response.status_code == 200
        assert response.json()["password"] == user_data[1]

    @allure.title("Можно изменить имя у авторизованного юзера")
    def test_change_name_of_authorized_user_name_changed(self, create_user_then_delete_user):
        user_data = create_user_then_delete_user[0]
        user_data["name"] = "Spock"
        response = requests.patch(f"{Constants.URL}{Endpoints.CHANGE_USER_DATA}",
                                  headers={"Authorization": create_user_then_delete_user[1]},
                                  data=user_data)
        assert response.status_code == 200
        assert response.json()["name"] == user_data[2]

    @allure.title("Нельзя изменить логин(email) у неавторизованного юзера")
    def test_change_email_of_unauthorized_user_email_not_changed(self, create_user_then_delete_user):
        user_data = create_user_then_delete_user[0]
        user_data["email"] = "spock.vulcan@yandex.ru"
        response = requests.patch(f"{Constants.URL}{Endpoints.CHANGE_USER_DATA}",
                                  data=user_data)
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"

    @allure.title("Нельзя изменить пароль у неавторизованного юзера")
    def test_change_password_of_unauthorized_user_password_not_changed(self, create_user_then_delete_user):
        user_data = create_user_then_delete_user[0]
        user_data["password"] = "424242"
        response = requests.patch(f"{Constants.URL}{Endpoints.CHANGE_USER_DATA}",
                                  data=user_data)
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"

    @allure.title("Нельзя изменить имя у неавторизованного юзера")
    def test_change_name_of_unauthorized_user_name_not_changed(self, create_user_then_delete_user):
        user_data = create_user_then_delete_user[0]
        user_data["name"] = "Spock"
        response = requests.patch(f"{Constants.URL}{Endpoints.CHANGE_USER_DATA}",
                                  data=user_data)
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"
