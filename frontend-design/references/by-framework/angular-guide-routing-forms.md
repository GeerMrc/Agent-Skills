# Angular 路由与表单

> 🔴 **Routing & Forms** - 路由高级用法、表单处理

---

## 📖 文档说明

本文档提供 Angular 的路由高级用法和表单处理详解。

**相关文档**：
- [指南总览](angular-guide.md) - 依赖注入、路由基础
- [测试与最佳实践](angular-guide-testing-best-practices.md) - 无障碍、测试、最佳实践
- [返回主文档](angular.md)

---

## 🛣️ 路由高级用法

### 路由守卫

**CanActivate - 激活守卫**：

```typescript
// auth.guard.ts
import { Injectable } from '@angular/core'
import { CanActivate, Router } from '@angular/router'

@Injectable({ providedIn: 'root' })
export class AuthGuard implements CanActivate {
  constructor(private router: Router, private authService: AuthService) {}

  canActivate(): boolean {
    if (this.authService.isLoggedIn()) {
      return true
    }

    this.router.navigate(['/login'])
    return false
  }
}

// 路由配置
const routes: Routes = [
  {
    path: 'dashboard',
    component: DashboardComponent,
    canActivate: [AuthGuard]
  }
]
```

**CanDeactivate - 停用守卫**：

```typescript
// can-deactivate.guard.ts
import { Injectable } from '@angular/core'
import { CanDeactivate } from '@angular/router'

export interface CanComponentDeactivate {
  canDeactivate: () => Observable<boolean> | Promise<boolean> | boolean
}

@Injectable({ providedIn: 'root' })
export class CanDeactivateGuard implements CanDeactivate<CanComponentDeactivate> {
  canDeactivate(component: CanComponentDeactivate): Observable<boolean> | Promise<boolean> | boolean {
    return component.canDeactivate ? component.canDeactivate() : true
  }
}

// 组件实现
export class EditComponent implements CanComponentDeactivate {
  canDeactivate(): boolean {
    if (this.hasUnsavedChanges()) {
      return confirm('你有未保存的更改，确定要离开吗？')
    }
    return true
  }
}
```

**Resolve - 数据解析**：

```typescript
// data.resolver.ts
import { Injectable } from '@angular/core'
import { Resolve } from '@angular/router'
import { Observable } from 'rxjs'

@Injectable({ providedIn: 'root' })
export class UserResolver implements Resolve<User> {
  constructor(private apiService: ApiService) {}

  resolve(): Observable<User> {
    return this.apiService.getCurrentUser()
  }
}

// 路由配置
const routes: Routes = [
  {
    path: 'profile',
    component: ProfileComponent,
    resolve: { user: UserResolver }
  }
]

// 组件使用
export class ProfileComponent {
  constructor(private route: ActivatedRoute) {
    this.user = route.snapshot.data['user']
  }
}
```

### 懒加载

**功能模块懒加载**：

```typescript
// 路由配置
const routes: Routes = [
  {
    path: 'home',
    component: HomeComponent
  },
  {
    path: 'users',
    loadChildren: () => import('./users/users.module')
      .then(m => m.UsersModule)
  },
  {
    path: 'admin',
    canLoad: [AuthGuard],
    loadChildren: () => import('./admin/admin.module')
      .then(m => m.AdminModule)
  }
]
```

**预加载策略**：

```typescript
// app.module.ts
import { PreloadAllModules } from '@angular/router'

@NgModule({
  imports: [
    RouterModule.forRoot(routes, {
      preloadingStrategy: PreloadAllModules
    })
  ]
})
export class AppModule {}
```

### 路由事件

**监听路由事件**：

```typescript
import { Router, NavigationStart, NavigationEnd, NavigationError } from '@angular/router'

@Component({ /* ... */ })
export class AppComponent {
  constructor(private router: Router) {
    this.router.events.subscribe(event => {
      if (event instanceof NavigationStart) {
        // 导航开始
        console.log('NavigationStart:', event.url)
      }

      if (event instanceof NavigationEnd) {
        // 导航成功
        console.log('NavigationEnd:', event.url)
      }

      if (event instanceof NavigationError) {
        // 导航错误
        console.error('NavigationError:', event.error)
      }
    })
  }
}
```

### 路由动画

**定义路由动画**：

```typescript
// animations.ts
import { trigger, transition, style, animate } from '@angular/animations'

export const slideInAnimation = trigger('routeAnimation', [
  transition('HomePage <=> AboutPage', [
    style({ position: 'relative', left: 0 }),
    animate('0.3s', style({ left: '100%' }))
  ])
])

// app.component.ts
@Component({
  selector: 'app-root',
  template: `
    <div [@routeAnimation]="o.activatedRouteData.animation">
      <router-outlet></router-outlet>
    </div>
  `,
  animations: [slideInAnimation]
})
export class AppComponent {}
```

---

## 📝 表单处理

### 响应式表单

**基础表单**：

```typescript
import { FormControl, FormGroup, FormBuilder, Validators } from '@angular/forms'

@Component({
  selector: 'app-user-form',
  template: `
    <form [formGroup]="userForm" (ngSubmit)="onSubmit()">
      <div>
        <label for="name">姓名</label>
        <input id="name" formControlName="name" />
        <div *ngIf="name.invalid && name.touched">
          <small *ngIf="name.errors?.['required']">姓名必填</small>
          <small *ngIf="name.errors?.['minlength']">至少3个字符</small>
        </div>
      </div>

      <div>
        <label for="email">邮箱</label>
        <input id="email" formControlName="email" />
        <div *ngIf="email.invalid && email.touched">
          <small *ngIf="email.errors?.['required']">邮箱必填</small>
          <small *ngIf="email.errors?.['email']">邮箱格式错误</small>
        </div>
      </div>

      <button type="submit" [disabled]="userForm.invalid">提交</button>
    </form>
  `
})
export class UserFormComponent {
  userForm: FormGroup

  constructor(private fb: FormBuilder) {
    this.userForm = this.fb.group({
      name: ['', [Validators.required, Validators.minLength(3)]],
      email: ['', [Validators.required, Validators.email]]
    })
  }

  get name() { return this.userForm.get('name') as FormControl }
  get email() { return this.userForm.get('email') as FormControl }

  onSubmit() {
    if (this.userForm.valid) {
      console.log(this.userForm.value)
    }
  }
}
```

**嵌套表单**：

```typescript
this.userForm = this.fb.group({
  name: ['', Validators.required],
  address: this.fb.group({
    street: ['', Validators.required],
    city: ['', Validators.required],
    zip: ['', Validators.required]
  })
})

// 访问嵌套值
console.log(this.userForm.value.address.street)
```

**FormArray**：

```typescript
this.userForm = this.fb.group({
  users: this.fb.array([
    this.fb.control('')
  ])
})

get users(): FormArray {
  return this.userForm.get('users') as FormArray
}

addUser() {
  this.users.push(this.fb.control(''))
}

removeUser(index: number) {
  this.users.removeAt(index)
}
```

### 模板驱动表单

**基础表单**：

```typescript
@Component({
  selector: 'app-user-form',
  template: `
    <form #userForm="ngForm" (ngSubmit)="onSubmit(userForm)">
      <div>
        <label for="name">姓名</label>
        <input id="name" name="name" ngModel required />
      </div>

      <div>
        <label for="email">邮箱</label>
        <input id="email" name="email" ngModel required email />
      </div>

      <button type="submit" [disabled]="userForm.invalid">提交</button>
    </form>
  `
})
export class UserFormComponent {
  onSubmit(form: NgForm) {
    if (form.valid) {
      console.log(form.value)
    }
  }
}
```

### 自定义验证器

**同步验证器**：

```typescript
// 自定义验证器函数
export function forbiddenNameValidator(nameRe: RegExp): ValidatorFn {
  return (control: AbstractControl): ValidationErrors | null => {
    const forbidden = nameRe.test(control.value)
    return forbidden ? { forbiddenName: { value: control.value } } : null
  }
}

// 使用验证器
this.userForm = this.fb.group({
  name: ['', [Validators.required, forbiddenNameValidator(/admin/i)]]
})
```

**异步验证器**：

```typescript
// 异步验证器函数
export const uniqueEmailValidator = (apiService: ApiService): AsyncValidatorFn => {
  return (control: AbstractControl): Observable<ValidationErrors | null> => {
    return apiService.checkEmailExists(control.value).pipe(
      map(isTaken => isTaken ? { uniqueEmail: true } : null),
      catchError(() => of(null))
    )
  }
}

// 使用异步验证器
this.userForm = this.fb.group({
  email: ['', '',
    [Validators.required, Validators.email],
    [uniqueEmailValidator(this.apiService)]
  ]
})
```

### 动态表单

**动态表单控件**：

```typescript
@Component({ /* ... */ })
export class DynamicFormComponent implements OnInit {
  form: FormGroup
  fields: FieldConfig[]

  constructor(private fb: FormBuilder) {}

  ngOnInit() {
    this.form = this.createFormGroup()
  }

  createFormGroup(): FormGroup {
    const group = this.fb.group({})

    this.fields.forEach(field => {
      const control = this.fb.control(
        field.value,
        this.bindValidations(field.validations || [])
      )
      group.addControl(field.name, control)
    })

    return group
  }

  bindValidations(validations: any[]) {
    if (validations.length > 0) {
      const validators = validations.map(v => {
        if (v.validator === 'required') return Validators.required
        if (v.validator === 'email') return Validators.email
        if (v.validator === 'minLength') return Validators.minLength(v.length)
      })
      return Validators.compose(validators)
    }
    return null
  }
}
```

---

## 🔗 相关文档

- [指南总览](angular-guide.md) - 依赖注入、路由基础
- [测试与最佳实践](angular-guide-testing-best-practices.md) - 无障碍、测试、最佳实践
- [返回主文档](angular.md) - Angular总览

---

## 🔗 快速导航

- [返回by-framework/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.1 (拆分版)
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
