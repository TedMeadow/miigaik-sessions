from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def get_registration_page():
    pass

@router.post('/')
async def registration():
    pass

