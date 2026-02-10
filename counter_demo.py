from counter import Counter
tally = Counter()
tally.reset()

#tally.click()
#tally.click()

result = tally.getStroke()
print("Stroke: ", result)

result = tally.getStroke()
print("Stroke:", result)

tally.setLimit(2)