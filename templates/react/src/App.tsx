import { useState } from 'react'
import './App.css'

/**
 * Frontend Design React Template
 *
 * 这是一个基于 Vite + React + TypeScript 的项目模板，
 * 符合 Frontend Design Agent Skills 最佳实践。
 *
 * @see https://github.com/your-org/frontend-design
 */
function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="app">
      <header className="app-header">
        <h1>Frontend Design React Template</h1>
        <p>React + Vite + TypeScript</p>
      </header>

      <main className="app-main">
        <div className="card">
          <button onClick={() => setCount((count) => count + 1)}>
            计数: {count}
          </button>
          <p>
            点击按钮增加计数。此模板展示了基础的 React 组件开发模式。
          </p>
        </div>

        <div className="info">
          <h2>模板特性</h2>
          <ul>
            <li>⚡ Vite - 极速开发服务器</li>
            <li>⚛️ React 18 - 最新的 React 特性</li>
            <li>📘 TypeScript - 类型安全</li>
            <li>🎨 ESLint - 代码质量检查</li>
            <li>📦 现代化构建配置</li>
          </ul>
        </div>

        <div className="links">
          <h2>相关资源</h2>
          <a href="https://vitejs.dev" target="_blank" rel="noreferrer">
            Vite 文档
          </a>
          <a href="https://react.dev" target="_blank" rel="noreferrer">
            React 文档
          </a>
          <a href="https://www.typescriptlang.org/" target="_blank" rel="noreferrer">
            TypeScript 文档
          </a>
        </div>
      </main>
    </div>
  )
}

export default App
