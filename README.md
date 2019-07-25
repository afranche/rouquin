# Rouquin

Small POC of a Python's sort-of Pattern Matching.

## Word of caution

This is an alpha project. The module will have a lot of interface changes
and internal changes as well. If you fell on this project by accident you
may star the project and come back later. If you're one of my coworkers,
please remind me that I left my water bottle in the fridge... :detective: 

## Why

While travelling through Github to search for pattern matching in Python
I saw [Pampy](https://github.com/santinic/pampy). I found it was awesome
and really well done and then I realized: "Hey, my code looks ugly using
[Black](https://github.com/psf/black) now. How comes ?"

So I decided to make this small project.

## Why would you need pattern matching in a Python project ?

It may be a personal point of view but there are cases at my work where
I could find some `if..elif..else` conditional structures that where
heavy. I figured out that, instead of having to resort to this. We could
use Pattern Matching, even more with the upcoming [Walrus operator](https://lwn.net/Articles/793818/).

It saves place.

## Examples

### I'd like to simply match against fixed values

```python
from rouquin import Match, ANY as _

age = input("What's your favourite number between 1, 3 and 21 ? ")

Match(age,
      (1, lambda: print("That's quite a .... singular number.")),
      (3, lambda: print("Jamais deux sans trois, hon hon.")),
      (21, lambda: print("I used to have that age... Once.")),
      (_, lambda: print("Ehm... I asked for something else but whatever.")))()
```

### Oooooh, fear the regex...


```python
from rouquin import Match, RegexMatch, ANY as _
pin = input("Please enter a valid 4-digits PIN Code: ")

Match(pin,
      (RegexMatch(r"\d{4}"), lambda: print("Nice PIN friend.")),
      (_, lambda: print("Sadly enough, it seems your PIN is invalid.")))()
```

## Roadmap

#### Allow conditional values to be put
- [ ]

```python
from rouquin import Match

age = input("What's your favourite number between 1, 3 and 21 ? ")

Match(age,
      (lambda v: v <= 12, lambda: print("WHEW KID, GROW UP A LITTLE!")),
      (lambda v: v >= 50, lambda: print("WHEW LAD, WHAT A GROWN UP MAN WE'VE GOT HERE")),
      (lambda v: v >= 13, lambda: print("'La fleur de l'âge'...")))  # Match will short-circuit if the second pattern matches.
```

#### Allow matching multiple values at the same time

- [ ] 

```python
from rouquin import Match, RegexMatch, ANY as _

citizens = {
    "Dordon Fightman": "Scientist",
    "Barnyu Calground": "Security Guard",
    "owo": "owo hewwooooo~",
}

the_wanted_citizen = ("The Fake Dordon", "Scientist")

Match(citizens,
      (_, "Scientist", lambda: print("I can guess you're the famous Dordon, last star of the Hokuto Mesa constellation..")),
      (RegexMatch(r"^Barnyu"), _, lambda: print("Not sure about this but I think I owe you a beer man..")),
      ("owo", _, lambda: print("ewe...")),
      (_, lambda: print("Congratulations, I don't know you...")))
```

#### Re-evaluate design to provide a much cleaner and beautiful module

- [ ] 

#### Backport for Python 2.7

- [ ] 

#### Eventually ship the project, idk...

- [ ] 
