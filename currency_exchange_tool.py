currency_dict  =  { 
    "dollar" : 1.31,
    "euro" : 1.31,
    "cad" : 1.80,
    "yen" : 194.87,
    "HKD":  10.17 }


def exchange(chosen_currency,total_price):
    if chosen_currency in currency_dict  :
      if 10 <= float(total_price) <=1000:
        FP = float(total_price)* currency_dict[chosen_currency]
        FP = round(FP,3)
        print(FP)
        return FP
      else:
        print("not a valid total price")

    else:
        print(f"{chosen_currency} is not an option")
