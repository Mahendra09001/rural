def format_person(data):
    return {
        "id": data.get("id"),
        "name": data.get("name"),
        "age": data.get("age"),
        "gender": data.get("gender"),
        "village": data.get("village"),
        "district": data.get("district"),
        "state": data.get("state"),
        "phone": data.get("phone"),
        "occupation": data.get("occupation"),
        "education": data.get("education"),
        "isSynced": data.get("isSynced", False),
    }
