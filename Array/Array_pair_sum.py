def pair_sum(arr, k):
    # Edge case check
    if len(arr) < 2:
        return

    #sets for tracking
    seen = set()
    output = set()

    for num in arr:
        target = k-num

        if target not in seen:
            seen.add(num)

        else:
            output.add((min(target,num),max(target,num)))

    print('\n'.join(map(str,output)))
    return len(output)

print(pair_sum([1,3,2,2],4))