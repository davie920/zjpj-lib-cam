import cv2

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

        # 當收集到四個點時，顯示座標並退出
        if len(points) == 4:
            print("四個點的座標：")
            for i, (px, py) in enumerate(points):
                print(f"點 {i+1}: ({px}, {py})")
            cv2.destroyAllWindows()


if __name__ == "__main__":
    # 載入圖片
    img = cv2.imread('./images/test1.png')

    # 顯示圖片並設置點擊事件的回調函數
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)

    # 按下任意鍵來退出
    cv2.waitKey(0)
    cv2.destroyAllWindows()