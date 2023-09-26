import cv2
import numpy as np

# 創建一個空的列表來存儲點的座標
points = []

# 點擊事件的回調函數
def click_event(event, x, y, flags, param):
    global points

    if event == cv2.EVENT_LBUTTONDOWN:
        # 在圖片上畫一個小圓圈來標記點的位置
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow('image', img)

        # 將點的座標添加到列表中
        points.append((x, y))

        # 當收集到四個點時，進行透視變換並顯示結果
        if len(points) == 4:
            cv2.destroyAllWindows()
            transform_image(img, points)

# 執行透視變換
def transform_image(img, points):
    # 設置目標圖像的寬度和高度與原圖相同
    width, height = img.shape[1], img.shape[0]
    new_points = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

    # 執行透視變換
    matrix = cv2.getPerspectiveTransform(np.array(points, dtype=np.float32), new_points)
    result = cv2.warpPerspective(img, matrix, (width, height))

    # 顯示變換後的圖像
    cv2.imshow('Transformed Image', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # 載入圖片
    img = cv2.imread('./images/test1.png')

    # 顯示圖片並設置點擊事件的回調函數
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)

    # 等待用戶按下任意鍵來退出
    cv2.waitKey(0)
    cv2.destroyAllWindows()
