from sqlmodel import select
from models import Task, TaskCreate, TaskUpdate
from sqlmodel import Session

def create_task(session: Session, task_create: TaskCreate) -> Task:
    task = Task.from_orm(task_create)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def get_task(session: Session, task_id: int) -> Task | None:
    return session.get(Task, task_id)

def get_tasks(session: Session) -> list[Task]:
    statement = select(Task)
    results = session.exec(statement).all()
    return results

def update_task(session: Session, task_id: int, task_update: TaskUpdate) -> Task | None:
    task = session.get(Task, task_id)
    if not task:
        return None
    update_data = task_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def delete_task(session: Session, task_id: int) -> bool:
    task = session.get(Task, task_id)
    if not task:
        return False
    session.delete(task)
    session.commit()
    return True
