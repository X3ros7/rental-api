# TenantCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | 
**property_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_create import TenantCreate

# TODO update the JSON string below
json = "{}"
# create an instance of TenantCreate from a JSON string
tenant_create_instance = TenantCreate.from_json(json)
# print the JSON string representation of the object
print(TenantCreate.to_json())

# convert the object into a dict
tenant_create_dict = tenant_create_instance.to_dict()
# create an instance of TenantCreate from a dict
tenant_create_from_dict = TenantCreate.from_dict(tenant_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


