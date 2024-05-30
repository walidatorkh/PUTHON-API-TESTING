import requests
from assertpy import assert_that

def test_register_user_happy_flow():
    register_user_data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post(
        url="https://reqres.in/api/register",
        json=register_user_data
    )
    
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.ok).is_true()
    response_json = response.json()
    assert_that(response_json).contains_key("id")
    assert_that(response_json).contains_key("token")
    

def test_register_user_missing_password():
    register_user_data = {
        "email": "eve.holt@reqres.in"
    }
    response = requests.post(
        url="https://reqres.in/api/register",
        json=register_user_data
    )
    
    assert_that(response.status_code).is_equal_to(400)
    assert_that(response.ok).is_false()
    response_json = response.json()
    assert_that(response_json).contains_key("error")
    assert_that(response_json).contains_entry({"error": "Missing password"})
    print(response.json()["error"])
    print("####################")
    # assert_that(response_json["error"]).is_not_empty()
    # print(response_json["error"])