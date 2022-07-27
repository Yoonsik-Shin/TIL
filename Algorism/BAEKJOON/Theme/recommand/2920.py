note = list(map(int,input().split()))
note_ascending = [1,2,3,4,5,6,7,8]
note_descending = note_ascending[::-1]

if note == note_ascending:
    print('ascending')
elif note == note_descending:
    print('descending')
else:
    print('mixed')