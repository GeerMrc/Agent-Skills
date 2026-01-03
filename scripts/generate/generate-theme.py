#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
主题生成工具

生成符合Design Token规范的light/dark主题，支持OKLCH色彩系统。

用法:
    python generate-theme.py --primary "oklch(0.7 0.15 250)"
    python generate-theme.py --config theme-config.json
    python generate-theme.py --output tokens/

示例:
    python generate-theme.py --primary "oklch(0.7 0.15 250)" --secondary "oklch(0.65 0.12 180)"
"""

import sys
import argparse
import json
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass, field

sys.path.insert(0, str(Path(__file__).parent.parent))


@dataclass
class ThemeConfig:
    """主题配置"""
    primary_color: str
    secondary_color: str
    name: str = "default"
    include_dark: bool = True
    output_format: str = "css"  # css, json, scss


class ThemeGenerator:
    """主题生成器"""

    # 默认基础Token
    BASE_TOKENS = {
        # 间距
        "spacing-xs": "0.25rem",
        "spacing-sm": "0.5rem",
        "spacing-md": "1rem",
        "spacing-lg": "1.5rem",
        "spacing-xl": "2rem",
        "spacing-2xl": "3rem",

        # 字体
        "font-size-xs": "0.75rem",
        "font-size-sm": "0.875rem",
        "font-size-base": "1rem",
        "font-size-lg": "1.125rem",
        "font-size-xl": "1.25rem",
        "font-size-2xl": "1.5rem",
        "font-size-3xl": "1.875rem",
        "font-size-4xl": "2.25rem",

        "font-weight-normal": "400",
        "font-weight-medium": "500",
        "font-weight-semibold": "600",
        "font-weight-bold": "700",

        "line-height-tight": "1.25",
        "line-height-normal": "1.5",
        "line-height-relaxed": "1.75",

        # 圆角
        "radius-sm": "0.25rem",
        "radius-md": "0.5rem",
        "radius-lg": "0.75rem",
        "radius-xl": "1rem",
        "radius-full": "9999px",

        # 阴影
        "shadow-sm": "0 1px 2px 0 rgb(0 0 0 / 0.05)",
        "shadow-md": "0 4px 6px -1px rgb(0 0 0 / 0.1)",
        "shadow-lg": "0 10px 15px -3px rgb(0 0 0 / 0.1)",
        "shadow-xl": "0 20px 25px -5px rgb(0 0 0 / 0.1)",

        # 动画
        "duration-fast": "150ms",
        "duration-normal": "300ms",
        "duration-slow": "500ms",
        "ease-in-out": "cubic-bezier(0.4, 0, 0.2, 1)",
        "ease-out": "cubic-bezier(0, 0, 0.2, 1)",
    }

    @staticmethod
    def generate_color_tokens(primary: str, secondary: str) -> Dict[str, str]:
        """
        生成颜色Token

        Args:
            primary: 主色 OKLCH
            secondary: 次要色 OKLCH

        Returns:
            颜色Token字典
        """
        return {
            # Light主题
            "color-primary": primary,
            "color-primary-hover": ThemeGenerator._adjust_color(primary, 0.05, 0.02, 0),
            "color-primary-active": ThemeGenerator._adjust_color(primary, -0.05, 0, 0),
            "color-secondary": secondary,
            "color-secondary-hover": ThemeGenerator._adjust_color(secondary, 0.05, 0.02, 0),
            "color-success": "oklch(0.75 0.15 145)",
            "color-warning": "oklch(0.80 0.12 85)",
            "color-error": "oklch(0.60 0.20 25)",
            "color-info": "oklch(0.65 0.15 250)",

            # 中性色
            "color-bg": "oklch(0.98 0 0)",
            "color-bg-subtle": "oklch(0.94 0 0)",
            "color-bg-muted": "oklch(0.90 0 0)",
            "color-text": "oklch(0.20 0 0)",
            "color-text-muted": "oklch(0.55 0 0)",
            "color-text-disabled": "oklch(0.65 0 0)",
            "color-border": "oklch(0.85 0 0)",

            # 功能色
            "color-focus": "oklch(0.70 0.18 250)",
            "color-error-bg": "oklch(0.95 0.08 25)",
        }

    @staticmethod
    def generate_dark_color_tokens(primary: str, secondary: str) -> Dict[str, str]:
        """
        生成暗色主题颜色Token

        Args:
            primary: 主色 OKLCH
            secondary: 次要色 OKLCH

        Returns:
            暗色Token字典
        """
        return {
            # Dark主题 - 调整亮度和色度
            "color-primary": ThemeGenerator._adjust_color(primary, 0.05, 0.02, 0),
            "color-primary-hover": ThemeGenerator._adjust_color(primary, 0.08, 0.03, 0),
            "color-primary-active": ThemeGenerator._adjust_color(primary, 0.02, 0, 0),
            "color-secondary": ThemeGenerator._adjust_color(secondary, 0.05, 0.02, 0),
            "color-secondary-hover": ThemeGenerator._adjust_color(secondary, 0.08, 0.03, 0),
            "color-success": "oklch(0.70 0.18 145)",
            "color-warning": "oklch(0.75 0.15 85)",
            "color-error": "oklch(0.65 0.22 25)",
            "color-info": "oklch(0.70 0.18 250)",

            # 中性色 - 反转
            "color-bg": "oklch(0.15 0 0)",
            "color-bg-subtle": "oklch(0.20 0 0)",
            "color-bg-muted": "oklch(0.25 0 0)",
            "color-text": "oklch(0.95 0 0)",
            "color-text-muted": "oklch(0.60 0 0)",
            "color-text-disabled": "oklch(0.45 0 0)",
            "color-border": "oklch(0.30 0 0)",

            # 功能色
            "color-focus": "oklch(0.75 0.18 250)",
            "color-error-bg": "oklch(0.25 0.05 25)",
        }

    @staticmethod
    def _adjust_color(color: str, dl: float, dc: float, dh: float) -> str:
        """
        调整OKLCH颜色值

        Args:
            color: OKLCH颜色字符串
            dl: 亮度调整量
            dc: 色度调整量
            dh: 色相调整量

        Returns:
            调整后的OKLCH颜色
        """
        import re
        match = re.match(r'oklch\s*\(\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*\)', color)
        if match:
            l, c, h = map(float, match.groups())
            l = max(0, min(1, l + dl))
            c = max(0, min(0.4, c + dc))
            h = (h + dh) % 360
            return f"oklch({l} {c} {h})"
        return color

    def generate(self, config: ThemeConfig) -> Dict[str, Any]:
        """
        生成完整主题

        Args:
            config: 主题配置

        Returns:
            完整主题字典
        """
        # 合并所有Token
        light_theme = {**self.BASE_TOKENS}
        light_theme.update(self.generate_color_tokens(config.primary_color, config.secondary_color))

        dark_theme = {**self.BASE_TOKENS}
        dark_theme.update(self.generate_dark_color_tokens(config.primary_color, config.secondary_color))

        return {
            "light": light_theme,
            "dark": dark_theme
        }

    def to_css(self, theme: Dict[str, Any], name: str = "theme") -> str:
        """
        转换为CSS格式

        Args:
            theme: 主题字典
            name: 主题名称

        Returns:
            CSS代码
        """
        lines = [
            f"/* {name} - Design Tokens */",
            "/* Generated by Frontend Design Agent Skills */",
            "",
            "/* Light Theme */",
            ":root {"
        ]

        for token, value in theme["light"].items():
            var_name = token.replace("_", "-")
            lines.append(f"  --{var_name}: {value};")

        lines.extend([
            "}",
            "",
            "/* Dark Theme */",
            "@media (prefers-color-scheme: dark) {",
            "  :root {"
        ])

        for token, value in theme["dark"].items():
            var_name = token.replace("_", "-")
            lines.append(f"    --{var_name}: {value};")

        lines.extend([
            "  }",
            "}",
            ""
        ])

        return "\n".join(lines)

    def to_json(self, theme: Dict[str, Any]) -> str:
        """转换为JSON格式"""
        return json.dumps(theme, ensure_ascii=False, indent=2)

    def to_scss(self, theme: Dict[str, Any], name: str = "theme") -> str:
        """转换为SCSS格式"""
        lines = [
            f"// {name} - Design Tokens",
            "// Generated by Frontend Design Agent Skills",
            "",
            "// Light Theme",
            ":root {{"
        ]

        for token, value in theme["light"].items():
            var_name = token.replace("_", "-")
            lines.append(f"  --{var_name}: {value};")

        lines.extend([
            "}}",
            "",
            "// Dark Theme",
            "@media (prefers-color-scheme: dark) {{",
            "  :root {{"
        ])

        for token, value in theme["dark"].items():
            var_name = token.replace("_", "-")
            lines.append(f"    --{var_name}: {value};")

        lines.extend([
            "  }}",
            "}}",
            ""
        ])

        return "\n".join(lines)


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='生成Design Token主题',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('--primary', type=str, help='主色 (OKLCH格式)')
    parser.add_argument('--secondary', type=str, help='次要色 (OKLCH格式)')
    parser.add_argument('--config', type=Path, help='配置文件路径 (JSON)')
    parser.add_argument('--name', type=str, default='default', help='主题名称')
    parser.add_argument('--format', '-f', choices=['css', 'json', 'scss'], default='css', help='输出格式')
    parser.add_argument('--output', '-o', type=Path, help='输出文件路径')
    parser.add_argument('--no-dark', action='store_true', help='不生成暗色主题')

    args = parser.parse_args()

    # 加载配置
    if args.config:
        with open(args.config, 'r', encoding='utf-8') as f:
            config_data = json.load(f)
        config = ThemeConfig(**config_data)
    else:
        if not args.primary or not args.secondary:
            print("❌ 错误: 必须提供 --primary 和 --secondary 参数，或使用 --config", file=sys.stderr)
            return 1
        config = ThemeConfig(
            primary_color=args.primary,
            secondary_color=args.secondary,
            name=args.name,
            include_dark=not args.no_dark,
            output_format=args.format
        )

    # 生成主题
    generator = ThemeGenerator()
    theme = generator.generate(config)

    # 输出
    if args.format == 'css':
        output = generator.to_css(theme, config.name)
        ext = '.css'
    elif args.format == 'scss':
        output = generator.to_scss(theme, config.name)
        ext = '.scss'
    else:
        output = generator.to_json(theme)
        ext = '.json'

    if args.output:
        output_path = args.output
        if output_path.is_dir():
            output_path = output_path / f"{config.name}{ext}"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"✅ 主题已生成: {output_path}")
    else:
        print(output)

    return 0


if __name__ == '__main__':
    sys.exit(main())
