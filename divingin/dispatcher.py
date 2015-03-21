import statsout

def output(data, format="text"):
    output_function = getattr(statsout, 'output_%s' % format)
    return output_function(data)