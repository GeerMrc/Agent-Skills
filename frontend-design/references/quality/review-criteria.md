# 代码审查标准

> 👁️ **Review Criteria** - 确保代码质量和一致性

---

## 📖 文档说明

本文档提供前端代码审查的标准和检查清单，帮助团队保持代码质量和一致性。

**目标读者**: 代码审查者、开发者
**文档长度**: 约280行
**阅读时间**: 约15分钟

---

## 🎯 审查原则

### 建设性审查

| 原则 | 说明 |
|------|------|
| **尊重** | 尊重作者的工作和努力 |
| **建设性** | 提供可操作的建议 |
| **解释原因** | 说明为什么需要修改 |
| **开放讨论** | 鼓励讨论不同观点 |

### 审查流程

```
1. 理解变更的目的
2. 检查代码质量
3. 验证功能正确性
4. 提供建设性反馈
5. 确认修改完成
```

---

## 🏗️ 架构和设计

### 代码组织

```javascript
// ✅ 好的做法：清晰的文件结构
src/
├── components/
│   ├── Button/
│   │   ├── Button.tsx
│   │   ├── Button.test.tsx
│   │   └── index.ts
│   └── Card/
├── hooks/
├── utils/
├── types/
└── styles/

// ❌ 避免：混乱的文件结构
src/
├── component.tsx
├── Component2.tsx
├── test.js
└── utils2.js
```

### 组件设计

```tsx
// ✅ 好的做法：单一职责
function UserAvatar({ src, alt, size }: AvatarProps) {
  return <img src={src} alt={alt} className={`avatar-${size}`} />
}

// ❌ 避免：组件职责过多
function UserWidget({ user }) {
  // 渲染头像
  // 获取用户数据
  // 处理表单提交
  // 管理状态
  // ...太多职责
}
```

### 命名规范

```tsx
// ✅ 好的做法：清晰描述性命名
function fetchUserData(userId: string) {}
const isAuthenticated = true;
const MAX_RETRY_COUNT = 3;

// ❌ 避免：模糊或不一致的命名
function getData(id) {}
const flag = true;
const n = 3;
```

---

## 🎨 代码质量

### 可读性

```tsx
// ✅ 好的做法：清晰易读
function calculateDiscount(price: number, discount: number): number {
  return price * (1 - discount / 100);
}

// ❌ 避免：难以理解的代码
const d = (p: number, d: number): number => p * (1 - d / 100);
```

### 代码注释

```tsx
// ✅ 好的做法：解释"为什么"而非"是什么"

// 使用折扣率计算最终价格，而不是直接相减，
// 因为这样可以确保折扣不会超过原价
function calculateFinalPrice(price: number, discount: number): number {
  return price * (1 - discount / 100);
}

// ❌ 避免：重复代码逻辑的注释
// 将价格乘以1减去折扣率
return price * (1 - discount / 100);
```

### 错误处理

```tsx
// ✅ 好的做法：完整的错误处理
async function fetchUser(id: string) {
  try {
    const response = await fetch(`/api/users/${id}`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Failed to fetch user:', error);
    throw error;
  }
}

// ❌ 避免：静默失败
async function fetchUser(id: string) {
  try {
    const response = await fetch(`/api/users/${id}`);
    return await response.json();
  } catch (error) {
    // 什么都不做
  }
}
```

---

## ⚡ 性能考虑

### 渲染优化

```tsx
// ✅ 好的做法：使用 memo 避免不必要的重渲染
const ExpensiveComponent = memo(function ExpensiveComponent({
  data,
  onUpdate
}: Props) {
  return (
    <div>
      {data.map(item => (
        <Item key={item.id} data={item} onUpdate={onUpdate} />
      ))}
    </div>
  );
});

// ❌ 避免：每次父组件更新都重渲染
function ExpensiveComponent({ data, onUpdate }: Props) {
  return (
    <div>
      {data.map(item => (
        <Item data={item} onUpdate={onUpdate} />
      ))}
    </div>
  );
}
```

### 依赖管理

```tsx
// ✅ 好的做法：正确使用依赖数组
useEffect(() => {
  fetchUser(userId);
}, [userId]);

// ✅ 缓存昂贵的计算
const sortedItems = useMemo(() => {
  return items.sort((a, b) => a.name.localeCompare(b.name));
}, [items]);

// ❌ 避免：缺失依赖或过度依赖
useEffect(() => {
  fetchUser(userId);
}, []); // 缺少 userId 依赖
```

---

## 🔒 安全考虑

### XSS 防护

```tsx
// ✅ 好的做法：React 自动转义
function UserGreeting({ name }: { name: string }) {
  return <h1>Hello, {name}!</h1>;
}

// ❌ 避免：直接渲染 HTML
function UserGreeting({ name }: { name: string }) {
  return <h1 dangerouslySetInnerHTML={{ __html: name }} />;
}
```

### 输入验证

```tsx
// ✅ 好的做法：验证用户输入
function EmailInput({ value, onChange }: EmailInputProps) {
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const email = e.target.value;
    if (isValidEmail(email) || email === '') {
      onChange(email);
    }
  };

  return <input type="email" value={value} onChange={handleChange} />;
}

// ❌ 避免：不验证输入
function EmailInput({ value, onChange }: EmailInputProps) {
  return <input type="email" value={value} onChange={e => onChange(e.target.value)} />;
}
```

---

## ♿ 无障碍性

### 语义化 HTML

```tsx
// ✅ 好的做法：使用语义化元素
function Navigation() {
  return (
    <nav aria-label="主导航">
      <ul>
        <li><a href="/">首页</a></li>
        <li><a href="/about">关于</a></li>
      </ul>
    </nav>
  );
}

// ❌ 避免：过度使用 div
function Navigation() {
  return (
    <div className="nav">
      <div className="nav-item">首页</div>
      <div className="nav-item">关于</div>
    </div>
  );
}
```

### ARIA 属性

```tsx
// ✅ 好的做法：提供适当的 ARIA 属性
function Modal({ isOpen, onClose, children }: ModalProps) {
  return (
    <div
      role="dialog"
      aria-modal="true"
      aria-labelledby="modal-title"
      className={isOpen ? 'open' : 'closed'}
    >
      <h2 id="modal-title">对话框标题</h2>
      {children}
      <button onClick={onClose}>关闭</button>
    </div>
  );
}
```

---

## 🧪 测试覆盖

### 单元测试

```tsx
// ✅ 好的做法：全面的测试覆盖
describe('Button', () => {
  it('renders children correctly', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByText('Click me')).toBeInTheDocument();
  });

  it('calls onClick when clicked', async () => {
    const user = userEvent.setup();
    const handleClick = vi.fn();
    render(<Button onClick={handleClick}>Click me</Button>);

    await user.click(screen.getByRole('button'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('is disabled when disabled prop is true', () => {
    render(<Button disabled>Click me</Button>);
    expect(screen.getByRole('button')).toBeDisabled();
  });
});

// ❌ 避免：测试不足或测试实现细节
describe('Button', () => {
  it('works', () => {
    // 太模糊
    expect(true).toBe(true);
  });
});
```

---

## 📝 审查检查清单

### 功能性

- [ ] 代码实现了预期功能
- [ ] 边界情况得到处理
- [ ] 错误得到适当处理
- [ ] 没有明显的 bug

### 代码质量

- [ ] 代码清晰易读
- [ ] 命名具有描述性
- [ ] 没有重复代码
- [ ] 遵循项目风格指南

### 性能

- [ ] 没有明显的性能问题
- [ ] 资源得到适当优化
- [ ] 没有内存泄漏
- [ ] 使用了适当的缓存

### 安全

- [ ] 用户输入得到验证
- [ ] 没有 XSS 漏洞
- [ ] 敏感数据得到保护
- [ ] 依赖项是安全的

### 无障碍性

- [ ] 使用语义化 HTML
- [ ] 提供 ARIA 属性
- [ ] 键盘导航可用
- [ ] 颜色对比度符合标准

### 测试

- [ ] 有足够的测试覆盖
- [ ] 测试通过
- [ ] 测试有意义
- [ ] 没有测试实现细节

---

## 💬 反馈技巧

### 给反馈的方式

```
❌ 避免：
"这段代码不好。"

✅ 推荐：
"我发现这段代码可能有问题，原因如下：
1. 函数名称不够描述性
2. 缺少错误处理
3. 可以拆分为更小的函数

建议：
1. 重命名为 calculateFinalPrice
2. 添加 try-catch 处理异常
3. 将折扣计算逻辑提取为单独函数"
```

### 接受反馈

```
✅ 积极回应：
- 感谢审查者的时间
- 讨论不同观点
- 解释设计决策
- 愿意修改代码

❌ 防御性回应：
- 争辩每个反馈
- 拒绝所有建议
- 认为反馈是针对个人
```

---

## 🔧 审查工具

### 自动化工具

```bash
# ESLint - 代码质量检查
npm run lint

# Prettier - 代码格式化
npm run format

# TypeScript - 类型检查
npm run typecheck

# Vitest - 单元测试
npm test

# 可访问性检查
npm run test:a11y
```

### Git 集成

```bash
# 使用 Git hooks 自动化检查
# .husky/pre-commit
npm run lint
npm run typecheck
npm test
```

---

## 📋 审查模板

### PR 审查模板

```markdown
## 代码审查清单

### 功能性
- [ ] 代码实现了预期功能
- [ ] 边界情况得到处理

### 代码质量
- [ ] 代码清晰易读
- [ ] 遵循项目风格指南

### 性能
- [ ] 没有明显的性能问题

### 安全
- [ ] 用户输入得到验证

### 测试
- [ ] 有足够的测试覆盖

## 反馈
<!-- 在这里提供具体的反馈 -->
```

---

## 💡 最佳实践总结

1. **保持建设性**：提供可操作的反馈
2. **解释原因**：说明为什么需要修改
3. **尊重作者**：保持专业和礼貌
4. **讨论权衡**：考虑不同的解决方案
5. **及时响应**：快速回复审查请求

---

## 🔗 相关资源

### 工具

- ** ESLint**: 代码质量检查
- ** Prettier**: 代码格式化
- ** SonarQube**: 代码质量分析

### 文档

- [Google Code Review Guide](https://google.github.io/eng-practices/review/)
- [Effective Code Review](https://medium.com/@palantir/code-reviews-best-practices-5cfa2c8a5a5c)

---

> **文档版本**: v1.0
> **最后更新**: 2026-01-04
> **维护者**: Frontend Design Agent Skills Team
