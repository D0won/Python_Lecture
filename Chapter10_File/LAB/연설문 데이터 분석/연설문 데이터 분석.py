# 입력 파일 출력 파일 열기
infile = open("input.txt", "r")
outfile = open("output.txt", "w")

# 단어의 빈도를 저장할 빈 딕셔너리 생성
word_dic = {}
total_count = 0

for line in infile :
    line = line.rstrip()
    word_list = line.split()

    for word in word_list :
        word = word.lower() # 소문자로 번경
        word = word.strip(',') # 콤마 삭제
        word = word.strip('.') # 마침표 삭제
    
        if word in word_dic : 
            word_dic[word] += 1
            total_count += 1
        else :
            word_dic[word] = 1
            total_count += 1


result = ""
for key in sorted(word_dic.keys()) :
    result = key + " " + str(word_dic[key]) + '\n'
    outfile.write(result)

print("총 단어 수 = ", total_count)

         