# 同时对数据做转换和换算

portfolio=[
    {'name':'bob','shares':50},
    {'name':'acc','shares':90},
    {'name':'sxz','shares':30},
    {'name':'edr','shares':70},
]

min_shares=min(s['shares'] for s in portfolio)

print(min_shares)

min_name_and_share=min(portfolio,key=lambda s: s['shares'])

print(min_name_and_share)