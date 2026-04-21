-- ==========================================
-- 1. TẠO BẢNG SETTINGS
-- ==========================================
CREATE TABLE IF NOT EXISTS settings (
    id SERIAL PRIMARY KEY,
    user_id UUID NOT NULL DEFAULT auth.user_id()::uuid, -- Tự động lấy từ JWT
    key TEXT NOT NULL,
    value TEXT NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(user_id, key)
);
-- ==========================================
-- 2. KÍCH HOẠT BẢO MẬT RLS
-- ==========================================
ALTER TABLE settings ENABLE ROW LEVEL SECURITY;

-- Xóa policy cũ nếu có để tránh lỗi khi chạy lại
DROP POLICY IF EXISTS "Users can manage their own settings" ON settings;

-- Tạo chính sách: Chỉ chủ sở hữu mới có quyền CRUD
CREATE POLICY "Users can manage their own settings" ON settings
    FOR ALL
    USING (user_id = auth.user_id()::uuid)
    WITH CHECK (user_id = auth.user_id()::uuid);
-- ==========================================
-- 3. TỰ ĐỘNG CẬP NHẬT THỜI GIAN (Optional)
-- ==========================================
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_settings_updated_at
    BEFORE UPDATE ON settings
    FOR EACH ROW
    EXECUTE PROCEDURE update_updated_at_column();
