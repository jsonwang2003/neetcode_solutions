class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        i, length = 0, len(senate)
        senator = list(senate)

        while(True):
            c = senator[i]
            if(c == '#'):
                i = (i + 1) % length
                continue
            removed = False
            for j in range(1, length):
                index = j + i
                if(c == 'D' and senator[index % length] == 'R'):
                    senator[index % length] = '#'
                    removed = True
                    break
                if(c == 'R' and senator[index % length] == 'D'):
                    senator[index % length] = '#'
                    removed = True
                    break

            if not removed:
                return "Radiant" if c == 'R' else "Dire"
            else:
                i = (i + 1) % length
                