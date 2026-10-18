# openapi_client.TenantsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_property_tenants_tenant_id_assign_post**](TenantsApi.md#assign_property_tenants_tenant_id_assign_post) | **POST** /tenants/{tenant_id}/assign | Assign Property
[**create_tenant_tenants_post**](TenantsApi.md#create_tenant_tenants_post) | **POST** /tenants | Create Tenant
[**delete_tenant_tenants_tenant_id_delete**](TenantsApi.md#delete_tenant_tenants_tenant_id_delete) | **DELETE** /tenants/{tenant_id} | Delete Tenant
[**get_tenant_tenants_tenant_id_get**](TenantsApi.md#get_tenant_tenants_tenant_id_get) | **GET** /tenants/{tenant_id} | Get Tenant
[**list_tenants_tenants_get**](TenantsApi.md#list_tenants_tenants_get) | **GET** /tenants | List Tenants
[**unassign_property_tenants_tenant_id_unassign_post**](TenantsApi.md#unassign_property_tenants_tenant_id_unassign_post) | **POST** /tenants/{tenant_id}/unassign | Unassign Property
[**update_tenant_tenants_tenant_id_put**](TenantsApi.md#update_tenant_tenants_tenant_id_put) | **PUT** /tenants/{tenant_id} | Update Tenant


# **assign_property_tenants_tenant_id_assign_post**
> TenantResponse assign_property_tenants_tenant_id_assign_post(tenant_id, assign_property_request)

Assign Property

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.assign_property_request import AssignPropertyRequest
from openapi_client.models.tenant_response import TenantResponse
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
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 56 # int | 
    assign_property_request = openapi_client.AssignPropertyRequest() # AssignPropertyRequest | 

    try:
        # Assign Property
        api_response = api_instance.assign_property_tenants_tenant_id_assign_post(tenant_id, assign_property_request)
        print("The response of TenantsApi->assign_property_tenants_tenant_id_assign_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->assign_property_tenants_tenant_id_assign_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **int**|  | 
 **assign_property_request** | [**AssignPropertyRequest**](AssignPropertyRequest.md)|  | 

### Return type

[**TenantResponse**](TenantResponse.md)

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

# **create_tenant_tenants_post**
> TenantResponse create_tenant_tenants_post(tenant_create)

Create Tenant

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.tenant_create import TenantCreate
from openapi_client.models.tenant_response import TenantResponse
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
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_create = openapi_client.TenantCreate() # TenantCreate | 

    try:
        # Create Tenant
        api_response = api_instance.create_tenant_tenants_post(tenant_create)
        print("The response of TenantsApi->create_tenant_tenants_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->create_tenant_tenants_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_create** | [**TenantCreate**](TenantCreate.md)|  | 

### Return type

[**TenantResponse**](TenantResponse.md)

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

# **delete_tenant_tenants_tenant_id_delete**
> delete_tenant_tenants_tenant_id_delete(tenant_id)

Delete Tenant

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
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 56 # int | 

    try:
        # Delete Tenant
        api_instance.delete_tenant_tenants_tenant_id_delete(tenant_id)
    except Exception as e:
        print("Exception when calling TenantsApi->delete_tenant_tenants_tenant_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **int**|  | 

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

# **get_tenant_tenants_tenant_id_get**
> TenantResponse get_tenant_tenants_tenant_id_get(tenant_id)

Get Tenant

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.tenant_response import TenantResponse
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
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 56 # int | 

    try:
        # Get Tenant
        api_response = api_instance.get_tenant_tenants_tenant_id_get(tenant_id)
        print("The response of TenantsApi->get_tenant_tenants_tenant_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant_tenants_tenant_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **int**|  | 

### Return type

[**TenantResponse**](TenantResponse.md)

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

# **list_tenants_tenants_get**
> List[TenantResponse] list_tenants_tenants_get()

List Tenants

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.tenant_response import TenantResponse
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
    api_instance = openapi_client.TenantsApi(api_client)

    try:
        # List Tenants
        api_response = api_instance.list_tenants_tenants_get()
        print("The response of TenantsApi->list_tenants_tenants_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->list_tenants_tenants_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TenantResponse]**](TenantResponse.md)

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

# **unassign_property_tenants_tenant_id_unassign_post**
> TenantResponse unassign_property_tenants_tenant_id_unassign_post(tenant_id)

Unassign Property

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.tenant_response import TenantResponse
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
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 56 # int | 

    try:
        # Unassign Property
        api_response = api_instance.unassign_property_tenants_tenant_id_unassign_post(tenant_id)
        print("The response of TenantsApi->unassign_property_tenants_tenant_id_unassign_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->unassign_property_tenants_tenant_id_unassign_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **int**|  | 

### Return type

[**TenantResponse**](TenantResponse.md)

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

# **update_tenant_tenants_tenant_id_put**
> TenantResponse update_tenant_tenants_tenant_id_put(tenant_id, tenant_update)

Update Tenant

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.tenant_response import TenantResponse
from openapi_client.models.tenant_update import TenantUpdate
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
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 56 # int | 
    tenant_update = openapi_client.TenantUpdate() # TenantUpdate | 

    try:
        # Update Tenant
        api_response = api_instance.update_tenant_tenants_tenant_id_put(tenant_id, tenant_update)
        print("The response of TenantsApi->update_tenant_tenants_tenant_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->update_tenant_tenants_tenant_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **int**|  | 
 **tenant_update** | [**TenantUpdate**](TenantUpdate.md)|  | 

### Return type

[**TenantResponse**](TenantResponse.md)

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

