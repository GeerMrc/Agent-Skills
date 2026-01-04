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

**核心价值**：
- 提供即时视觉反馈
- 减少用户等待焦虑
- 明确系统正在工作
- 预估等待时间

---

## 📊 加载模式对比

| 模式 | 适用场景 | 优点 | 缺点 | 推荐度 | 详细文档 |
|------|----------|------|------|--------|----------|
| **旋转圆环** | 按钮、小组件 | 轻量、通用 | 不显示进度 | ⭐⭐⭐⭐⭐ | [查看详情](component-states-loading-patterns.md#1-旋转圆环spinner) |
| **进度条** | 文件上传 | 显示进度 | 需要知道总量 | ⭐⭐⭐⭐☆ | [查看详情](component-states-loading-patterns.md#2-进度条) |
| **骨架屏** | 列表、卡片 | 保持布局 | 实现复杂 | ⭐⭐⭐⭐⭐ | [查看详情](component-states-loading-patterns.md#3-骨架屏-skeleton) |
| **模糊覆盖** | 模态框 | 区域明确 | 阻塞操作 | ⭐⭐⭐☆☆ | [查看详情](component-states-loading-patterns.md#4-模糊覆盖-overlay) |

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
async function loadProgressiveData() {
  // 先加载关键数据
  const critical = await fetchCriticalData();
  renderCritical(critical);

  // 再加载次要数据
  const secondary = await fetchSecondaryData();
  renderSecondary(secondary);

  // 最后加载增强数据
  const enhancement = await fetchEnhancementData();
  renderEnhancement(enhancement);
}
```

---

## ⚠️ 常见问题

### Q1: 加载指示器什么时候显示？

**A**:
- **不要显示**: 加载时间 < 500ms
- **应该显示**: 加载时间 >= 500ms
- 使用最小显示时间避免闪烁

### Q2: 如何选择加载模式？

**A**: 根据场景选择：
- **按钮/小组件**: 旋转圆环
- **文件上传/下载**: 进度条
- **列表/卡片加载**: 骨架屏
- **模态框/区域**: 模糊覆盖

详见：[加载模式详解](component-states-loading-patterns.md)

### Q3: 如何实现最小显示时间？

**A**: 参考上面的"避免闪烁"示例代码

### Q4: 加载状态需要无障碍支持吗？

**A**: **必须**。详见：[视觉描述与交互设计](component-states-loading-visual.md#♿-无障碍要求)

### Q5: 进度条什么时候使用？

**A**:
- ✅ 知道总进度（文件上传）
- ✅ 长时间操作（> 2s）
- ❌ 不知道总进度（API调用）

### Q6: 骨架屏比旋转圆环好？

**A**: 各有优势：
- **骨架屏**: 保持布局，体验更好
- **旋转圆环**: 实现简单，适用广泛

### Q7: 如何处理加载失败？

**A**:
1. 显示错误提示
2. 提供重试按钮
3. 保留已加载数据
4. 记录错误日志

```javascript
async function loadDataWithRetry(url, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fetch(url).then(r => r.json());
    } catch (error) {
      if (i === maxRetries - 1) throw error;
      await new Promise(r => setTimeout(r, 1000 * (i + 1)));
    }
  }
}
```

### Q8: 如何实现全局加载状态？

**A**: 使用状态管理（如 Redux、Vuex）：
```javascript
// Redux 示例
const loadingSlice = createSlice({
  name: 'loading',
  initialState: { global: false },
  reducers: {
    setGlobalLoading: (state, action) => {
      state.global = action.payload;
    }
  }
});
```

---

## 📚 详细文档

### 加载模式与实现
详见：[加载模式详解与实现示例](component-states-loading-patterns.md)
- 旋转圆环（Spinner）完整实现
- 进度条（Progress Bar）完整实现
- 骨架屏（Skeleton Screen）完整实现
- 模糊覆盖（Overlay）完整实现

### 视觉设计与交互
详见：[视觉描述与交互设计](component-states-loading-visual.md)
- CSS 设计规范
- 交互行为定义
- 无障碍要求（WCAG AA）

---

## 🔗 相关文档

- [组件状态总览](component-states.md)
- [交互状态](component-states-interactive.md)
- [功能状态](component-states-functional.md)
- [禁用状态](component-states-disabled.md)
- [空状态](component-states-empty.md)
- [错误状态](component-states-error.md)

---

> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills 项目团队
