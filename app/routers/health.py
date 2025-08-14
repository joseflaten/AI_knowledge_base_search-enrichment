from fastapi import APIRouter

router = APIRouter(tags=["Health"])

@router.get("/health", summary="Health check endpoint")
def health_check():
    """
    Returns the health status of the API.
    """
    return {"status": "ok"}
