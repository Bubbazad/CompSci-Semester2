# x = "Whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
# count = 0
# for i in range(0,len(x)):
#     y = x[i:i+1]
#     if y == "w" or y == "W":
#         y = x[i:i+2]
#         if y == "wh" or y == "Wh":
#             y = x[i:i+3]
#             if y == "wha" or y == "Wha":
#                 y = x[i:i+4]
#                 if y == "whal" or y == "Whal":
#                     y = x[i:i+5]
#                     if y == "whale" or y == "Whale":
#                         count = count + 1
# print(count)
with open('moby.txt') as f:
    count = 0
    Whale = []
    for line in f:
        sentence = line.strip()
        for i in range(0,len(line)):
            y = line[i:i+1]
            if y == "w" or y == "W":
               y = line[i:i+2]
               if y == "wh" or y == "Wh":
                  y = line[i:i+3]
                  if y == "wha" or y == "Wha":
                     y = line[i:i+4]
                     if y == "whal" or y == "Whal":
                        y = line[i:i+5]
                        if y == "whale" or y == "Whale":
                            count = count + 1
            y = line[i:i+5]
            if y == "WHALE":
                count = count + 1
print(count)
f.close()
