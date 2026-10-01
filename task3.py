words = ["кот", "пёс", "кот", "кот", "ёж", "пёс", "кот"]
freq = {}
for word in words:
    if word not in freq:
        freq[word] = 1
    else:
        freq[word] += 1
res = []
for key, val in freq.items():
    res.append([val, key])
res.sort(reverse=True)
cnt_display = 0
for n, lst in enumerate(res, 1):
    cnt, word = lst
    if cnt_display == 3:
        break
    print(f'{n}. {word} — {cnt}')
    cnt_display += 1