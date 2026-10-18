# PropertyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**title** | **str** |  | 
**address** | **str** |  | 
**city** | **str** |  | 
**price_per_month** | **float** |  | 
**bedrooms** | **int** |  | 
**available** | **bool** |  | 

## Example

```python
from openapi_client.models.property_response import PropertyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyResponse from a JSON string
property_response_instance = PropertyResponse.from_json(json)
# print the JSON string representation of the object
print(PropertyResponse.to_json())

# convert the object into a dict
property_response_dict = property_response_instance.to_dict()
# create an instance of PropertyResponse from a dict
property_response_from_dict = PropertyResponse.from_dict(property_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


