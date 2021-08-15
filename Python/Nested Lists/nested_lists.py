if __name__ == '__main__':
    
    scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append([score,name])
        
#second_highest = sorted(scores)[1][0]

second_highest = sorted(set([score for score, name in scores]))[1]

print("\n".join(sorted([name for score, name in scores if score == second_highest])))

#for item in biglist:
#    if item[0] == second_highest:
#        newlist.append([item[1],item[0]])
#
#for item in sorted(newlist):
#    print(item[0])
