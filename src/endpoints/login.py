from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def get_login_page():
    pass

@router.post('/')
async def login():
    pass