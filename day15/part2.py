#!/usr/bin/env pypy

with open(0) as f:
    steps = list(
        filter(
            lambda x: len(x) > 0,
            f.read().split(",")
        )
    )

steps = list(map(list, steps))

current_box, boxes = 0, {}

for step in steps:
    last = step.pop()
    sign = "-" if last == "-" else "="
    
    if sign == "=":
        step.pop()
    
    label = "".join(step)

    box = 0

    for c in label:
        box = ((box + ord(c)) * 17) % 256

    bk = boxes.keys()

    match sign:
        case "-":
            if not box in bk:
                continue
            
            boxes[box] = list(filter(lambda l: l[0] != label, boxes[box]))
        case "=":
            lens = (label, last)

            if not box in bk:
                boxes[box] = [lens]
                continue
            
            idx = None
            
            for i, (l, _) in enumerate(boxes[box]):
                if l == label:
                    idx = i
                    break
            
            if idx == None:
                boxes[box].append(lens)
            else:
                boxes[box][idx] = lens
fp = 0

for box_number, box in boxes.items():
    for slot, (_, focal_length) in enumerate(box):
        fp += (box_number + 1) * (slot + 1) * int(focal_length)

print(fp)
