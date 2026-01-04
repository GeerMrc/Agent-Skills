# Angular 完整实现指南

> 🔴 **Complete Implementation Guide** - 依赖注入、路由、表单、测试

---

## 📖 文档说明

本文档提供 Angular 的完整实现细节，包括依赖注入、路由、表单、无障碍和测试等高级功能。

**相关文档**：
- [返回主文档](angular.md)

---

## 💉 依赖注入

### 服务定义

```typescript
import { Injectable } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

@Injectable({ providedIn: 'root' })
export class ApiService {
  constructor(private http: HttpClient) {}

  getData(): Observable<Data[]> {
    return this.http.get<Data[]>('/api/data')
  }

  getDataById(id: string): Observable<Data> {
    return this.http.get<Data>(`/api/data/${id}`)
  }

  createData(data: Data): Observable<Data> {
    return this.http.post<Data>('/api/data', data)
  }

  updateData(id: string, data: Data): Observable<Data> {
    return this.http.put<Data>(`/api/data/${id}`, data)
  }

  deleteData(id: string): Observable<void> {
    return this.http.delete<void>(`/api/data/${id}`)
  }
}
```

### 组件注入

```typescript
import { Component, OnInit } from '@angular/core'
import { ApiService } from './api.service'

@Component({
  selector: 'app-users',
  standalone: true,
  template: `
    <ul>
      @for (user of users(); track user.id) {
        <li>{{ user.name }}</li>
      }
    </ul>
  `
})
export class UsersComponent implements OnInit {
  users = signal<User[]>([])

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.apiService.getData().subscribe(data => {
      this.users.set(data)
    })
  }
}
```

### Provider配置

```typescript
@Component({
  selector: 'app-component',
  providers: [
    // useClass: 使用指定类
    { provide: ApiService, useClass: ApiService },

    // useExisting: 使用已有实例
    { provide: BaseApiService, useExisting: ApiService },

    // useValue: 使用指定值
    { provide: API_URL, useValue: 'https://api.example.com' },

    // useFactory: 使用工厂函数
    {
      provide: ApiService,
      useFactory: (http: HttpClient, apiUrl: string) => {
        return new ApiService(http, apiUrl)
      },
      deps: [HttpClient, API_URL]
    }
  ]
})
export class MyComponent {}
```

### Injector手动注入

```typescript
import { Injector } from '@angular/core'

// 手动创建injector
const injector = Injector.create({
  providers: [
    { provide: ApiService, useClass: ApiService }
  ]
})

// 获取服务实例
const apiService = injector.get(ApiService)
```

### Token注入

```typescript
// InjectionToken定义
import { InjectionToken } from '@angular/core'

export const API_URL = new InjectionToken<string>('api.url')

// 提供token
@NgModule({
  providers: [
    { provide: API_URL, useValue: 'https://api.example.com' }
  ]
})
export class AppModule {}

// 注入token
@Component({ /* ... */ })
export class MyComponent {
  constructor(@Inject(API_URL) private apiUrl: string) {}
}
```

---

## 🛣️ 路由（Angular Router）

### 路由配置

```typescript
import { Routes } from '@angular/router'

const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    pathMatch: 'full'
  },
  {
    path: 'home',
    loadComponent: () => import('./home/home.component')
      .then(m => m.HomeComponent)
  },
  {
    path: 'users/:id',
    component: UserComponent,
    // 路由守卫
    canActivate: [AuthGuard],
    // 激活守卫（子路由）
    canActivateChild: [AuthChildGuard],
    // 解析守卫（预加载数据）
    resolve: {
      user: UserResolver
    }
  },
  {
    path: 'admin',
    loadChildren: () => import('./admin/admin.routes')
      .then(m => m.adminRoutes),
    canActivate: [AdminGuard]
  },
  {
    path: '**',
    component: NotFoundComponent
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
import { Component } from '@angular/core'
import { Router, ActivatedRoute } from '@angular/router'
import { map } from 'rxjs/operators'

@Component({ /* ... */ })
export class MyComponent {
  constructor(
    private router: Router,
    private route: ActivatedRoute
  ) {}

  // 编程式导航
  goToUsers(): void {
    this.router.navigate(['/users'])
  }

  goToUserWithId(id: string): void {
    this.router.navigate(['/users', id])
  }

  // 带查询参数
  goToUsersWithFilter(): void {
    this.router.navigate(['/users'], {
      queryParams: { page: 1, limit: 10 }
    })
  }

  // 路由参数（Observable方式）
  ngOnInit(): void {
    this.route.params.subscribe(params => {
      const id = params['id']
      console.log('User ID:', id)
    })

    // 或使用signal
    const id = this.route.paramMap.pipe(
      map(params => params.get('id'))
    )
  }

  // 查询参数
  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      const page = params['page']
      const limit = params['limit']
      console.log('Page:', page, 'Limit:', limit)
    })
  }
}
```

### 路由守卫

```typescript
import { Injectable } from '@angular/core'
import {
  CanActivate,
  CanActivateChild,
  CanLoad,
  Router
} from '@angular/router'
import { Observable } from 'rxjs'

// canActivate守卫
@Injectable({ providedIn: 'root' })
export class AuthGuard implements CanActivate {
  constructor(
    private authService: AuthService,
    private router: Router
  ) {}

  canActivate(): Observable<boolean> {
    return this.authService.isAuthenticated$.pipe(
      tap(authenticated => {
        if (!authenticated) {
          this.router.navigate(['/login'])
        }
      })
    )
  }
}

// canActivateChild守卫
@Injectable({ providedIn: 'root' })
export class AuthChildGuard implements CanActivateChild {
  constructor(private authService: AuthService) {}

  canActivateChild(): Observable<boolean> {
    return this.authService.isAuthenticated$
  }
}

// canLoad守卫（懒加载模块）
@Injectable({ providedIn: 'root' })
export class AdminGuard implements CanLoad {
  constructor(private authService: AuthService) {}

  canLoad(): Observable<boolean> {
    return this.authService.isAdmin$
  }
}
```

### 路由解析器（Resolver）

```typescript
import { Injectable } from '@angular/core'
import {
  Resolve,
  ActivatedRouteSnapshot,
  RouterStateSnapshot
} from '@angular/router'
import { Observable } from 'rxjs'
import { ApiService } from './api.service'

@Injectable({ providedIn: 'root' })
export class UserResolver implements Resolve<User> {
  constructor(private apiService: ApiService) {}

  resolve(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): Observable<User> {
    const id = route.paramMap.get('id')!
    return this.apiService.getDataById(id)
  }
}

// 在路由配置中使用
{
  path: 'users/:id',
  component: UserComponent,
  resolve: {
    user: UserResolver
  }
}

// 在组件中访问
@Component({ /* ... */ })
export class UserComponent {
  constructor(private route: ActivatedRoute) {}

  ngOnInit(): void {
    const user = this.route.snapshot.data['user']
    console.log('User:', user)
  }
}
```

---

## 📝 表单

### 模板驱动表单

```typescript
import { Component } from '@angular/core'
import { NgForm } from '@angular/forms'

@Component({
  selector: 'app-template-form',
  template: `
    <form #form="ngForm" (ngSubmit)="onSubmit(form.value)">
      <div>
        <label for="username">Username</label>
        <input
          id="username"
          name="username"
          ngModel
          required
          minlength="3"
          #username="ngModel"
        />

        @if (username.invalid && username.touched) {
          @if (username.hasError('required')) {
            <small>Name is required</small>
          }
          @if (username.hasError('minlength')) {
            <small>Name must be at least 3 characters</small>
          }
        }
      </div>

      <div>
        <label for="email">Email</label>
        <input
          id="email"
          name="email"
          ngModel
          required
          email
          #email="ngModel"
        />

        @if (email.invalid && email.touched) {
          @if (email.hasError('required')) {
            <small>Email is required</small>
          }
          @if (email.hasError('email')) {
            <small>Invalid email format</small>
          }
        }
      </div>

      <button type="submit" [disabled]="form.invalid">Submit</button>
    </form>
  `
})
export class TemplateFormComponent {
  onSubmit(value: any): void {
    console.log('Form value:', value)
  }
}
```

### 响应式表单

```typescript
import { Component, OnInit } from '@angular/core'
import {
  FormBuilder,
  FormGroup,
  FormControl,
  Validators
} from '@angular/forms'

@Component({
  selector: 'app-reactive-form',
  template: `
    <form [formGroup]="form" (ngSubmit)="onSubmit()">
      <div>
        <label for="username">Username</label>
        <input id="username" formControlName="username" />

        @if (form.get('username')?.invalid && form.get('username')?.touched) {
          @if (form.get('username')?.hasError('required')) {
            <small>Name is required</small>
          }
          @if (form.get('username')?.hasError('minlength')) {
            <small>Name must be at least 3 characters</small>
          }
        }
      </div>

      <div>
        <label for="email">Email</label>
        <input id="email" formControlName="email" />

        @if (form.get('email')?.invalid && form.get('email')?.touched) {
          @if (form.get('email')?.hasError('required')) {
            <small>Email is required</small>
          }
          @if (form.get('email')?.hasError('email')) {
            <small>Invalid email format</small>
          }
        }
      </div>

      <div formGroupName="address">
        <label for="street">Street</label>
        <input id="street" formControlName="street" />

        <label for="city">City</label>
        <input id="city" formControlName="city" />
      </div>

      <button type="submit" [disabled]="form.invalid">Submit</button>
    </form>
  `
})
export class ReactiveFormComponent implements OnInit {
  form: FormGroup

  constructor(private fb: FormBuilder) {}

  ngOnInit(): void {
    this.form = this.fb.group({
      username: ['', [Validators.required, Validators.minLength(3)]],
      email: ['', [Validators.required, Validators.email]],
      address: this.fb.group({
        street: [''],
        city: ['']
      })
    })
  }

  onSubmit(): void {
    if (this.form.valid) {
      console.log('Form value:', this.form.value)
    }
  }
}
```

### 自定义验证器

```typescript
import { AbstractControl, ValidationErrors, ValidatorFn } from '@angular/forms'

// 同步验证器
export function forbiddenNameValidator(nameRe: RegExp): ValidatorFn {
  return (control: AbstractControl): ValidationErrors | null => {
    const forbidden = nameRe.test(control.value)
    return forbidden ? { forbiddenName: { value: control.value } } : null
  }
}

// 异步验证器
export function uniqueUsernameValidator(
  userService: UserService
): AsyncValidatorFn {
  return (control: AbstractControl): Observable<ValidationErrors | null> => {
    return userService.checkUsernameExists(control.value).pipe(
      map(exists => (exists ? { uniqueUsername: true } : null))
    )
  }
}

// 使用验证器
this.form = this.fb.group({
  username: [
    '',
    [Validators.required, forbiddenNameValidator(/admin/)],
    [uniqueUsernameValidator(this.userService)]
  ]
})
```

### 动态表单

```typescript
@Component({ /* ... */ })
export class DynamicFormComponent implements OnInit {
  form: FormGroup

  ngOnInit(): void {
    this.form = this.fb.group({})

    // 动态添加表单控件
    this.addControl('username', ['', Validators.required])
    this.addControl('email', ['', [Validators.required, Validators.email]])
  }

  addControl(name: string, config: any): void {
    const control = this.fb.control(config)
    this.form.addControl(name, control)
  }

  removeControl(name: string): void {
    this.form.removeControl(name)
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
    <li><a routerLink="/contact">Contact</a></li>
  </ul>
</nav>

<main>
  <h1>Page Title</h1>
  <article>
    <h2>Article Title</h2>
    <p>Article content...</p>
  </article>
</main>

<aside>
  <h3>Sidebar</h3>
</aside>

<footer>
  <p>&copy; 2025</p>
</footer>

<!-- ❌ 避免：纯div -->
<div class="nav" (click)="goHome()">Home</div>
```

### ARIA属性

```html
<!-- 按钮状态 -->
<button
  [attr.aria-pressed]="isPressed()"
  [attr.aria-expanded]="isExpanded()"
  (click)="toggle()"
>
  Toggle
</button>

<!-- 加载状态 -->
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

<!-- 模态框 -->
<div
  role="dialog"
  aria-modal="true"
  aria-labelledby="modal-title"
  aria-describedby="modal-description"
>
  <h2 id="modal-title">Modal Title</h2>
  <p id="modal-description">Modal description</p>
</div>

<!-- 表单关联 -->
<label for="username">Username</label>
<input
  id="username"
  [attr.aria-required]="true"
  [attr.aria-invalid]="form.get('username')?.invalid"
  [attr.aria-describedby]="username-error"
/>
<small id="username-error" role="alert">
  @if (form.get('username')?.hasError('required')) {
    Username is required
  }
</small>
```

### 键盘导航

```html
<!-- 可聚焦的div -->
<div
  role="button"
  tabindex="0"
  (click)="handleClick()"
  (keydown.enter)="handleClick()"
  (keydown.space)="handleClick()"
>
  Click me or press Enter/Space
</div>

<!-- 键盘陷阱（模态框） -->
<div (keydown)="handleKeydown($event)">
  <!-- ... -->
</div>

@Component({ /* ... */ })
export class ModalComponent {
  focusableElements: HTMLElement[]

  ngAfterViewInit(): void {
    // 获取所有可聚焦元素
    this.focusableElements = this.modalRef.nativeElement.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    )
    this.focusableElements[0]?.focus()
  }

  handleKeydown(event: KeyboardEvent): void {
    if (event.key === 'Tab') {
      const firstElement = this.focusableElements[0]
      const lastElement = this.focusableElements[this.focusableElements.length - 1]

      if (event.shiftKey && document.activeElement === firstElement) {
        event.preventDefault()
        lastElement.focus()
      } else if (
        !event.shiftKey &&
        document.activeElement === lastElement
      ) {
        event.preventDefault()
        firstElement.focus()
      }
    }

    if (event.key === 'Escape') {
      this.close()
    }
  }
}
```

### 屏幕阅读器支持

```html
<!-- 隐藏内容（仅屏幕阅读器可见） -->
<span class="sr-only">Only visible to screen readers</span>

<!-- 跳过导航链接 -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<main id="main-content">
  <!-- ... -->
</main>

<!-- CSS -->
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: #000;
  color: #fff;
  padding: 8px;
  text-decoration: none;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}
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
    fixture.detectChanges()
  })

  it('should create', () => {
    expect(component).toBeTruthy()
  })

  it('should increment count', () => {
    component.increment()
    expect(component.localCount()).toBe(1)
  })

  it('should emit update on increment', () => {
    jest.spyOn(component.update, 'emit')
    component.increment()
    expect(component.update.emit).toHaveBeenCalledWith(1)
  })

  it('should display count', () => {
    component.localCount.set(5)
    fixture.detectChanges()
    const element = fixture.nativeElement.querySelector('.count')
    expect(element.textContent).toContain('5')
  })
})
```

### 组件测试（带服务）

```typescript
import { ComponentFixture, TestBed } from '@angular/core/testing'
import { HttpClientTestingModule } from '@angular/common/http/testing'
import { UsersComponent } from './users.component'
import { ApiService } from './api.service'
import { of } from 'rxjs'

describe('UsersComponent', () => {
  let component: UsersComponent
  let fixture: ComponentFixture<UsersComponent>
  let apiService: ApiService

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [
        UsersComponent,
        HttpClientTestingModule
      ],
      providers: [ApiService]
    })
    fixture = TestBed.createComponent(UsersComponent)
    component = fixture.componentInstance
    apiService = TestBed.inject(ApiService)
  })

  it('should load users on init', () => {
    const mockUsers = [
      { id: '1', name: 'Alice' },
      { id: '2', name: 'Bob' }
    ]

    jest.spyOn(apiService, 'getData').mockReturnValue(of(mockUsers))

    component.ngOnInit()
    fixture.detectChanges()

    expect(component.users()).toEqual(mockUsers)
    expect(apiService.getData).toHaveBeenCalled()
  })
})
```

### 路由测试

```typescript
import { ComponentFixture, TestBed } from '@angular/core/testing'
import { RouterTestingModule } from '@angular/router/testing'
import { Location } from '@angular/common'
import { Router } from '@angular/router'
import { AppComponent } from './app.component'

describe('AppComponent', () => {
  let fixture: ComponentFixture<AppComponent>
  let router: Router
  let location: Location

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [
        AppComponent,
        RouterTestingModule.withRoutes([
          { path: '', component: HomeComponent },
          { path: 'about', component: AboutComponent }
        ])
      ]
    })
    fixture = TestBed.createComponent(AppComponent)
    router = TestBed.inject(Router)
    location = TestBed.inject(Location)
  })

  it('should navigate to about', async () => {
    await router.navigate(['/about'])
    expect(location.path()).toBe('/about')
  })
})
```

### 测试工具函数

```typescript
// 测试信号
it('should update signal value', () => {
  const count = signal(0)
  count.set(5)
  expect(count()).toBe(5)
})

// 测试异步操作
it('should load data asynchronously', async () => {
  const data = await loadData()
  expect(data).toBeDefined()
})

// 测试表单验证
it('should validate required field', () => {
  component.form.get('username')?.setValue('')
  expect(component.form.get('username')?.valid).toBeFalsy()
})

// 测试DOM元素
it('should render button', () => {
  const button = fixture.nativeElement.querySelector('button')
  expect(button).toBeTruthy()
})
```

---

## 📋 最佳实践总结

### 1. 依赖注入

- 使用 `providedIn: 'root'` 注册单例服务
- 避免在服务中注入组件
- 使用 InjectionToken 注入配置值
- 合理使用 provider 配置

### 2. 路由

- 使用懒加载优化性能
- 使用路由守卫保护路由
- 使用 Resolver 预加载数据
- 避免在组件中硬编码路由路径

### 3. 表单

- 优先使用响应式表单
- 创建可复用的验证器
- 使用 FormArray 处理动态表单
- 合理使用 FormGroup 嵌套

### 4. 无障碍

- 使用语义化HTML元素
- 添加适当的 ARIA 属性
- 确保键盘导航可用
- 支持屏幕阅读器

### 5. 测试

- 保持测试简单明了
- 使用测试替身（Mock/Stub）
- 测试用户行为而非实现细节
- 保持高测试覆盖率

---

## 🔗 相关文档

- [返回主文档](angular.md)
- [React最佳实践](./react.md)
- [Vue最佳实践](./vue.md)
- [Svelte最佳实践](./svelte.md)
- [无障碍指南](../implementation/accessibility.md)

---

## 🔗 快速导航

- [返回by-framework/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.0
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
