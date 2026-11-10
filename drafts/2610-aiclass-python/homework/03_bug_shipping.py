# 과제 3. 배송비 계산기 버그 찾기
# 아래 코드를 Colab 셀에 붙여넣고 실행하세요.
# 이 코드는 에러 없이 "실행은" 됩니다. 하지만 결과가 틀린 곳이 2군데 있습니다. (논리 오류)
#
# [기획 규칙]
# 1) 주문 금액이 50,000원 "이상"이면 배송비 무료
# 2) 그 외에는 기본 배송비 3,000원
# 3) 제주·도서산간 지역은 추가 배송비 3,000원 (무료배송이어도 추가 배송비는 받음)
# 4) 최종 결제 금액 = 주문 금액 + 배송비

def shipping_fee(order_amount, is_remote):
    if order_amount > 50000:
        fee = 0
    else:
        fee = 3000

    if is_remote:
        fee = 3000

    return fee


def total_price(order_amount, is_remote):
    return order_amount + shipping_fee(order_amount, is_remote)


# ----- 실행해 보기 -----
print(total_price(30000, False))
print(total_price(60000, True))

# ----- 할 일 -----
# 1. 기획 규칙을 보고 "이 입력이면 이 결과가 나와야 한다"를 직접 계산해 아래 표를 채우세요.
#    | 주문 금액 | 도서산간 | 기대 배송비 |
#    | 30,000   | 아니오   |            |
#    | 50,000   | 아니오   |            |
#    | 60,000   | 아니오   |            |
#    | 30,000   | 예       |            |
#    | 60,000   | 예       |            |
# 2. 표를 assert 테스트로 옮기세요. 예: assert shipping_fee(30000, False) == 3000
# 3. 실패하는 테스트를 찾고, ChatGPT 질문 템플릿으로 원인을 물어보세요.
# 4. 고친 뒤 모든 assert가 통과하는지 확인하세요.
