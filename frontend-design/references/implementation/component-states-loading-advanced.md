# Loading状态 - 高级加载模式

> ⚙️ **Advanced Loading Patterns** - 骨架屏、覆盖层、实用技巧

---

## 📖 文档说明

本文档提供 2 种高级加载模式和实用技巧的完整实现代码和详细说明。

**相关文档**：
- [基础加载模式](component-states-loading-patterns.md) - 旋转圆环、进度条
- [返回主文档](component-states-loading.md)
- [视觉描述与交互设计](component-states-loading-visual.md)

---

## 📋 高级加载模式

### 3. 骨架屏（Skeleton Screen）

**适用场景**：
- 内容列表加载
- 图片预加载
- 内容结构已知的场景
- 社交媒体应用

**优点**：
- 提供内容预览
- 减少感知加载时间
- 优雅的加载体验

**缺点**：
- 实现相对复杂
- 需要了解内容结构
- 长时间加载体验差

#### 完整实现

**CSS**：
```css
.skeleton {
  background: var(--color-skeleton-start);
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

**React 实现**：
```tsx
function SkeletonCard() {
  return (
    <div className="skeleton-card" aria-busy="true" aria-live="polite">
      <div className="skeleton-avatar" aria-hidden="true" />
      <div className="skeleton-content">
        <div className="skeleton-title" aria-hidden="true" />
        <div className="skeleton-text" aria-hidden="true" />
        <div className="skeleton-text" aria-hidden="true" />
      </div>
      <span className="sr-only">正在加载用户信息...</span>
    </div>
  );
}

// 使用示例
function UserList() {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchUsers().then(data => {
      setUsers(data);
      setLoading(false);
    });
  }, []);

  if (loading) {
    return Array.from({ length: 5 }).map((_, i) => (
      <SkeletonCard key={i} />
    ));
  }

  return users.map(user => <UserCard key={user.id} user={user} />);
}
```

**Vue 实现**：
```vue
<template>
  <div v-if="loading" class="skeleton-card" aria-busy="true" aria-live="polite">
    <div class="skeleton-avatar" aria-hidden="true" />
    <div class="skeleton-content">
      <div class="skeleton-title" aria-hidden="true" />
      <div class="skeleton-text" aria-hidden="true" />
      <div class="skeleton-text" aria-hidden="true" />
    </div>
    <span class="sr-only">正在加载用户信息...</span>
  </div>

  <div v-else>
    <!-- 实际内容 -->
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

const loading = ref(true);

onMounted(async () => {
  await fetchData();
  loading.value = false;
});
</script>
```

---

### 4. 覆盖层（Overlay）

**适用场景**：
- 模态框加载
- 页面级加载
- 阻塞式操作
- 需要阻止用户交互

**优点**：
- 明确的加载状态
- 防止重复操作
- 视觉焦点集中

**缺点**：
- 阻塞用户操作
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
        <div className="modal__overlay" aria-busy="true" aria-live="polite">
          <div className="spinner" aria-hidden="true" />
          <span className="sr-only">正在保存...</span>
        </div>
      )}
    </div>
  );
}
```

**Vue 模态框加载**：
```vue
<template>
  <div class="modal">
    <div class="modal__content">
      <h2>用户设置</h2>
      <form>
        <!-- 表单字段 -->
      </form>
    </div>

    <div v-if="loading" class="modal__overlay" aria-busy="true" aria-live="polite">
      <div class="spinner" aria-hidden="true" />
      <span class="sr-only">正在保存...</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const loading = ref(false);

const handleSave = async () => {
  loading.value = true;
  try {
    await saveSettings();
  } finally {
    loading.value = false;
  }
};
</script>
```

---

## 🛠️ 实用技巧

### 示例1：最小加载时间

避免加载闪烁，确保用户能看到加载状态。

```javascript
function showLoading(minDuration = 500) {
  const startTime = Date.now();
  let isHidden = false;

  function hide() {
    if (isHidden) return;

    const elapsed = Date.now() - startTime;
    const remaining = Math.max(0, minDuration - elapsed);

    setTimeout(() => {
      isHidden = true;
      // 隐藏加载指示器
    }, remaining);
  }

  return { hide };
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

### 示例4：错误重试

```javascript
async function loadDataWithRetry(url, maxRetries = 3) {
  let lastError;

  for (let i = 0; i < maxRetries; i++) {
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }
      return await response.json();
    } catch (error) {
      lastError = error;

      // 最后一次重试失败
      if (i === maxRetries - 1) {
        throw new Error(`加载失败，已重试 ${maxRetries} 次`);
      }

      // 等待后重试
      await new Promise(resolve => setTimeout(resolve, 1000 * (i + 1)));
    }
  }
}
```

---

## 🔗 相关文档

- [基础加载模式](component-states-loading-patterns.md) - 旋转圆环、进度条
- [返回主文档](component-states-loading.md)
- [视觉描述与交互设计](component-states-loading-visual.md)

---

## 🔗 快速导航

- [返回implementation/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.1 (拆分版)
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
