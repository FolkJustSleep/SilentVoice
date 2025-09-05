from model import result


def Create(db, table_name, data) : 
    try:
        response = db.table(table_name).insert(data).execute()
        return response, "Data inserted successfully"
    except Exception as e:
        return e, "Error inserting data"

def GetByID(db, table_name, column_name , id) :
    try:
        response = db.table(table_name).select(column_name).eq("id", id).execute()
        return response, "Data fetched successfully"
    except Exception as e:
        return e, "Error fetching data"

def GetAll(db, table_name, column_name) :
    try:
        response = db.table(table_name).select(column_name).execute()
        return response, "Data fetched successfully"
    except Exception as e:
        return e, "Error fetching data"

def Update(db, table_name, data, id) :
    try:
        response = db.table(table_name).update(data).eq("id", id).execute()
        return response, "Data updated successfully"
    except Exception as e:
        return e, "Error updating data"

def Delete(db, table_name, id) :
    try:
        response = db.table(table_name).delete().eq("id", id).execute()
        return response, "Data deleted successfully"
    except Exception as e:
        return e, "Error deleting data"