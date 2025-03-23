import cv2

# 카툰 렌더링 함수
def cartoonize_image(img):
    # 1. 이미지 크기 축소
    img_small = cv2.pyrDown(img)
    
    # 2. 이미지 상향 샘플링 (컬러를 부드럽게)
    for _ in range(7):
        img_small = cv2.pyrDown(img_small)
    
    # 3. 컬러 이미지 부드럽게 하기
    img_color = cv2.bilateralFilter(img, 9, 300, 300)
    
    # 4. 이미지의 가장자리를 감지하기 위한 그라디언트
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.medianBlur(img_gray, 5)
    
    # 5. 엣지 감지
    img_edge = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    
    # 6. 색상과 엣지를 결합하여 카툰 효과 만들기
    img_cartoon = cv2.bitwise_and(img_color, img_color, mask=img_edge)
    
    return img_cartoon

# 이미지 로드
img = cv2.imread('bird.webp')
img2 = cv2.imread('bird2.jpg')

# 카툰 효과 적용
cartoon_img = cartoonize_image(img)
cartoon_img2 = cartoonize_image(img2)

cv2.imwrite('Cartoon_image.jpg',cartoon_img)
cv2.imwrite('Cartoon_image2.jpg',cartoon_img2)