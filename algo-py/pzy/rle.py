def rle(data):
    res_mapping = {}
    for d in data:
        if d in res_mapping:
            res_mapping[d] += 1
        else:
            res_mapping[d] = 1
    return res_mapping

def get_output(res_mapping):
    res = []
    for c in sorted(res_mapping.keys()):
        res.append('{}{}'.format(
            c, res_mapping[c]))
    return ''.join(res)

if __name__ == "__main__":
    data = 'aaabbbcccadddeeffacdbbec'
    print get_output(rle(data))
