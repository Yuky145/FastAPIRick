from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlmodel import Session

from database import get_session
from models import Task, TaskCreate, TaskUpdate
import crud

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task_endpoint(task_create: TaskCreate, session: Session = Depends(get_session)):
    return crud.create_task(session, task_create)

@router.get("/", response_model=List[Task])
def list_tasks(session: Session = Depends(get_session)):
    return crud.get_tasks(session)

@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int, session: Session = Depends(get_session)):
    task = crud.get_task(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskUpdate, session: Session = Depends(get_session)):
    task = crud.update_task(session, task_id, task_update)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    success = crud.delete_task(session, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return
