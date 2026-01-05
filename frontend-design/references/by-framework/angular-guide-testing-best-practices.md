# Angular 测试与最佳实践

> 🔴 **Testing & Best Practices** - 无障碍、测试、最佳实践

---

## 📖 文档说明

本文档提供 Angular 的无障碍最佳实践、测试策略和最佳实践总结。

**相关文档**：
- [指南总览](angular-guide.md) - 依赖注入、路由基础
- [路由与表单](angular-guide-routing-forms.md) - 路由高级用法、表单处理
- [返回主文档](angular.md)

---

## ♿ 无障碍最佳实践

### 语义化HTML

**使用正确的 HTML 元素**：

```html
<!-- ✅ 好的做法：语义化元素 -->
<nav aria-label="主导航">
  <ul>
    <li><a routerLink="/home">Home</a></li>
    <li><a routerLink="/about">About</a></li>
  </ul>
</nav>

<main>
  <h1>页面标题</h1>
  <article>
    <h2>文章标题</h2>
    <p>文章内容...</p>
  </article>
</main>

<!-- ❌ 避免：纯div -->
<div class="nav">
  <div (click)="goHome()">Home</div>
</div>
```

### ARIA属性

**按钮状态**：

```html
<button
  [attr.aria-pressed]="isPressed"
  [attr.aria-expanded]="isExpanded"
  aria-controls="panel-1"
  (click)="toggle()">
  Toggle
</button>

<div id="panel-1" [hidden]="!isExpanded">
  面板内容
</div>
```

**加载状态**：

```html
<div
  role="status"
  [attr.aria-busy]="isLoading"
  aria-live="polite">
  <span *ngIf="isLoading">加载中...</span>
  <span *ngIf="!isLoading">完成</span>
</div>
```

**表单关联**：

```html
<label for="username">用户名</label>
<input
  id="username"
  aria-required="true"
  [attr.aria-invalid]="errors.username ? 'true' : 'false'"
  aria-describedby="username-error"
  [(ngModel)]="username"
/>
<span *ngIf="errors.username" id="username-error" role="alert">
  {{ errors.username }}
</span>
```

### 键盘导航

**可聚焦的div**：

```html
<div
  role="button"
  tabindex="0"
  (click)="handleClick()"
  (keydown)="handleKeydown($event)">
  点击我或按 Enter/Space
</div>
```

```typescript
handleKeydown(event: KeyboardEvent) {
  if (event.key === 'Enter' || event.key === ' ') {
    event.preventDefault()
    this.handleClick()
  }
}
```

**模态框焦点陷阱**：

```typescript
import { AfterViewInit, ElementRef, OnDestroy } from '@angular/core'

export class ModalComponent implements AfterViewInit, OnDestroy {
  private focusableElements: HTMLElement[]
  private firstElement: HTMLElement
  private lastElement: HTMLElement

  constructor(private elementRef: ElementRef) {}

  ngAfterViewInit() {
    this.focusableElements = Array.from(
      this.elementRef.nativeElement.querySelectorAll(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
      )
    )
    this.firstElement = this.focusableElements[0]
    this.lastElement = this.focusableElements[this.focusableElements.length - 1]

    this.firstElement?.focus()

    document.addEventListener('keydown', this.trapFocus)
  }

  trapFocus = (event: KeyboardEvent) => {
    if (event.key === 'Tab') {
      if (event.shiftKey && document.activeElement === this.firstElement) {
        event.preventDefault()
        this.lastElement?.focus()
      } else if (
        !event.shiftKey &&
        document.activeElement === this.lastElement
      ) {
        event.preventDefault()
        this.firstElement?.focus()
      }
    }

    if (event.key === 'Escape') {
      this.close()
    }
  }

  ngOnDestroy() {
    document.removeEventListener('keydown', this.trapFocus)
  }

  close() {
    // 关闭模态框
  }
}
```

---

## 🧪 测试

### 单元测试（Jest + TestBed）

**测试组件**：

```typescript
// user.component.spec.ts
import { ComponentFixture, TestBed } from '@angular/core/testing'
import { ReactiveFormsModule } from '@angular/forms'
import { UserComponent } from './user.component'

describe('UserComponent', () => {
  let component: UserComponent
  let fixture: ComponentFixture<UserComponent>

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [UserComponent],
      imports: [ReactiveFormsModule]
    }).compileComponents()

    fixture = TestBed.createComponent(UserComponent)
    component = fixture.componentInstance
    fixture.detectChanges()
  })

  it('should create', () => {
    expect(component).toBeTruthy()
  })

  it('should display user name', () => {
    component.user = { name: 'John Doe' }
    fixture.detectChanges()

    const element = fixture.nativeElement
    expect(element.querySelector('.user-name').textContent).toContain('John Doe')
  })

  it('should call onSubmit when form submitted', () => {
    spyOn(component, 'onSubmit')

    const form = fixture.nativeElement.querySelector('form')
    form.dispatchEvent(new Event('submit'))

    expect(component.onSubmit).toHaveBeenCalled()
  })
})
```

**测试服务**：

```typescript
// api.service.spec.ts
import { TestBed } from '@angular/core/testing'
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing'
import { ApiService } from './api.service'

describe('ApiService', () => {
  let service: ApiService
  let httpMock: HttpTestingController

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [ApiService]
    })

    service = TestBed.inject(ApiService)
    httpMock = TestBed.inject(HttpTestingController)
  })

  afterEach(() => {
    httpMock.verify()
  })

  it('should fetch data', () => {
    const mockData = [{ id: 1, name: 'Test' }]

    service.getData().subscribe(data => {
      expect(data).toEqual(mockData)
    })

    const req = httpMock.expectOne('/api/data')
    expect(req.request.method).toBe('GET')
    req.flush(mockData)
  })
})
```

### 测试指令和管道

**测试管道**：

```typescript
// uppercase.pipe.spec.ts
import { UppercasePipe } from './uppercase.pipe'

describe('UppercasePipe', () => {
  it('should transform text to uppercase', () => {
    const pipe = new UppercasePipe()
    expect(pipe.transform('hello')).toBe('HELLO')
  })
})
```

**测试指令**：

```typescript
// highlight.directive.spec.ts
import { Directive } from '@angular/core'

describe('HighlightDirective', () => {
  it('should add highlight class on mouseenter', () => {
    const fixture = TestBed.createComponent(TestComponent)
    const directive = fixture.debugElement.query(By.directive(HighlightDirective))

    directive.triggerEventHandler('mouseenter', {})
    fixture.detectChanges()

    expect(directive.nativeElement.classList.contains('highlight')).toBe(true)
  })
})
```

### 集成测试

**测试路由**：

```typescript
// app.component.spec.ts
import { Router } from '@angular/router'
import { Location } from '@angular/common'
import { ComponentFixture, TestBed } from '@angular/core/testing'
import { RouterTestingModule } from '@angular/router/testing'
import { AppModule } from './app.module'
import { AppComponent } from './app.component'

describe('Routing', () => {
  let router: Router
  let location: Location
  let fixture: ComponentFixture<AppComponent>

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [RouterTestingModule.withRoutes(routes)]
    }).compileComponents()

    router = TestBed.inject(Router)
    location = TestBed.inject(Location)
    fixture = TestBed.createComponent(AppComponent)
  })

  it('should navigate to home', fakeAsync(() => {
    router.navigate([''])
    tick()
    expect(location.path()).toBe('/')
  }))

  it('should navigate to about', fakeAsync(() => {
    router.navigate(['/about'])
    tick()
    expect(location.path()).toBe('/about')
  }))
})
```

### E2E测试

**使用 Cypress**：

```typescript
// e2e/app.cy.ts
describe('App E2E', () => {
  beforeEach(() => {
    cy.visit('/')
  })

  it('should display welcome message', () => {
    cy.contains('Welcome').should('be.visible')
  })

  it('should navigate to about page', () => {
    cy.get('a[href="/about"]').click()
    cy.url().should('include', '/about')
    cy.contains('About').should('be.visible')
  })

  it('should submit form', () => {
    cy.get('#name').type('John Doe')
    cy.get('#email').type('john@example.com')
    cy.get('button[type="submit"]').click()

    cy.contains('Form submitted').should('be.visible')
  })
})
```

---

## 📋 最佳实践总结

### 1. 组件设计

- 单一职责原则
- 保持组件小型和专注
- 使用输入和输出进行通信
- 避免直接操作DOM

### 2. 状态管理

- 使用服务进行跨组件通信
- 利用 RxJS 进行响应式编程
- 使用 NgRx 进行大型应用状态管理
- 保持状态简单和可预测

### 3. 性能优化

- 使用 OnPush 变更检测策略
- 懒加载功能模块
- 虚拟滚动长列表
- 优化管道和异步操作

```typescript
@Component({
  selector: 'app-item',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ItemComponent {
  @Input() item: Item
}
```

### 4. 代码组织

- 按功能组织模块
- 使用统一的文件命名约定
- 保持导入路径整洁
- 使用绝对路径导入

### 5. 依赖注入

- 依赖注入而非硬编码依赖
- 使用 providedIn: 'root' 注册服务
- 避免过度注入
- 使用 InjectionToken 注入配置值

### 6. 路由

- 使用路由守卫保护路由
- 懒加载路由模块
- 使用解析器预加载数据
- 避免深层路由嵌套

### 7. 表单

- 选择合适的表单类型（响应式 vs 模板驱动）
- 使用验证器确保数据完整性
- 自定义验证器提高可复用性
- 动态表单提高灵活性

### 8. 测试

- 编写可测试的代码
- 测试用户行为而非实现
- 保持测试简单明了
- 测试覆盖关键功能

### 9. 无障碍

- 使用语义化HTML
- 添加适当的ARIA属性
- 确保键盘导航可用
- 支持屏幕阅读器

### 10. 安全

- 防止XSS攻击（使用DomSanitizer）
- 验证和清理用户输入
- 使用HTTPS进行通信
- 遵循OWASP安全最佳实践

```typescript
import { DomSanitizer } from '@angular/platform-browser'

constructor(private sanitizer: DomSanitizer) {}

sanitizeHtml(html: string) {
  return this.sanitizer.sanitize(SecurityContext.HTML, html)
}
```

---

## 🔗 相关文档

- [指南总览](angular-guide.md) - 依赖注入、路由基础
- [路由与表单](angular-guide-routing-forms.md) - 路由高级用法、表单处理
- [返回主文档](angular.md) - Angular总览
- [无障碍指南](../implementation/accessibility.md) - WCAG AA标准

---

## 🔗 快速导航

- [返回by-framework/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.1 (拆分版)
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
