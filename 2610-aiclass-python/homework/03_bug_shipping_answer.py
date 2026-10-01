# 과제 3 정답 (강사용)
# 버그 1: order_amount > 50000  → 50,000원 "이상"이므로 >= 이어야 함 (경계값 오류)
# 버그 2: fee = 3000            → 추가 배송비이므로 fee += 3000 이어야 함 (덮어쓰기 오류)

def shipping_fee(order_amount, is_remote):
    if order_amount >= 50000:
        fee = 0
    else:
        fee = 3000
    if is_remote:
        fee += 3000
    return fee

assert shipping_fee(30000, False) == 3000
assert shipping_fee(50000, False) == 0
assert shipping_fee(60000, False) == 0
assert shipping_fee(30000, True) == 6000
assert shipping_fee(60000, True) == 3000
print("모든 테스트 통과")
