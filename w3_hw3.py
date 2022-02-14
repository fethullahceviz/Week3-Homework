items = input("Enter different words with hyphen (-) in between:").split('-')
print("Input  >>>","-".join(items))
def word_sort(items):
    return print("Output >>>",'-'.join(items))
items.sort()
word_sort(items)