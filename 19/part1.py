#!/usr/bin/env pypy

with open(0) as f:
    blocks = list(
        filter(
            lambda x: len(x) > 0,
            f.read().split("\n\n")
        )
    )

blocks = list(map(lambda x: x.splitlines(), blocks))

workflows, rules = {}, []

for workflow in blocks.pop(0):
    name, tests = workflow[:-1].split("{")
    
    workflows[name] = tests.split(",")

for rule in blocks.pop(0):
    rule = rule[1:-1].split(",")
    
    rule = [int(r.split("=").pop()) for r in rule]

    rules.append(rule)

_sum = 0

while rules:
    rule = rules.pop(0)
    x, m, a, s = rule
    
    workflow = "in"
    
    while not workflow in ("A", "R"):
        tests = workflows[workflow]
        
        for t in tests:
            test = t.split(":")
            
            if len(test) <= 1:
                workflow = test.pop()
                break
            
            e, o = test
            
            if eval(e):
                workflow = o
                break

    if workflow == "A":
        _sum += sum(rule)

print(_sum)
