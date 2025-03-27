def pdata(input_data):
    return[x+10 for x in input_data]

data = [1,2,3,4,5]
processdata = pdata(data)

print(processdata)

def transform_date(input_data):

    return[x*2 for x in input_data]

transformdata = transform_data(data)

print(transformdata)

def validate_data(input_data):
    return[x >= 0 for x in input_data]


dataval = validate_data(data)

print(dataval)
