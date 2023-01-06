
## [Introduction to Transformers](https://www.youtube.com/watch?v=1G4ACbebybM)

1. Drawbacks of RNN:

    - Sequential computation(slow!)
    - Long term dependencies -> signal vanishing
    - Last cell bottleneck ( for translation, the state when the last input word is processed needs to hold the entire sentence context for the decoding part )

2. Attention in RNNs:

    - solves long term dependencies
    - provides some interpretability
    - great performance
    - bypasses bottleneck

    - If Attention gives access to any encoder state, why do we need RNNs at all?
    - **Attention is All You Need**

3. What is a Transformer?
    - Replicate encoder-decoder architecture without recurrency
    - Positional encoding is used to specify order of words
    - N x Encoder & Decoder blocks
    - M x Attention Heads
    - Feed Forward needs normalization
    - Residual connections
    - Autoregressive decoding
    - **Parallel** training
  <img width="359" alt="Screenshot 2023-01-06 at 11 16 43 AM" src="https://user-images.githubusercontent.com/2610866/210938353-840ee8b8-4b75-46c7-b384-aa39f38c531d.png">


4. Positional Encoding
    - Small absolute value
    - Independent of sequence length
    - Distinct far & near representation
    - Feed Forward NN friendly: float-point
    - Vanilla transformers use a sine-cosine formulation for positional encoding
  
5. Self-attention
    - sentence: "when you play the game of thrones"
       - sum to each word weighted embeddings of related words
       - game = 0.03 * play + 0.02 * the + 0.72 * game + 0.23 * throne 
       - given two vectors, cosine measures similarity
     
  <img width="410" alt="Screenshot 2023-01-06 at 11 27 59 AM" src="https://user-images.githubusercontent.com/2610866/210939631-62613071-ce40-400c-b63f-5df6fa4d82ac.png">

6. Multi-headed Attention 
    - multiple linear mappings learn different feature selection 
    - the only time words interact in the pipeline

7. Masked Self-Attention 
    - Decoder (only look at earlier words)
8. Cross Attention 
    - Query: latest contextual vector from decoder
    - Keys: Encoder embeddings
    - Result: weighted relevant encoder embeddings
    - original vector is preserved through residual
  
9. Decoder
    - Self-attention gives contextual representation
    - Cross-attention incorporates encoder's info
    - Feed Forward extracts complex features
    - In last layers, FF works towards next token
     
     
