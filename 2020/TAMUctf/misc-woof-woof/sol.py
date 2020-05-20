a ="woof woof bark ruff bark bark ruff woof woof bark ruff bark ruff woof woof ruff woof bark bark bark bark woof ruff woof bark bark ruff woof woof woof woof woof ruff woof woof bark ruff woof ruff bark woof woof bark woof bark ruff bark bark bark ruff woof ruff bark woof woof woof woof ruff woof bark woof bark ruff bark woof woof woof ruff woof woof woof woof woof ruff woof bark bark bark ruff woof bark bark bark bark woof"

a = a.replace("woof", "0")
a = a.replace("bark", "1")
a = a.replace(" ", "")
a = a.replace("ruff", " ")

print(a)
