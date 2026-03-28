import numpy as np

def data_featuring(df):
    # Vị trí & Lưu thông
    df['is_mat_tien'] = df['full_text'].str.contains(r'mặt tiền|mt |mặt đường|mt', regex=True).astype(int)
    df['is_hxh'] = df['full_text'].str.contains(r'hẻm xe hơi|hxh|hẻm ô tô|hẻm oto|hẻm 6m|hẻm 8m|hẻm rộng', regex=True).astype(int)
    df['is_lo_goc'] = df['full_text'].str.contains(r'lô góc|góc 2 mặt|2 mặt tiền|3 mặt tiền|nhà góc|2mt|3mt|hai mặt|ba mặt', regex=True).astype(int)
    
    # Tiềm năng kinh tế
    df['is_kinh_doanh'] = df['full_text'].str.contains(r'kinh doanh|buôn bán|mặt bằng', regex=True).astype(int)
    df['is_dong_tien'] = df['full_text'].str.contains(r'cho thuê|dòng tiền|thu nhập|chdv|căn hộ dịch vụ', regex=True).astype(int)
    
    # Đặc tính & Phong thủy
    df['is_no_hau'] = df['full_text'].str.contains(r'nở hậu', regex=True).astype(int)
    df['has_thang_may'] = df['full_text'].str.contains(r'thang máy', regex=True).astype(int)
    df['is_nha_moi'] = df['full_text'].str.contains(r'nhà mới|mới đẹp|full nội thất|xách vali', regex=True).astype(int)
    df['is_nha_nat'] = df['full_text'].str.contains(r'nhà nát|cũ nát|tiện xây mới|bán đất|đập đi', regex=True).astype(int)
    df['has_quy_hoach'] = df['full_text'].str.contains(r'quy hoạch|lộ giới|dính quy', regex=True).astype(int)
    df['is_chinh_chu'] = df['full_text'].str.contains(r'chính chủ|1 đời chủ|đời chủ', regex=True).astype(int)
    df['has_san_thuong'] = df['full_text'].str.contains(r'sân thượng', regex=True).astype(int)
    df['has_gara'] = df['full_text'].str.contains(r'gara|ga ra|garage|ô tô đỗ|xe hơi ngủ|ô tô vào nhà|xe hơi vào', regex=True).astype(int)
    df['o_ngay'] = df['full_text'].str.contains(r'ở ngay|ở liền|dọn vào ở|vào ở ngay', regex=True).astype(int)
    
    # Tín hiệu Gấp/Ngộp (Cho Anomaly Detection)
    df['is_ngop_bank'] = df['full_text'].str.contains(r'ngộp|ngân hàng|giải chấp|vỡ nợ|phá sản|vay bank', regex=True).astype(int)
    df['is_ban_gap'] = df['full_text'].str.contains(r'bán gấp|hạ chào|giảm giá|cắt lỗ|giảm sâu|cần tiền', regex=True).astype(int)
    
    # Tiện nghi score
    tien_ich_kw = ["gara","garage","hồ bơi","sân thượng","thang máy","sân vườn",
                "ban công","giếng trời","ô tô","xe hơi","kinh doanh",
                "trường học","bệnh viện","chợ","công viên","siêu thị"]

    df["tien_nghi_score"] = df['full_text'].apply(
        lambda x: sum(1 for kw in tien_ich_kw if kw in str(x)))
    
    df["log_gia_ban"] = np.log(df["gia_ban"])
    
    return df