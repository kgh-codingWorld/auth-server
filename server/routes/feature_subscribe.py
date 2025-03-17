from fastapi import APIRouter, Header, Depends
from sqlalchemy.orm import Session
from db.configs.database import get_db
from server.utils.access_token_util import validate_access_token
from server.utils.api_key_util import validate_api_key
from server.utils.feature_utils.feature_subscribe_util import add_feature_subscribe

router = APIRouter(
    prefix="/feature",
    tags=["Feature Subscribe"]
)

@router.post("/subscribe/{feature_name}")
async def feature_subscribe(
    feature_name: str,
    access_token: str = Header(None, alias="Access-Token"),
    api_key: str = Header(None, alias="API-Key"),
    db: Session = Depends(get_db)
):
    user_id = validate_access_token(access_token, db)
    if api_key:
        validate_api_key(api_key, db)
    return add_feature_subscribe(user_id, feature_name, api_key, db)