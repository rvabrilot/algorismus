# Huffman Coding in python

# The time complexity for encoding each unique character based on its frequency is O(nlog n).

# Extracting minimum frequency from the priority queue takes place 2*(n-1) times and its complexity is O(log n). 
# Thus the overall complexity is O(nlog n)

# Applications 
# Huffman coding is used in conventional compression formats like GZIP, BZIP2, PKZIP, etc.
# For text and fax transmissions.

#PSEUDO
#create a priority queue Q consisting of each unique character.
#sort then in ascending order of their frequencies.
#for all the unique characters:
#    create a newNode
#    extract minimum value from Q and assign it to leftChild of newNode
#    extract minimum value from Q and assign it to rightChild of newNode
#    calculate the sum of these two minimum values and assign it to the value of newNode
#    insert this newNode into the tree
#return rootNode

string = 'BCAADDDCCACACAC'


# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


# Calculating frequency
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))