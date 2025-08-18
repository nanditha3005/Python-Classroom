product= {
    'pid':101,
    'pname':'Marker pen',
    'price':50,
    'details':{
        'color':['blue','red','yellow'],
        'size':'small',
        'avail':True
    }
}
print(product['details']['color'][0])
print(product['details']['color'][1])
print(product['details']['color'][2])
print(product['details']['size'])
