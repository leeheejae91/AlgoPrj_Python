import re


def solution(word, pages):
    word = "("+word.lower()+")"
    word_re = re.compile(word)
    meta = re.compile('content="(.+?)"/>')
    link = re.compile('<a href="(.+?)">')
    basic_point = []
    link_point = []

    for i in pages:
        temp_tuple = {}
        i = i.lower()
        meta_data = meta.findall(i)
        temp_tuple['page'] = meta_data[0]
        temp_tuple['word_point'] = word_re.findall(i)
        print word_re.findall(i)

        basic_point.append(temp_tuple)

        link_data = list(set(link.findall(i)))
        for j in link_data:
            temp_tuple = {'from_page': meta_data[0], 'to_page': j, 'point' : i.count(j)}
            link_point.append(temp_tuple)

    answer = []
    for i in basic_point:
        cur_page = i['page']
        answer_point = i['word_point']

        for j in link_point:
            if j['to_page'] == cur_page:
                link_count = 0
                basic_count = 0

                for k in link_point:
                    if j['from_page'] == k['from_page']:
                        link_count += 1

                for k in basic_point:
                    if j['from_page'] == k['page']:
                        basic_count = k['word_point']
                        break;

                answer_point += float(basic_count)/link_count

        answer.append({'page': cur_page, 'answer_point': answer_point})

    print basic_point
    print link_point
    print answer
    max_point = 0
    max_idx = 0
    for i in range(len(answer)):
        if max_point < answer[i]['answer_point']:
            max_point = answer[i]['answer_point']
            max_idx = i

    return max_idx



print solution('Muzi', ['<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>', '<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>'])