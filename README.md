# visual-saliency-detection
 Fast and easy detection based on spectral residual approach

基于谱残差/余谱理论的显著性检测, 其实就是频域上由对数谱减去平滑曲线.  
据作者的理论与人类视觉预处理阶段有异曲同工之处, 通过观察大量自然图像的对数谱发现其分布较为一致, 现在通过某种算法或者先验信息给出其分布, 再用log谱减去该分布所得到的奇点即为显著点.  
based on [Saliency detection: A spectral residual approach](https://www.researchgate.net/profile/Liqing_Zhang3/publication/221364530_Saliency_Detection_A_Spectral_Residual_Approach/links/55b497f208ae092e9653c2bc.pdf)</br>

My result :  
![0](https://github.com/MirusUmbra/Display-data/raw/master/visual-saliency-detection/s1.jpg)![1](https://github.com/MirusUmbra/Display-data/raw/master/visual-saliency-detection/s1_2.png)</br>
![2](https://github.com/MirusUmbra/Display-data/raw/master/visual-saliency-detection/s2.png)![3](https://github.com/MirusUmbra/Display-data/raw/master/visual-saliency-detection/s2_2.png)</br>

需要注意的是数据的大小会影响结果, 一般来讲小图得到图中目标整体较大的区域, 而大图则得到目标的细节.  
Size of image will influence the result
