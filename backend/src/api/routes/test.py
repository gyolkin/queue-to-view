from fastapi import APIRouter, Depends, status

from src.api.dependencies.repository import get_repository
from src.models.schemas.test import TestCreate, TestResponse
from src.repository.crud.test import TestCRUDRepository

router = APIRouter(prefix="/main", tags=["main"])


@router.get(
    path="/",
    response_model=list[TestResponse],
    status_code=status.HTTP_200_OK,
)
async def get_tests(
    test_repo: TestCRUDRepository = Depends(
        get_repository(repo_type=TestCRUDRepository)
    ),
):
    db_tests = await test_repo.read_tests()
    return db_tests


@router.post(
    "/create_test/",
    response_model=TestResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_test(
    test_data: TestCreate,
    test_repo: TestCRUDRepository = Depends(
        get_repository(repo_type=TestCRUDRepository)
    ),
):
    new_test = await test_repo.create_test(test_data=test_data)
    return new_test
