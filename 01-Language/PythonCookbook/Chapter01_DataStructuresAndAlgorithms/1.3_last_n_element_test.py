"""
模拟服务器日志文本，实现一个生成器函数：
输入：
    可迭代文本行、要匹配的关键字、后置上下文行数（默认 3）
    逻辑：遍历每一行日志，如果当前行包含目标关键字
    先产出匹配行本身
    再产出匹配行之后最多 N 行日志（后置上下文）
    
约束：
    不能一次性把所有日志存入列表，要用惰性 yield 流式输出
    匹配后的后置行需要缓存，用 deque 保存待输出的后置上下文
    读到文件末尾时，缓存里剩余未输出的行直接丢弃
"""
from collections import deque

def find_log_after_jyj(lines, keyword: str, after=3):
    boolean_flag = False
    remaining_after = 0
    for line in lines:
        if boolean_flag and remaining_after > 0:
            yield line
            remaining_after -= 1
            if remaining_after == 0:
                boolean_flag = False
        if keyword in line:
            boolean_flag = True
            yield line
            remaining_after = after

def find_log_after(lines, keyword: str, after=3):
    cache = deque(maxlen=after)
    for line in lines:
        if keyword in line:
            yield line
            # 把缓存里已经读到的后置行全部吐出
            for cache_line in cache:
                yield cache_line
            cache.clear()
        else:
            cache.append(line)

if __name__ == "__main__":
    log_text = """
2026-07-01 10:00:00 user login success
2026-07-01 10:00:01 request /api/user
2026-07-01 10:00:02 database query start
2026-07-01 10:00:03 ERROR: connection timeout
2026-07-01 10:00:04 retry connect db
2026-07-01 10:00:05 retry connect db
2026-07-01 10:00:06 recover success
2026-07-01 10:00:07 business logic done
2026-07-01 10:00:08 ERROR: second error
2026-07-01 10:00:09 test1
2026-07-01 10:00:10 test2
"""
    lines = log_text.strip().splitlines()
    # 检索关键字 ERROR，打印匹配行+后面3行上下文
    for line in find_log_after(lines, "ERROR", after=3):
        print(line)
        print("-" * 50)