import sys

file_log = open(sys.argv[1], 'r', encoding='utf-8')
content_log = file_log.readlines()
content_result = []
for line in content_log:
    if line[0:6] == '[CHAT]':
        content_result.append(line)
file_result = open('chat.log', 'w', encoding='utf-8')
file_result.writelines(content_result)
