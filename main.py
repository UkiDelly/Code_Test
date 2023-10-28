def solution(words: list[str], queries: list[str]):
    answer = []
    head, head_prev = {},{}

    def add(head: dict, word: str):
        node = head
        # 단어의 각 문자마다,
        for w in word:
            # node에 해당 문자의 key가 존재하지 않을때,
            if w not in node:
                # 해당 문자의 키를 생성과 동시에 딕셔너리를 생성
                node[w] = {}

            # node를 해당 문자의 dict으로 전환
            node = node[w]

            # len 키가 존재하지 않은 경우, 키 생성과 함께 단어의 길이를 저장
            if "len" not in node:
                node["len"] = [len(word)]
            else:
                # len키가 존재하는 경우, 단어의 길이를 저장
                node["len"].append(len(word))
        # 각 문자마다 end 키를 추가
        node["end"] = True

    for word in words:
        add(head, word)

    # words = set(words)
    # for query in queries:
    #     letter = re.sub(r"[?]", "", query)
    #     q_count = query.count("?")
    #     q_first = query.index("?")
    #     if q_first != 0:
    #         raw_pattern = r"'" + letter + r"[a-zA-Z]{" + str(q_count) + r"}'"
    #     else:
    #         raw_pattern = r"'[a-zA-Z]{" + str(q_count) + r"}" + letter + r"'"
    #     pattern = re.compile(raw_pattern)
    #     l = pattern.findall(str(words))
    #     answer.append(len(l))
    return answer


print(
    solution(
        ["frodo", "front", "frost", "frozen", "frame", "kakao"],
        ["fro??", "????o", "fr???", "fro???", "pro?"],
    )
)
