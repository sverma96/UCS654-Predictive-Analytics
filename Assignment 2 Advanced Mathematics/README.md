# Title: Learning Probability Density Function using GAN



## 1. Methodology

### Step-wise Approach

1. **Data Collection**
   - NO₂ concentration values were extracted from the air quality dataset.

2. **Data Preprocessing**
   - The NO₂ values were standardized using:
     
     x = (x − mean) / standard deviation

3. **Transformation**
   - Each value of x was transformed into z using:

   <img width="1139" height="217" alt="image" src="https://github.com/user-attachments/assets/01473099-617e-46b1-a9a8-e87173145588" />


4. **GAN Training**
   - A Generative Adversarial Network (GAN) was implemented using PyTorch.
   - The GAN learned the distribution of the transformed variable z using only data samples.
   - The generator produced fake samples from random noise.
   - The discriminator distinguished between real and fake samples.

5. **PDF Estimation**
   - After training, the generator produced a large number of samples.
   - Kernel Density Estimation (KDE) was applied to approximate the probability density function.





## 2. GAN Architecture

### Generator
| Layer | Units | Activation |
|------|------|------------|
| Dense | 32 | ReLU |
| Dense | 32 | ReLU |
| Output | 1 | Linear |

### Discriminator
| Layer | Units | Activation |
|------|------|------------|
| Dense | 32 | ReLU |
| Dense | 32 | ReLU |
| Output | 1 | Sigmoid |







## 3. Result Graph

<img width="926" height="562" alt="image" src="https://github.com/user-attachments/assets/a2ee3d1b-2dcc-45bb-ac97-1b6e61c4276c" />


## 7. Observations

1. The GAN-generated distribution closely follows the real data distribution.
2. The dominant mode is captured with visible overlap.
3. Training remained stable without severe mode collapse.
4. Minor differences are present in peak sharpness and tail regions.
5. Overall, the GAN successfully approximated the unknown probability density function.



## 8. Conclusion

- The GAN was able to learn the distribution of the transformed variable using only data samples.
- The estimated PDF from generator samples closely matches the real distribution.
- This demonstrates the effectiveness of GANs for non-parametric density estimation.

## **9. Live link**
Link: https://colab.research.google.com/drive/1_F_CYdDkZWXywU8RqkpeLwmql6gqfWMw#scrollTo=hZH6zy_pRubK









## 10. How to Run

1. Place `data.csv` in the project folder.
2. Open the notebook or Python script.
3. Ensure the roll number is set correctly.
4. Run all cells.
5. The final PDF plot will be displayed.
