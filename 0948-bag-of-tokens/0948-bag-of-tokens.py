class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        lentoken=len(tokens)
        if lentoken==0:
            return 0
        tokens=sorted(tokens)
        if tokens[0]>power:
            return 0
        score = 0
        i=0
        j=lentoken-1
        while(i<j):
            if power-tokens[i]>=0:
                power=power-tokens[i]
                score+=1
                i+=1
            elif score!=0:
                score-=1
                power=power+tokens[j]
                j-=1
        if power-tokens[i]>=0:
            score+=1
        return score
        
                
                
                
        
            