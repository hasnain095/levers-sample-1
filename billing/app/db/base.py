# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.subbill import SubBill
from app.models.bill import Bill
