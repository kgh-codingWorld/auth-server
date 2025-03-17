import logging
from fastapi import APIRouter, Header, Depends
from sqlalchemy.orm import Session
from db.configs.database import get_db
from db.models import User
from server.models.request_model import FeatureRequest
from server.utils.access_token_util import validate_access_token
from server.utils.admin_utils.feature_admin_util import check_admin_permissions, validate_feature_request, check_existing_feature, add_new_feature

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/admin/feature",
    tags=["Feature Admin"]
)

@router.post("/add")
async def add_feature(request: FeatureRequest, db: Session = Depends(get_db), access_token: str = Header(None)):
    user_id_from_token_data = validate_access_token(access_token, db)
    user = db.query(User).filter(User.id == user_id_from_token_data).first()
    check_admin_permissions(user)
    validate_feature_request(request)
    check_existing_feature(request, db)
    add_new_feature(request, db)
    return {"message": "기능 추가 성공"}