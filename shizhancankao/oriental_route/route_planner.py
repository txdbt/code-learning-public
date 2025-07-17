import cv2
import numpy as np
import matplotlib.pyplot as plt
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# --------------------------
# 模块1：打卡点检测
# --------------------------
def detect_checkpoints(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"图片 {image_path} 未找到或无法读取")
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    
    # 霍夫圆检测（调整参数适应你的地图）
    circles = cv2.HoughCircles(
        edges, 
        cv2.HOUGH_GRADIENT, 
        dp=1, 
        minDist=20,
        param1=50, 
        param2=30, 
        minRadius=10, 
        maxRadius=50
    )
    
    checkpoints = []
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            x, y, r = circle
            checkpoints.append((x, y))
    return checkpoints

# --------------------------
# 模块2：坐标转换与距离计算
# --------------------------
def pixel_to_meter(points, scale):
    return [(x * scale, y * scale) for (x, y) in points]

def calculate_distance_matrix(points):
    n = len(points)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            dist_matrix[i][j] = np.sqrt(dx**2 + dy**2)
    return dist_matrix

# --------------------------
# 模块3：TSP求解
# --------------------------
def solve_tsp(distance_matrix):
    manager = pywrapcp.RoutingIndexManager(
        len(distance_matrix), 
        1,  # 车辆数量
        0   # 起点索引
    )
    routing = pywrapcp.RoutingModel(manager)
    
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]
    
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )
    
    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        route = []
        index = routing.Start(0)
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            index = solution.Value(routing.NextVar(index))
        route.append(manager.IndexToNode(index))  # 添加终点
        return route
    else:
        raise RuntimeError("无法找到最优路径")

# --------------------------
# 模块4：可视化
# --------------------------
def plot_route(image_path, checkpoints, route):
    img = cv2.imread(image_path)
    plt.figure(figsize=(12, 8))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    
    # 绘制打卡点
    for i, (x, y) in enumerate(checkpoints):
        plt.scatter(x, y, s=200, c='red', marker='o')
        plt.text(x+10, y+10, str(i), fontsize=12, color='white', 
                bbox=dict(facecolor='black', alpha=0.5))
    
    # 绘制路线
    route_points = [checkpoints[i] for i in route]
    xs, ys = zip(*route_points)
    plt.plot(xs, ys, 'b-', linewidth=3, markersize=12)
    plt.title(f"最优路线（共 {len(checkpoints)} 个打卡点）", fontsize=14)
    plt.axis('off')
    plt.show()

# --------------------------
# 主程序
# --------------------------
if __name__ == "__main__":
    # 配置参数
    image_path = r"F:\python\实战参考\oriental_route\map.png"  # 替换为你的地图文件路径
    scale = 0.1             # 比例尺：1像素=0.1米（根据实际地图调整）
    
    try:
        print("步骤1：检测打卡点...")
        checkpoints_pixel = detect_checkpoints(image_path)
        print(f"检测到 {len(checkpoints_pixel)} 个打卡点")
        
        print("步骤2：转换坐标并计算距离...")
        checkpoints_meter = pixel_to_meter(checkpoints_pixel, scale)
        distance_matrix = calculate_distance_matrix(checkpoints_meter)
        
        print("步骤3：规划最优路线...")
        optimal_route = solve_tsp(distance_matrix)
        print("规划完成！路线顺序：", optimal_route)
        
        print("步骤4：可视化结果...")
        plot_route(image_path, checkpoints_pixel, optimal_route)
        
    except Exception as e:
        print(f"错误发生：{str(e)}")