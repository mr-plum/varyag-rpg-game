class Equipment:
    left_hand = None
    right_hand = None
    torso = None
    legs = None
    feet = None
    head = None

    def add(self, stuff):
        if stuff.slot == 'both_hands':
            self.right_hand = self.left_hand = stuff
        elif stuff.slot == 'hand' and self.right_hand is None:
            self.right_hand = stuff
        elif stuff.slot == 'hand' and self.left_hand is None:
            self.left_hand = stuff
