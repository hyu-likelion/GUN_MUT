# pizza : 토핑 없음 가능(빈배열) + 중복 가능 토핑
# drink : 사이즈 ( small, medium, large, tub)
# wings : int 개수
# coupon : .25 25퍼센트
# tax : 6.25 vjtpsxm
# round 반올림 round(x, 2)


def cost_calculator(x, drinks, wings, coupon):
    pizza = 13.00
    toppings = {"pepperoni":1.00,"mushroom":0.50,"olive":2.00, "anchovy":2.00,"ham":1.5}
    drinks = {"small":2.00, "medium": 3.00, "large":3.50,"tub":3.75}
    wings = {10:5.00,20:9.00,40:17.5,100:48}

    total = 0
    
    # pizza
    for i in x :
        total += pizza
        for j in i:
            if i in toppings.keys():
                total += toppings[i]

    # drinks
    for i in drinks:
        if i in drinks.keys():
            total += drinks[i]

    # wings
    for i in wings:
        if i in wings.keys():
            total += wings[i]

    total *= ( 1 + 0.0625)
    
    if not coupon:
        total = total * (1- coupon)

    answer = round(total, 2)


    return answer

    
