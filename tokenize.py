'''
    Blocks:
      1. Input Tokenization ----------- HERE
      2. Positional Encoding
      3. Attention 
      4. Layer Normalization
      5. Feed Forward Network
      6. MLP layer
'''

'''

    Explaining Tokenization:

      The atomic unit for language understanding in LLMs is not words as in humans, but tokens which are usually subwords. This is crucial in handling word variations. For 
      instance, climb, climbing, climbed are all different variations of the same word, but dividing them into the base word climb and their suffixes results in a better way 
      to capture language morphology.

      How are subword tokens generated? There are a few ways to do that. The standard way is to use Byte-Pair encoding. Start from individual characters and pair up characters
      that appear together frequently. Eg: the number 123 gets grouped together since these numbers tend to be used together frequently. 


'''

class Tokenize(nn.Module):

  def __init__(self):
    super(Tokenize, self).__init__()



  def forward(self, input):

    return   