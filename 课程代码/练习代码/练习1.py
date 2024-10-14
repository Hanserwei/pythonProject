name = "牛马工作室"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
grow_days = 7
print(f"公司：{name},股票代码{stock_code}，当前股价{stock_price}")
print("每日增长系数是%s,经过%d的增长,股价达到了%.2f" % (stock_price_daily_growth_factor, 7 , stock_price*(stock_price_daily_growth_factor**grow_days)))