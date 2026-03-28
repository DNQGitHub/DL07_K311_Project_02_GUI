import streamlit as st

# CSS for pagination styling
_PAGINATION_STYLES = """
<style>
    .pagination-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 2rem;
        padding: 1.5rem;
        margin: 1.5rem 0;
    }

    .pagination-link {
        display: inline-block;
        color: #0f2027;
        text-decoration: none;
        font-weight: 700;
        font-size: 1rem;
        transition: all 0.3s ease;
        cursor: pointer;
        padding: 0.5rem 0.8rem;
        border-radius: 4px;
    }

    .pagination-link:hover:not(.disabled) {
        color: #ff4757;
        background: rgba(255, 107, 53, 0.05);
        text-decoration: underline;
        text-decoration-thickness: 2px;
        text-underline-offset: 4px;
    }

    .pagination-link.disabled {
        color: #999;
        opacity: 0.5;
        cursor: not-allowed;
        pointer-events: none;
    }

    .pagination-info {
        font-size: 0.95rem;
        color: #142e3a;
        font-weight: 600;
        white-space: nowrap;
    }
</style>
"""

def display(df, page, page_size):
    total_pages = (len(df) - 1) // page_size + 1
    disable_prev = page <= 0
    disable_next = page >= total_pages - 1
    
    prev_class = "disabled" if disable_prev else ""
    next_class = "disabled" if disable_next else ""
    
    st.html(f"""
        {_PAGINATION_STYLES}
        <div class="pagination-container">
            <a href="?page={max(0, page - 1)}" class="pagination-link {prev_class}">← Trước</a>
            
            <div class="pagination-info">
                Trang <strong>{page + 1}</strong> / <strong>{total_pages}</strong>
            </div>
            
            <a href="?page={min(total_pages - 1, page + 1)}" class="pagination-link {next_class}">Tiếp theo →</a>
        </div>
    """)

