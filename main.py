def main():
  text = get_book_text("books/frankenstein.txt")
  print(count_words(text))
  # print(count_characters(text))
  list = dict_to_list(count_characters(text))
  print_report("books/frankenstein.txt", list)

def count_words(text):
  return len(text.split())


def count_characters(text):
  lowered_text = text.lower()
  char_dict = {}
  for char in lowered_text:
    if char not in char_dict:
      char_dict[char] = 1
    else:
      char_dict[char] += 1
  return char_dict


def get_book_text(path):
  with open(path) as f:
    return f.read()

def dict_to_list(dict):
  dict_list = []
  for i in dict:
    if i.isalpha():
      dict_list.append({"char": i, "num": dict[i]})
  return dict_list

def sort_on(dict):
  return dict["num"]


def print_report(path, list):
  list.sort(reverse=True, key=sort_on)
  print(f"--- Begin report of {path} ---")
  print("\n")

  for dict in list:
      print(f"The '{dict["char"]}' character was found {dict["num"]} times")
  
  print("--- End report --- ")








main()



