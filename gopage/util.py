import sys
sys.dont_write_bytecode = True
reload(sys)
sys.setdefaultencoding('utf8')


def create_dir_if_not_exist(dir_path):
    import os
    if not os.path.exists(dir_path):
        print 'creating path:', dir_path
        os.mkdir(dir_path)


def del_a_from_b(a, b):
    if a not in b:
        return b
    part_pos = b.find(a)
    if part_pos + len(a) >= len(b):
        b = b[:part_pos]
    else:
        b = b[:part_pos] + b[(part_pos+len(a)):]
    return b


def is_a_in_b(a, b):
    a = str(a)
    b = str(b)
    if a not in b:
        return False
    start_pattern = a + ' '
    end_pattern = ' ' + a
    if (' ' + a + ' ') in b:
        return True
    if start_pattern in b and b.find(start_pattern) == 0:
        return True
    if end_pattern in b and b.find(end_pattern) == (len(b) - len(end_pattern)):
        return True
    return False


def clean_head_and_tail(s):
        if not s:
            return ''
        head_pos = 0
        while head_pos < len(s)-1 and not s[head_pos].isalpha():
            head_pos += 1
        tail_pos = -1
        while tail_pos > -1 and not s[tail_pos].isalpha():
            tail_pos -= 1
        if tail_pos == -1:
            return s[head_pos:]
        return s[head_pos: tail_pos+1]


def prefix_is_invalid_keyword(prefix):
        invalid_keyword_list = ['email', 'info', 'mailto', 'lastname', 'name']
        is_invalid_prefix = False
        for invalid_keyword in invalid_keyword_list:
            if prefix == invalid_keyword:
                is_invalid_prefix = True
                break
        return is_invalid_prefix


# get_known_top_1000()

if __name__ == '__main__':
    get_top_citation()
    get_known_top_1000()