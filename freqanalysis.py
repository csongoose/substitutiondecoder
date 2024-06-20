def analyse(filename, ignore_specials=True):

    ignore = (' ', ',', '.', '-', '!', '?', ':', ';', '\n', '\t')

    frequencies = {}

    with open(filename, 'r') as f:
        encoded = f.read().lower()

    for i in encoded:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1

    freq_ignored: dict[str, int] = frequencies

    if ignore_specials:
        for i in ignore:
            if i in freq_ignored:
                del freq_ignored[i]

    all_letters = sum(freq_ignored.values())

    freq_sorted = dict(reversed(sorted(freq_ignored.items(), key=lambda x: x[1])))

    output = {}

    for i in freq_sorted:

        percentage = round(freq_sorted[i]/all_letters * 100, 2)

        output.setdefault(i, []).append(str(percentage) + "%")
        output.setdefault(i, []).append(freq_sorted[i])

    return output


def generate_table(analyse_filename, table_filename):

    analysed = analyse(analyse_filename)

    with open(table_filename, 'w') as f:
        for i in analysed:
            element = analysed[i]

            v = 0

            f.write(i + ': ')

            while v < len(element):
                val = element[v]
                f.write(str(val) + '  \t')
                v += 1

            f.write('\n')

    print('\nFrequency analysis file saved as: ' + str(table_filename))

    return True
