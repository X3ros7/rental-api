# TenantUpdate


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
from openapi_client.models.tenant_update import TenantUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TenantUpdate from a JSON string
tenant_update_instance = TenantUpdate.from_json(json)
# print the JSON string representation of the object
print(TenantUpdate.to_json())

# convert the object into a dict
tenant_update_dict = tenant_update_instance.to_dict()
# create an instance of TenantUpdate from a dict
tenant_update_from_dict = TenantUpdate.from_dict(tenant_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


