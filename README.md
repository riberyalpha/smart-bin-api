# smart-bin-api

# API Documentation

## Overview

This API is designed to receive data from an AI and forward it to a mobile application. It requires a specific JSON format to ensure proper functionality. This document will guide you through the required data structure and provide examples of how to use the API.

## Data Requirements

### JSON Structure

The API expects to receive a JSON object in the following format:

```json
{
  "type": "Organico",
  "imageName": "leaf.fill"
}
```

### Field Descriptions

- **`type`** (string):  
  The type of waste or category. This field specifies the nature of the item, and it is required.  
  **Example values**: `"Organico"`, `"Inorganico"`, `"Reciclable"`.

- **`imageName`** (string):  
  The name of the image associated with the type of waste. This field is also required and should correspond to the specific image used in the mobile application.  
  **Example values**: `"leaf.fill"`, `"trash"`, `"recycle"`.

### Example Payload

Here is an example of a complete JSON payload that you might send to the API:

```json
{
  "type": "Organico",
  "imageName": "leaf.fill"
}
```

## How to Use the API

### HTTP Method

This API supports the following HTTP method:

- **POST**: Send the JSON payload to the API endpoint.

### Endpoint

Send your requests to the following endpoint:

```
POST /api/v1/data
```

### Example Request

Here is an example of how to send a request using `curl`:

```bash
curl -X POST https://api.yourdomain.com/api/v1/data \
-H "Content-Type: application/json" \
-d '{"type": "Organico", "imageName": "leaf.fill"}'
```

### Response

The API will return a JSON response indicating whether the data was successfully processed.

```json
{
  "status": "success",
  "message": "Data received and processed."
}
```

## Error Handling

If the JSON structure is incorrect or missing required fields, the API will return an error response:

```json
{
  "status": "error",
  "message": "Invalid JSON format. Required fields: 'type', 'imageName'."
}
```

## Conclusion

This API is designed to be straightforward and easy to integrate with your existing systems. Ensure that you are sending the correct JSON format to avoid errors and ensure smooth operation.

---

You can customize this `README.md` file further based on specific needs or additional features of your API.