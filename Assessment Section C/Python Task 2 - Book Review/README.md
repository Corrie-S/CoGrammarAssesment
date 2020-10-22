# BookReview
## Requirements: 
Create, train and test an ML Model that predicts the sentiment of a book review.

## Implementation

Review data is given in two text files positive.txt and negative.txt for positive and negative reviews.

Only the title of the review is used for this implementation. 

Review titles are extracted after which some EDA is done on the reviews. NLP is used to tokenize the data to be passed to the model.

It was specified that the model be built using Keras, so a Sequencial Model is created with the layers as specified.

It is specified to tune the model with different output dimension on the Embedding layer.

After tuning the models, the different models are assessed to find the best fit.

Finally the model is tested on some unique data.

## Considerations

Using only the title data limits the ability of the model somewhat as some of the shorter titles tokinizes to zero tokens. This effectively has zero training value for the model and can cause confusion. Still we get a better than average prediction with the model.

## Usage

1. Run the notebook on a Jupyter Notebook server or Google Colab.

