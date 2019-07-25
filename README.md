# Rouquin

Small project of a Python's sort-of Pattern Matching.

## Why

While travelling through Github to search for pattern matching in Python
I saw [Pampy](https://github.com/santinic/pampy). I found it was awesome
and really well done but my code sadly got disappointing since I began
using Black at work.

So I decided to make this small project, I could have forked pampy but
I prefer to make my own project for learning reasons..

**tl;dr, use [Pampy](https://github.com/santinic/pampy) if you do not use Black on your project**.

## Examples

### Match a single value

```python
label = "label_4"

if label == "label_1":
    pass # do this...
elif label == "label_2":
    pass # do this...
elif label == "label_2":
    pass # do this...
else:
    pass # do other stuff...
```

vs.

```python
from rouquin import Match, ANY as _

label = "label_4"

Match(label,
      ("label_1", lambda: print("Do this")),
      ("label_2", lambda: print("Do this")),
      ("label_3", lambda: print("Do this")),
      (_, lambda: print("Do other stuff...")),)() # --> "Do other stuff"
```

### Match on multiple values

```python
import random

danger_level = random.randint(1, 5)
first_name = input("Glory to Arstotzka, what's your first name ?\n")
last_name = input("Good, good... Last name ?\n")

if danger_level >= 4 or (
    first_name == "Jorji"
    and last_name == "Costava"
    ) or (
    first_name == "Vince"
    and last_name == "Lestrade"
    and danger_level > 2
    ):
    can_pass = False
else:
    can_pass = True
```

vs.

```python
import random
from rouquin import Match, ANY as _

danger_level = random.randint(1, 5)
first_name = input("Glory to Arstotzka, what's your first name ?\n")
last_name = input("Good, good... Last name ?\n")

can_pass = Match((danger_level, first_name, last_name),
                 ((lambda d: d >= 4, _, _), False),
                 ((_, "Jorji", "Costava"), False),
                 ((lambda d: d > 2, "Vince", "Lestrade"), False),
                 (_, True)
                )  
```

## Roadmap

- Allow matching multiple values at the same time :heavy_check_mark:

- Allow conditional functions :timer_clock:

- Re-evaluate design to provide a much cleaner and beautiful module :negative_squared_cross_mark:
