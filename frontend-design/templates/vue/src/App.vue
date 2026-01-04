<script setup lang="ts">
import { ref } from 'vue'

/**
 * Frontend Design Vue Template
 *
 * 这是一个基于 Vite + Vue 3 + TypeScript 的项目模板，
 * 符合 Frontend Design Agent Skills 最佳实践。
 *
 * @see https://github.com/your-org/frontend-design
 */
const count = ref(0)

function increment() {
  count.value++
}
</script>

<template>
  <div class="app">
    <header class="app-header">
      <h1>Frontend Design Vue Template</h1>
      <p>Vue 3 + Vite + TypeScript</p>
    </header>

    <main class="app-main">
      <div class="card">
        <button @click="increment">
          计数: {{ count }}
        </button>
        <p>
          点击按钮增加计数。此模板展示了基础的 Vue 3 Composition API 开发模式。
        </p>
      </div>

      <div class="info">
        <h2>模板特性</h2>
        <ul>
          <li>⚡ Vite - 极速开发服务器</li>
          <li>💚 Vue 3 - 最新特性和 Composition API</li>
          <li>📘 TypeScript - 类型安全</li>
          <li>🎨 ESLint - 代码质量检查</li>
          <li>📦 现代化构建配置</li>
        </ul>
      </div>

      <div class="links">
        <h2>相关资源</h2>
        <a href="https://vitejs.dev" target="_blank" rel="noreferrer">
          Vite 文档
        </a>
        <a href="https://vuejs.org" target="_blank" rel="noreferrer">
          Vue 文档
        </a>
        <a href="https://www.typescriptlang.org/" target="_blank" rel="noreferrer">
          TypeScript 文档
        </a>
      </div>
    </main>
  </div>
</template>

<style scoped>
.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-header {
  background-color: #1a1a1a;
  color: #fff;
  padding: 2rem;
  text-align: center;
}

.app-header h1 {
  margin: 0 0 0.5rem 0;
  font-size: 2rem;
}

.app-header p {
  margin: 0;
  opacity: 0.8;
}

.app-main {
  flex: 1;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

.card {
  padding: 2rem;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  margin-bottom: 2rem;
  background-color: #fff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.card button {
  background-color: #42b883;
  color: #fff;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.2s;
}

.card button:hover {
  background-color: #35a372;
}

.card p {
  margin-top: 1rem;
  line-height: 1.6;
  color: #666;
}

.info {
  padding: 2rem;
  background-color: #f5f5f5;
  border-radius: 8px;
  margin-bottom: 2rem;
}

.info h2 {
  margin-top: 0;
  color: #1a1a1a;
}

.info ul {
  list-style: none;
  padding: 0;
}

.info li {
  padding: 0.5rem 0;
  font-size: 1rem;
}

.links {
  padding: 2rem;
}

.links h2 {
  margin-top: 0;
  color: #1a1a1a;
}

.links a {
  display: block;
  padding: 0.75rem;
  margin: 0.5rem 0;
  color: #0066cc;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.2s;
}

.links a:hover {
  background-color: #f0f0f0;
}

@media (prefers-color-scheme: dark) {
  .app-header {
    background-color: #000;
  }

  .card {
    background-color: #1a1a1a;
    border-color: #333;
  }

  .card p {
    color: #aaa;
  }

  .info {
    background-color: #2a2a2a;
  }

  .info h2,
  .links h2 {
    color: #fff;
  }

  .links a:hover {
    background-color: #333;
  }
}
</style>
