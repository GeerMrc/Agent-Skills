# 测试策略

> 🧪 **Testing Strategy** - 构建可靠的测试体系

---

## 📖 文档说明

本文档提供前端测试的完整策略，包括单元测试、集成测试、E2E测试和视觉回归测试。

**目标读者**: 前端开发者、QA工程师
**文档长度**: 约280行
**阅读时间**: 约15分钟

---

## 🎯 测试金字塔

```
           /\
          /  \
         / E2E \        少量
        /--------\
       /  集成测试  \     适量
      /------------\
     /   单元测试    \   大量
    /----------------\
```

| 测试类型 | 数量 | 速度 | 成本 | 覆盖范围 |
|----------|------|------|------|----------|
| **单元测试** | 多 | 快 | 低 | 函数、组件 |
| **集成测试** | 中 | 中 | 中 | 模块交互 |
| **E2E 测试** | 少 | 慢 | 高 | 用户流程 |

---

## 📦 单元测试

### 测试框架配置

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: ['./src/test/setup.ts'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      lines: 80,
      functions: 80,
      branches: 80,
      statements: 80,
    },
  },
});
```

### 组件测试

```tsx
// Button.test.tsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect, vi } from 'vitest';
import { Button } from './Button';

describe('Button', () => {
  it('renders children correctly', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByRole('button', { name: 'Click me' }))
      .toBeInTheDocument();
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

  it('applies variant classes correctly', () => {
    const { rerender } = render(<Button variant="primary">Primary</Button>);
    expect(screen.getByRole('button')).toHaveClass('btn-primary');

    rerender(<Button variant="secondary">Secondary</Button>);
    expect(screen.getByRole('button')).toHaveClass('btn-secondary');
  });
});
```

### Hook 测试

```tsx
// useCounter.test.ts
import { renderHook, act } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import { useCounter } from './useCounter';

describe('useCounter', () => {
  it('initializes with default value', () => {
    const { result } = renderHook(() => useCounter());
    expect(result.current.count).toBe(0);
  });

  it('increments count', () => {
    const { result } = renderHook(() => useCounter());

    act(() => {
      result.current.increment();
    });

    expect(result.current.count).toBe(1);
  });

  it('decrements count', () => {
    const { result } = renderHook(() => useCounter());

    act(() => {
      result.current.decrement();
    });

    expect(result.current.count).toBe(-1);
  });
});
```

---

## 🔗 集成测试

### API 集成测试

```typescript
// userService.test.ts
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { fetchUser, updateUser } from './userService';

// Mock fetch
global.fetch = vi.fn();

describe('UserService', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('fetchUser', () => {
    it('fetches user successfully', async () => {
      const mockUser = { id: '1', name: 'John Doe' };
      vi.mocked(fetch).mockResolvedValueOnce({
        ok: true,
        json: async () => mockUser,
      } as Response);

      const user = await fetchUser('1');
      expect(user).toEqual(mockUser);
      expect(fetch).toHaveBeenCalledWith('/api/users/1');
    });

    it('handles error response', async () => {
      vi.mocked(fetch).mockResolvedValueOnce({
        ok: false,
        status: 404,
      } as Response);

      await expect(fetchUser('1')).rejects.toThrow('HTTP error! status: 404');
    });
  });
});
```

### 组件集成测试

```tsx
// UserForm.test.tsx
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect, vi } from 'vitest';
import { UserForm } from './UserForm';

describe('UserForm Integration', () => {
  it('submits form with valid data', async () => {
    const handleSubmit = vi.fn();
    render(<UserForm onSubmit={handleSubmit} />);

    await user.type(screen.getByLabelText(/name/i), 'John Doe');
    await user.type(screen.getByLabelText(/email/i), 'john@example.com');
    await user.click(screen.getByRole('button', { name: /submit/i }));

    await waitFor(() => {
      expect(handleSubmit).toHaveBeenCalledWith({
        name: 'John Doe',
        email: 'john@example.com',
      });
    });
  });

  it('shows validation errors for invalid data', async () => {
    render(<UserForm onSubmit={vi.fn()} />);

    await user.click(screen.getByRole('button', { name: /submit/i }));

    await waitFor(() => {
      expect(screen.getByText(/name is required/i)).toBeInTheDocument();
      expect(screen.getByText(/email is required/i)).toBeInTheDocument();
    });
  });
});
```

---

## 🎭 E2E 测试

### Playwright 配置

```typescript
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 5'] },
    },
  ],
});
```

### E2E 测试示例

```typescript
// login.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Authentication', () => {
  test('user can login with valid credentials', async ({ page }) => {
    await page.goto('/login');

    await page.fill('input[name="email"]', 'user@example.com');
    await page.fill('input[name="password"]', 'password123');
    await page.click('button[type="submit"]');

    await expect(page).toHaveURL('/dashboard');
    await expect(page.locator('h1')).toContainText('欢迎回来');
  });

  test('shows error with invalid credentials', async ({ page }) => {
    await page.goto('/login');

    await page.fill('input[name="email"]', 'user@example.com');
    await page.fill('input[name="password"]', 'wrong-password');
    await page.click('button[type="submit"]');

    await expect(page.locator('.error')).toContainText('邮箱或密码错误');
  });
});
```

---

## 🎨 视觉回归测试

### Playwright 视觉测试

```typescript
// visual.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Visual Regression', () => {
  test('homepage matches snapshot', async ({ page }) => {
    await page.goto('/');

    // 等待页面稳定
    await page.waitForLoadState('networkidle');

    // 截图对比
    await expect(page).toHaveScreenshot('homepage.png', {
      maxDiffPixels: 100,
    });
  });

  test('button matches snapshot', async ({ page }) => {
    await page.goto('/components/button');

    const button = page.locator('.btn-primary');
    await expect(button).toHaveScreenshot('button-primary.png');
  });
});
```

---

## 🧪 测试最佳实践

### 测试命名

```typescript
// ✅ 好的做法：描述性的测试名称
describe('UserService', () => {
  it('should return user data when fetch is successful', () => {});
  it('should throw error when user is not found', () => {});
  it('should update user data with valid input', () => {});
});

// ❌ 避免：模糊的测试名称
describe('UserService', () => {
  it('works', () => {});
  it('test 1', () => {});
  it('error', () => {});
});
```

### AAA 模式（Arrange-Act-Assert）

```typescript
// ✅ 好的做法：清晰的 AAA 结构
it('calculates total price correctly', () => {
  // Arrange - 准备测试数据
  const price = 100;
  const discount = 20;
  const expectedTotal = 80;

  // Act - 执行被测试的代码
  const result = calculateTotal(price, discount);

  // Assert - 验证结果
  expect(result).toBe(expectedTotal);
});

// ❌ 避免：混合 AAA 阶段
it('calculates total price correctly', () => {
  const price = 100;
  const result = calculateTotal(price, 20);
  expect(result).toBe(80);
  const discount = 20; // Arrange 在 Act 之后
});
```

### 测试隔离

```typescript
// ✅ 好的做法：每个测试独立
describe('Counter', () => {
  it('starts at 0', () => {
    const { result } = renderHook(() => useCounter());
    expect(result.current.count).toBe(0);
  });

  it('increments independently', () => {
    const { result } = renderHook(() => useCounter());
    act(() => {
      result.current.increment();
    });
    expect(result.current.count).toBe(1);
  });
});

// ❌ 避免：测试相互依赖
describe('Counter', () => {
  let counter: Counter;

  beforeEach(() => {
    counter = new Counter();
  });

  it('starts at 0', () => {
    expect(counter.count).toBe(0);
  });

  it('increments from previous test', () => {
    // 依赖上一个测试的状态
    counter.increment();
    expect(counter.count).toBe(1);
  });
});
```

---

## 📊 测试覆盖率

### 覆盖率目标

| 指标 | 目标 | 说明 |
|------|------|------|
| **行覆盖率** | >80% | 代码行被执行的比例 |
| **函数覆盖率** | >80% | 函数被调用的比例 |
| **分支覆盖率** | >75% | 条件分支被执行的比例 |
| **语句覆盖率** | >80% | 语句被执行的比例 |

### 生成覆盖率报告

```bash
# 运行测试并生成覆盖率报告
npm test -- --coverage

# 查看覆盖率报告
open coverage/index.html
```

---

## 🔧 CI/CD 集成

### GitHub Actions 配置

```yaml
# .github/workflows/test.yml
name: Test

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run lint
        run: npm run lint

      - name: Run type check
        run: npm run typecheck

      - name: Run unit tests
        run: npm test

      - name: Run E2E tests
        run: npm run test:e2e

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/lcov.info
```

---

## 📋 测试检查清单

### 单元测试

- [ ] 每个组件都有测试
- [ ] 每个 hook 都有测试
- [ ] 每个工具函数都有测试
- [ ] 测试覆盖了边界情况

### 集成测试

- [ ] 关键用户流程有测试
- [ ] API 集成有测试
- [ ] 状态管理有测试
- [ ] 错误处理有测试

### E2E 测试

- [ ] 主要用户流程有测试
- [ ] 跨浏览器测试
- [ ] 移动端测试
- [ ] 关键功能有测试

### 持续集成

- [ ] 所有测试在 CI 中运行
- [ ] 测试失败阻止合并
- [ ] 覆盖率报告生成
- [ ] 测试结果可视化

---

## 💡 最佳实践总结

1. **测试金字塔**：大量单元测试，适量集成测试，少量E2E测试
2. **测试隔离**：每个测试独立运行
3. **描述性命名**：测试名称清晰表达意图
4. **AAA 模式**：Arrange-Act-Assert 结构
5. **持续集成**：自动运行测试

---

## 🔗 相关资源

### 工具

- ** Vitest**: 单元测试框架
- ** Testing Library**: 组件测试工具
- ** Playwright**: E2E 测试框架
- ** MSW**: API Mock 工具

### 文档

- [Vitest 文档](https://vitest.dev/)
- [Testing Library 文档](https://testing-library.com/)
- [Playwright 文档](https://playwright.dev/)

---

> **文档版本**: v1.0
> **最后更新**: 2026-01-04
> **维护者**: Frontend Design Agent Skills Team
