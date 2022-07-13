from_ = 1657689730
offset = 60*60*(24*3+15)
duration = 60*60*24*7

startAt = (from_ - offset)//duration*duration + offset

print(startAt)