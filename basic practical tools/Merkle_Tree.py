import hashlib

# Planting a basic Merkletree
class Merkletree:
    def plant_Merkle_Tree(self, leaves):
        # If one leaf, return it as root
        if len(leaves) == 1:
            return leaves[0]
        # if we have odd leaves then we duplicae one
        if len(leaves) % 2 == 1:
            leaves.append(leaves[-1])
       # Now we have even leaves for pairs! Pair em up into a branch
        branches = [leaves[i] + leaves[i+1] for i in range(0, len(leaves), 2)]
       # Now hash up the branches
        branches = [hashlib.sha3_256(branches.encode()).hexidigest() for branch in branches]
       # Recurcively build a tree
        return self.plant_Merkle_Tree(branches)
        # Now we have a tree!
        