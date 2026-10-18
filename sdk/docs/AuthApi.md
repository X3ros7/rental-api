# openapi_client.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_auth_login_post**](AuthApi.md#login_auth_login_post) | **POST** /auth/login | Login
[**me_auth_me_get**](AuthApi.md#me_auth_me_get) | **GET** /auth/me | Me
[**register_auth_register_post**](AuthApi.md#register_auth_register_post) | **POST** /auth/register | Register


# **login_auth_login_post**
> Token login_auth_login_post(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)

Login

### Example


```python
import openapi_client
from openapi_client.models.token import Token
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthApi(api_client)
    username = 'username_example' # str | 
    password = 'password_example' # str | 
    grant_type = 'grant_type_example' # str |  (optional)
    scope = '' # str |  (optional) (default to '')
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)

    try:
        # Login
        api_response = api_instance.login_auth_login_post(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)
        print("The response of AuthApi->login_auth_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->login_auth_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **password** | **str**|  | 
 **grant_type** | **str**|  | [optional] 
 **scope** | **str**|  | [optional] [default to &#39;&#39;]
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_auth_me_get**
> UserResponse me_auth_me_get()

Me

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.user_response import UserResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthApi(api_client)

    try:
        # Me
        api_response = api_instance.me_auth_me_get()
        print("The response of AuthApi->me_auth_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->me_auth_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_auth_register_post**
> UserResponse register_auth_register_post(user_create)

Register

### Example


```python
import openapi_client
from openapi_client.models.user_create import UserCreate
from openapi_client.models.user_response import UserResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthApi(api_client)
    user_create = openapi_client.UserCreate() # UserCreate | 

    try:
        # Register
        api_response = api_instance.register_auth_register_post(user_create)
        print("The response of AuthApi->register_auth_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->register_auth_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

