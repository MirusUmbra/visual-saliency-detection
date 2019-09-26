def visual_saliency_detection(mat):
    fourier = cv2.dft(np.float32(mat), flags=cv2.DFT_COMPLEX_OUTPUT)
    re, im = cv2.split(fourier)
    tmp1 = re * re
    tmp2 = im * im
    tmp3 = cv2.pow(tmp1 + tmp2, 0.5)
	
	# get natural image
    # log graph
    log = cv2.log(tmp3)
    blur = cv2.blur(log, (7, 7))

    # get residual
    residual = log - blur

    # inverse
    residual = cv2.exp(residual)
    sin = im / tmp3
    cos = re / tmp3

    tmp1 = residual * cos
    tmp2 = residual * sin
    fourier = cv2.merge((tmp1, tmp2))
    inverse = cv2.dft(fourier, flags=cv2.DFT_INVERSE + cv2.DFT_REAL_OUTPUT)

    min_v, max_v, _, _ = cv2.minMaxLoc(inverse)
    _, thre = cv2.threshold(inverse, 0, 255, cv2.THRESH_TOZERO)
    thre = thre * (255 / max_v)
    res = cv2.GaussianBlur(thre, (7, 7), 0)

    return res