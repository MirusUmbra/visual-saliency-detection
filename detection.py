def visual_saliency_detection(mat):
    fourier = cv2.dft(np.float32(mat), flags=cv2.DFT_COMPLEX_OUTPUT)

    # 实部和虚部平方和再开方，得到合并的频域用作后续运算
    # 虽然论文提到全程计算只使用振幅谱,相位谱不变,但是实际计算振幅谱的对数时出现超过定义域因而无法计算对数, 并且论文作者实际也是计算振幅+相位, 所以暂时与作者代码保持一致
    # Different with paper, the author actually used both imaginary and real part of the frequency domain.
    re, im = cv2.split(fourier)
    base = (re ** 2 + im ** 2) ** 0.5

    # 对数谱
    log = cv2.log(base)
    # 平滑曲线
    blur = cv2.blur(log, (7, 7))

    # 显著性余谱
    # Get residual
    residual = log - blur

    # 指数还原对数谱
    # Restore
    residual = cv2.exp(residual)

    # 求原频域上实虚的夹角, 利用夹角还原实虚
    sin = im / base
    cos = re / base 
    re = residual * cos
    im = residual * sin

    # 傅里叶逆变换
    fourier = cv2.merge((re, im))
    inverse = cv2.dft(fourier, flags=cv2.DFT_INVERSE + cv2.DFT_REAL_OUTPUT)

    # 优化结果显示
    min_v, max_v, _, _ = cv2.minMaxLoc(inverse)
    _, thre = cv2.threshold(inverse, 0, 255, cv2.THRESH_TOZERO)
    thre = thre * (255 / max_v)
    res = cv2.GaussianBlur(thre, (7, 7), 0)

    return res