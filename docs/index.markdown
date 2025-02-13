---
layout: page
title: Overview
permalink: /
---
<div style="text-align: center; display: flex; width: 100%; justify-content: space-evenly; align-items: center; gap: 1em; padding: 2em">
  <img style="width: 20%;" src="https://github.com/Open-Finance-Lab/FinRL_Contest_2025/blob/main/docs/assets/logos/ieee-logo.png?raw=true" alt="IEEE Logo">
  <img style="width: 20%;" src="https://github.com/Open-Finance-Lab/FinRL_Contest_2025/blob/main/docs/assets/logos/columbiau.jpeg?raw=true" alt="Columbia Logo">
</div>

#### **All FinRL Contests**
**FinRL Contest 2023**: [Contest Website](https://open-finance-lab.github.io/finrl-contest.github.io/); [Github](https://github.com/Open-Finance-Lab/FinRL_Contest_2023)

**FinRL Contest 2024**: [Contest Website](https://open-finance-lab.github.io/finrl-contest-2024.github.io/); [Github](https://github.com/Open-Finance-Lab/FinRL_Contest_2024)

## Introduction
Financial reinforcement learning (FinRL)[1,2] is an interdisciplinary field that applies reinforcement learning to financial tasks, such as portfolio management, algorithmic trading, and option pricing. With the rapid development of large language models (LLMs), AI is driving open finance, which enables customers to make intelligent decisions, build personalized financial search, and robo-advisors.


The FinRL contest is a competition that explores and evaluates the capability of machine learning methods in finance. FinRL Contest 2025 introduces three tasks designed to promote open science. It features with: 
1. **Factor Mining in FinRL**. Factors play a critical role in driving trading decisions, enabling traders to design efficient, data-driven strategies. In FinRL Contest 2024, we set up two stages -- factor engineering and ensemble learning -- but only focused on the second stage and provided the factors directly. In this contest, we will continue to open the first stage and encourage participants to independently perform factor engineering and selection to create their trading strategies.
2. **Open FinLLM Leaderboard**. The [Open FinLLM Leaderboard](https://huggingface.co/spaces/finosfoundation/Open-Financial-LLM-Leaderboard) [3] serves as an open platform to evaluate LLMs’ performance on various tasks. It encourages the community to explore the models’ capability and openness. In addition, complex financial regulations and industry standards are critical to the financial services, but the leaderboard haven’t included such benchmark datasets. We expanded and upgraded the regulations datasets developed during the [Regulations Challenge at COLING 2025](https://coling2025regulations.thefin.ai/home) [4]. In FinRL Contest 2025, we selected three domains for regulatory reporting: the Common Domain Model (CDM), the Model Openness Framework (MOF), and eXtensible Business Reporting Language (XBRL). We aim to contribute these datasets to the leaderboard so that the participants can explore both existing tasks and the new regulatory reporting task.

We design three tasks to promote open finance: **(1) Factor Mining and Ensemble Learning for Stock Trading**, **(2) Open FinLLM Leaderboard – Make the Top**, and **(3) Open FinLLM Leaderboard – Regulatory Reporting**. These tasks allow contestants to participate in various financial tasks and contribute to open finance using state-of-the-art technologies. We welcome students, researchers, and engineers who are passionate about finance and machine learning. 

<p style="font-size: 10px;">
[1] [MLJ] X.-Y. Liu, Z. Xia, H. Yang, J. Gao, D. Zha, M. Zhu, Christina D. Wang*, Zhaoran Wang, and Jian Guo*. Dynamic datasets and market environments for financial reinforcement learning. Machine Learning Journal, Springer Nature, 2023.
</p>
<p style="font-size: 10px;">
[2] [NeurIPS] X.-Y. Liu, Z. Xia, J. Rui, J. Gao, H. Yang, M. Zhu, C. Wang, Z. Wang, J. Guo. FinRL-Meta: Market environments and benchmarks for data-driven financial reinforcement learning. NeurIPS, Special Track on Datasets and Benchmarks, 2022.
</p>
<p style="font-size: 10px;">
[3] Shengyuan Colin Lin, Felix Tian, Keyi Wang, Xingjian Zhao, Jimin Huang, Qian-qian Xie, Luca Borella, Christina Dan Wang Matt White, Kairong Xiao, Xiao-Yang Liu Yanglet, and Li Deng. 2024. Open FinLLM Leaderboard: Towards Financial AI Readiness. International Workshop on Multimodal Financial Foundation Models (MFFMs) at 5th ACM International Conference on AI in Finance (MFFM at ICAIF ’24), (2024).
</p>
<p style="font-size: 10px;">
[4] Keyi Wang, Jaisal Patel, Charlie Shen, Daniel Kim, Andy Zhu, Alex Lin, Luca Borella, Cailean Osborne, Matt White, Steve Yang, Kairong Xiao, and Xiao-Yang Liu Yanglet. 2025. A Report on Financial Regulations Challenge at COLING 2025. arXiv:2412.11159.
</p>

## Data
For market data, we have more than 30 market data sources to deal with different financial tasks. We hold the data APIs and sample market environments in an open-source repository, [FinRL-Meta](https://github.com/AI4Finance-Foundation/FinRL-Meta), as shown in Figure 1. Participants are welcome to explore and use in the FinRL Contest.

<div style="display: flex; justify-content: center; align-items: flex-start; flex-wrap: wrap; text-align: center;">
  <figure style="display: inline-block; margin: 10px; text-align: center;">
    <img src="https://github.com/Open-Finance-Lab/FinRL_Contest_2025/blob/main/docs/assets/pictures/FinRL_Meta_Data.png?raw=true" alt="Figure 1: Market data sources of FinRL-Meta" width="500"/>
    <p>Figure 1: FinRL-Meta market data sources</p>
  </figure>
</div>

The [Open FinLLM Leaderboard](https://huggingface.co/spaces/finosfoundation/Open-Financial-LLM-Leaderboard) contains 40 tasks in 7 categories, including information extraction, textual analysis, question answering, text generation, risk management, forecasting, and decision making. Participants are free to explore these benchmark datasets. We will also release our question datasets for regulatory reporting.

## Environment
With a deep reinforcement learning approach, market datasets are processed into gym-style environments. The market environment provided to participants is designed to enhance both the realism and efficiency of the simulation process.

Table 1 lists the state spaces, action spaces, and reward functions of different FinRL applications. A state shows how an agent perceives a market situation. Facing a state, the agent can take an action from the action set, which may vary according to the financial tasks. Reward is an incentive mechanism for an agent to learn a better policy. Contestants will specify the state space, action space, and reward functions in the environment for both tasks.

Figure 2 shows the provided vectorized environment to support massively parallel simulataions. It manages multiple parallel sub-environments, each simulating different market scenarios and incorporating realistic market constraints.

<div style="display: flex; justify-content: center; align-items: flex-start; flex-wrap: wrap; text-align: center;">
  <figure style="display: inline-block; margin: 10px; text-align: center;">
    <img src="https://github.com/Open-Finance-Lab/FinRL_Contest_2025/blob/main/docs/assets/pictures/table1.png?raw=true" alt="Table 1: List of state space, action space, and reward function" width="300"/>
    <p>Table 1: List of state space, action space, and reward function</p>
  </figure>
  <figure style="display: inline-block; margin: 10px; text-align: center;">
    <img src="https://github.com/Open-Finance-Lab/FinRL_Contest_2025/blob/main/docs/assets/pictures/vec_env.png?raw=true" alt="Figure 3: Vectorized environment" width="210"/>
    <p>Figure 2: Vectorized environment</p>
  </figure>
</div>

## Timeline
* **Team Registration Begin**: Mar 5, 2024
* **Starter-Kit Release**: Mar 10, 2024
* **Solution Submission Deadline**: Apr 15, 2024
* **Report Submission Deadline**: Apr 20, 2024
* **Winner Notification**: Apr 25, 2024
* **Winner Announcement**: TBA

<span style="color:blue;">(All deadlines are at 11:59pm EST on the specified date.)</span>

Winners will be invited to attend the conference and have the opportunity to present their work at the conference.

## Tasks

Each team can choose to participate in one or more tasks. The prizes will be awarded for each task.


### Tutorials and Starter Kit
We will provide tutorials for participants to learn FinRL and the Open FinLLM Leaderboard.


### Task I: Factor Mining and Ensemble Learning for Stock Trading.
This task aims to 

#### Dataset

#### Environments

The contestants are required to:


#### Model Evaluation
The performance of the model will be assessed by the following metrics:

1. Cumulative return. It is the total return generated by the trading strategy over a trading period.
2. Sharpe ratio. It takes into account both the returns of the portfolio and the level of risk.
3. Max drawdown. It is the portfolio’s largest percentage drop from a peak to a trough in a certain time period, which provides a measure of downside risk.

#### Submission
Participants need to submit a well-organized repository containing all scripts, models, and any custom libraries used to implement the solution. Each team should also submit a 1-2 page report with the IEEE template through TBD. The title should start with “FinRL Contest 2025 Task I.”

### Task II: Open FinLLM Leaderboard – Make the Top
This task aims to 

#### Dataset

#### Requirements

#### Model Evaluation

#### Submission

### Task III: Open FinLLM Leaderboard – Regulatory Reporting
This task aims to 

#### Dataset

#### Requirements

#### Model Evaluation

#### Submission



## Evaluation
For each task, the final ranking of participants will be determined by a weighted combination of model evaluation and report assessment, with weights of 60% and 40% respectively.

**Model evaluation**:
* Task 1: the geometric mean of the rankings of cumulative return, Sharpe ratio, and Max drawdown.
* Task 2:
* Task 3:

**Report assessment**:

The assessment of the reports will be conducted by invited experts and professionals. The judges will independently rate the data and model analysis, results and discussion, robustness and generalizability, innovation and creativity, organization and readability, each accounting for 20% of the qualitative assessment. 

## Organizers

### Core Organizers

| Photo                | Biography              |
|----------------------|-------------------|
| ![Keyi Wang](https://github.com/Open-Finance-Lab/finrl-contest-2024.github.io/blob/main/assets/organizers/keyi.jpeg?raw=true)      | **Keyi Wang**, master at Northwestern University, bachelor at Columbia University. Organizer of FinRL Contest 2023 and  FinRL Contest 2024 at ACM ICAIF conferecens, and Regulations Challenge at COLING 2025. Interested in machine learning and financial engineering. Core member of AI4Finance open-source community, responsible for project development and maintenance of FinRL.|
| ![Arnav Grover](https://github.com/Open-Finance-Lab/finrl-contest-2024.github.io/blob/main/assets/organizers/arnav_grover.jpeg?raw=true)      | **Arnav Grover**|




### Advisors

| Photo                | Biography              |
|----------------------|-------------------|
| ![Xiao-Ying Liu](https://github.com/Open-Finance-Lab/FinRL_Contest_2025/blob/main/docs/assets/organizers/supervisors/liu-xy.png?raw=true) | **Xiao-Yang Liu**, Ph.D., Columbia University, faculty at Rensselaer Polytechnic Institute. His research interests include deep reinforcement learning, big data, and high-performance computing. He created several open-source projects, such as FinRL, ElegantRL, and FinGPT. He contributed chapters to a textbook on reinforcement learning for cyber-physical systems and a textbook on tensors for data processing. He serves as a PC member for NeurIPS, ICML, ICLR, AAAI, IJCAI, AISTATS, and ICAIF. He also served as a Session Chair for IJCAI 2019. He organized Financial Challenges in Large Language Models (FinLLM)@IJCAI 2024, FinRL Competition at ACM ICAIF 2023, the First/Second Workshop on Quantum Tensor Networks in Machine Learning (QTNML) at NeurIPS 2020/2021, IJCAI 2020 Workshop on Tensor Networks Representations in Machine Learning, and the NeurIPS 2019 Workshop on Machine Learning for Autonomous Driving.|
| ![Kairong Xiao](https://github.com/Open-Finance-Lab/FinRL_Contest_2025/blob/main/docs/assets/organizers/supervisors/kairong_xiao.jpg?raw=true) | **Kairong Xiao**, Roger F. Murray Associate Professor of Business at Columbia Business School. His research interests span financial intermediation, corporate finance, monetary economics, industrial organization, and political economy. His research papers have been published in top finance and economics journals, including the Journal of Finance, the Review of Financial Studies, the  Journal of Financial Economics, Econometrica, the Journal of Monetary Economics, and Management Science. He received numerous awards for research excellence, including the Review of Financial Studies Rising Scholar Award, the Journal of Finance Dimensional Fund Advisors Prize for Distinguished Paper, and the Review of Financial Studies Best Paper Award runner-up.|


## Contact
Contestants can communicate any questions on [Discord](https://discord.gg/RNYsEwcXVj).

Contact email: [finrlcontest@gmail.com](mailto:finrlcontest@gmail.com)
