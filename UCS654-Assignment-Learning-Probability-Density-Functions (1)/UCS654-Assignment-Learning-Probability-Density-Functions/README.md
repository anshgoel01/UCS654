## Objective

The objective of this assignment is to learn the probability density function (PDF) of a random variable using only data samples. No parametric or analytical form of the distribution is assumed. A Generative Adversarial Network (GAN) is used to model the unknown distribution.

---

## Dataset

- Dataset: India Air Quality Dataset (Kaggle)
- Feature used: NO₂ concentration values
- Preprocessing steps:
  - Missing values were removed
  - Extreme outliers were ignored to reduce training instability

Only one feature was used to keep the focus on probability density learning.

---

## Data Transformation

Each NO₂ value $x$ is transformed using the following equation:

$$z = x + a_r \sin(b_r x)$$

where:
- $a_r = 0.5 (r \mod 7)$
- $b_r = 0.3 ((r \mod 5) + 1)$
- $r$ is the university roll number: **102317042**

For r = 102317042:
- $a_r = 0.5 \times (102317042 \mod 7)$ = **0.1**
- $b_r = 0.3 \times ((102317042 \mod 5) + 1)$ = **0.9**

This transformation introduces nonlinearity into the data distribution.

---

## Methodology

- The transformed variable $z$ is treated as samples from an unknown distribution
- A simple one-dimensional GAN is used
- The generator takes random noise sampled from a normal distribution and generates fake samples
- The discriminator tries to distinguish between real and generated samples
- Both networks are trained alternately using Binary Cross Entropy loss

### Training Details
- Optimizer: Adam
- Batch size: 32
- Number of epochs: approximately 2500
- Noise distribution: Normal (0,1)

---

## Results

After training, a large number of samples were generated using the trained generator. Histogram-based density estimation was used to approximate the probability density function.

### Training Parameters

| Parameter | Value |
|-----------|-------|
| Epochs | 2500 |
| Batch Size | 32 |
| Learning Rate | 0.001 |

### Result Graph

The histogram of generated samples overlaps well with the histogram of real transformed data, indicating that the GAN learned the overall shape of the distribution. See the output in `code.ipynb` for the result plot.

---

## Observations

- Major modes of the distribution were captured
- The generated distribution appears slightly smoother than the real data
- Training was unstable in the beginning but improved after several epochs

---

## Conclusion

This assignment demonstrates that GANs can be used to learn probability density functions using data only. Even with a simple architecture, the GAN was able to approximate the distribution of the transformed NO₂ values reasonably well.
