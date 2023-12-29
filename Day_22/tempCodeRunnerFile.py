for tr in items[:15]:
#     fixed_info = tr.find(['div'], {'class': 'item-info'})
#     info = fixed_info.contents
#     for inf in info[1:2]:
#         gpu_info = inf.string

#     fixed_price = tr.find(['div'], {'class': 'item-action'})
#     price = fixed_price.strong.string

#     # product_info[gpu_info] = price
    
#     # keys = product_info.keys()
#     # values = product_info.values()
    
#     print(f'{gpu_info}' +'  ' f'Price:{price}')