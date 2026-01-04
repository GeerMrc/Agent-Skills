/**
 * Frontend Design Vanilla Template
 *
 * 这是一个基于 Vite + TypeScript 的原生 JavaScript 项目模板，
 * 符合 Frontend Design Agent Skills 最佳实践。
 *
 * @see https://github.com/your-org/frontend-design
 */

// 计数器状态
let count = 0

// 获取DOM元素
const counterBtn = document.getElementById('counter-btn') as HTMLButtonElement

// 计数器点击事件
counterBtn?.addEventListener('click', () => {
  count++
  counterBtn.textContent = `计数: ${count}`
})

// 打印初始化信息
console.log('Frontend Design Vanilla Template initialized')
console.log('TypeScript is working!')
