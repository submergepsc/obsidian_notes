class User:
    def __init__(self, is_new=False, is_vip=False):
        self.is_new = is_new
        self.is_vip = is_vip
class Order:
    def __init__(self, amount, category=None, shipping_fee=0):
        self.amount = amount
        self.category = category
        self.shipping_fee = shipping_fee
class FullReductionCoupon:
    """满减券：满300减50"""
    def calculate(self, user, order):
        if order.amount >= 300:
            return 50
        return 0
class DiscountCoupon:
    """折扣券：8折，相当于优惠20%"""
    def calculate(self, user, order):
        return order.amount * 0.2
class NewUserCoupon:
    """新用户券：新用户减20"""
    def calculate(self, user, order):
        if user.is_new:
            return 20
        return 0
class CategoryCoupon:
    """品类券：生鲜满100减10"""
    def calculate(self, user, order):
        if order.category == "生鲜" and order.amount >= 100:
            return 10
        return 0
class VipCoupon:
    """VIP券：VIP 95折，相当于优惠5%"""
    def calculate(self, user, order):
        if user.is_vip:
            return order.amount * 0.05
        return 0
class FlashSaleCoupon:
    """秒杀券：限时优惠30"""
    def calculate(self, user, order):
        return 30
class ShippingCoupon:
    """运费券：包邮"""
    def calculate(self, user, order):
        return order.shipping_fee
class CouponService:
    def calculate_discount(self, user, order, coupons):
        total_discount = 0
        for coupon in coupons:
            total_discount += coupon.calculate(user, order)
        max_discount = order.amount + order.shipping_fee
        if total_discount > max_discount:
            return max_discount
        return total_discount
if __name__ == "__main__":
    user = User(is_new=True, is_vip=True)
    order = Order(amount=350, category="生鲜", shipping_fee=12)
    service = CouponService()
    coupons = [
        FullReductionCoupon(),
        NewUserCoupon(),
        CategoryCoupon(),
        VipCoupon(),
        ShippingCoupon()
    ]
    discount = service.calculate_discount(user, order, coupons)
    print("订单金额：", order.amount)
    print("运费：", order.shipping_fee)
    print("优惠金额：", discount)
    print("最终支付：", order.amount + order.shipping_fee - discount)