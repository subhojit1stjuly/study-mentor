---
name: ai-ml-mastery
description: "Use when: studying artificial intelligence, learning machine learning, building AI/ML study plan, mastering deep learning, practicing ML algorithms, understanding neural networks, studying NLP, computer vision, reinforcement learning, MLOps, preparing for AI interviews, reviewing ML math foundations, implementing ML from scratch."
argument-hint: "Topic or phase to study (e.g., 'neural networks', 'Phase 2', 'NLP project')"
---

# AI & ML Mastery Roadmap

A structured, phase-based skill for achieving deep mastery in Artificial Intelligence and Machine Learning — from mathematical foundations through cutting-edge research.

## When to Use

- Starting or resuming an AI/ML study journey
- Requesting a study plan or learning roadmap
- Diving deep into a specific AI/ML topic
- Building projects to reinforce learning
- Preparing for ML engineer / AI researcher interviews
- Reviewing and self-assessing progress

## How This Skill Works

1. **Assess** the user's current level (beginner / intermediate / advanced)
2. **Place** them in the appropriate phase of the roadmap
3. **Teach** topics in order with theory, math, code, and intuition
4. **Assign** exercises and mini-projects after each module
5. **Assess** understanding with checkpoint questions before advancing
6. **Track** progress using the todo list and workspace files

---

## Phase 0: Mathematical Foundations

> **Goal**: Build the math intuition that underpins all of ML.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 0.1 | Linear Algebra | Vectors, matrices, dot product, matrix multiplication, eigenvalues/eigenvectors, SVD, PCA derivation, norms, orthogonality, linear transformations |
| 0.2 | Calculus | Derivatives, partial derivatives, chain rule, gradients, Jacobians, Hessians, Taylor series, multivariate optimization, Lagrange multipliers |
| 0.3 | Probability & Statistics | Probability axioms, Bayes' theorem, random variables, distributions (Gaussian, Bernoulli, Poisson, uniform, exponential), expectation, variance, covariance, MLE, MAP, hypothesis testing, confidence intervals |
| 0.4 | Optimization | Gradient descent (batch, stochastic, mini-batch), learning rate, momentum, Adam, convex vs non-convex, constrained optimization, KKT conditions |
| 0.5 | Information Theory | Entropy, cross-entropy, KL divergence, mutual information — and why they matter for ML loss functions |

### Checkpoint
- Derive the gradient of a linear regression loss function by hand
- Explain why eigenvalues matter for PCA
- Solve a Bayesian inference problem from scratch

---

## Phase 1: Classical Machine Learning

> **Goal**: Master the core ML algorithms, understand them deeply enough to implement from scratch.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 1.1 | ML Fundamentals | Supervised vs unsupervised vs reinforcement, bias-variance tradeoff, overfitting/underfitting, cross-validation, train/val/test split, no free lunch theorem |
| 1.2 | Linear Models | Linear regression (normal equation + gradient descent), polynomial regression, regularization (L1 Lasso, L2 Ridge, Elastic Net), logistic regression, softmax regression |
| 1.3 | Tree-Based Models | Decision trees (ID3, C4.5, CART), information gain, Gini impurity, pruning, random forests, bagging, boosting (AdaBoost, Gradient Boosting, XGBoost, LightGBM, CatBoost) |
| 1.4 | Support Vector Machines | Linear SVM, margin maximization, kernel trick (RBF, polynomial), soft margin, SVM for regression, dual formulation |
| 1.5 | Instance-Based & Probabilistic | KNN (distance metrics, curse of dimensionality), Naive Bayes (Gaussian, Multinomial, Bernoulli), Gaussian Processes |
| 1.6 | Unsupervised Learning | K-Means, K-Medoids, DBSCAN, hierarchical clustering, Gaussian Mixture Models, EM algorithm, PCA, t-SNE, UMAP, anomaly detection (Isolation Forest, One-Class SVM) |
| 1.7 | Feature Engineering | Feature scaling, encoding (one-hot, target, ordinal), feature selection (filter, wrapper, embedded), handling missing data, imbalanced datasets (SMOTE, class weights), data augmentation |
| 1.8 | Model Evaluation | Accuracy, precision, recall, F1, ROC-AUC, PR curve, confusion matrix, log loss, MSE, RMSE, MAE, R², calibration, statistical significance of results |

### Exercises per Module
- **Implement from scratch** in Python (NumPy only — no sklearn)
- **Then use sklearn** to validate your implementation matches
- **Analyze** on a real dataset (UCI, Kaggle) with full EDA → model → evaluation pipeline

### Checkpoint
- Implement logistic regression with gradient descent from scratch
- Explain the math behind SVM's kernel trick
- Build a complete ML pipeline: EDA → feature engineering → model selection → evaluation

---

## Phase 2: Deep Learning Foundations

> **Goal**: Understand neural networks from neurons to architectures, and implement them.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 2.1 | Neural Network Basics | Perceptron, multi-layer perceptron, activation functions (ReLU, sigmoid, tanh, softmax, GELU, Swish), universal approximation theorem |
| 2.2 | Training Deep Networks | Loss functions (cross-entropy, MSE, hinge, focal), backpropagation (full derivation), vanishing/exploding gradients, weight initialization (Xavier, He, Kaiming), gradient clipping |
| 2.3 | Regularization & Optimization | Dropout, batch normalization, layer normalization, weight decay, data augmentation, early stopping, learning rate scheduling (step, cosine, warm-up), optimizers (SGD, Momentum, RMSProp, Adam, AdamW, LAMB) |
| 2.4 | Convolutional Neural Networks | Convolution operation, filters, stride, padding, pooling, architectures (LeNet → AlexNet → VGG → GoogLeNet → ResNet → DenseNet → EfficientNet), transfer learning, fine-tuning |
| 2.5 | Recurrent Neural Networks | Vanilla RNN, LSTM (gate mechanics), GRU, bidirectional RNNs, seq2seq, teacher forcing, beam search, attention mechanism (Bahdanau, Luong) |
| 2.6 | Practical Deep Learning | PyTorch workflow (Dataset, DataLoader, Module, training loop), TensorFlow/Keras workflow, GPU training, mixed precision, debugging neural networks, hyperparameter tuning |

### Projects
- Build a CNN image classifier on CIFAR-10 (from scratch in PyTorch)
- Build a character-level language model with LSTM
- Implement backpropagation for a 2-layer network using only NumPy

### Checkpoint
- Derive backpropagation through a 2-layer network with ReLU
- Explain why ResNet works (skip connections and gradient flow)
- Debug a neural network that isn't converging (systematic checklist)

---

## Phase 3: Transformers & Modern Architectures

> **Goal**: Master the transformer architecture and its applications across domains.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 3.1 | Attention Mechanism | Self-attention, scaled dot-product attention, multi-head attention, positional encoding (sinusoidal, learned, RoPE, ALiBi) |
| 3.2 | Transformer Architecture | Encoder-decoder structure, layer norms, residual connections, feed-forward layers, masking (padding, causal), full implementation from scratch |
| 3.3 | NLP Transformers | BERT (MLM, NSP, fine-tuning), GPT (autoregressive LM, in-context learning), T5 (text-to-text), RoBERTa, DeBERTa, XLNet, ELECTRA |
| 3.4 | Vision Transformers | ViT, DeiT, Swin Transformer, patch embedding, comparison with CNNs, hybrid architectures |
| 3.5 | Multimodal Models | CLIP, DALL-E, Flamingo, vision-language models, contrastive learning, cross-attention |
| 3.6 | Efficient Transformers | Flash Attention, sparse attention, linear attention, quantization (INT8, INT4, GPTQ, AWQ), pruning, knowledge distillation, LoRA, QLoRA |

### Projects
- Implement a transformer encoder from scratch in PyTorch
- Fine-tune BERT for text classification using Hugging Face
- Build a mini-GPT (character-level) following Karpathy's approach

### Checkpoint
- Explain self-attention step by step with a concrete example
- Compare BERT vs GPT: pretraining objectives, use cases, strengths
- Implement multi-head attention from scratch

---

## Phase 4: Specialized AI Domains

> **Goal**: Go deep in major AI sub-fields. Pick at least 2 to specialize in.

### 4A. Natural Language Processing
| Module | Topics |
|--------|--------|
| Fundamentals | Tokenization (BPE, WordPiece, SentencePiece), embeddings (Word2Vec, GloVe, FastText), language modeling (n-gram, neural) |
| Core Tasks | Text classification, NER, POS tagging, sentiment analysis, machine translation, summarization, question answering |
| Advanced | Prompt engineering, few-shot learning, chain-of-thought reasoning, RAG (Retrieval Augmented Generation), instruction tuning, RLHF, constitutional AI |
| **Project** | Build a RAG system with document retrieval + LLM generation |

### 4B. Computer Vision
| Module | Topics |
|--------|--------|
| Fundamentals | Image representation, convolution, edge detection, feature extraction (SIFT, HOG), histogram equalization |
| Core Tasks | Classification, object detection (YOLO, SSD, Faster R-CNN), semantic/instance/panoptic segmentation (U-Net, Mask R-CNN, SAM) |
| Advanced | GANs (DCGAN, StyleGAN, CycleGAN), diffusion models (DDPM, Stable Diffusion), 3D vision, video understanding, neural radiance fields (NeRF) |
| **Project** | Build an object detection pipeline with YOLO on a custom dataset |

### 4C. Reinforcement Learning
| Module | Topics |
|--------|--------|
| Fundamentals | MDP, value functions, policy functions, Bellman equations, discount factor, exploration vs exploitation |
| Classical RL | Q-learning, SARSA, temporal difference, Monte Carlo methods, multi-armed bandits (epsilon-greedy, UCB, Thompson sampling) |
| Deep RL | DQN (experience replay, target networks), policy gradients (REINFORCE), actor-critic (A2C, A3C, PPO, SAC, DDPG, TD3) |
| Advanced | Model-based RL (Dreamer, MuZero), offline RL, inverse RL, hierarchical RL, multi-agent RL, RLHF |
| **Project** | Train an agent to play Atari games using DQN → PPO |

### 4D. Generative AI
| Module | Topics |
|--------|--------|
| Foundations | Latent spaces, generative vs discriminative models, likelihood-based vs implicit models |
| Architectures | VAEs, GANs, flow-based models, diffusion models, autoregressive models |
| LLMs | Scaling laws, pretraining, fine-tuning, RLHF, DPO, prompt engineering, agents, tool use, function calling |
| Applications | Text generation, image generation, code generation, music generation, video generation |
| **Project** | Fine-tune an LLM on a custom dataset with LoRA |

---

## Phase 5: Production ML & MLOps

> **Goal**: Learn to deploy, monitor, and maintain ML systems in production.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 5.1 | Model Serving | Model serialization (pickle, ONNX, TorchScript, SavedModel), serving (FastAPI, TorchServe, TF Serving, Triton), REST vs gRPC, batching, latency optimization |
| 5.2 | Experiment Tracking | MLflow, Weights & Biases, experiment design, reproducibility, random seeds, configuration management (Hydra, OmegaConf) |
| 5.3 | Data Pipelines | ETL for ML, data validation (Great Expectations), feature stores (Feast), data versioning (DVC), labeling workflows |
| 5.4 | Model Monitoring | Data drift, concept drift, model degradation, A/B testing, shadow deployment, canary rollout, monitoring dashboards |
| 5.5 | Infrastructure | Docker for ML, Kubernetes for ML (KubeFlow), GPU management, distributed training (DDP, FSDP, DeepSpeed), cloud ML services (SageMaker, Vertex AI, Azure ML) |
| 5.6 | Hyperparameter Tuning | Grid search, random search, Bayesian optimization (Optuna, Ray Tune), neural architecture search (NAS), AutoML |

### Project
- Build an end-to-end ML pipeline: data → training → evaluation → deployment → monitoring

---

## Phase 6: Research & Cutting Edge

> **Goal**: Read, understand, and implement research papers. Contribute to the field.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 6.1 | Reading Papers | How to read ML papers (3-pass method), finding papers (arXiv, Semantic Scholar, Papers With Code), understanding notation, replicating results |
| 6.2 | Key Papers to Study | Attention Is All You Need, BERT, GPT-2/3, ResNet, BatchNorm, Adam, Dropout, GANs, VAEs, DDPM, LoRA, Flash Attention, Chinchilla scaling laws |
| 6.3 | Research Skills | Identifying open problems, designing experiments, ablation studies, statistical significance, writing results, LaTeX |
| 6.4 | Current Frontiers | State space models (Mamba), mixture of experts (MoE), multimodal AI, AI agents, world models, test-time compute, reasoning models |

### Project
- Pick a recent paper, implement it from scratch, and write a blog-post-style explanation

---

## Study Method for Every Topic

Follow this sequence for each module:

```
1. THEORY    → Read/watch → Take notes → Build mental model
2. MATH      → Derive key equations by hand → Understand every symbol
3. CODE      → Implement from scratch (NumPy/PyTorch) → Then use libraries
4. PRACTICE  → Apply to real dataset → Full pipeline
5. EXPLAIN   → Teach it back (Feynman technique) → Write summary notes
6. ASSESS    → Answer checkpoint questions → Identify gaps → Revisit
```

## Progress Tracking

- Create a file `ai-ml-progress.md` in the workspace to track completed modules
- Use the todo list for current study sessions
- After each module, save notes under `ml/` or `ai/` folders in the workspace
- Review previous notes periodically (spaced repetition)

## Recommended Resources

| Resource | Type | Best For |
|----------|------|----------|
| Andrew Ng's ML Specialization | Course | Phase 1 (Classical ML) |
| Fast.ai | Course | Phase 2 (Practical Deep Learning) |
| Stanford CS229 | Course | Phase 1 (ML theory + math) |
| Stanford CS231n | Course | Phase 2-4B (CNNs, Vision) |
| Stanford CS224n | Course | Phase 3-4A (NLP, Transformers) |
| Deep Learning Book (Goodfellow) | Book | Phase 0-2 (Foundations) |
| Andrej Karpathy's videos | Video | Phase 2-3 (Neural Nets, GPT) |
| Hugging Face Course | Tutorial | Phase 3-4A (Transformers) |
| Spinning Up in Deep RL (OpenAI) | Tutorial | Phase 4C (Reinforcement Learning) |
| Papers With Code | Reference | Phase 6 (Research) |
| Designing ML Systems (Huyen) | Book | Phase 5 (MLOps) |
