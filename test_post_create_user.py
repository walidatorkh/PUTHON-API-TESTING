import requests
from assertpy import assert_that


def test_user_creation():
    name = "Vasya"
    job = "assasin"
    
    name_entry = {"name": name}
    job_entry = {"job": job}
    
    # creation_user_data = {{"name": name}, {"job": job}}
    #
    # creation_user_data = { **name_entry, **job_entry}
    creation_user_data = name_entry|job_entry
    print(f"creation_user_data: {creation_user_data}")
    
    response = requests.post(
        url="https://reqres.in/api/users",
        json=creation_user_data
    )
    
    assert_that(response.status_code).is_equal_to(201)
    assert_that(response.ok).is_equal_to(True)
    assert_that(response.reason).is_equal_to("Created")
    
    json_response = response.json()
    print(json_response["name"])
    assert_that(response.json()["name"]).is_equal_to(name)
    assert_that(json_response["job"]).is_equal_to(job)
    assert_that(json_response).contains_entry(name_entry)
    assert_that(json_response).contains_entry(job_entry)
    