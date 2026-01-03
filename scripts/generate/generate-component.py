#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
组件生成工具

生成包含8种状态的完整组件代码，符合Design Token规范。

用法:
    python generate-component.py Button
    python generate-component.py Card --framework vue --output components/

示例:
    python generate-component.py Button
    python generate-component.py Modal --framework react --output src/components/
"""

import sys
import argparse
from pathlib import Path
from typing import Dict, List, Optional
from string import Template


class ComponentGenerator:
    """组件生成器"""

    # 组件状态模板
    STATES = ['default', 'hover', 'active', 'focus', 'disabled', 'loading', 'empty', 'error']

    # 组件类型
    COMPONENT_TYPES = {
        'button': {
            'props': ['variant', 'size', 'disabled', 'loading', 'icon'],
            'variants': ['primary', 'secondary', 'ghost', 'danger'],
            'sizes': ['sm', 'md', 'lg']
        },
        'input': {
            'props': ['type', 'size', 'disabled', 'error', 'placeholder'],
            'variants': ['default', 'filled', 'outlined'],
            'sizes': ['sm', 'md', 'lg']
        },
        'card': {
            'props': ['variant', 'hoverable', 'loading'],
            'variants': ['default', 'outlined', 'elevated'],
            'sizes': ['sm', 'md', 'lg']
        },
        'modal': {
            'props': ['open', 'closable', 'size', 'title'],
            'variants': ['default', 'centered'],
            'sizes': ['sm', 'md', 'lg', 'xl']
        },
        'dropdown': {
            'props': ['items', 'trigger', 'placement'],
            'variants': ['default', 'hover'],
            'placements': ['bottom', 'top', 'left', 'right']
        },
        'badge': {
            'props': ['count', 'dot', 'overflow'],
            'variants': ['default', 'success', 'warning', 'error'],
        },
        'tooltip': {
            'props': ['content', 'placement', 'trigger'],
            'placements': ['top', 'bottom', 'left', 'right']
        },
        'switch': {
            'props': ['checked', 'disabled', 'loading'],
            'variants': ['default', 'primary']
        },
    }

    def __init__(self, component_name: str, framework: str = 'react'):
        self.component_name = component_name
        self.framework = framework.lower()
        self.component_type = self._infer_component_type(component_name)

    def _infer_component_type(self, name: str) -> str:
        """推断组件类型"""
        name_lower = name.lower()
        for comp_type in self.COMPONENT_TYPES:
            if comp_type in name_lower:
                return comp_type
        return 'button'  # 默认

    def generate(self) -> str:
        """生成组件代码"""
        if self.framework == 'react':
            return self._generate_react()
        elif self.framework == 'vue':
            return self._generate_vue()
        elif self.framework == 'svelte':
            return self._generate_svelte()
        elif self.framework == 'typescript':
            return self._generate_typescript()
        else:
            return self._generate_javascript()

    def _generate_react(self) -> str:
        """生成React组件"""
        type_info = self.COMPONENT_TYPES.get(self.component_type, self.COMPONENT_TYPES['button'])

        code = f'''// {self.component_name}.tsx
import {{ designTokens }} from '@/tokens';

interface {self.component_name}Props {{
{'\\n'.join(f'  {prop}?: {self._get_prop_type(prop)};' for prop in type_info['props'])}
  children?: React.ReactNode;
  className?: string;
}}

export function {self.component_name}({{
  variant = 'default',
  size = 'md',
  disabled = false,
  loading = false,
  className,
  children,
  ...props
}}: {self.component_name}Props) {{
  const classes = [
    '{self._get_css_class()}',
    `{self._get_css_class()}--${{variant}}`,
    `{self._get_css_class()}--${{size}}`,
    disabled && `{self._get_css_class()}--disabled`,
    loading && `{self._get_css_class()}--loading`,
    className,
  ].filter(Boolean).join(' ');

  return (
    <div
      className={{classes}}
      disabled={{disabled}}
      aria-disabled={{disabled}}
      aria-busy={{loading}}
      {{...props}}
    >
      {self._get_react_content()}
    </div>
  );
}}

// ===== 8种状态样式 =====
/*
  1. Default (默认状态) - 基础样式
  2. Hover (悬停状态) - 鼠标悬停反馈
  3. Active (激活状态) - 点击/按下反馈
  4. Focus (焦点状态) - 键盘导航焦点
  5. Disabled (禁用状态) - 不可用状态
  6. Loading (加载状态) - 加载中状态
  7. Empty (空状态) - 无内容状态
  8. Error (错误状态) - 错误提示
*/

export const styles = `
.{self._get_css_class()} {{
  /* ===== 1. Default (默认状态) ===== */
  background: var(--color-bg);
  color: var(--color-text);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: var(--spacing-sm) var(--spacing-md);
  cursor: pointer;
  transition: all var(--duration-fast) var(--ease-out);
  font-size: var(--font-size-base);
}}

.{self._get_css_class()}:hover {{
  /* ===== 2. Hover (悬停状态) ===== */
  background: var(--color-bg-subtle);
  border-color: var(--color-primary);
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}}

.{self._get_css_class()}:active {{
  /* ===== 3. Active (激活状态) ===== */
  background: var(--color-bg-muted);
  transform: translateY(0) scale(0.98);
  box-shadow: var(--shadow-sm);
}}

.{self._get_css_class()}:focus-visible {{
  /* ===== 4. Focus (焦点状态) ===== */
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}}

.{self._get_css_class()}--disabled,
.{self._get_css_class()}[disabled] {{
  /* ===== 5. Disabled (禁用状态) ===== */
  background: var(--color-disabled);
  color: var(--color-text-disabled);
  cursor: not-allowed;
  opacity: 0.6;
  pointer-events: none;
}}

.{self._get_css_class()}--loading {{
  /* ===== 6. Loading (加载状态) ===== */
  position: relative;
  color: transparent;
  pointer-events: none;
}}

.{self._get_css_class()}--loading::after {{
  content: "";
  position: absolute;
  width: 1em;
  height: 1em;
  top: 50%;
  left: 50%;
  margin-left: -0.5em;
  margin-top: -0.5em;
  border: 2px solid currentColor;
  border-radius: 50%;
  border-right-color: transparent;
  animation: spin 0.6s linear infinite;
}}

@keyframes spin {{
  to {{ transform: rotate(360deg); }}
}}

/* ===== 7. Empty (空状态) ===== */
.{self._get_css_class()}--empty {{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-xl);
  color: var(--color-text-muted);
}}

/* ===== 8. Error (错误状态) ===== */
.{self._get_css_class()}--error {{
  border-color: var(--color-error);
  background: var(--color-error-bg);
}}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {{
  .{self._get_css_class()}:hover,
  .{self._get_css_class()}:active {{
    transform: none;
  }}
}}
`;
'''
        return code

    def _generate_vue(self) -> str:
        """生成Vue组件"""
        return f'''<!-- {self.component_name}.vue -->
<script setup lang="ts">
interface Props {{
  variant?: string
  size?: string
  disabled?: boolean
  loading?: boolean
}}

const props = withDefaults(defineProps<Props>(), {{
  variant: 'default',
  size: 'md',
  disabled: false,
  loading: false,
}})
</script>

<template>
  <div
    :class="[
      '{self._get_css_class()}',
      `{self._get_css_class()}--${{variant}}`,
      `{self._get_css_class()}--${{size}}`,
      {{ '{self._get_css_class()}--disabled': disabled }},
      {{ '{self._get_css_class()}--loading': loading }}
    ]"
    :disabled="disabled"
    :aria-disabled="disabled"
    :aria-busy="loading"
  >
    {{ self._get_vue_content() }}
  </div>
</template>

<style scoped>
.{self._get_css_class()} {{
  /* 8种状态样式 - 参考React版本 */
}}
</style>
'''

    def _generate_svelte(self) -> str:
        """生成Svelte组件"""
        return f'''<!-- {self.component_name}.svelte -->
<script lang="ts">
export let variant: string = 'default';
export let size: string = 'md';
export let disabled: boolean = false;
export let loading: boolean = false;
</script>

<div
  class="{self._get_css_class()} {self._get_css_class()}--{{variant}} {self._get_css_class()}--{{size}} {{{{disabled ? '{self._get_css_class()}--disabled' : ''}}}} {{{{loading ? '{self._get_css_class()}--loading' : ''}}}}"
  {{disabled}}
  aria-disabled={{disabled}}
  aria-busy={{loading}}
>
  {self._get_svelte_content()}
</div>

<style>
.{self._get_css_class()} {{
  /* 8种状态样式 */
}}
</style>
'''

    def _generate_typescript(self) -> str:
        """生成TypeScript类型定义"""
        return f'''// {self.component_name}.types.ts

export interface {self.component_name}Props {{
  variant?: '{self._get_css_class()}';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  loading?: boolean;
  children?: React.ReactNode;
  className?: string;
}}

export type {self.component_name}State =
  | 'default'
  | 'hover'
  | 'active'
  | 'focus'
  | 'disabled'
  | 'loading'
  | 'empty'
  | 'error';

export type {self.component_name}Variant =
  | 'primary'
  | 'secondary'
  | 'ghost'
  | 'danger';

export type {self.component_name}Size = 'sm' | 'md' | 'lg';
'''

    def _generate_javascript(self) -> str:
        """生成JavaScript组件"""
        return f'''// {self.component_name}.js
import {{ designTokens }} from '@/tokens';

export function {self.component_name}({{
  variant = 'default',
  size = 'md',
  disabled = false,
  loading = false,
  children,
}}) {{
  const className = [
    '{self._get_css_class()}',
    `{self._get_css_class()}--${{variant}}`,
    `{self._get_css_class()}--${{size}}`,
    disabled && `{self._get_css_class()}--disabled`,
    loading && `{self._get_css_class()}--loading`,
  ].filter(Boolean).join(' ');

  return (
    <div
      className={{className}}
      disabled={{disabled}}
      aria-disabled={{disabled}}
      aria-busy={{loading}}
    >
      {{children}}
    </div>
  );
}}

// 参考React版本获取完整的8种状态样式
'''

    def _get_css_class(self) -> str:
        """获取CSS类名"""
        import re
        # 将PascalCase转换为kebab-case
        name = re.sub(r'([A-Z])', r'-\1', self.component_name).lower().lstrip('-')
        return name

    def _get_prop_type(self, prop: str) -> str:
        """获取属性类型"""
        types = {
            'variant': 'string',
            'size': 'string',
            'disabled': 'boolean',
            'loading': 'boolean',
            'error': 'boolean',
            'checked': 'boolean',
            'open': 'boolean',
            'closable': 'boolean',
            'hoverable': 'boolean',
            'icon': 'React.ReactNode',
            'children': 'React.ReactNode',
            'className': 'string',
            'type': 'string',
            'placeholder': 'string',
            'items': 'any[]',
            'trigger': 'string',
            'placement': 'string',
            'count': 'number',
            'dot': 'boolean',
            'overflow': 'number',
            'content': 'string',
            'title': 'string',
        }
        return types.get(prop, 'any')

    def _get_react_content(self) -> str:
        """获取React内容"""
        return '''{loading && <span className="sr-only">加载中...</span>}
        {children}'''

    def _get_vue_content(self) -> str:
        """获取Vue内容"""
        return '''<span v-if="loading" class="sr-only">加载中...</span>
    <slot />'''

    def _get_svelte_content(self) -> str:
        """获取Svelte内容"""
        return '''{#if loading}
      <span class="sr-only">加载中...</span>
    {/if}
    <slot />'''


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='生成包含8种状态的组件代码',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s Button                           # 生成React按钮组件
  %(prog)s Button --framework vue            # 生成Vue按钮组件
  %(prog)s Modal --framework svelte          # 生成Svelte模态框组件
  %(prog)s Card --output src/components/     # 指定输出目录

支持的组件类型:
  button, input, card, modal, dropdown, badge, tooltip, switch
        """
    )

    parser.add_argument('component_name', help='组件名称 (如 Button, Modal)')
    parser.add_argument('--framework', '-f', choices=['react', 'vue', 'svelte', 'typescript', 'javascript'],
                       default='react', help='目标框架 (默认: react)')
    parser.add_argument('--output', '-o', type=Path, help='输出目录 (默认: 当前目录)')
    parser.add_argument('--file', action='store_true', help='输出到文件而非控制台')

    args = parser.parse_args()

    # 生成组件
    generator = ComponentGenerator(args.component_name, args.framework)
    code = generator.generate()

    # 输出
    if args.file or args.output:
        output_dir = args.output or Path.cwd()
        output_dir.mkdir(parents=True, exist_ok=True)

        # 确定文件扩展名
        exts = {
            'react': 'tsx',
            'vue': 'vue',
            'svelte': 'svelte',
            'typescript': 'ts',
            'javascript': 'js'
        }
        ext = exts.get(args.framework, 'tsx')
        filename = f"{args.component_name}.{ext}"
        output_path = output_dir / filename

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(code)

        print(f"✅ 组件已生成: {output_path}")
        print(f"   类型: {args.framework}")
        print(f"   状态: 8种完整状态 (default/hover/active/focus/disabled/loading/empty/error)")
    else:
        print(code)
        print(f"\n# ===== 使用说明 =====")
        print(f"# 组件: {args.component_name}")
        print(f"# 框架: {args.framework}")
        print(f"# 状态: 8种完整状态")
        print(f"# 保存: 添加 --file 或 --output 参数保存到文件")

    return 0


if __name__ == '__main__':
    sys.exit(main())
