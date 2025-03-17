from fastapi import APIRouter, Header, Depends
from sqlalchemy.orm import Session
from db.configs.database import get_db
from server.utils.access_token_util import validate_access_token
from server.utils.api_key_util import validate_api_key
from server.utils.feature_utils.feature_query import get_feature_id_by_name
from server.utils.feature_utils.feature_access_util import check_user_feature_access

router = APIRouter(
    prefix="/feature",
    tags=["Feature"]
)

@router.post("/access/{feature_name}")
async def feature_access(
    feature_name: str,
    access_token: str = Header(None, alias="Access-Token"), 
    api_key: str = Header(None, alias="API-Key"),
    db: Session = Depends(get_db)):

    user_id = validate_access_token(access_token, db)
    if api_key:
        validate_api_key(api_key, db)

    feature_id = get_feature_id_by_name(feature_name, db)
    check_user_feature_access(user_id, feature_id, db)

    return {"message": "기능 접근 허용됨"}
