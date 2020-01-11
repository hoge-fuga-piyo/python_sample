# Shift JISのファイル
src_file_path = "./data/shift_jis.txt"

# UTF-8のファイル
dst_file_path = "./result/utf8.txt"

dst_file = open(dst_file_path, 'a')

with open(src_file_path, 'r', encoding="shift_jis") as f:
  for line in f:
    print(line, end='')
    dst_file.write(line)