from collections import deque

# キュー
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print()

# スタック
stack = deque()
stack.append(3)
stack.append(4)
stack.append(5)
print(stack.pop())
print(stack.pop())
print(stack.pop())

# キュー
stack.appendleft(7)
stack.appendleft(8)
stack.appendleft(9)
print(stack.pop())
print(stack.pop())
print(stack.pop())

# appendleftは使うことなくキューとスタックとして使用できる
