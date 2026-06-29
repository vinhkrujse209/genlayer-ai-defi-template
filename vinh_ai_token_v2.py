# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class VinhAITokenV2(gl.Contract):
    token_name: str
    token_symbol: str
    owner: Address
    total_supply: u256
    burned_tokens: u256  # Biến mới: Theo dõi lượng token đã bị đốt
    
    # Biến lưu trữ dữ liệu AI
    ai_prediction: str
    ai_confidence: str   # Biến mới: Đánh giá độ tin cậy của AI

    # Khởi tạo token
    def __init__(self, name: str, symbol: str):
        self.token_name = name
        self.token_symbol = symbol
        self.owner = gl.message.sender_address  
        self.total_supply = 1000000000  # Tổng cung 1 tỷ token
        self.burned_tokens = 0
        self.ai_prediction = "Waiting for analysis..."
        self.ai_confidence = "0%"

    # Hàm lấy thông tin cơ bản
    @gl.public.view
    def get_token_info(self) -> str:
        return f"Token: {self.token_name} ({self.token_symbol}) - Supply: {self.total_supply} - Burned: {self.burned_tokens}"

    # Hàm ghi dữ liệu on-chain: Cập nhật insight kèm độ tin cậy
    @gl.public.write
    def update_market_insight(self, new_insight: str, confidence: str) -> None:
        self.ai_prediction = f"Insight: {new_insight}"
        self.ai_confidence = confidence

    # TÍNH NĂNG MỚI: Hàm mô phỏng đốt Token (Giảm tổng cung)
    @gl.public.write
    def burn_token(self, amount: u256) -> None:
        self.total_supply = self.total_supply - amount
        self.burned_tokens = self.burned_tokens + amount

    # Hàm đọc kết quả AI
    @gl.public.view
    def get_ai_result(self) -> str:
        return f"{self.ai_prediction} | Confidence: {self.ai_confidence}"
