# Angular最佳实践

> 🔴 **Angular 17+** - 组件设计、依赖注入和Signals

---

## 📖 核心概念

Angular是完整的平台，提供CLI、路由、表单、HTTP客户端等一整套解决方案。最新版本引入Standalone组件和Signals。

**核心特性**：
- TypeScript优先
- 依赖注入（DI）
- RxJS响应式编程
- Signals（新响应式系统）
- Standalone组件

---

## 🎯 组件设计

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

## 🔨 响应式系统

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

## 📡 依赖注入

### 服务

```typescript
@Injectable({ providedIn: 'root' })
export class ApiService {
  constructor(private http: HttpClient) {}

  getData(): Observable<Data[]> {
    return this.http.get<Data[]>('/api/data')
  }
}
```

### 组件注入

```typescript
@Component({
  selector: 'app-users',
  // ...
})
export class UsersComponent {
  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.apiService.getData().subscribe(data => {
      this.users = data
    })
  }
}
```

### Injector

```typescript
// 手动注入
const injector = Injector.create({
  providers: [
    { provide: ApiService, useClass: ApiService }
  ]
})

const apiService = injector.get(ApiService)
```

---

## 🛣️ 路由（Angular Router）

### 路由配置

```typescript
const routes: Routes = [
  {
    path: '',
    component: HomeComponent
  },
  {
    path: 'users/:id',
    component: UserComponent,
    // 路由守卫
    canActivate: [AuthGuard]
  },
  {
    path: 'admin',
    loadChildren: () => import('./admin/admin.routes')
      .then(m => m.ADMIN_ROUTES)
  }
]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
```

### 路由导航

```typescript
@Component({ /* ... */ })
export class MyComponent {
  constructor(private router: Router, private route: ActivatedRoute) {}

  // 编程式导航
  goToUsers(): void {
    this.router.navigate(['/users'])
  }

  // 路由参数
  ngOnInit(): void {
    this.route.params.subscribe(params => {
      const id = params['id']
    })

    // 或使用signal
    const id = this.route.paramMap.pipe(
      map(params => params.get('id'))
    )
  }
}
```

### 路由守卫

```typescript
@Injectable({ providedIn: 'root' })
export class AuthGuard implements CanActivate {
  constructor(private authService: AuthService) {}

  canActivate(): Observable<boolean> {
    return this.authService.isAuthenticated$
  }
}
```

---

## 📝 表单

### 模板驱动表单

```html
<form #form="ngForm" (ngSubmit)="onSubmit(form.value)">
  <input
    name="username"
    ngModel
    required
    minlength="3"
    #username="ngModel"
  />

  @if (username.invalid && username.touched) {
    <small>Name is required</small>
  }

  <button type="submit" [disabled]="form.invalid">Submit</button>
</form>
```

### 响应式表单

```typescript
@Component({
  selector: 'app-form',
  template: `
    <form [formGroup]="form" (ngSubmit)="onSubmit()">
      <input formControlName="username" />

      @if (form.get('username')?.hasError('required')) {
        <small>Name is required</small>
      }

      <button type="submit" [disabled]="form.invalid">Submit</button>
    </form>
  `
})
export class FormComponent {
  form = this.fb.group({
    username: ['', [Validators.required, Validators.minLength(3)]],
    email: ['', [Validators.required, Validators.email]]
  })

  constructor(private fb: FormBuilder) {}

  onSubmit(): void {
    if (this.form.valid) {
      console.log(this.form.value)
    }
  }
}
```

---

## ♿ 无障碍最佳实践

### 语义化HTML

```html
<!-- ✅ 好的做法：语义化元素 -->
<nav>
  <ul>
    <li><a routerLink="/">Home</a></li>
    <li><a routerLink="/about">About</a></li>
  </ul>
</nav>

<!-- ❌ 避免：纯div -->
<div class="nav" (click)="goHome()">Home</div>
```

### ARIA属性

```html
<button
  [attr.aria-pressed]="isPressed()"
  [attr.aria-expanded]="isExpanded()"
  (click)="toggle()"
>
  Toggle
</button>

<div
  role="status"
  [attr.aria-busy]="isLoading()"
  aria-live="polite"
>
  @if (isLoading()) {
    Loading...
  } @else {
    Done
  }
</div>
```

### 键盘导航

```html
<div
  role="button"
  tabindex="0"
  (click)="handleClick()"
  (keydown.enter)="handleClick()"
  (keydown.space)="handleClick()"
>
  Click me or press Enter/Space
</div>
```

---

## 🧪 测试

### 单元测试（Jest）

```typescript
import { ComponentFixture, TestBed } from '@angular/core/testing'
import { CounterComponent } from './counter.component'

describe('CounterComponent', () => {
  let component: CounterComponent
  let fixture: ComponentFixture<CounterComponent>

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [CounterComponent]
    })
    fixture = TestBed.createComponent(CounterComponent)
    component = fixture.componentInstance
  })

  it('should create', () => {
    expect(component).toBeTruthy()
  })

  it('should increment count', () => {
    component.increment()
    expect(component.localCount()).toBe(1)
  })
})
```

---

## 📚 相关文档

- [React](./react.md) - React最佳实践
- [Vue](./vue.md) - Vue最佳实践
- [Svelte](./svelte.md) - Svelte最佳实践
- [组件状态覆盖](../implementation/component-states.md) - 组件状态管理

---

## 🔗 快速导航

- [返回by-framework/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **状态**: ✅ DONE
> **最后更新**: 2025-01-03
> **维护者**: 项目团队
