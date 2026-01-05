# Angular 指南总览

> 🔴 **Quick Start** - 依赖注入、路由基础

---

## 📖 文档说明

本文档提供 Angular 的快速入门指南，包括依赖注入和路由基础。

**相关文档**：
- [路由与表单](angular-guide-routing-forms.md) - 路由高级用法、表单处理
- [测试与最佳实践](angular-guide-testing-best-practices.md) - 无障碍、测试、最佳实践
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

## 🛣️ 路由基础

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
    canActivate: [AuthGuard]
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
import { Router } from '@angular/router'

@Component({ /* ... */ })
export class NavigationComponent {
  constructor(private router: Router) {}

  goToHome() {
    this.router.navigate(['/home'])
  }

  goToUser(id: string) {
    this.router.navigate(['/users', id])
  }

  goWithQueryParams() {
    this.router.navigate(['/search'], {
      queryParams: { q: 'angular' }
    })
  }
}
```

### 路由参数

```typescript
import { ActivatedRoute } from '@angular/router'
import { Observable } from 'rxjs'

@Component({ /* ... */ })
export class UserComponent {
  user$: Observable<User>

  constructor(private route: ActivatedRoute) {
    // 获取路由参数
    this.user$ = route.paramMap.pipe(
      map(params => params.get('id')),
      switchMap(id => this.apiService.getUser(id))
    )
  }
}
```

---

## 🔗 相关文档

- [路由与表单](angular-guide-routing-forms.md) - 路由高级用法、表单处理
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
