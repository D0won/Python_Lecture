# 입력 파일과 출력 파일 이름을 받습니다.
infilename = input("입력 파일 이름 : ")
outfilename = input("출력 파일 이름 : ")

#입력과 출력을 위한 파일을 엽니다.
infile = open(infilename, "r")
outfile = open(outfilename, "w")

# 전체 파일을 읽습니다.
s = infile.read()

# 전체 파일을 씁니다.
outfile.write(s)

# 파일을 닫습니다.
infile.close()
outfile.close()
