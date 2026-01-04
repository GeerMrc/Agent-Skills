# Angular最佳实践

> 🔴 **Angular 17+** - 组件设计、依赖注入和Signals

---

## 📖 文档说明

本文档提供 Angular 的完整最佳实践指南，涵盖组件设计、响应式系统、样式管理和性能优化等内容。

**目标读者**: Angular 开发者
**文档长度**: ~270行（主文档）
**阅读时间**: 约15分钟

**相关文档**:
- [完整实现指南](angular-guide.md) - 依赖注入、路由、表单、测试等详细内容

---

## 🎯 核心概念

Angular是完整的平台，提供CLI、路由、表单、HTTP客户端等一整套解决方案。最新版本引入Standalone组件和Signals。

**核心特性**：
- TypeScript优先
- 依赖注入（DI）
- RxJS响应式编程
- Signals（新响应式系统）
- Standalone组件

---

## 🎨 组件设计

### 组件定义（Standalone）

```typescript
import { Component, signal, computed, input, output } from '@angular/core'
import { CommonModule } from '@angular/common'

@Component({
  selector: 'app-counter',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './counter.component.html',
  styleUrls: ['./counter.component.css']
})
export class CounterComponent {
  // Inputs（使用signal）
  readonly title = input.required<string>()
  readonly count = input(0)

  // Outputs（使用EventEmitter）
  readonly update = output<number>()

  // 响应式状态
  private localCount = signal(0)

  // 派生状态
  readonly isDouble = computed(() => this.localCount() > 1)

  // 方法
  increment(): void {
    this.localCount.update(n => n + 1)
    this.update.emit(this.localCount())
  }
}
```

### 模板

```html
<div class="counter">
  <h2>{{ title() }}</h2>
  <p>Count: {{ localCount() }}</p>
  @if (isDouble()) {
    <p>Double!</p>
  }
  <button (click)="increment()">Increment</button>
</div>
```

### 组件命名

```typescript
// ✅ 好的做法：描述性名称 + Component后缀
@Component({
  selector: 'app-user-profile',
  // ...
})
export class UserProfileComponent {}

@Component({
  selector: 'app-data-table',
  // ...
})
export class DataTableComponent {}

// ❌ 避免：模糊名称
@Component({
  selector: 'app-user',
  // ...
})
export class UserComponent {}
```

### Input/Output最佳实践

```typescript
@Component({
  selector: 'app-button',
  // ...
})
export class ButtonComponent {
  // ✅ 使用signal input
  readonly label = input.required<string>()
  readonly variant = input<'primary' | 'secondary'>('primary')
  readonly disabled = input(false)

  // ✅ 使用output
  readonly clicked = output<void>()
  readonly changed = output<string>()

  handleClick(): void {
    if (!this.disabled()) {
      this.clicked.emit()
    }
  }
}
```

---

## 📡 响应式系统

### Signals（推荐）

```typescript
import { signal, computed, effect } from '@angular/core'

// writable signal
const count = signal(0)
count() // 读取
count.set(1) // 设置
count.update(n => n + 1) // 更新

// computed signal
const doubleCount = computed(() => count() * 2)

// effect（副作用）
effect(() => {
  console.log('Count changed:', count())
})

// 对象signal
interface User {
  name: string
  age: number
}

const user = signal<User>({ name: 'Alice', age: 30 })
user.update(u => ({ ...u, age: u.age + 1 }))

// 数组signal
const items = signal<number[]>([1, 2, 3])
items.update(list => [...list, 4])
```

### RxJS Observable

```typescript
import { Observable, BehaviorSubject, Subject } from 'rxjs'
import { map, filter, switchMap } from 'rxjs/operators'

// BehaviorSubject（有初始值）
const count$ = new BehaviorSubject(0)

// Subject（无初始值）
const click$ = new Subject<void>()

// 操作符
const doubledCount$ = count$.pipe(
  filter(n => n > 0),
  map(n => n * 2)
)

// 在组件中使用
@Component({ /* ... */ })
export class MyComponent implements OnInit, OnDestroy {
  private destroy$ = new Subject<void>()

  ngOnInit(): void {
    this.count$.pipe(
      takeUntil(this.destroy$)
    ).subscribe(count => {
      console.log('Count:', count)
    })
  }

  ngOnDestroy(): void {
    this.destroy$.next()
    this.destroy$.complete()
  }
}
```

---

## 🎨 样式管理

### View Encapsulation

```typescript
@Component({
  selector: 'app-card',
  // ...
  encapsulation: ViewEncapsulation.ShadowDom // Shadow DOM
  // encapsulation: ViewEncapsulation.None // 无封装
  // encapsulation: ViewEncapsulation.Emulated // 默认
})
export class CardComponent {}
```

### 样式绑定

```html
<!-- 类名绑定 -->
<div [class.active]="isActive()">Active</div>
<div [class]="{'active': isActive(), 'disabled': isDisabled()}">...</div>

<!-- 样式绑定 -->
<div [style.background]="color()">Background</div>
<div [style.--color]="themeColor()">Custom Property</div>

<!-- NgClass/NgStyle -->
<div [ngClass]="{'active': isActive(), 'disabled': isDisabled()}">...</div>
<div [ngStyle]="{'background': color(), 'padding': size()}">...</div>
```

### 样式文件

```css
/* 使用:host选择组件本身 */
:host {
  display: block;
  padding: var(--spacing-md);
}

/* 使用:host()条件样式 */
:host(.active) {
  background: var(--color-primary);
}

/* 使用::ng-deep穿透样式 */
:host ::ng-deep .child-component {
  color: var(--color-text);
}
```

---

## 🚀 性能优化

### OnPush变更检测

```typescript
@Component({
  selector: 'app-item',
  // ...
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ItemComponent {
  // 只在输入引用变化时重新渲染
  readonly item = input.required<Item>()
}
```

### 纯管道（Pure Pipes）

```typescript
import { Pipe, PipeTransform } from '@angular/core'

@Pipe({
  name: 'filter',
  standalone: true,
  pure: true // 纯管道，仅在输入变化时重新计算
})
export class FilterPipe implements PipeTransform {
  transform<T>(items: T[], predicate: (item: T) => boolean): T[] {
    return items.filter(predicate)
  }
}
```

### 异步管道（Async Pipe）

```html
<!-- ✅ 好的做法：使用async pipe自动订阅 -->
<div *ngFor="let item of items$ | async">{{ item.name }}</div>

<!-- ❌ 避免：手动订阅 -->
<div *ngFor="let item of items">{{ item.name }}</div>
```

### 路由懒加载

```typescript
const routes: Routes = [
  {
    path: 'home',
    loadComponent: () => import('./home/home.component')
      .then(m => m.HomeComponent)
  },
  {
    path: 'admin',
    loadChildren: () => import('./admin/admin.routes')
      .then(m => m.adminRoutes)
  }
]
```

---

## 🔗 组件通信

### @Input/@Output

```typescript
// 父组件 ParentComponent
@Component({
  selector: 'app-parent',
  template: `
    <app-child
      [data]="parentData"
      (update)="handleUpdate($event)"
    />
  `
})
export class ParentComponent {
  parentData = { name: 'Alice' }

  handleUpdate(value: string): void {
    console.log('Update:', value)
  }
}

// 子组件 ChildComponent
@Component({
  selector: 'app-child',
  // ...
})
export class ChildComponent {
  readonly data = input.required<Data>()
  readonly update = output<string>()

  emitUpdate(): void {
    this.update.emit('updated')
  }
}
```

### 双向绑定（[(ngModel)]）

```typescript
@Component({
  selector: 'app-input',
  template: `
    <input [(ngModel)]="value" (ngModelChange)="onChange($event)" />
  `
})
export class InputComponent {
  value = ''

  onChange(value: string): void {
    console.log('Value changed:', value)
  }
}
```

### Service共享

```typescript
// 共享服务
@Injectable({ providedIn: 'root' })
export class DataService {
  private data$ = new BehaviorSubject<Data>(initialData)

  getData(): Observable<Data> {
    return this.data$.asObservable()
  }

  updateData(data: Data): void {
    this.data$.next(data)
  }
}

// 组件使用
@Component({ /* ... */ })
export class MyComponent {
  data = this.dataService.getData()

  constructor(private dataService: DataService) {}
}
```

---

## 📋 功能总览

### 核心功能

| 功能 | 说明 | 详细文档 |
|------|------|----------|
| **依赖注入** | 服务、组件注入、Injector | [查看详情](angular-guide.md#依赖注入) |
| **路由** | 路由配置、导航、守卫 | [查看详情](angular-guide.md#路由) |
| **表单** | 模板驱动、响应式表单 | [查看详情](angular-guide.md#表单) |
| **无障碍** | ARIA、键盘导航 | [查看详情](angular-guide.md#无障碍最佳实践) |
| **测试** | 单元测试、集成测试 | [查看详情](angular-guide.md#测试) |

---

## 📋 检查清单

### 组件设计

- [ ] 使用 Standalone 组件
- [ ] 使用 signal input/output
- [ ] 描述性组件命名
- [ ] OnPush 变更检测

### 响应式系统

- [ ] 优先使用 Signals
- [ ] 正确使用 computed
- [ ] 避免 effect 滥用
- [ ] RxJS 订阅清理

### 性能优化

- [ ] OnPush 变更检测
- [ ] 纯管道优化
- [ ] 异步管道自动订阅
- [ ] 路由懒加载

### 样式管理

- [ ] 合理选择 View Encapsulation
- [ ] 使用样式绑定
- [ ] 避免过度使用 ::ng-deep

---

## 💡 最佳实践总结

### 1. 组件化

每个组件职责单一，可复用性强

```typescript
// ✅ 好的做法
@Component({
  selector: 'app-user-card',
  standalone: true
})
export class UserCardComponent {}
```

### 2. 响应式优先

优先使用 Signals，而非 RxJS

```typescript
// ✅ 使用 Signals
readonly count = signal(0)
readonly doubleCount = computed(() => count() * 2)

// ❌ 避免：过度使用 RxJS
count$ = new BehaviorSubject(0)
```

### 3. 性能优先

使用 OnPush 和懒加载

```typescript
@Component({
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ItemComponent {}
```

### 4. 类型安全

充分利用 TypeScript

```typescript
interface User {
  name: string
  age: number
}

readonly user = input.required<User>()
```

---

## 🔗 相关文档

- [完整实现指南](angular-guide.md) - 依赖注入、路由、表单、测试
- [React最佳实践](./react.md)
- [Vue最佳实践](./vue.md)
- [Svelte最佳实践](./svelte.md)
- [组件状态覆盖](../implementation/component-states.md)

---

## 🔗 快速导航

- [返回by-framework/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.0
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
