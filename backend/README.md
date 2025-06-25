# Test the API

```
# Update an entry
http PUT http://127.0.0.1:8000/api/diary/1 entry="Update entry"

# Get list of tags
http GET http://127.0.0.1:8000/api/tags/

# Get list of diary entries
http GET http://127.0.0.1:8000/api/diary/

# Get list of diary entries for 2025
http GET http://127.0.0.1:8000/api/diary/?year=2025
```
