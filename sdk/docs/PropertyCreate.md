# PropertyCreate


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
from openapi_client.models.property_create import PropertyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyCreate from a JSON string
property_create_instance = PropertyCreate.from_json(json)
# print the JSON string representation of the object
print(PropertyCreate.to_json())

# convert the object into a dict
property_create_dict = property_create_instance.to_dict()
# create an instance of PropertyCreate from a dict
property_create_from_dict = PropertyCreate.from_dict(property_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


