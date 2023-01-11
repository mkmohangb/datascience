
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
    - Normalization employed is **Layer Normalization**. See this [video](https://www.youtube.com/watch?v=l_3zj6HeWUE) for overview of Normalization
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
     
10. Why Transformers work?

    [A primer in BERTology](https://arxiv.org/pdf/2002.12327.pdf)
    - Transformers operate tokens(language words) as a vectorial space of 768+ features
    - From the embeddings step, layer by layer, Transformers extract and build complex features that interact linearly and nonlinearly
    - Attention moves new token interactions into each vector's features
    - Feed forward operates on these features towards the training goal, making or extracting new features.
    - Efficiency & Parallelism allow learning from massive data.
11. Explainability
12. Pretraining
    - train for general unsupervised tasks and then fine-tune the model
    <img width="399" alt="Screenshot 2023-01-06 at 1 01 28 PM" src="https://user-images.githubusercontent.com/2610866/210952306-25aa72bf-e6bb-4740-9c5e-56de34e5f91f.png">

13. Existing Models
    - GPT - Generative Pre-trained Transformer - just the Decoder
    - BERT - Bidirectional Encoder Representations from Transformers - Encoder only - predict masked word, predict likelihood that sentence B comes after A
    - GPT-2
    - GPT-3 (175B params) - bias is a concern
    - T5 - Text-to-Text Transfer Transformer - Refined Vanilla transformer - Encoder + Decoder
        - every task is text-to-text
        - very versatile for all kinds of tasks
        - cola - Corpus of Linguistic Acceptablity
        - stsb - semantic textual similiarty benchmark
        <img width="831" alt="Screenshot 2023-01-06 at 1 10 47 PM" src="https://user-images.githubusercontent.com/2610866/210953765-36bb1897-2b67-4eec-92c4-1eea62ba1dfc.png">

14. HuggingFace ecosystem
15. Vision Transformers - more general than Convolution
    - since it can look at relations between image patches from any corner of the image unlike CNN which does local details aggregated in a hierarchical manner?
    - [Paper Explanation by Yannic Kilcher](https://www.youtube.com/watch?v=TrdevFK_am4)
    - Attention is quadratic - pairwise innerproduct of each of the bubbles
    - Global attention by going over image patches
    <img width="657" alt="Screenshot 2023-01-06 at 4 49 19 PM" src="https://user-images.githubusercontent.com/2610866/211002436-42da776e-a251-4e48-a89d-9cd6ca13653d.png">
    
    - Transformer is a generalization of MLP - in MLP 'w' is fixed while in Transformer it is computed on the fly - Permutation invariant ? 
    <img width="347" alt="Screenshot 2023-01-06 at 8 10 13 PM" src="https://user-images.githubusercontent.com/2610866/211034122-6fd72b15-65ab-41ac-b4fb-2ca4def9d793.png">
    <img width="417" alt="Screenshot 2023-01-06 at 8 18 38 PM" src="https://user-images.githubusercontent.com/2610866/211035751-0d7d9f0b-c6b3-4f79-a891-c7869d0a6c69.png">
    
    - with CNNs & LSTMs we introduce inductive priors or biases since the data is limited we restrict the model towards certain solutions. With lots of data, biased models will perform worse than an unbiased model, so Transformers as a more general model than MLP will shine in these scenarios.
   
17. DALL.E
18. Wav2Vec - speech
