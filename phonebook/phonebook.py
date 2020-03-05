book = ['123', '456', '789']


def check_valid(phone_book):
    for i in range(len(phone_book)):
        cur = phone_book[i]

        for j in range(i+1, len(phone_book)):
            next_book = phone_book[j]
            if ''.join(next_book[:len(cur)]) == cur:
                return False
            elif ''.join(cur[:len(next_book)]) == next_book:
                return False

    return True


print(check_valid(book))
