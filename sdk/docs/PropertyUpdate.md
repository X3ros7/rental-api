# PropertyUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**address** | **str** |  | 
**city** | **str** |  | 
**price_per_month** | **float** |  | 
**bedrooms** | **int** |  | 
**available** | **bool** |  | [optional] [default to True]

## Example

```python
from openapi_client.models.property_update import PropertyUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyUpdate from a JSON string
property_update_instance = PropertyUpdate.from_json(json)
# print the JSON string representation of the object
print(PropertyUpdate.to_json())

# convert the object into a dict
property_update_dict = property_update_instance.to_dict()
# create an instance of PropertyUpdate from a dict
property_update_from_dict = PropertyUpdate.from_dict(property_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


