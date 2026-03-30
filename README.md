<p align="center">
  <h1 align="center">📊 Ứng dụng Data Science trong Bất Động Sản</h1>
  <p align="center">
    <strong>Hệ thống gợi ý bất động sản & phân khúc thị trường nhà ở</strong>
  </p>
  <p align="center">
    <em>Dự án môn Đồ án tốt nghiệp — Nhóm 09</em>
  </p>
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.10.5-3776AB?logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit">
    <img src="https://img.shields.io/badge/Scikit--Learn-ML-F7931E?logo=scikitlearn&logoColor=white" alt="Scikit-learn">
    <img src="https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?logo=pytorch&logoColor=white" alt="PyTorch">
    <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  </p>
</p>

---

## 📑 Mục lục

- [Giới thiệu](#-giới-thiệu)
- [Tính năng chính](#-tính-năng-chính)
- [Kiến trúc hệ thống](#-kiến-trúc-hệ-thống)
- [Cấu trúc thư mục](#-cấu-trúc-thư-mục)
- [Công nghệ sử dụng](#%EF%B8%8F-công-nghệ-sử-dụng)
- [Cài đặt & Chạy](#-cài-đặt--chạy)
- [Các trang giao diện](#-các-trang-giao-diện)
- [Dữ liệu](#-dữ-liệu)
- [Thành viên nhóm](#-thành-viên-nhóm)

---

## 🏠 Giới thiệu

Dự án tập trung xây dựng ứng dụng Data Science trong lĩnh vực **Bất Động Sản**, áp dụng trên dữ liệu thực tế từ nền tảng **Nhà Tốt (nhatot.com)** — thuộc hệ sinh thái Chợ Tốt, nền tảng mua bán trực tuyến hàng đầu Việt Nam.

Hai bài toán chính được giải quyết:

| # | Bài toán | Mô tả |
|---|----------|-------|
| 1 | **Recommendation System** | Gợi ý nhà tương tự dựa trên nội dung (Content-based Filtering & Hybrid) |
| 2 | **Market Segmentation** | Phân khúc thị trường nhà ở bằng các thuật toán clustering |

> **GVHD:** Thạc sỹ Khuất Thùy Phương

---

## ✨ Tính năng chính

### 🔍 Hệ thống gợi ý (Recommendation System)
- **Content-based Filtering** — Sử dụng Cosine Similarity & Gensim LSI trên đặc trưng văn bản
- **Hybrid Filtering** — Kết hợp Text + Price + Location Similarity
- **Sentence Transformers (BERT)** — Mô hình embedding nâng cao *(phần cộng điểm)*
- Tìm kiếm bất động sản bằng từ khóa tự nhiên
- Gợi ý nhà tương tự khi xem chi tiết bài đăng

### 🏘️ Phân khúc thị trường (Market Segmentation)
- **Scikit-learn:** KMeans, GMM, Agglomerative Clustering
- **PySpark:** KMeans, GMM, Bisecting K-Means
- **Spectral Clustering** *(phần cộng điểm)*
- Tự động phân loại nhà ở vào phân khúc khi nhập thông tin

### 📊 Dashboard tương tác
- Giao diện Streamlit hiện đại với thiết kế premium
- Duyệt danh sách bài đăng với phân trang
- Xem chi tiết bài đăng kèm biểu đồ giá bán theo thời gian
- Sidebar thông minh với thanh tìm kiếm & bài đăng nổi bật

---

## 🏗 Kiến trúc hệ thống

```
┌──────────────────────────────────────────────────────┐
│                    Streamlit UI                       │
│  (Home, Posts, Post Detail, Search, Clustering, ...) │
└──────────────┬───────────────────────┬───────────────┘
               │                       │
    ┌──────────▼──────────┐ ┌──────────▼──────────┐
    │   Recommendation    │ │     Clustering       │
    │      Engine         │ │      Engine          │
    │                     │ │                      │
    │ • Cosine Similarity │ │ • KMeans / GMM       │
    │ • Gensim LSI        │ │ • Agglomerative      │
    │ • Sentence BERT     │ │ • Spectral           │
    └──────────┬──────────┘ └──────────┬───────────┘
               │                       │
    ┌──────────▼───────────────────────▼───────────┐
    │          Pre-trained Models (Google Drive)     │
    │         (auto-download on first launch)        │
    └──────────────────────┬───────────────────────┘
                           │
              ┌────────────▼────────────┐
              │     Nhà Tốt Dataset     │
              │   8,273 tin đăng nhà    │
              └─────────────────────────┘
```

---

## 📂 Cấu trúc thư mục

```
DL07_K311_Project_02_GUI/
├── app.py                          # Entry point — download models & redirect
├── requirements.txt                # Dependencies
├── Procfile                        # Heroku deployment config
├── setup.sh                        # Streamlit server config script
├── .python-version                 # Python 3.10.5
│
├── .streamlit/
│   └── config.toml                 # Streamlit theme & UI config
│
├── pages/                          # 📄 Các trang giao diện
│   ├── home.py                     # Trang chủ — tổng quan dự án
│   ├── business_problem.py         # Bối cảnh & mục tiêu
│   ├── task_assignment.py          # Bảng phân công công việc
│   ├── posts.py                    # Danh sách bài đăng (phân trang)
│   ├── post_detail.py              # Chi tiết bài đăng + gợi ý + phân khúc
│   ├── search_result.py            # Kết quả tìm kiếm
│   └── market_clustering.py        # Phân khúc thị trường (nhập liệu)
│
├── components/                     # 🧩 UI Components tái sử dụng
│   ├── sidebar.py                  # Sidebar chính (nav + search + posts)
│   ├── search_input.py             # Thanh tìm kiếm
│   ├── post_card.py                # Card bài đăng
│   ├── post_card_list.py           # Danh sách card bài đăng
│   ├── post_detail.py              # Component chi tiết bài đăng
│   ├── post_price_chart.py         # Biểu đồ giá
│   ├── pagination.py               # Phân trang
│   ├── sidebar_post.py             # Card bài đăng trong sidebar
│   └── sidebar_post_list.py        # Danh sách bài đăng sidebar
│
├── features/                       # ⚙️ Logic nghiệp vụ
│   ├── recommendation/
│   │   ├── data/                   # Dữ liệu recommendation
│   │   ├── models/                 # Mô hình đã train (*.pkl)
│   │   └── helpers/
│   │       ├── download_models.py  # Tải models từ Google Drive
│   │       ├── join_models.py      # Ghép file model đã chunk
│   │       ├── load_data.py        # Load data & similarity matrix
│   │       ├── data_preprocessing.py
│   │       ├── data_featuring.py
│   │       ├── recommend_posts_by_idx.py   # Gợi ý theo index
│   │       └── recommend_posts_by_query.py # Gợi ý theo truy vấn
│   │
│   └── clustering/
│       ├── data/                   # Dữ liệu clustering
│       ├── models/                 # Mô hình clustering (*.pkl)
│       └── helpers/
│           ├── download_models.py
│           ├── join_models.py
│           ├── load_data.py
│           ├── data_featuring.py   # Feature engineering
│           └── clusterize.py       # Phân khúc bất động sản
│
├── models/
│   └── recommendation/             # Pre-trained models (BERT, etc.)
│
├── helpers/                        # 🔧 Tiện ích
│   ├── chunk_file.py               # Chia nhỏ file lớn
│   ├── join_file.py                # Ghép file đã chia
│   └── recommendation/
│
├── tool_scripts/                   # 🛠 Scripts hỗ trợ
│   ├── chunk_sentence_transformer_embeddings.py
│   ├── chunk_sentence_transformer_model.py
│   ├── chunk_sim_matrix_sentence_transformer.py
│   └── chunk_spectral_clustering_model.py
│
└── docs/
    └── REQUIREMENT.md              # Yêu cầu dự án gốc
```

---

## ⚙️ Công nghệ sử dụng

| Nhóm | Công nghệ |
|------|-----------|
| **Ngôn ngữ** | Python 3.10.5 |
| **Web Framework** | Streamlit |
| **Data Processing** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn, Gensim |
| **Deep Learning** | PyTorch, Sentence Transformers (BERT) |
| **NLP** | PyVi (Vietnamese NLP), BeautifulSoup4 |
| **Visualization** | Matplotlib, Seaborn |
| **Model Storage** | Google Drive (via gdown) |
| **Deployment** | Heroku (Procfile + setup.sh) |

---

## 🚀 Cài đặt & Chạy

### Yêu cầu hệ thống
- Python **3.10.5** (khuyến nghị sử dụng [pyenv](https://github.com/pyenv/pyenv) để quản lý phiên bản)
- Git

### Bước 1: Clone repository

```bash
git clone https://github.com/DNQGitHub/DL07_K311_Project_02_GUI.git
cd DL07_K311_Project_02_GUI
```

### Bước 2: Tạo môi trường ảo & cài đặt dependencies

```bash
# Tạo virtual environment
python -m venv venv

# Kích hoạt (Windows)
venv\Scripts\activate

# Kích hoạt (macOS/Linux)
source venv/bin/activate

# Cài đặt dependencies
pip install -r requirements.txt
```

### Bước 3: Chạy ứng dụng

```bash
streamlit run app.py
```

> ⚠️ **Lưu ý:** Lần đầu chạy, ứng dụng sẽ tự động tải các mô hình đã train từ Google Drive. Quá trình này có thể mất vài phút tùy tốc độ mạng.

Ứng dụng sẽ mở tại: **http://localhost:8501**

---

## 🖥 Các trang giao diện

| Trang | Đường dẫn | Mô tả |
|-------|-----------|-------|
| **Trang chủ** | `/home` | Tổng quan dự án, tech stack, roadmap |
| **Bối cảnh & Mục tiêu** | `/business_problem` | Bài toán kinh doanh, dữ liệu đầu vào |
| **Phân công** | `/task_assignment` | Bảng phân công công việc nhóm |
| **Bài đăng** | `/posts` | Danh sách bài đăng BĐS có phân trang |
| **Chi tiết bài đăng** | `/post_detail?post_id=...` | Thông tin chi tiết + gợi ý + phân khúc + biểu đồ giá |
| **Kết quả tìm kiếm** | `/search_result` | Gợi ý BĐS theo truy vấn từ khóa |
| **Phân khúc** | `/market_clustering` | Nhập thông tin nhà → phân loại phân khúc |

---

## 📦 Dữ liệu

- **Nguồn:** [Nhà Tốt (nhatot.com)](https://www.nhatot.com/) — nền tảng BĐS thuộc Chợ Tốt
- **Quy mô:** **8,273** tin đăng nhà riêng lẻ
- **Khu vực:** Bình Thạnh, Gò Vấp, Phú Nhuận (TP. Hồ Chí Minh)
- **Các trường dữ liệu chính:**

| Trường | Mô tả |
|--------|-------|
| `tieu_de` | Tiêu đề bài đăng |
| `gia_ban` | Giá bán (VND) |
| `dien_tich` | Diện tích (m²) |
| `dia_chi` | Địa chỉ |
| `so_phong_ngu` | Số phòng ngủ |
| `loai_hinh` | Loại hình (nhà phố, biệt thự, ...) |
| `quan` | Quận |
| `mo_ta` | Mô tả chi tiết |
| `bieu_do_gia` | Dữ liệu biểu đồ giá theo thời gian |
| ... | Và nhiều trường khác |

---

## 👥 Thành viên nhóm

| Thành viên | Email |
|------------|-------|
| **Đoàn Nhật Quang** | [dnq.httt@gmail.com](mailto:dnq.httt@gmail.com) |
| **Phan Ngọc Minh Quân** | [quan.phanngocminh111@gmail.com](mailto:quan.phanngocminh111@gmail.com) |

---

<p align="center">
  <sub>© 2026 — Nhóm 09 · GVHD: ThS. Khuất Thùy Phương</sub>
</p>
