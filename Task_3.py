def writing_to_file(*args):
    dict_name_len = {}
    for file in args:
        with open(file, encoding='utf-8') as f:
            dict_name_len[file] = len(f.readlines())

    sort_dict = sorted(dict_name_len.items(), key=lambda x: x[1])
    dict_name_len = dict(sort_dict)

    for name, count in dict_name_len.items():
        with open('result.txt', 'a', encoding='utf-8') as res:
            res.write(name + '\n')
            res.write(str(count) + '\n')
            with open(name, encoding='utf-8') as text:
                for line in text:
                    res.write(line)
                res.write('\n')


writing_to_file('1.txt', '2.txt', '3.txt')
