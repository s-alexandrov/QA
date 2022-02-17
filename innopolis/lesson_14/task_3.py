def words():
    text = input().split('_')
    keywords = input().split(', ')
    for word in keywords:
        if word not in text:
            return False
    return True


print(words())