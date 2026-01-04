# Error状态详解

> ⚠️ **错误状态** - 异常处理和错误反馈的完整规范

---

## 📖 状态概述

Error（错误状态）是组件出现验证错误、系统错误时的视觉反馈，明确告知用户问题所在。

**适用场景**：
- 表单字段验证失败
- 网络请求失败
- 权限不足
- 服务器错误

**核心价值**：
- 明确的错误信息
- 具体的修复建议
- 友好的用户体验
- 快速的问题定位

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

## 🎯 Error状态最佳实践

### ✅ DO（推荐）

1. 具体的错误描述
2. 提供修复建议
3. 错误字段自动聚焦
4. 错误消息使用 `role="alert"`
5. 错误颜色对比度符合WCAG AA标准

### ❌ DON'T（避免）

1. 错误消息过于模糊（"错误"、"无效"）
2. 使用技术术语（"400 Bad Request"）
3. 错误消息远离错误字段
4. 错误颜色对比度不足
5. 不提供修复建议

---

## 📊 实现示例

### 示例1：表单验证错误

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

      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? '登录中...' : '登录'}
      </button>
    </form>
  );
}
```

### 示例2：错误边界组件

```tsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('ErrorBoundary caught:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="error-page" role="alert">
          <div className="error-illustration" aria-hidden="true">
            <ErrorIcon />
          </div>
          <h1 className="error-title">出现错误</h1>
          <p className="error-description">
            {this.state.error?.message || '页面加载出现问题'}
          </p>
          <div className="error-actions">
            <button onClick={() => window.location.reload()}>
              刷新页面
            </button>
            <a href="/" variant="secondary">
              返回首页
            </a>
          </div>
        </div>
      );
    }

    return this.props.children;
  }
}
```

### 示例3：API错误处理

```tsx
function useApi() {
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const fetch = async (url, options = {}) => {
    setLoading(true);
    setError(null);

    try {
      const response = await fetch(url, options);

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.message || `HTTP ${response.status}`);
      }

      return await response.json();
    } catch (err) {
      const errorMessage = err.message || '网络连接失败';
      setError(errorMessage);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  return { fetch, error, loading };
}

// 使用示例
function UserProfile() {
  const { fetch, error, loading } = useApi();

  useEffect(() => {
    fetch('/api/user/profile')
      .then(setData)
      .catch(() => {
        // 错误已在hook中处理
      });
  }, []);

  if (error) {
    return (
      <div className="error-state" role="alert">
        <div className="error-icon">⚠️</div>
        <h3>加载失败</h3>
        <p>{error}</p>
        <button onClick={() => window.location.reload()}>
          重试
        </button>
      </div>
    );
  }

  // 正常渲染...
}
```

---

## ⚠️ 常见错误

### ❌ 避免

**1. 错误消息模糊**
- "输入无效"
- "错误"
- "失败"

**2. 使用技术术语**
- "400 Bad Request"
- "500 Internal Server Error"
- "Validation Error"

**3. 错误位置不明确**
- 错误消息远离错误字段
- 不高亮显示错误字段
- 不自动聚焦到错误位置

**4. 缺少修复建议**
- 只说"错误"，不说如何修复
- 不提供重试按钮
- 没有返回路径

### ✅ 推荐

**1. 具体明确的错误消息**
- "邮箱地址格式不正确，请包含@符号"
- "密码长度至少8位，当前6位"
- "网络连接失败，请检查网络设置"

**2. 用户友好的语言**
- "页面不存在，可能已被删除"
- "您没有权限访问此内容"
- "请检查您的输入"

**3. 错误位置明确**
- 错误消息靠近错误字段
- 高亮显示错误字段
- 自动聚焦到第一个错误字段

**4. 提供修复建议**
- 提供重试按钮
- 显示正确格式示例
- 提供返回路径

---

## 🔗 相关文档

- [功能状态详解](./component-states-functional.md) - 功能状态总览
- [Empty状态详解](./component-states-empty.md) - 空状态规范
- [Disabled状态详解](./component-states-disabled.md) - 禁用状态规范
- [Loading状态详解](./component-states-loading.md) - 加载状态规范
- [无障碍指南](./accessibility.md) - WCAG AA无障碍标准

---

## 🔗 快速导航

- [返回implementation/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **状态**: ✅ DONE
> **最后更新**: 2026-01-05 (从component-states-empty-error.md拆分)
> **维护者**: 项目团队
