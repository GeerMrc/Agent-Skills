# Loading状态 - 加载模式与实现

> ⚙️ **4种加载模式详解** - 完整实现代码和示例

---

## 📖 文档说明

本文档提供 4 种常用加载模式的完整实现代码和详细说明。

**相关文档**：
- [返回主文档](component-states-loading.md)
- [视觉描述与交互设计](component-states-loading-visual.md)

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

#### 完整实现

**CSS**：
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

/* 响应式尺寸 */
.spinner--sm { width: 16px; height: 16px; }
.spinner--md { width: 20px; height: 20px; }
.spinner--lg { width: 32px; height: 32px; }
.spinner--xl { width: 48px; height: 48px; }

/* 尊重用户动画偏好 */
@media (prefers-reduced-motion: reduce) {
  .spinner {
    animation: none;
    border-top-color: transparent;
    border-right-color: transparent;
    border-bottom-color: transparent;
  }
}
```

**HTML**：
```html
<button class="button is-loading"
        aria-busy="true"
        aria-live="polite">
  <span class="spinner" aria-hidden="true"></span>
  <span class="sr-only">加载中...</span>
  <span>保存</span>
</button>
```

**React 实现**：
```tsx
function LoadingButton() {
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try {
      await submitData();
    } finally {
      setLoading(false);
    }
  };

  return (
    <button
      onClick={handleClick}
      disabled={loading}
      aria-busy={loading}
      className={`button ${loading ? 'is-loading' : ''}`}
    >
      {loading ? (
        <>
          <span className="spinner" aria-hidden="true" />
          <span className="sr-only">提交中...</span>
        </>
      ) : (
        '提交'
      )}
    </button>
  );
}
```

---

### 2. 进度条（Progress Bar）

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

#### 完整实现

**CSS**：
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
  animation: progress-pulse 1.5s infinite;
}

@keyframes progress-pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.7; }
}

.progress-text {
  font-size: var(--font-size-sm);
  color: var(--color-text-muted);
  margin-top: var(--spacing-xs);
  text-align: center;
}

/* 不同颜色状态 */
.progress-bar--primary { background: var(--color-primary); }
.progress-bar--success { background: var(--color-success); }
.progress-bar--warning { background: var(--color-warning); }
.progress-bar--danger { background: var(--color-danger); }
```

**HTML**：
```html
<div role="progressbar"
     aria-valuenow="60"
     aria-valuemin="0"
     aria-valuemax="100"
     aria-label="上传进度">
  <div class="progress">
    <div class="progress-bar progress-bar--primary" style="width: 60%"></div>
  </div>
  <div class="progress-text">60%</div>
</div>
```

**JavaScript 实现**：
```javascript
class ProgressBar {
  constructor(element, options = {}) {
    this.element = element;
    this.min = options.min || 0;
    this.max = options.max || 100;
    this.value = options.value || 0;
    this.update();
  }

  set(value) {
    this.value = Math.min(Math.max(value, this.min), this.max);
    this.update();
    this.element.setAttribute('aria-valuenow', this.value);
  }

  update() {
    const percent = ((this.value - this.min) / (this.max - this.min)) * 100;
    const bar = this.element.querySelector('.progress-bar');
    const text = this.element.querySelector('.progress-text');

    bar.style.width = `${percent}%`;
    if (text) {
      text.textContent = `${Math.round(percent)}%`;
    }
  }
}

// 使用
const progress = new ProgressBar(document.querySelector('#progress'));
progress.set(60); // 设置为60%
```

**React 上传组件**：
```tsx
function FileUpload() {
  const [progress, setProgress] = useState(0);
  const [uploading, setUploading] = useState(false);

  const handleUpload = async (file: File) => {
    setUploading(true);

    const xhr = new XMLHttpRequest();
    xhr.upload.addEventListener('progress', (e) => {
      if (e.lengthComputable) {
        const percent = (e.loaded / e.total) * 100;
        setProgress(percent);
      }
    });

    xhr.addEventListener('load', () => {
      setUploading(false);
      setProgress(100);
    });

    xhr.open('POST', '/upload');
    xhr.send(new FormData(file));
  };

  return (
    <div>
      <input
        type="file"
        onChange={(e) => {
          const file = e.target.files?.[0];
          if (file) handleUpload(file);
        }}
        disabled={uploading}
      />

      {uploading && (
        <div
          role="progressbar"
          aria-valuenow={progress}
          aria-valuemin={0}
          aria-valuemax={100}
          aria-label="文件上传进度"
        >
          <div className="progress">
            <div
              className="progress-bar"
              style={{ width: `${progress}%` }}
            />
          </div>
          <div className="progress-text">{Math.round(progress)}%</div>
        </div>
      )}
    </div>
  );
}
```

---

### 3. 骨架屏（Skeleton Screen）

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

#### 完整实现

**CSS**：
```css
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

/* 卡片骨架 */
.skeleton-card {
  padding: var(--spacing-md);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  display: flex;
  gap: var(--spacing-md);
}

.skeleton-avatar {
  width: 40px;
  height: 40px;
  border-radius: var(--radius-full);
  flex-shrink: 0;
  background: var(--color-skeleton);
  animation: shimmer 1.5s infinite;
}

.skeleton-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: var(--spacing-sm);
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

.skeleton-text:last-child {
  width: 60%;
}
```

**HTML**：
```html
<div aria-busy="true" aria-live="polite">
  <!-- 骨架屏 -->
  <div class="skeleton-card">
    <div class="skeleton-avatar" aria-hidden="true"></div>
    <div class="skeleton-content">
      <div class="skeleton-title" aria-hidden="true"></div>
      <div class="skeleton-text" aria-hidden="true"></div>
      <div class="skeleton-text" aria-hidden="true"></div>
    </div>
  </div>

  <!-- 屏幕阅读器提示 -->
  <span class="sr-only">正在加载用户信息...</span>
</div>
```

**React 列表骨架**：
```tsx
function UserListSkeleton() {
  return (
    <div aria-busy="true" aria-live="polite">
      {Array.from({ length: 5 }).map((_, i) => (
        <div key={i} className="skeleton-card">
          <div className="skeleton-avatar" aria-hidden="true" />
          <div className="skeleton-content">
            <div className="skeleton-title" aria-hidden="true" />
            <div className="skeleton-text" aria-hidden="true" />
            <div className="skeleton-text" aria-hidden="true" />
          </div>
        </div>
      ))}
      <span className="sr-only">正在加载用户列表...</span>
    </div>
  );
}

function UserList() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchUsers()
      .then(data => {
        setUsers(data);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <UserListSkeleton />;
  }

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>
          <img src={user.avatar} alt="" />
          <h3>{user.name}</h3>
          <p>{user.email}</p>
        </li>
      ))}
    </ul>
  );
}
```

---

### 4. 模糊覆盖层（Overlay）

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

#### 完整实现

**CSS**：
```css
.overlay-container {
  position: relative;
}

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

/* 深色主题 */
@media (prefers-color-scheme: dark) {
  .overlay {
    background: rgba(0, 0, 0, 0.8);
  }
}

.overlay__spinner {
  width: 32px;
  height: 32px;
  border: 3px solid currentColor;
  border-radius: 50%;
  border-right-color: transparent;
  animation: spin 0.6s linear infinite;
}
```

**HTML**：
```html
<div class="overlay-container">
  <!-- 内容区域 -->
  <div class="content">
    <h2>用户设置</h2>
    <form>
      <!-- 表单内容 -->
    </form>
  </div>

  <!-- 覆盖层 -->
  <div class="overlay" aria-busy="true" aria-live="polite">
    <div class="overlay__spinner" aria-hidden="true"></div>
    <span class="sr-only">正在加载...</span>
  </div>
</div>
```

**React 模态框加载**：
```tsx
function SettingsModal() {
  const [loading, setLoading] = useState(false);

  const handleSave = async () => {
    setLoading(true);
    try {
      await saveSettings();
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="modal">
      <div className="modal__content">
        <h2>用户设置</h2>
        <form>
          {/* 表单字段 */}
        </form>
      </div>

      {loading && (
        <div
          className="modal__overlay"
          aria-busy="true"
          aria-live="polite"
        >
          <div className="spinner" aria-hidden="true" />
          <span className="sr-only">正在保存设置...</span>
        </div>
      )}
    </div>
  );
}
```

---

## 📊 实现示例

### 示例1：带最小显示时间的加载

```javascript
// 避免闪烁的最小显示时间
function showLoading(minDuration = 500) {
  const startTime = Date.now();
  const loadingIndicator = document.querySelector('.loading');

  loadingIndicator.style.display = 'block';

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

// 使用示例
async function loadData() {
  const loading = showLoading(500);

  try {
    const data = await fetch(url);
    return await data.json();
  } finally {
    loading.hide();
  }
}
```

### 示例2：超时处理加载

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

// 使用
loadDataWithTimeout('/api/data', 5000)
  .then(data => console.log(data))
  .catch(error => console.error(error.message));
```

### 示例3：渐进式加载

```javascript
async function loadProgressiveData() {
  // 1. 立即显示骨架屏
  showSkeleton();

  // 2. 加载关键数据（优先级高）
  const critical = await fetchCriticalData();
  renderCriticalData(critical);
  hideSkeleton();

  // 3. 加载次要数据（后台加载）
  fetchSecondaryData().then(secondary => {
    renderSecondaryData(secondary);
  });

  // 4. 加载增强数据（低优先级）
  fetchEnhancementData().then(enhancement => {
    renderEnhancementData(enhancement);
  });
}
```

---

## 🔗 相关文档

- [返回主文档](component-states-loading.md)
- [视觉描述与交互设计](component-states-loading-visual.md)
- [组件状态总览](component-states.md)

---

> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills 项目团队
