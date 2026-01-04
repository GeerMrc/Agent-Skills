# Empty & Error状态详解

> 📭 ⚠️ **空状态与错误状态** - 数据缺失与异常处理的视觉反馈规范

---

## 📖 状态概述

### Empty（空状态）

组件/区域没有内容时的友好提示，引导用户进行下一步操作。

**适用场景**：
- 列表/表格无数据
- 搜索无结果
- 筛选后无匹配项
- 用户首次使用

### Error（错误状态）

组件出现验证错误、系统错误时的视觉反馈，明确告知用户问题所在。

**适用场景**：
- 表单字段验证失败
- 网络请求失败
- 权限不足
- 服务器错误

---

## 📭 Empty状态详解

### 视觉设计

**设计规范**：
```css
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-xl);
  text-align: center;
  color: var(--color-text-muted);
  min-height: 300px;
}

.empty-state-icon {
  font-size: 3rem;
  margin-bottom: var(--spacing-md);
  opacity: 0.5;
}

.empty-state-title {
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-semibold);
  margin-bottom: var(--spacing-sm);
  color: var(--color-text);
}

.empty-state-description {
  font-size: var(--font-size-sm);
  max-width: 400px;
  line-height: 1.5;
  margin-bottom: var(--spacing-md);
}

.empty-state-action {
  margin-top: var(--spacing-sm);
}
```

**设计要点**：
1. **插图/图标**：大尺寸（3-4rem），降低透明度
2. **标题**：描述性文字，告知用户当前状态
3. **说明**：友好的解释文字，告知原因
4. **操作建议**：明确的CTA按钮或链接

### 内容要求

**完整结构**：
- 清晰的插图或图标（📭、📂、🔍等）
- 描述性标题（"暂无消息"、"没有找到结果"）
- 友好的说明文字（解释原因或提供帮助）
- 明确的操作建议（"发送消息"、"清除筛选"）

**内容示例**：
```html
<div class="empty-state" role="status">
  <div class="empty-state-icon" aria-hidden="true">📭</div>
  <h3 class="empty-state-title">暂无消息</h3>
  <p class="empty-state-description">
    您还没有收到任何消息。当有新消息时，它们会显示在这里。
  </p>
  <div class="empty-state-action">
    <button>发送消息</button>
  </div>
</div>
```

### 空状态类型

| 类型 | 场景 | 标题示例 | 操作建议 |
|------|------|----------|----------|
| **首次使用** | 新用户，无数据 | "开始创建您的第一个项目" | "创建项目" |
| **清空状态** | 用户删除所有内容 | "列表已清空" | "添加新项目" |
| **搜索无结果** | 搜索/筛选后无匹配 | "没有找到结果" | "清除筛选" |
| **权限不足** | 无权限查看内容 | "您没有权限访问此内容" | "联系管理员" |
| **网络错误** | 加载失败 | "加载失败" | "重试" |
| **功能未开放** | 功能未上线 | "功能即将上线" | "了解更多" |

### 交互行为

- 提供可操作的按钮
- 引导用户到下一步
- 避免让用户感到困惑
- 保持界面布局稳定

### 无障碍要求

**关键ARIA属性**：
```html
<div class="empty-state" role="status">
  <div class="empty-state-icon" aria-hidden="true">📭</div>
  <h3 class="empty-state-title">暂无消息</h3>
  <p class="empty-state-description">
    您还没有收到任何消息。
  </p>
  <div class="empty-state-action">
    <button>发送消息</button>
  </div>
</div>
```

- `role="status"` 或 `aria-live="polite"`：通知屏幕阅读器
- `aria-hidden="true"`：装饰性图标隐藏
- 操作按钮标准无障碍：确保可访问
- 语义化HTML：使用 `<h3>`、`<p>` 等标签

### Empty状态示例

**示例1：首次使用空状态**
```html
<div class="empty-state" role="status">
  <svg class="empty-state-icon" aria-hidden="true">
    <!-- 插图SVG -->
  </svg>
  <h3 class="empty-state-title">开始您的第一个项目</h3>
  <p class="empty-state-description">
    项目是组织您工作的好方法。创建第一个项目，开始您的工作之旅。
  </p>
  <div class="empty-state-action">
    <button type="button">创建项目</button>
  </div>
</div>
```

**示例2：搜索无结果**
```html
<div class="empty-state" role="status">
  <div class="empty-state-icon" aria-hidden="true">🔍</div>
  <h3 class="empty-state-title">没有找到结果</h3>
  <p class="empty-state-description">
    没有找到与"<span id="search-term">关键词</span>"匹配的结果。
  </p>
  <div class="empty-state-action">
    <button type="button">清除筛选</button>
    <button type="button" variant="secondary">查看全部内容</button>
  </div>
</div>
```

**示例3：网络错误空状态**
```html
<div class="empty-state" role="alert">
  <div class="empty-state-icon" aria-hidden="true">⚠️</div>
  <h3 class="empty-state-title">加载失败</h3>
  <p class="empty-state-description">
    网络连接出现问题，无法加载内容。
  </p>
  <div class="empty-state-action">
    <button type="button">重试</button>
  </div>
</div>
```

---

## ⚠️ Error状态详解

### 视觉设计

**设计规范**：
```css
.input.is-error {
  border-color: var(--color-error);
  background: var(--color-error-bg);
}

.input.is-error:focus-visible {
  outline-color: var(--color-error);
  box-shadow: 0 0 0 3px var(--color-error-alpha);
}

.error-message {
  display: flex;
  align-items: center;
  gap: var(--spacing-xs);
  color: var(--color-error);
  font-size: var(--font-size-sm);
  margin-top: var(--spacing-xs);
}

.error-message::before {
  content: "⚠️";
  font-size: 1.2em;
}

/* 内联错误 */
.input-wrapper {
  position: relative;
}

.input-wrapper .error-icon {
  position: absolute;
  right: var(--spacing-sm);
  top: 50%;
  transform: translateY(-50%);
  color: var(--color-error);
}

/* Toast错误通知 */
.toast-error {
  background: var(--color-error);
  color: white;
  padding: var(--spacing-md);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
}
```

**设计要点**：
- **颜色**：使用红色系传达"错误"
- **图标**：⚠️、❌、✕ 等警告图标
- **位置**：靠近错误字段（内联或下方）
- **对比度**：确保错误信息清晰可见

### 内容要求

**错误消息四要素**：
1. **明确的问题**：什么出错
2. **具体的位置**：哪里出错
3. **建议的解决方案**：如何修复
4. **视觉强调**：错误图标或颜色

**错误消息示例**：
- ❌ "输入无效"
- ✅ "邮箱地址格式不正确，请包含@符号"

- ❌ "错误"
- ✅ "密码长度至少8位，当前6位"

### 交互行为

- 错误字段自动聚焦
- 错误消息清晰可见
- 提供修复建议
- 错误解除后移除提示

### 无障碍要求

**关键ARIA属性**：
```html
<div class="form-field">
  <label for="email">邮箱地址</label>
  <div class="input-wrapper">
    <input
      type="email"
      id="email"
      class="input is-error"
      aria-invalid="true"
      aria-describedby="email-error"
      aria-required="true"
    />
    <span class="error-icon" aria-hidden="true">⚠️</span>
  </div>
  <div id="email-error" class="error-message" role="alert">
    请输入有效的邮箱地址
  </div>
</div>
```

- `aria-invalid="true"`：标记错误字段
- `aria-describedby`：关联错误消息与表单字段
- `role="alert"` 或 `aria-live="assertive"`：立即通知
- 自动聚焦：错误字段自动获得焦点

### 错误消息最佳实践

**1. 明确具体**
- ❌ "输入无效"
- ✅ "邮箱地址格式不正确，请包含@符号"

**2. 提供解决方案**
- ❌ "错误"
- ✅ "密码长度至少8位，当前6位"

**3. 避免技术术语**
- ❌ "404 Not Found"
- ✅ "页面不存在，可能已被删除"

**4. 保持友好语气**
- ❌ "您输入了错误的数据"
- ✅ "请检查您的输入"

### 错误状态场景

| 场景 | 错误类型 | 消息示例 | 解决方案 |
|------|----------|----------|----------|
| **表单验证** | 字段错误 | "邮箱地址格式不正确" | 提供格式示例 |
| **网络请求** | API错误 | "网络连接失败" | 提供重试按钮 |
| **权限不足** | 403错误 | "您没有权限访问" | 联系管理员 |
| **资源不存在** | 404错误 | "页面不存在" | 返回首页 |
| **服务器错误** | 500错误 | "服务器出现问题" | 稍后重试 |

### Error状态示例

**示例1：表单字段错误**
```html
<div class="form-field">
  <label for="email">
    邮箱地址
    <span aria-hidden="true" class="required">*</span>
    <span class="sr-only">(必填)</span>
  </label>

  <div class="input-wrapper">
    <input
      type="email"
      id="email"
      name="email"
      class="input is-error"
      aria-invalid="true"
      aria-describedby="email-error"
      aria-required="true"
      placeholder="your@example.com"
    />
    <span class="error-icon" aria-hidden="true">⚠️</span>
  </div>

  <div id="email-error" class="error-message" role="alert">
    请输入有效的邮箱地址，例如：your@example.com
  </div>
</div>
```

**示例2：多个错误摘要**
```html
<ul class="error-summary" role="alert" aria-labelledby="error-title">
  <li id="error-title">表单提交失败，请修正以下问题：</li>
  <li>
    <a href="#field-email">邮箱地址格式不正确</a>
  </li>
  <li>
    <a href="#field-password">密码长度至少8位</a>
  </li>
  <li>
    <a href="#field-phone">手机号码格式不正确</a>
  </li>
</ul>
```

**示例3：Toast错误通知**
```html
<div class="toast toast-error" role="alert" aria-live="assertive">
  <span aria-hidden="true" class="toast-icon">⚠️</span>
  <div class="toast-content">
    <strong>网络连接失败</strong>
    <p>请检查您的网络设置后重试</p>
  </div>
  <button aria-label="关闭通知" class="toast-close">×</button>
</div>
```

**示例4：全局错误页面**
```html
<div class="error-page" role="alert">
  <div class="error-illustration" aria-hidden="true">
    <!-- 错误插图 -->
  </div>

  <h1 class="error-title">页面不存在</h1>

  <p class="error-description">
    您访问的页面可能已被删除或移动。
  </p>

  <div class="error-actions">
    <button type="button" onclick="history.back()">
      返回上一页
    </button>
    <a href="/" variant="secondary">
      返回首页
    </a>
  </div>
</div>
```

---

## 🎯 Empty & Error最佳实践

### Empty状态最佳实践

**✅ DO（推荐）**：
1. 插图/图标 + 标题 + 说明 + CTA按钮
2. 友好的用户语言，避免技术术语
3. 提供明确的下一步操作
4. 保持与品牌风格一致的视觉设计

**❌ DON'T（避免）**：
1. 空状态只有文字，无视觉吸引力
2. 不提供操作建议，用户不知如何继续
3. 使用技术术语（"空数据"、"null"）
4. 空状态设计过于简单，缺乏情感连接

### Error状态最佳实践

**✅ DO（推荐）**：
1. 具体的错误描述
2. 提供修复建议
3. 错误字段自动聚焦
4. 错误消息使用 `role="alert"`

**❌ DON'T（避免）**：
1. 错误消息过于模糊（"错误"、"无效"）
2. 使用技术术语（"400 Bad Request"）
3. 错误消息远离错误字段
4. 错误颜色对比度不足

---

## 📊 实现示例

### 示例1：数据列表状态切换

```tsx
function DataList() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchData()
      .then(setData)
      .catch(setError)
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return <SkeletonLoader aria-busy="true" />;
  }

  if (error) {
    return (
      <EmptyState
        role="alert"
        icon="⚠️"
        title="加载失败"
        description={error.message}
        action={<button onClick={retry}>重试</button>}
      />
    );
  }

  if (data.length === 0) {
    return (
      <EmptyState
        role="status"
        icon="📭"
        title="暂无数据"
        description="还没有任何内容"
        action={<button>创建新项目</button>}
      />
    );
  }

  return (
    <ul>
      {data.map(item => (
        <li key={item.id}>{item.name}</li>
      ))}
    </ul>
  );
}
```

### 示例2：搜索输入状态

```tsx
function SearchInput() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [searching, setSearching] = useState(false);

  const handleSearch = async (q) => {
    setQuery(q);
    if (!q.trim()) {
      setResults([]);
      return;
    }

    setSearching(true);
    try {
      const data = await searchAPI(q);
      setResults(data);
    } finally {
      setSearching(false);
    }
  };

  const hasQuery = query.trim().length > 0;
  const hasNoResults = hasQuery && results.length === 0;

  return (
    <div>
      <input
        type="search"
        value={query}
        onChange={(e) => handleSearch(e.target.value)}
        aria-busy={searching}
        placeholder="搜索..."
      />

      {searching && <Spinner aria-hidden="true" />}

      {hasNoResults && (
        <EmptyState
          role="status"
          icon="🔍"
          title="没有找到结果"
          description={`没有找到与"${query}"匹配的结果`}
          action={
            <button onClick={() => setQuery('')}>
              清除搜索
            </button>
          }
        />
      )}

      {!hasNoResults && results.length > 0 && (
        <ul>
          {results.map(r => (
            <li key={r.id}>{r.name}</li>
          ))}
        </ul>
      )}
    </div>
  );
}
```

### 示例3：表单验证错误

```tsx
function LoginForm() {
  const [errors, setErrors] = useState({});
  const [isSubmitting, setIsSubmitting] = useState(false);

  const validate = (values) => {
    const errors = {};

    if (!values.email) {
      errors.email = '请输入邮箱地址';
    } else if (!isValidEmail(values.email)) {
      errors.email = '邮箱地址格式不正确，请包含@符号';
    }

    if (!values.password) {
      errors.password = '请输入密码';
    } else if (values.password.length < 8) {
      errors.password = '密码长度至少8位';
    }

    return errors;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const values = getFormValues(e.target);
    const validationErrors = validate(values);

    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
      // 聚焦到第一个错误字段
      const firstErrorField = e.target.querySelector('[aria-invalid="true"]');
      firstErrorField?.focus();
      return;
    }

    setIsSubmitting(true);
    try {
      await login(values);
    } catch (error) {
      setErrors({ form: error.message });
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {errors.form && (
        <div className="error-summary" role="alert">
          {errors.form}
        </div>
      )}

      <FormField>
        <label htmlFor="email">邮箱地址</label>
        <input
          type="email"
          id="email"
          name="email"
          aria-invalid={errors.email ? 'true' : 'false'}
          aria-describedby={errors.email ? 'email-error' : undefined}
        />
        {errors.email && (
          <div id="email-error" className="error-message" role="alert">
            {errors.email}
          </div>
        )}
      </FormField>

      {/* 其他字段... */}

      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? '登录中...' : '登录'}
      </button>
    </form>
  );
}
```

---

## 🔗 相关文档

- [功能状态详解](./component-states-functional.md) - 功能状态总览
- [Disabled状态详解](./component-states-disabled.md) - 禁用状态规范
- [Loading状态详解](./component-states-loading.md) - 加载状态规范
- [无障碍指南](./accessibility.md) - WCAG AA无障碍标准

---

> **状态**: ✅ DONE
> **最后更新**: 2026-01-04 (从component-states-functional.md拆分)
> **维护者**: 项目团队
