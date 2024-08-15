from fastapi import Depends
from sqlalchemy.orm import Session

from user_management_system.config.database import get_db
from user_management_system.contexts.user.application.service.user_service import (
    UserApplicationService,
)
from user_management_system.contexts.user.domain.repository.user_repository import UserRepository
from user_management_system.contexts.user.infraestructure.database.db_user_repository import (
    UserPostgresRepository,
)


def get_user_repository(db: Session = Depends(get_db)):
    return UserPostgresRepository(db)


def get_user_application_service(
    user_repository: UserRepository = Depends(get_user_repository),
) -> UserApplicationService:
    return UserApplicationService(user_repository)
