class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        if groupSize == 1:
            return True
        
        freq = defaultdict(int)

        for card in hand:
            freq[card] += 1
        
        hand.sort()

        for card in hand:
            if freq[card]:
                for c in range(card, card + groupSize):
                    if freq[c] == 0:
                        return False
                    freq[c] -= 1
            
        return True
                