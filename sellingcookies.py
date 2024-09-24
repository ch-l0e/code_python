#input
start_money = float(input("Enter the amount of money you currently have: "))
cookies_sold = input("Enter the amount of cookies sold. Use 'c' for normal cookies and 'b' for big cookies. ").lower()

#proccessing
big_cookies = 0
cookies = 0

for current_cookies in cookies_sold:
    #print(current_cookies)
    if current_cookies == 'c':
        cookies+= 1
    elif current_cookies == 'b':
        big_cookies += 1
    else:
        print(f"{current_cookies} is not a vaild sale item. moving on.")
# end of for loop

total_cookies = big_cookies + cookies
profit = (big_cookies * 1.25) + (cookies * 0.75)
total_money = profit + start_money

print(f"We sold {total_cookies} cookies. We made a profit of ${profit}. We now have ${total_money}.")