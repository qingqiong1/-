import cv2
import numpy as np

# 使用 medianBlur(src: cv2.typing.MatLike, ksize: int)

def quicksort(arr):
    if len(arr) < 1:
        return arr
    
    pivot = arr[len(arr) //  2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(right) + middle + quicksort(left)



def  my_medianBlur(image:cv2.typing.MatLike,ksize:int):
    if ksize %2 == 0:
        raise ValueError("ksize必须为奇数")
    h,w =  image.shape
    pad = ksize // 2
    # 1. 边界填充：用“复制边缘像素”的方式，避免边缘黑边
    padded_image = cv2.copyMakeBorder(image,pad,pad,pad,pad,cv2.BORDER_REPLICATE)
    # 2. 创建输出图像
    output_image = np.zeros_like(image)
    # 3. 遍历每个像素，执行中值滤波
    for i in range(h):
        for j in range(w):
            # 提取当前像素的邻域（kernel_size × kernel_size）并排序
            neighborhood = padded_image[i:i+ksize,j:j+ksize].flatten()
            neighborhood.sort()
            # 取中位数
            median_value = neighborhood[len(neighborhood)//2]
            # # 5. 用中位数替换当前像素值
            output_image[i,j]  = median_value
    return output_image.astype(np.uint8)

# --- 测试 ---
if __name__ == "__main__":
    data = [3, 6, 8, 10, 1, 2, 1]
    print(f"排序前: {data}")
    sorted_data = quicksort(data)
    print(f"排序后: {sorted_data}")