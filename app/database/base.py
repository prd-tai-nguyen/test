# Import all the models, so that Base has them before being
# imported by Alembic
from app.database.base_class import Base  # noqa
from app.models.product import Product  # noqa
from app.models.env import Env 
from app.models.feed import Feed
from app.models.env_feed import EnvFeed