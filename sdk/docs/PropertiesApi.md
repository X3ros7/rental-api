# openapi_client.PropertiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_property_properties_post**](PropertiesApi.md#create_property_properties_post) | **POST** /properties | Create Property
[**delete_property_properties_property_id_delete**](PropertiesApi.md#delete_property_properties_property_id_delete) | **DELETE** /properties/{property_id} | Delete Property
[**get_property_properties_property_id_get**](PropertiesApi.md#get_property_properties_property_id_get) | **GET** /properties/{property_id} | Get Property
[**list_properties_properties_get**](PropertiesApi.md#list_properties_properties_get) | **GET** /properties | List Properties
[**update_property_properties_property_id_put**](PropertiesApi.md#update_property_properties_property_id_put) | **PUT** /properties/{property_id} | Update Property


# **create_property_properties_post**
> PropertyResponse create_property_properties_post(property_create)

Create Property

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.property_create import PropertyCreate
from openapi_client.models.property_response import PropertyResponse
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
    api_instance = openapi_client.PropertiesApi(api_client)
    property_create = openapi_client.PropertyCreate() # PropertyCreate | 

    try:
        # Create Property
        api_response = api_instance.create_property_properties_post(property_create)
        print("The response of PropertiesApi->create_property_properties_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertiesApi->create_property_properties_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_create** | [**PropertyCreate**](PropertyCreate.md)|  | 

### Return type

[**PropertyResponse**](PropertyResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_property_properties_property_id_delete**
> delete_property_properties_property_id_delete(property_id)

Delete Property

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
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
    api_instance = openapi_client.PropertiesApi(api_client)
    property_id = 56 # int | 

    try:
        # Delete Property
        api_instance.delete_property_properties_property_id_delete(property_id)
    except Exception as e:
        print("Exception when calling PropertiesApi->delete_property_properties_property_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_property_properties_property_id_get**
> PropertyResponse get_property_properties_property_id_get(property_id)

Get Property

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.property_response import PropertyResponse
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
    api_instance = openapi_client.PropertiesApi(api_client)
    property_id = 56 # int | 

    try:
        # Get Property
        api_response = api_instance.get_property_properties_property_id_get(property_id)
        print("The response of PropertiesApi->get_property_properties_property_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertiesApi->get_property_properties_property_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 

### Return type

[**PropertyResponse**](PropertyResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_properties_properties_get**
> List[PropertyResponse] list_properties_properties_get(city=city, min_price=min_price, max_price=max_price, available=available)

List Properties

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.property_response import PropertyResponse
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
    api_instance = openapi_client.PropertiesApi(api_client)
    city = 'city_example' # str |  (optional)
    min_price = 3.4 # float |  (optional)
    max_price = 3.4 # float |  (optional)
    available = True # bool |  (optional)

    try:
        # List Properties
        api_response = api_instance.list_properties_properties_get(city=city, min_price=min_price, max_price=max_price, available=available)
        print("The response of PropertiesApi->list_properties_properties_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertiesApi->list_properties_properties_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city** | **str**|  | [optional] 
 **min_price** | **float**|  | [optional] 
 **max_price** | **float**|  | [optional] 
 **available** | **bool**|  | [optional] 

### Return type

[**List[PropertyResponse]**](PropertyResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_property_properties_property_id_put**
> PropertyResponse update_property_properties_property_id_put(property_id, property_update)

Update Property

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.property_response import PropertyResponse
from openapi_client.models.property_update import PropertyUpdate
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
    api_instance = openapi_client.PropertiesApi(api_client)
    property_id = 56 # int | 
    property_update = openapi_client.PropertyUpdate() # PropertyUpdate | 

    try:
        # Update Property
        api_response = api_instance.update_property_properties_property_id_put(property_id, property_update)
        print("The response of PropertiesApi->update_property_properties_property_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertiesApi->update_property_properties_property_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 
 **property_update** | [**PropertyUpdate**](PropertyUpdate.md)|  | 

### Return type

[**PropertyResponse**](PropertyResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

