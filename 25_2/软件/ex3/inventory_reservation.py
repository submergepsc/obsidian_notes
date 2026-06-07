import uuid
import threading
class InventoryError(Exception):
    """库存相关异常"""
    pass
class Inventory:
    def __init__(self, product_id, total_stock):
        if not product_id:
            raise InventoryError("product_id 不能为空")
        if not isinstance(total_stock, int):
            raise InventoryError("total_stock 必须是整数")
        if total_stock < 0:
            raise InventoryError("total_stock 不能小于 0")
        self.product_id = product_id
        self.total_stock = total_stock
        self.available_stock = total_stock
        self.reserved_stock = 0
        # 用锁保证库存检查和库存修改是一个整体操作，避免并发情况下超卖
        self._lock = threading.RLock()
    def __repr__(self):
        return (
            f"Inventory(product_id={self.product_id}, "
            f"total_stock={self.total_stock}, "
            f"available_stock={self.available_stock}, "
            f"reserved_stock={self.reserved_stock})"
        )
class Reservation:
    STATUS_RESERVED = "RESERVED"
    STATUS_CANCELLED = "CANCELLED"
    STATUS_PAID = "PAID"
    def __init__(self, product_id, user_id, quantity):
        if not product_id:
            raise InventoryError("product_id 不能为空")
        if not user_id:
            raise InventoryError("user_id 不能为空")
        if not isinstance(quantity, int):
            raise InventoryError("quantity 必须是整数")
        if quantity <= 0:
            raise InventoryError("quantity 必须大于 0")
        self.id = str(uuid.uuid4())
        self.product_id = product_id
        self.user_id = user_id
        self.quantity = quantity
        self.status = Reservation.STATUS_RESERVED
    def __repr__(self):
        return (
            f"Reservation(id={self.id[:8]}..., "
            f"product_id={self.product_id}, "
            f"user_id={self.user_id}, "
            f"quantity={self.quantity}, "
            f"status={self.status})"
        )
class InventoryService:
    def _check_inventory(self, inventory):
        if inventory is None:
            raise InventoryError("inventory 不能为空")
        if inventory.total_stock < 0:
            raise InventoryError("total_stock 不能小于 0")
        if inventory.available_stock < 0:
            raise InventoryError("available_stock 不能小于 0")
        if inventory.reserved_stock < 0:
            raise InventoryError("reserved_stock 不能小于 0")
        if inventory.total_stock != inventory.available_stock + inventory.reserved_stock:
            raise InventoryError("库存数据不一致")
    def _check_reservation(self, reservation):
        if reservation is None:
            raise InventoryError("reservation 不能为空")
        if reservation.quantity <= 0:
            raise InventoryError("reservation.quantity 必须大于 0")
        if reservation.status not in {
            Reservation.STATUS_RESERVED,
            Reservation.STATUS_CANCELLED,
            Reservation.STATUS_PAID,
        }:
            raise InventoryError("reservation.status 状态非法")
    def _check_product_match(self, inventory, reservation):
        if inventory.product_id != reservation.product_id:
            raise InventoryError("预留记录与库存商品不匹配")
    def reserve(self, inventory, user_id, quantity):
        if inventory is None:
            raise InventoryError("inventory 不能为空")
        if not user_id:
            raise InventoryError("user_id 不能为空")
        if not isinstance(quantity, int):
            raise InventoryError("quantity 必须是整数")
        if quantity <= 0:
            raise InventoryError("预留数量必须大于 0")
        with inventory._lock:
            self._check_inventory(inventory)
            if inventory.available_stock < quantity:
                raise InventoryError("可售库存不足，不能创建预留")
            reservation = Reservation(inventory.product_id, user_id, quantity)
            inventory.available_stock -= quantity
            inventory.reserved_stock += quantity
            self._check_inventory(inventory)
            return reservation
    def cancel(self, inventory, reservation):
        self._check_inventory(inventory)
        self._check_reservation(reservation)
        self._check_product_match(inventory, reservation)
        with inventory._lock:
            self._check_inventory(inventory)
            if reservation.status == Reservation.STATUS_CANCELLED:
                raise InventoryError("已取消的预留不能重复取消")
            if reservation.status == Reservation.STATUS_PAID:
                raise InventoryError("已完成支付的预留不能取消")
            if reservation.status != Reservation.STATUS_RESERVED:
                raise InventoryError("只有 RESERVED 状态的预留才能取消")
            if inventory.reserved_stock < reservation.quantity:
                raise InventoryError("预留库存不足，库存数据异常")
            inventory.available_stock += reservation.quantity
            inventory.reserved_stock -= reservation.quantity
            reservation.status = Reservation.STATUS_CANCELLED
            self._check_inventory(inventory)
    def confirm_payment(self, inventory, reservation):
        self._check_inventory(inventory)
        self._check_reservation(reservation)
        self._check_product_match(inventory, reservation)
        with inventory._lock: 
            self._check_inventory(inventory)
            if reservation.status == Reservation.STATUS_PAID:
                raise InventoryError("已支付的预留不能重复支付")
            if reservation.status == Reservation.STATUS_CANCELLED:
                raise InventoryError("已取消的预留不能确认支付")
            if reservation.status != Reservation.STATUS_RESERVED:
                raise InventoryError("只有 RESERVED 状态的预留才能确认支付")
            if inventory.reserved_stock < reservation.quantity:
                raise InventoryError("预留库存不足，库存数据异常")
            inventory.reserved_stock -= reservation.quantity
            inventory.total_stock -= reservation.quantity
            reservation.status = Reservation.STATUS_PAID
            self._check_inventory(inventory)
if __name__ == "__main__":
    service = InventoryService()
    inventory = Inventory("product_001", 10)
    print("初始库存：")
    print(inventory)
    reservation1 = service.reserve(inventory, "user_001", 3)
    reservation2 = service.reserve(inventory, "user_002", 4)
    print("\n创建预留后：")
    print(inventory)
    print(reservation1)
    print(reservation2)
    service.cancel(inventory, reservation1)
    print("\n取消 reservation1 后：")
    print(inventory)
    print(reservation1)
    service.confirm_payment(inventory, reservation2)
    print("\n确认支付 reservation2 后：")
    print(inventory)
    print(reservation2)