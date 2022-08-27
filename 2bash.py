# This file using for generating of bash script,
# which will be used for requesting data from GitHub

import pandas as pd

access_token = ""

ex_data = pd.read_excel('methods.xlsx')

langauge_names = ['Java', 'Ruby', 'Python', 'C++', 'JavaScript', 'Go', 'C#', 'Swift', 'PHP', 'Rust']

separation_line = "echo -e \"\\n\""

print()

print(separation_line)

print("echo -e \"\\n\" > results.txt")

print(separation_line)

for name in langauge_names:
    array_name = "req" + name
    names = list(filter(lambda w: str(w) != "nan", ex_data[name].values.tolist()))
    function_names_string = "\"" + '\" \"'.join(map(str, names)) + "\""

    print("echo \"%s Started\"" % name)
    print("%s=(%s)" % (array_name, function_names_string))

    print("for str in ${%s[@]}; do" % array_name)
    print("  INPUT=$(curl --location --request GET \"https://api.github.com/search/code?q=$str+in:file+language:%s\" "
          "--header \'Authorization: Token %s\')" % (name.lower(), access_token))
    print("  sub1=${INPUT#*:}")
    print("  sub2=${INPUT#*,}")
    print("  left=$((${#INPUT} - ${#sub1} + 1))")
    print("  right=$((${#INPUT} - ${#sub2}))")
    print("  length=$(($right - $left - 1))")
    print("  result=${INPUT:${left}:${length}}")
    print("  echo lang: %s, answer_length: ${#INPUT}, method: $str, amount: $result >> results.txt" % name)
    print("  sleep 61")
    print("done")

    print("echo \"%s Finished\"" % name)
    print(separation_line)
    print()
