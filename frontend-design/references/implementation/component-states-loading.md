# Loading状态详解

> ⏳ **加载状态** - 异步操作进行中的视觉反馈和交互规范

---

## 📖 状态概述

Loading（加载状态）表示组件正在处理数据或等待响应，告知用户系统正在工作。

**适用场景**：
- 表单提交后等待服务器响应
- 异步数据加载中
- 文件上传/下载进行中
- 页面/组件初始化加载

---

## 🎨 视觉描述

### 设计规范

```css
/* 按钮加载状态 */
.button.is-loading {
  position: relative;
  color: transparent;
  pointer-events: none;
}

.button.is-loading::after {
  content: "";
  position: absolute;
  width: 1em;
  height: 1em;
  top: 50%;
  left: 50%;
  margin-left: -0.5em;
  margin-top: -0.5em;
  border: 2px solid currentColor;
  border-radius: 50%;
  border-right-color: transparent;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* 骨架屏加载 */
.skeleton {
  background: linear-gradient(
    90deg,
    var(--color-skeleton-start) 25%,
    var(--color-skeleton-middle) 50%,
    var(--color-skeleton-end) 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: var(--radius-md);
}

@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

/* 进度条 */
.progress-bar {
  height: 4px;
  background: var(--color-bg-progress);
  border-radius: var(--radius-full);
  overflow: hidden;
}

.progress-bar-fill {
  height: 100%;
  background: var(--color-primary);
  transition: width 0.3s ease;
  animation: progress-pulse 1.5s infinite;
}

@keyframes progress-pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.7; }
}
```

### 设计要点

**1. 加载指示器选择**
- 旋转圆环：轻量级，通用
- 进度条：显示具体进度
- 骨架屏：保持布局结构
- 模糊覆盖：区域划分明确

**2. 视觉尺寸要求**
- 旋转圆环至少 16×16px
- 进度条高度 4-8px
- 骨架屏与实际内容同尺寸
- 确保足够的对比度

**3. 交互处理**
- `pointer-events: none` 防止重复点击
- 保持按钮/组件宽度避免抖动
- 加载中禁用所有交互

**4. 布局稳定性**
- 预留加载指示器空间
- 避免加载完成后布局变化
- 使用占位符保持空间

---

## 🖱️ 交互行为

### 标准行为

**加载开始时**：
- 显示加载指示器
- 禁用用户交互
- 保持组件尺寸
- 隐藏或遮罩内容

**加载进行中**：
- 持续显示动画效果
- 更新进度（如果可计算）
- 保持用户等待状态

**加载完成后**：
- 移除加载指示器
- 恢复正常交互
- 显示加载内容或错误
- 通知用户加载完成

### 交互限制

| 交互类型 | 加载中行为 | 说明 |
|---------|----------|------|
| 鼠标点击 | 无效 | 防止重复提交 |
| 键盘操作 | 禁用 | Enter/Space无效 |
| 触摸操作 | 无效 | 移动端点击无效 |
| 焦点管理 | 保持 | 不移除当前焦点 |

---

## ♿ 无障碍要求

### ARIA属性

**1. 基本属性**

```html
<button
  class="button is-loading"
  aria-busy="true"
  aria-live="polite"
>
  <span class="sr-only">加载中...</span>
  <span>保存</span>
</button>
```

**关键属性**：
- `aria-busy="true"`：表示元素正在加载
- `aria-live="polite"`：状态变化时通知屏幕阅读器
- `sr-only`：屏幕阅读器专用文字

**2. 进度条**

```html
<div
  role="progressbar"
  aria-valuenow="60"
  aria-valuemin="0"
  aria-valuemax="100"
  aria-label="文件上传进度"
>
  <div class="progress-bar" style="width: 60%"></div>
</div>
```

**关键属性**：
- `role="progressbar"`：标识为进度条
- `aria-valuenow`：当前进度值
- `aria-valuemin/max`：进度范围
- `aria-label`：进度描述

**3. 骨架屏**

```html
<div aria-busy="true" aria-live="polite">
  <div class="skeleton" aria-hidden="true"></div>
  <div class="skeleton" aria-hidden="true"></div>
  <span class="sr-only">正在加载内容...</span>
</div>
```

### 无障碍最佳实践

**✅ DO（推荐）**：
1. 使用 `aria-busy="true"` 标记加载状态
2. 提供屏幕阅读器文字提示
3. 加载完成后通知状态变化
4. 进度可计算时提供具体数值

**❌ DON'T（避免）**：
1. 加载指示器过小或对比度不足
2. 没有屏幕阅读器文字提示
3. 加载时间过短（< 500ms）导致闪烁
4. 不通知用户加载完成

---

## 📋 加载模式详解

### 1. 旋转圆环（Spinner）

**适用场景**：
- 按钮、小组件加载
- 不确定加载时间
- 空间有限的场景

**优点**：
- 轻量级，实现简单
- 通用性强，用户熟悉
- 不占用过多空间

**缺点**：
- 不显示具体进度
- 长时间加载让用户焦虑

```css
.spinner {
  display: inline-block;
  width: 20px;
  height: 20px;
  border: 2px solid currentColor;
  border-radius: 50%;
  border-right-color: transparent;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

```html
<button class="button is-loading">
  <span class="spinner" aria-hidden="true"></span>
  <span class="sr-only">加载中...</span>
  <span>保存</span>
</button>
```

### 2. 进度条

**适用场景**：
- 文件上传/下载
- 长时间任务处理
- 可计算进度的操作

**优点**：
- 显示具体进度百分比
- 用户明确知道剩余时间
- 减少等待焦虑

**缺点**：
- 需要知道总进度
- 实现相对复杂

```css
.progress {
  height: 6px;
  background: var(--color-bg-progress);
  border-radius: var(--radius-full);
  overflow: hidden;
}

.progress-bar {
  height: 100%;
  background: var(--color-primary);
  transition: width 0.3s ease;
}

.progress-text {
  font-size: var(--font-size-sm);
  color: var(--color-text-muted);
  margin-top: var(--spacing-xs);
}
```

```html
<div role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" aria-label="上传进度">
  <div class="progress">
    <div class="progress-bar" style="width: 60%"></div>
  </div>
  <div class="progress-text">60%</div>
</div>
```

### 3. 骨架屏

**适用场景**：
- 列表、卡片、feed加载
- 保持布局结构
- 内容结构固定的场景

**优点**：
- 保持布局结构稳定
- 提供更好的视觉连续性
- 用户感知加载更快

**缺点**：
- 实现相对复杂
- 需要预知内容结构

```css
.skeleton-card {
  padding: var(--spacing-md);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
}

.skeleton-avatar {
  width: 40px;
  height: 40px;
  border-radius: var(--radius-full);
  background: var(--color-skeleton);
  animation: shimmer 1.5s infinite;
}

.skeleton-title {
  height: 20px;
  width: 60%;
  background: var(--color-skeleton);
  border-radius: var(--radius-sm);
  animation: shimmer 1.5s infinite;
  animation-delay: 0.1s;
}

.skeleton-text {
  height: 14px;
  width: 80%;
  background: var(--color-skeleton);
  border-radius: var(--radius-sm);
  animation: shimmer 1.5s infinite;
  animation-delay: 0.2s;
}
```

```html
<div aria-busy="true" aria-live="polite">
  <div class="skeleton-card">
    <div class="skeleton-avatar" aria-hidden="true"></div>
    <div class="skeleton-title" aria-hidden="true"></div>
    <div class="skeleton-text" aria-hidden="true"></div>
  </div>
  <span class="sr-only">正在加载用户信息...</span>
</div>
```

### 4. 模糊+覆盖层

**适用场景**：
- 模态框、对话框加载
- 页面级加载
- 需要明确区域划分

**优点**：
- 明确的区域划分
- 阻塞用户操作
- 视觉焦点突出

**缺点**：
- 阻塞用户所有操作
- 长时间加载体验差

```css
.overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(2px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
}
```

```html
<div style="position: relative;">
  <div class="content">
    <!-- 内容 -->
  </div>

  <div class="overlay" aria-busy="true" aria-live="polite">
    <div class="spinner" aria-hidden="true"></div>
    <span class="sr-only">正在加载...</span>
  </div>
</div>
```

---

## 📊 加载模式对比

| 模式 | 适用场景 | 优点 | 缺点 | 推荐度 |
|------|----------|------|------|--------|
| **旋转圆环** | 按钮、小组件 | 轻量、通用 | 不显示进度 | ⭐⭐⭐⭐⭐ |
| **进度条** | 文件上传 | 显示进度 | 需要知道总量 | ⭐⭐⭐⭐☆ |
| **骨架屏** | 列表、卡片 | 保持布局 | 实现复杂 | ⭐⭐⭐⭐⭐ |
| **模糊覆盖** | 模态框 | 区域明确 | 阻塞操作 | ⭐⭐⭐☆☆ |

---

## 🎯 最佳实践

### 1. 加载时长控制

**短时间加载（< 500ms）**
- 不显示加载状态
- 避免视觉闪烁
- 直接显示结果

**中等时长（500ms - 2s）**
- 显示加载指示器
- 不必显示具体进度
- 使用旋转圆环

**长时间加载（> 2s）**
- 显示具体进度
- 提供预估时间
- 考虑添加取消选项

**超长加载（> 10s）**
- 必须提供进度
- 必须提供取消按钮
- 定期更新状态

### 2. 避免闪烁

**问题**：加载时间过短导致加载指示器一闪而过

**解决方案**：
```javascript
// 添加最小显示时间
function showLoading(minDuration = 500) {
  const startTime = Date.now();
  const loadingIndicator = document.querySelector('.loading');

  return {
    hide: () => {
      const elapsed = Date.now() - startTime;
      const remaining = Math.max(0, minDuration - elapsed);

      setTimeout(() => {
        loadingIndicator.style.display = 'none';
      }, remaining);
    }
  };
}

// 使用
const loading = showLoading();
await fetchData();
loading.hide();
```

### 3. 提供超时处理

```javascript
async function loadDataWithTimeout(url, timeout = 10000) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeout);

  try {
    const response = await fetch(url, {
      signal: controller.signal
    });
    clearTimeout(timeoutId);
    return await response.json();
  } catch (error) {
    if (error.name === 'AbortError') {
      throw new Error('加载超时，请重试');
    }
    throw error;
  }
}
```

### 4. 渐进式加载

```javascript
// 先显示关键内容，再加载次要内容
async function loadPage() {
  // 1. 立即显示骨架屏
  showSkeleton();

  // 2. 加载关键内容
  const criticalData = await loadCriticalData();
  renderCriticalData(criticalData);

  // 3. 加载次要内容
  const secondaryData = await loadSecondaryData();
  renderSecondaryData(secondaryData);
}
```

---

## ⚠️ 常见问题

### ❌ 避免

1. **加载时间过短（< 500ms）导致闪烁**
   - 用户来不及看清
   - 造成视觉干扰
   - 体验不佳

2. **加载指示器过小或对比度不足**
   - 用户难以察觉
   - 不符合WCAG对比度标准
   - 可访问性差

3. **没有屏幕阅读器文字提示**
   - 盲屏用户不知道状态
   - 无障碍体验差
   - 不符合ARIA标准

4. **长时间加载无取消选项**
   - 用户无法中断
   - 造成等待焦虑
   - 体验差

### ✅ 推荐

1. **设置最小显示时间（500ms）**
   - 避免闪烁
   - 确保用户看清
   - 体验平滑

2. **加载指示器至少16×16px**
   - 确保可见性
   - 符合WCAG标准
   - 对比度足够

3. **提供加载进度或预估时间**
   - 减少等待焦虑
   - 用户有预期
   - 体验更好

4. **加载超时（> 10s）提供取消选项**
   - 用户可控制
   - 避免长时间等待
   - 尊重用户选择

---

## 📊 实现示例

### 示例1：按钮加载状态

```tsx
function SubmitButton() {
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async () => {
    setIsSubmitting(true);
    try {
      await submitForm();
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <button
      onClick={handleSubmit}
      disabled={isSubmitting}
      aria-busy={isSubmitting}
      aria-live="polite"
      className={`button ${isSubmitting ? 'is-loading' : ''}`}
    >
      {isSubmitting ? (
        <>
          <span className="sr-only">提交中...</span>
          <span>保存</span>
        </>
      ) : (
        '提交'
      )}
    </button>
  );
}
```

### 示例2：骨架屏加载

```tsx
function UserList() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadUsers().then(data => {
      setUsers(data);
      setLoading(false);
    });
  }, []);

  if (loading) {
    return (
      <div aria-busy="true" aria-live="polite">
        {[1, 2, 3].map(i => (
          <div key={i} className="skeleton-card">
            <div className="skeleton-avatar" aria-hidden="true" />
            <div className="skeleton-title" aria-hidden="true" />
            <div className="skeleton-text" aria-hidden="true" />
          </div>
        ))}
        <span className="sr-only">正在加载用户列表...</span>
      </div>
    );
  }

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>
          <img src={user.avatar} alt="" />
          <h3>{user.name}</h3>
        </li>
      ))}
    </ul>
  );
}
```

### 示例3：进度条上传

```tsx
function FileUpload() {
  const [progress, setProgress] = useState(0);
  const [uploading, setUploading] = useState(false);

  const handleUpload = async (file) => {
    setUploading(true);
    setProgress(0);

    try {
      await uploadFile(file, (progress) => {
        setProgress(progress);
      });
    } finally {
      setUploading(false);
    }
  };

  return (
    <div>
      <input
        type="file"
        onChange={(e) => handleUpload(e.target.files[0])}
        disabled={uploading}
      />

      {uploading && (
        <div
          role="progressbar"
          aria-valuenow={progress}
          aria-valuemin="0"
          aria-valuemax="100"
          aria-label="文件上传进度"
        >
          <div className="progress">
            <div
              className="progress-bar"
              style={{ width: `${progress}%` }}
            />
          </div>
          <div className="progress-text">{progress}%</div>
        </div>
      )}
    </div>
  );
}
```

---

## 🔗 相关文档

- [功能状态详解](./component-states-functional.md) - 功能状态总览
- [Disabled状态详解](./component-states-disabled.md) - 禁用状态规范
- [Empty & Error状态详解](./component-states-empty-error.md) - 空/错误状态规范
- [性能优化 - 渲染优化](./performance-rendering.md) - 加载性能最佳实践

---

> **状态**: ✅ DONE
> **最后更新**: 2026-01-04 (从component-states-functional.md拆分)
> **维护者**: 项目团队
