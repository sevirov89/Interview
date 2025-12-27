class Stack:
    def __init__(self, my_stack=None):
        if my_stack is None:
            self.my_stack = []
        else:
            self.my_stack = my_stack

    def is_empty(self):
        return len(self.my_stack) == 0

    def push(self, new_elem):
        self.my_stack.append(new_elem)

    def pop(self):
        if not self.is_empty():
            return self.my_stack.pop()
        else:
            return IndexError("Error pop - empty stack")

    def peek(self):
        if not self.is_empty():
            return self.my_stack[-1]
        else:
            return IndexError("Error peek - empty stack")

    def size(self):
        return len(self.my_stack)

def is_balanced(brackets):
    stack = Stack()
    open_brackets = ['(', '[', '{']
    close_brackets = [')', ']', '}']
    pairs = {')': '(', ']': '[', '}': '{'}

    for bracket in brackets:
        if bracket in open_brackets:
            stack.push(bracket)
        elif bracket in close_brackets:
            if stack.is_empty() or stack.pop() != pairs[bracket]:
                return "Несбалансировано"
    return "Сбалансировано"

if __name__ == "__main__":
    test_cases = [
        "(((([{}]))))",
        "[([])((([[[]]])))]{()}",
        "{{[()]}}",
        "}{}",
        "{{[(])]}}",
        "[[{())}]"
    ]

    for case in test_cases:
        print(f"{case}: {is_balanced(case)}")