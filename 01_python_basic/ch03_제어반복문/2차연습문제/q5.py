HEIGHT = 5
for start_count in range(1, HEIGHT+1):
    blank_count =  HEIGHT - start_count
    print( (' ' * blank_count) + ('*' * start_count) )