# Setup

202 Pokemons, given ranks from highest to lowest: S, A-G.

# Results

## Explanation of results

- Parameters **alpha** and **max_iter** are configured so that:
  - *alpha = 10 ^ alpha_power*
  - *max_iter = 10 ^ max_iter_power*
- **hidden_layer_amt** := hidden_layers_sizes[0]
- Dev split is used for recall, precision and F1 score
- The values recall, precision and F1 score are weighted averages across all classes to prevent a class from skewing the value (in this case, classes with many Pokemons such as E and F). Since we don't have any special priorities for minimizing false positives/negatives, these values are much less important than accuracy.

## Model using standard dataset

| alpha_power | max_iter_power | hidden_layer_amt | Overfit/underfit? | *Train accuracy* | *Dev accuracy* | Recall | Precision | F1 score |
|:----------- | -------------- | ---------------- | ----------------- | ---------------- |:-------------- |:------ |:--------- |:-------- |
| -4          | 2              | 10               | underfit          | 0.6059           | 0.5693         | 0.49   | 0.57      | 0.52     |
| -4          | 3              | 10               | good fit          | 0.7341           | 0.6931         | 0.67   | 0.69      | 0.67     |
| -4          | 4              | 10               | good fit          | 0.7352           | 0.6980         | 0.67   | 0.70      | 0.67     |
| -1          | 2              | 10               | underfit          | 0.6049           | 0.5693         | 0.48   | 0.57      | 0.52     |
| -1          | 3              | 10               | good fit          | 0.7426           | 0.698          | 0.68   | 0.70      | 0.67     |
| -1          | 4              | 10               | good fit          | 0.7436           | 0.703          | 0.70   | 0.70      | 0.68     |
| 0           | 2              | 10               | underfit          | 0.6038           | 0.5693         | 0.48   | 0.57      | 0.51     |
| 0           | 3              | 10               | good fit          | 0.7309           | 0.6782         | 0.66   | 0.68      | 0.65     |
| 0           | 4              | 10               | good fit          | 0.7288           | 0.6733         | 0.64   | 0.67      | 0.63     |
| 1           | 2              | 10               | underfit          | 0.5371           | 0.5396         | 0.46   | 0.54      | 0.46     |
| 1           | 3              | 10               | underfit          | 0.6504           | 0.6386         | 0.53   | 0.64      | 0.56     |
| 1           | 4              | 10               | underfit          | 0.6504           | 0.6386         | 0.53   | 0.64      | 0.56     |
| -1          | 3              | 20               | overfit           | 0.7839           | 0.6782         | 0.64   | 0.68      | 0.65     |
| -1          | 3              | 50               | overfit           | 0.8072           | 0.7079         | 0.70   | 0.71      | 0.69     |
| -1          | 3              | 100              | overfit           | 0.8178           | 0.698          | 0.68   | 0.70      | 0.68     |

### Observations

- Model improves (accuracy and F1 score increasing) as max amount of iterations increases, but plateaus around 10^3
- Model improves as alpha decreases, but peaks around 0.1 (10^-1); decreasing further to 10^-4 yields no significant gain
- Changing alpha has little effect when max_iter is low (10^2) — sufficient iterations are needed for regularization to take effect
- The difference between train accuracy and dev accuracy is small (< 0.05) when the amount of hidden layers is low, which means the model only fits well or underfits in these cases
- Increasing amount of hidden layers improves train accuracy, but not dev accuracy, widening the gap between them. This means the model overfits in these cases
- hidden_layer_amt = 50 achieves the highest dev accuracy among all runs (0.7079) but has a train/dev gap of 0.0993, indicating overfitting; not selected as ideal
- Ideal parameters: alpha = 0.1, max_iter = 1000, hidden_layer_amt = 10; prediction accuracy: ~70%

## Model using post-PCA dataset

- 10 hidden layers: Pretty much the same as standard model, with differences between respective metrics being <= 0.02
- 100 hidden layers: Model plateaus early instead if improving like the standard model did

## Observations on the confusion matrices

- Correct predictions live on the SS-GG diagonal
- Different definitions of common metrics
  - **Accuracy:** sum of cells on diagonal / total
  - **Recall:** cell on diagonal / sum of cells on row
  - **Precision:** cell on diagonal / sum of cells on column

--> From looking at the CMs, we can tell roughly if certain sets of parameters increase or decrease these metrics
