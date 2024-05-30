import requests
from assertpy import assert_that

response = requests.get("https://reqres.in/api/users", params={"page": "2"})
print(f"response: {response.status_code}")
print(response.ok)
json_response = response.json()
print(f"json_response: {json_response}")
print(f"json_response: {json_response['per_page']}")
print(f"total_pages" in json_response.keys())
print(f"total_pagesssss" in json_response.keys())

def test_get_all_users_status_code():
    response = requests.get("https://reqres.in/api/users", params={"page": "2"})
    json_response = response.json()
    assert response.status_code == 200
    assert_that(response.status_code).is_equal_to(200) 
    assert response.ok ==True
    assert_that(response.ok).is_true()
    print(response.ok)
    

def test_get_all_users_existing_keys():
    response = requests.get("https://reqres.in/api/users", params={"page": "2"})
    json_response = response.json()
    assert "total_pages" in json_response.keys()
    # assert_that("total_pagesssss" in json_response.keys())
    assert_that(json_response).contains_key("total_pages")
    assert_that(json_response).contains_key("data")
    