import fastapi

router = fastapi.APIRouter()


@router.get("/courses")
async def read_courses():
    return {"courses": []}


@router.post("/courses")
async def create_course():
    return {"courses": []}


@router.get("/course/{id}")
async def read_course():
    return {"courses": []}


@router.patch("/course/{id}")
async def update_course():
    return {"courses": []}


@router.delete("/course/{id}")
async def delete_course():
    return {"courses": []}


@router.get("/course/{id}/sections")
async def read_course_sections():
    return {"courses": []}
