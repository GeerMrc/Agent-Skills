# 用户反馈组件

> 🧩 **Feedback & Composite Components** - Toast、Modal、复合组件

---

## 📖 文档说明

本文档提供用户反馈和复合组件的完整实现示例，包括代码、类型定义和最佳实践。

**相关文档**：
- [数据展示组件](component-examples-display.md) - Card、Badge、Container、Grid
- [返回主文档](component-examples.md)
- [基础与表单组件](component-examples-basic-form.md)

---

## 🔔 反馈组件

### Toast 组件

**适用场景**：临时通知消息

**特性**：
- 4种类型：success、error、warning、info
- 自动关闭（可配置时长）
- 关闭按钮
- 固定定位

```tsx
// Toast.tsx
import { useEffect } from 'react';
import { X } from 'lucide-react';

interface ToastProps {
  message: string;
  type?: 'success' | 'error' | 'warning' | 'info';
  duration?: number;
  onClose: () => void;
}

export function Toast({
  message,
  type = 'info',
  duration = 3000,
  onClose,
}: ToastProps) {
  useEffect(() => {
    const timer = setTimeout(onClose, duration);
    return () => clearTimeout(timer);
  }, [duration, onClose]);

  const typeStyles = {
    success: 'bg-green-500',
    error: 'bg-red-500',
    warning: 'bg-yellow-500',
    info: 'bg-blue-500',
  };

  return (
    <div className="fixed bottom-4 right-4 z-50 animate-slide-up">
      <div className={`${typeStyles[type]} text-white px-4 py-3 rounded-lg shadow-lg flex items-center gap-3`}>
        <span>{message}</span>
        <button
          onClick={onClose}
          className="hover:bg-white/20 rounded p-1 transition-colors"
        >
          <X size={16} />
        </button>
      </div>
    </div>
  );
}
```

**使用示例**：
```tsx
function App() {
  const [toast, setToast] = useState(null);

  const showToast = () => {
    setToast({ message: '操作成功', type: 'success' });
  };

  return (
    <>
      <Button onClick={showToast}>显示通知</Button>
      {toast && (
        <Toast
          {...toast}
          onClose={() => setToast(null)}
        />
      )}
    </>
  );
}
```

---

### Modal 组件

**适用场景**：对话框、确认框

**特性**：
- 背景遮罩
- 键盘 ESC 关闭
- body 滚动锁定
- 完整 ARIA 属性

```tsx
// Modal.tsx
import { useEffect } from 'react';
import { X } from 'lucide-react';
import { ReactNode } from 'react';

interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title?: string;
  children: ReactNode;
}

export function Modal({ isOpen, onClose, title, children }: ModalProps) {
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = 'unset';
    }

    return () => {
      document.body.style.overflow = 'unset';
    };
  }, [isOpen]);

  useEffect(() => {
    const handleEscape = (e: KeyboardEvent) => {
      if (e.key === 'Escape' && isOpen) {
        onClose();
      }
    };

    document.addEventListener('keydown', handleEscape);
    return () => document.removeEventListener('keydown', handleEscape);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      {/* Backdrop */}
      <div
        className="absolute inset-0 bg-black/50"
        onClick={onClose}
      />

      {/* Modal */}
      <div
        role="dialog"
        aria-modal="true"
        aria-labelledby={title ? 'modal-title' : undefined}
        className="relative bg-white rounded-lg shadow-xl max-w-md w-full mx-4 animate-fade-in"
      >
        {/* Header */}
        {title && (
          <div className="flex items-center justify-between p-6 border-b">
            <h2 id="modal-title" className="text-lg font-semibold">
              {title}
            </h2>
            <button
              onClick={onClose}
              className="text-gray-400 hover:text-gray-600 transition-colors"
              aria-label="关闭对话框"
            >
              <X size={20} />
            </button>
          </div>
        )}

        {/* Body */}
        <div className="p-6">
          {children}
        </div>
      </div>
    </div>
  );
}
```

**使用示例**：
```tsx
function DeleteConfirm() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      <Button variant="danger" onClick={() => setIsOpen(true)}>
        删除
      </Button>

      <Modal
        isOpen={isOpen}
        onClose={() => setIsOpen(false)}
        title="确认删除"
      >
        <p className="mb-4">确定要删除此项目吗？此操作无法撤销。</p>
        <div className="flex gap-2 justify-end">
          <Button variant="secondary" onClick={() => setIsOpen(false)}>
            取消
          </Button>
          <Button
            variant="danger"
            onClick={() => {
              deleteItem();
              setIsOpen(false);
            }}
          >
            确认删除
          </Button>
        </div>
      </Modal>
    </>
  );
}
```

---

## 🎭 复合组件示例

### UserCard 组件

**适用场景**：用户信息卡片

**特性**：
- 组合 Card、Badge、Button 组件
- 显示用户头像、姓名、邮箱、角色
- 编辑/删除操作

```tsx
// UserCard.tsx
import { Card } from './Card';
import { Badge } from './Badge';
import { Button } from './Button';

interface User {
  id: string;
  name: string;
  email: string;
  role: 'admin' | 'user' | 'guest';
  avatar?: string;
}

interface UserCardProps {
  user: User;
  onEdit?: (user: User) => void;
  onDelete?: (userId: string) => void;
}

export function UserCard({ user, onEdit, onDelete }: UserCardProps) {
  const roleColors = {
    admin: 'success',
    user: 'info',
    guest: 'default',
  } as const;

  return (
    <Card>
      <div className="flex items-start gap-4">
        {/* Avatar */}
        <div className="w-12 h-12 rounded-full bg-blue-500 flex items-center justify-center text-white font-semibold">
          {user.name.charAt(0).toUpperCase()}
        </div>

        {/* Content */}
        <div className="flex-1">
          <div className="flex items-center gap-2 mb-1">
            <h3 className="font-semibold">{user.name}</h3>
            <Badge variant={roleColors[user.role]} size="sm">
              {user.role}
            </Badge>
          </div>
          <p className="text-sm text-gray-600">{user.email}</p>
        </div>
      </div>

      {/* Actions */}
      <Card.Footer className="flex gap-2 justify-end">
        {onEdit && (
          <Button
            variant="secondary"
            size="sm"
            onClick={() => onEdit(user)}
          >
            编辑
          </Button>
        )}
        {onDelete && (
          <Button
            variant="danger"
            size="sm"
            onClick={() => onDelete(user.id)}
          >
            删除
          </Button>
        )}
      </Card.Footer>
    </Card>
  );
}
```

**使用示例**：
```tsx
const users = [
  { id: '1', name: '张三', email: 'zhang@example.com', role: 'admin' },
  { id: '2', name: '李四', email: 'li@example.com', role: 'user' },
];

function UserList() {
  return (
    <Grid cols={2}>
      {users.map(user => (
        <UserCard
          key={user.id}
          user={user}
          onEdit={(u) => console.log('编辑', u)}
          onDelete={(id) => console.log('删除', id)}
        />
      ))}
    </Grid>
  );
}
```

---

## 💡 完整示例

### 用户管理页面

```tsx
function UserManagement() {
  const [users, setUsers] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [toast, setToast] = useState(null);

  const handleDelete = (id) => {
    setUsers(users.filter(u => u.id !== id));
    setToast({ message: '用户已删除', type: 'success' });
  };

  return (
    <Container size="xl">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">用户管理</h1>
        <Button onClick={() => setIsModalOpen(true)}>
          添加用户
        </Button>
      </div>

      <Grid cols={3} gap={6}>
        {users.map(user => (
          <UserCard
            key={user.id}
            user={user}
            onEdit={(u) => console.log('编辑', u)}
            onDelete={handleDelete}
          />
        ))}
      </Grid>

      {toast && <Toast {...toast} onClose={() => setToast(null)} />}
    </Container>
  );
}
```

---

## 🔗 相关文档

- [数据展示组件](component-examples-display.md) - Card、Badge、Container、Grid
- [返回主文档](component-examples.md)
- [基础与表单组件](component-examples-basic-form.md)
- [组件状态覆盖](../implementation/component-states.md)

---

## 🔗 快速导航

- [返回examples/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.1 (拆分版)
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
