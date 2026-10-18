# TenantResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | 
**property_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_response import TenantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TenantResponse from a JSON string
tenant_response_instance = TenantResponse.from_json(json)
# print the JSON string representation of the object
print(TenantResponse.to_json())

# convert the object into a dict
tenant_response_dict = tenant_response_instance.to_dict()
# create an instance of TenantResponse from a dict
tenant_response_from_dict = TenantResponse.from_dict(tenant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


