from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class OrderSide(Enum):
    BUY = "BUY"
    SELL = "SELL"


class OrderType(Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"


class OrderStatus(Enum):
    CREATED = "CREATED"
    SUBMITTED = "SUBMITTED"
    PARTIALLY_FILLED = "PARTIALLY_FILLED"
    FILLED = "FILLED"
    CANCELLED = "CANCELLED"
    REJECTED = "REJECTED"
    FAILED = "FAILED"


@dataclass
class Order:
    symbol: str
    side: OrderSide
    quantity: float
    order_type: OrderType = OrderType.MARKET
    price: Optional[float] = None
    status: OrderStatus = OrderStatus.CREATED
    order_id: Optional[str] = None
    filled_quantity: float = 0.0
    created_at: datetime = field(default_factory=datetime.utcnow)

    def fill(self, quantity: float):
        self.filled_quantity = quantity
        self.status = OrderStatus.FILLED

    def cancel(self):
        self.status = OrderStatus.CANCELLED

    def reject(self):
        self.status = OrderStatus.REJECTED
