from mcp.server.fastmcp import FastMCP
import pyttsx3

# Initialize FastMCP server
mcp = FastMCP(
    "simulator", 
    host="0.0.0.0",
    port=8000,
    cors_allowed_origins=["*"],  # 允许跨域请求
    response_headers={"Content-Type": "text/event-stream"}  # 确保正确的内容类型头
)

# 初始化 pyttsx3 引擎
engine = pyttsx3.init()
# 设置语速，默认值是200
engine.setProperty('rate', 150)

@mcp.tool()
async def simu_control(direction: str, distance: float) -> str:
    """Simulate controlling a device in a specific direction for a given distance.
    
    Args:
        direction: Direction to move (forward, back, up, down, left, right)
        distance: Distance to move in meters
    """
    # 检查方向参数是否有效
    valid_directions = ["up", "down", "left", "right", "forward", "back"]
    if direction.lower() not in valid_directions:
        return f"Invalid direction: {direction}. Please use forward, back, up, down, left, or right."
    
    # 组装英文句子
    message = f"Moving {direction.lower()} for {distance} meters."
    
    # 朗读文本
    engine.say(message)
    engine.runAndWait()
    
    return message

if __name__ == "__main__":
    # Initialize and run the server
    # mcp.run(transport='stdio', debug=True)
    mcp.run(transport='sse')
