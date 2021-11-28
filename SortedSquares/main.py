Solution = open("solution.py", "r")
solution = Solution.read()
Test = open("tests.py", "r")
test = Test.read()
Text = open("text.txt", "r")
text = Text.read()
url = "https://leetcode.com/problems/squares-of-a-sorted-array/"
task = "Squares of a Sorted Array"

result = ""

def task_r(task: str):
    return "# " + task + "\n\n"

def text_r(text: str):
    return text + "\n\n"

def url_r(task: str, url: str):
    return "[" + task + "](" + url + ")\n\n"

def test_r(test: str):
    return "Tests:\n```python\n" + test + "\n```\n\n"

def solution_r(solution: str):
    return "Solution:\n```python\n" + solution + "\n```\n\n"

result += task_r(task)
result += text_r(text)
result += url_r(task, url)
result += test_r(test)
result += solution_r(solution)

def main():
    file = open("Damir.md", "w+")
    file.write(result)

if __name__ == "__main__":
    main()