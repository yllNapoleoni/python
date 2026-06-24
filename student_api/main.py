from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import SessionLocal, engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student API")


# Dependency: get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------------------------
# CREATE STUDENT
# -------------------------
@app.post("/students")
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)


# -------------------------
# READ STUDENTS
# -------------------------
@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    return crud.get_students(db)


# -------------------------
# UPDATE STUDENT (PUT)
# -------------------------
@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    updated_student = crud.update_student(db, student_id, student)

    if not updated_student:
        raise HTTPException(status_code=404, detail="Student not found")

    return updated_student


# -------------------------
# DELETE STUDENT
# -------------------------
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    deleted_student = crud.delete_student(db, student_id)

    if not deleted_student:
        raise HTTPException(status_code=404, detail="Student not found")

    return {"message": "Student deleted successfully"}