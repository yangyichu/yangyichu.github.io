---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>
I'm currently a researcher at Seed Robotics, Bytedance.

I graduated from Northeastern University with my MS degree in Robotics, concentrating in Mechanical Engineering. I got my BS degree in Mechanical Engineering at Shanghai Jiaotong University. 

My research interests primarily focus on robotics. I have experience in VLA, reinforcement Learning and robotics. I also have a strong background in control theory, mechanical design, and prototyping. 


# 🔥 News
- *2025.07*: &nbsp;🎉🎉 GR-3 released! A large scale VLA model that generalizes and can handle long-horizon and dexterous tasks. 
- *2024.09*: &nbsp;🎉🎉 GR-2 released! A new state of the art generative VLA model that achieves average success rate of 97.7% across more than 100 tasks. 
- *2024.06*: &nbsp;🎉🎉 Cyberdog2 released! The first comme with ai-powered auto fall-recovery.

# 📝 Publications 
<!-- 1 -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Tech Report 2025</div><img src='images/gr3.gif' alt="sym" width=500 height=300></div></div>
<div class='paper-box-text' markdown="1">
<h2>
  <a href="https://arxiv.org/abs/2507.15493" target="_blank">
    GR-3 Technical Report
  </a>
</h2>
Chilam Cheang, Sijin Chen, Zhongren Cui, Yingdong Hu, Liqun Huang, Tao Kong, Hang Li, Yifeng Li, Yuxiao Liu, Xiao Ma, Hao Niu, Wenxuan Ou, Wanli Peng, Zeyu Ren, Haixin Shi, Jiawen Tian, Hongtao Wu, Xin Xiao, Yuyang Xiao, Jiafeng Xu, <span style="font-weight: bold; color: #00369f;">Yichu Yang</span>

[**Project**](https://seed.bytedance.com/zh/GR3)  [**Paper**](https://arxiv.org/abs/2507.15493) 
- GR-3 showcases exceptional capabilities in generalizing to novel objects, environments, and instructions involving abstract concepts.
- GR-3 also excels in handling long-horizon and dexterous tasks
</div>
</div>

<!-- 2 -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Tech Report 2024</div><img src='images/gr-2.png' alt="sym" width=500 height=300></div></div>
<div class='paper-box-text' markdown="1">
<h2>
  <a href="https://arxiv.org/pdf/2410.06158" target="_blank">
    GR-2: A Generative Video-Language-Action Model with
Web-Scale Knowledge for Robot Manipulation
  </a>
</h2>
Chi-Lam Cheang, Guangzeng Chen, Ya Jing, Tao Kong,
Hang Li, Yifeng Li, Yuxiao Liu, Hongtao Wu,
Jiafeng Xu, <span style="font-weight: bold; color: #00369f;">Yichu Yang</span>, Hanbo Zhang, Minzhao Zhu

[**Project**](https://gr2-manipulation.github.io/)  [**Paper**](https://arxiv.org/pdf/2410.06158) <strong><span class='show_paper_citations' data='A_oWM24AAAAJ:u5HHmVD_uO8C'></span></strong>
- GR-2 achieves a 97.7% success rate across 100+ tasks
- GR-2 excels in industrial scenarios like end-to-end picking and adapts well to unseen environments. 
</div>
</div>

<!-- 3 State Estimation Transformers for Agile Legged Locomotion-->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IROS 2024/ Deployable@CoRL2023</div><img src='images/dog_sideflip.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
<h2>
  <a href="https://arxiv.org/abs/2410.13496" target="_blank">
    State Estimation Transformers for Agile Legged Locomotion
  </a>
</h2>

Chen Yu, <span style="font-weight: bold; color: #00369f;">Yichu Yang</span>, Tianlin Liu, Yangwei You, Mingliang Zhou, Diyun Xiang

[**Video**](https://www.youtube.com/watch?v=NAhYAmN2pYE) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Best Paper Runner-Up at [Deployable@CoRL2023](https://corl2023deployable.github.io/schedule/)
- The policy was successfully deployed on Cyberdog2, enabling it to execute agile maneuvers such as running jumps, running backflips, and running sideflips
</div>
</div>

# 🔍 Research and Projects
<!-- ####################################research1###################################### -->
<div class="research-row" style="display: flex; gap: 20px; width: 100%;">

<div class='paper-box'>
  <!-- 标题区域（带徽章） -->
  <div class="title-container">
      <span class="research-badge">R&D</span>
      <h2 class="main-title"> <img src="images/xiaomi.png" alt="Coffee icon" style="height: 1em; vertical-align: middle;"> First Product-level Robust Fall-Recovery Ability On All Kinds of Terrains</h2>
  </div>

  <!-- 图片行（保持相同大小） -->
<div class="image-row" style="display: flex; gap: 15px; margin-bottom: 15px; width: 100%;">
  <img src="images/dog1.gif" alt="dog1"
       style="height: 150px; width: auto; object-fit: contain; border-radius: 8px; min-width: 0;">
  <img src="images/dog2.gif" alt="dog2"
       style="height: 150px; width: auto; object-fit: contain; border-radius: 8px; min-width: 0;">
  <img src="images/dog-reset.gif" alt="image"
       style="height: 150px; width: auto; object-fit: cover; border-radius: 8px; min-width: 0;">
  
  <img src="images/dog-reset2.gif" alt="image"
      style="height: 150px; width: auto; object-fit: cover; border-radius: 8px; min-width: 0;">
</div>
</div>
</div>

<!-- ####################################research23###################################### -->
<!-- 父容器：Flexbox布局实现并排显示 -->
<div class="research-row" style="display: flex; gap: 20px; width: 100%;">
  <!-- 第一个paper-box：自适应宽度 -->
  <div class='paper-box' style="flex: 1; min-width: 0; padding: 15px; border: none solid #eee; border-radius: 8px;">
    <!-- 标题区域（带徽章） -->
    <div class="title-container">
      <span class="research-badge">R&D</span>
      <h2 class="main-title">
        <img src="images/xiaomi.png" alt="Coffee icon" style="height: 1em; vertical-align: middle;">
        Learning Agile Locomotion and Acrobatic Motions
      </h2>
    </div>
    <!-- 图片行（保持相同大小） -->
    <div class="image-row" style="display: flex; gap: 15px; margin-bottom: 15px; width: 100%;">
      <img src="images/dog_flip.gif" alt="dog1"
          style="height: 150px; width: auto; object-fit: contain; border-radius: 8px; min-width: 0;">
      <img src="images/dog_flip2.gif" alt="dog2"
          style="height: 150px; width: auto; object-fit: contain; border-radius: 8px; min-width: 0;">
    </div>
  </div>

  <!-- 第二个paper-box：自适应宽度 -->
  <div class='paper-box' style="flex: 1; min-width: 0; padding: 15px; border: none solid #eee; border-radius: 8px;">
    <!-- 标题区域（带徽章） -->
    <div class="title-container">
      <span class="research-badge">Patent</span>
      <h2 class="main-title">
        <img src="images/xiaomi.png" alt="Coffee icon" style="height: 1em; vertical-align: middle;">
        Dog foot contact sensor based on hall effect
      </h2>
    </div>
    <!-- 图片行（保持相同大小） -->
    <div class='image-row' style="display: flex; gap: 15px; margin-bottom: 15px; width: 100%;">
      <img src="images/foot_sensor.gif" alt="dog2"
          style="height: 150px; width: auto; object-fit: contain; border-radius: 8px; min-width: 0;">
      <img src="images/patent.png" alt="patent"
          style="height: 150px; width: auto; object-fit: contain; border-radius: 8px; min-width: 0;">
    </div>
  </div>
</div>


# 💼 Work Experience
- *2024.01 - now*, Researcher, Seed Robotics, Bytedance. 
- *2022.07 - 2024.01*, Researcher, Xiaomi Robotics Lab, Xiaomi. 
- *2021.06 - 2022.03*, RA, Khoury College of Computer Sciences, Northeastern University. 
- *2019.05 - 2019.12*, Mechatronics Engineer, Qlibrium (previously CamMed)

# 📖 Educations
- *2018.09 - 2021.06*, Robotics, Khoury College of Computer Sciences, Northeastern University. 
- *2014.09 - 2018.06*, Mechanical Engineering, Shanghai Jiaotong University. 

