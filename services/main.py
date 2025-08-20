from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from data_loader.DAL import Client
from data_loader.document import Document

app = FastAPI()  # יצירת אפליקציית FastAPI

client = Client()  # יצירת מופע של המחלקה שמתחברת ל־MongoDB

# מודל נתונים של Pydantic לבדיקה ואימות נתונים שמגיעים מה־API
class DocumentModel(BaseModel):
    id: str
    first_name: str
    last_name: str
    phone_number: str
    rank: str

# ------------------- CREATE -------------------
@app.post("/documents/")
def create_document(doc: DocumentModel):
    try:
        # המרת DocumentModel ל־Document
        document = Document(
            id=doc.id,
            first_name=doc.first_name,
            last_name=doc.last_name,
            phone_number=doc.phone_number,
            rank=doc.rank
        )
        client.create_document(document)  # שמירה במסד
        return {"message": "Document created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ------------------- READ -------------------
@app.get("/soldiersdb/")
def read_documents():
    try:
        docs = client.read_document()
        result = []
        for doc in docs:
            doc["_id"] = str(doc["_id"])  # המרת ObjectId ל־string
            result.append(doc)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ------------------- UPDATE -------------------
@app.put("/soldiersdb/{doc_id}")
def update_document(doc_id: str, doc: DocumentModel):
    try:
        col = client.conn.get_collection()
        result = col.update_one(
            {"id": doc_id},
            {"$set": {
                "first_name": doc.first_name,
                "last_name": doc.last_name,
                "phone": doc.phone_number,
                "rank": doc.rank
            }}
        )
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Document not found")
        return {"message": "Document updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ------------------- DELETE -------------------
@app.delete("/soldiersdb/{doc_id}")
def delete_document(doc_id: str):
    try:
        col = client.conn.get_collection()
        result = col.delete_one({"id": doc_id})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Document not found")
        return {"message": "Document deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
