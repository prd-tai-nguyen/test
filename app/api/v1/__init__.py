from fastapi import APIRouter

from app.api.v1.endpoints import products, envs, feeds, job_search_service


api_router = APIRouter()
api_router.include_router(products.router,
                          prefix="/products",
                          tags=["products"])

api_router.include_router(envs.router,
                          prefix="/envs",
                          tags=["envs"])

api_router.include_router(feeds.router,
                          prefix="/feeds",
                          tags=["feeds"])

api_router.include_router(job_search_service.router,
                          prefix="/jobs/",
                          tags=["jobs"])
