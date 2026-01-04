# -*- coding: utf-8 -*-
"""
色彩工具模块

提供OKLCH色彩空间处理和对比度计算功能。
"""

import re
from typing import Tuple, Optional
from dataclasses import dataclass


@dataclass
class OKLCHColor:
    """OKLCH颜色表示"""
    l: float  # 亮度 0-1
    c: float  # 色度 0-0.4
    h: float  # 色相 0-360

    def __str__(self) -> str:
        return f"oklch({self.l} {self.c} {self.h})"

    def to_css(self) -> str:
        """转换为CSS格式"""
        return f"oklch({self.l} {self.c} {self.h})"


class ColorUtils:
    """色彩工具类"""

    # OKLCH正则表达式
    OKLCH_PATTERN = re.compile(
        r'oklch\s*\(\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*\)',
        re.IGNORECASE
    )

    # 十六进制颜色正则
    HEX_PATTERN = re.compile(r'^#?([0-9a-f]{3}|[0-9a-f]{6})$', re.IGNORECASE)

    @staticmethod
    def parse_oklch(color_str: str) -> Optional[OKLCHColor]:
        """
        解析OKLCH颜色字符串

        Args:
            color_str: OKLCH颜色字符串 (e.g., "oklch(0.7 0.15 250)")

        Returns:
            OKLCHColor对象或None
        """
        match = ColorUtils.OKLCH_PATTERN.match(color_str.strip())
        if match:
            l, c, h = map(float, match.groups())
            return OKLCHColor(l, c, h)
        return None

    @staticmethod
    def is_valid_oklch(color_str: str) -> bool:
        """
        验证OKLCH格式是否正确

        Args:
            color_str: 颜色字符串

        Returns:
            是否有效
        """
        color = ColorUtils.parse_oklch(color_str)
        if not color:
            return False
        # 验证范围
        return 0 <= color.l <= 1 and 0 <= color.c <= 0.4 and 0 <= color.h <= 360

    @staticmethod
    def calculate_contrast_ratio(foreground: str, background: str) -> float:
        """
        计算对比度 (简化版, 实际需要完整转换)

        Args:
            foreground: 前景色
            background: 背景色

        Returns:
            对比度比值
        """
        # 简化实现 - 实际需要OKLCH到sRGB转换
        fg = ColorUtils.parse_oklch(foreground)
        bg = ColorUtils.parse_oklch(background)

        if not fg or not bg:
            return 1.0

        # 使用亮度差简化计算
        luminance_diff = abs(fg.l - bg.l)
        if luminance_diff == 0:
            return 1.0

        lighter = max(fg.l, bg.l)
        darker = min(fg.l, bg.l)
        return (lighter + 0.05) / (darker + 0.05)

    @staticmethod
    def meets_wcag_aa(foreground: str, background: str, large_text: bool = False) -> bool:
        """
        检查是否满足WCAG AA标准

        Args:
            foreground: 前景色
            background: 背景色
            large_text: 是否大文本 (大文本要求更低)

        Returns:
            是否满足标准
        """
        ratio = ColorUtils.calculate_contrast_ratio(foreground, background)
        threshold = 3.0 if large_text else 4.5
        return ratio >= threshold

    @staticmethod
    def meets_wcag_aaa(foreground: str, background: str, large_text: bool = False) -> bool:
        """
        检查是否满足WCAG AAA标准

        Args:
            foreground: 前景色
            background: 背景色
            large_text: 是否大文本

        Returns:
            是否满足标准
        """
        ratio = ColorUtils.calculate_contrast_ratio(foreground, background)
        threshold = 4.5 if large_text else 7.0
        return ratio >= threshold
