# TOPSIS for Conversational Pretrained NLP Models

## 1. Introduction

This project applies the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS), a multi-criteria decision-making (MCDM) method, to determine the most suitable conversational pre-trained NLP model.

As the roll number ends with 4, the assigned category is:

Text Conversational Models

The objective is to evaluate multiple conversational models based on performance and efficiency criteria and identify the optimal model using TOPSIS methodology.

---

## 2. Models Considered

The following conversational pre-trained models were evaluated:

1. DialoGPT  
2. BlenderBot  
3. GPT-2  
4. LLaMA2-Chat  
5. Mistral-Chat  
6. T5-Conversational  
7. Falcon-Chat  

These models are widely used for dialogue systems and conversational AI applications.

---

## 3. Evaluation Criteria

The models were evaluated using both quality-based and efficiency-based metrics.

| Criteria       | Type    | Description |
|---------------|---------|-------------|
| BLEU          | Benefit | Measures response generation quality |
| ROUGE         | Benefit | Measures overlap with reference responses |
| Perplexity    | Cost    | Lower value indicates better language modeling |
| Response Time | Cost    | Lower inference time preferred |
| Model Size    | Cost    | Smaller model size preferred for deployment |

Benefit criteria are those where higher values are preferred.  
Cost criteria are those where lower values are preferred.

---

## 4. Criteria Weights

Weights were assigned based on relative importance:

| Criteria       | Weight |
|---------------|--------|
| BLEU          | 0.25   |
| ROUGE         | 0.25   |
| Perplexity    | 0.20   |
| Response Time | 0.15   |
| Model Size    | 0.15   |

The sum of all weights equals 1.

---

## 5. Methodology: TOPSIS Procedure

The following steps were implemented:

1. Construct the decision matrix from the dataset.
2. Normalize the decision matrix using vector normalization:

   r_ij = x_ij / √(Σ x_ij²)

3. Multiply the normalized matrix by the assigned weights to obtain the weighted normalized matrix.
4. Determine:
   - Ideal Best (A⁺)
   - Ideal Worst (A⁻)

   For benefit criteria:
   - Ideal Best = maximum value
   - Ideal Worst = minimum value

   For cost criteria:
   - Ideal Best = minimum value
   - Ideal Worst = maximum value

5. Compute Euclidean distances:

   S_i⁺ = Distance from Ideal Best  
   S_i⁻ = Distance from Ideal Worst  

6. Compute the Closeness Coefficient:

   C_i = S_i⁻ / (S_i⁺ + S_i⁻)

7. Rank models in descending order of C_i.

The model with the highest closeness coefficient is considered the optimal alternative.

---

## 6. Results

The final TOPSIS scores and rankings are:

| Rank | Model              | TOPSIS Score |
|------|-------------------|--------------|
| 1    | BlenderBot        | 0.5367       |
| 2    | GPT-2             | 0.5224       |
| 3    | DialoGPT          | 0.4983       |
| 4    | Mistral-Chat      | 0.4907       |
| 5    | T5-Conversational | 0.4847       |
| 6    | LLaMA2-Chat       | 0.4403       |
| 7    | Falcon-Chat       | 0.4164       |

A bar chart visualization was also generated to compare the closeness coefficients.

---

## 7. Discussion

Although Mistral-Chat and LLaMA2-Chat demonstrated strong BLEU and ROUGE scores, their larger model sizes and slower response times reduced their overall ranking.

BlenderBot achieved the highest closeness coefficient due to its balanced performance across both quality and efficiency metrics.

This demonstrates that optimal model selection requires considering multiple criteria rather than focusing solely on performance scores.

---

## 8. Conclusion

Based on the TOPSIS multi-criteria decision-making analysis, BlenderBot is identified as the most suitable conversational pre-trained model among the evaluated alternatives.

The study highlights the importance of balancing generation quality with computational efficiency in real-world conversational AI deployment.

---


---

## 9. Tools and Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Jupyter Notebook
- Git and GitHub

---

## 10. How to Execute

1. Open `TOPSIS_Conversational.ipynb`
2. Ensure Python environment contains:
   - numpy
   - pandas
   - matplotlib
3. Run all cells
4. Final ranking and visualization will be generated

---

