# -*- coding: utf-8 -*-
"""
Token验证工具模块

提供Design Token命名规范和结构验证功能。
"""

import re
import json
from typing import List, Dict, Any, Optional
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class TokenIssue:
    """Token问题记录"""
    level: str  # 'error', 'warning', 'info'
    token_name: str
    message: str
    suggestion: Optional[str] = None


@dataclass
class ValidationResult:
    """验证结果"""
    is_valid: bool
    total_tokens: int
    errors: List[TokenIssue] = field(default_factory=list)
    warnings: List[TokenIssue] = field(default_factory=list)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class TokenValidator:
    """Token验证器"""

    # 命名规范模式
    NAMING_PATTERNS = {
        'color': re.compile(r'^color-[a-z]+(-[a-z]+)*$'),
        'spacing': re.compile(r'^spacing-[a-z]+(-[a-z]+)*$'),
        'font': re.compile(r'^font-[a-z]+(-[a-z]+)*$'),
        'shadow': re.compile(r'^shadow-[a-z]+(-[a-z]+)*$'),
        'radius': re.compile(r'^radius-[a-z]+(-[a-z]+)*$'),
        'breakpoint': re.compile(r'^breakpoint-[a-z]+(-[a-z]+)*$'),
        'duration': re.compile(r'^duration-[a-z]+(-[a-z]+)*$'),
        'ease': re.compile(r'^ease-[a-z]+(-[a-z]+)*$'),
    }

    # 必需的Token类别
    REQUIRED_CATEGORIES = ['color', 'spacing', 'font', 'shadow', 'radius']

    # 语义化Token前缀
    SEMANTIC_PREFIXES = [
        'primary', 'secondary', 'success', 'warning', 'error', 'info',
        'bg', 'text', 'border', 'focus', 'disabled'
    ]

    @staticmethod
    def validate_naming(token_name: str) -> List[str]:
        """
        验证Token命名规范

        Args:
            token_name: Token名称

        Returns:
            问题列表
        """
        issues = []

        # 检查是否使用小写和连字符
        if not re.match(r'^[a-z][a-z0-9-]*$', token_name):
            issues.append(
                "Token名称必须使用小写字母、数字和连字符，且以字母开头"
            )

        # 检查是否包含禁止的模式
        if '--' in token_name:
            issues.append("Token名称不应包含连续的连字符")

        if '_' in token_name:
            issues.append("Token名称应使用连字符而非下划线")

        # 检查是否使用语义化命名
        if token_name.startswith('color-'):
            # 提取颜色概念部分
            parts = token_name.split('-')
            if len(parts) >= 3:
                concept = parts[2]
                # 检查是否使用具体颜色名（应使用语义化名称）
                concrete_colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
                if concept in concrete_colors:
                    issues.append(
                        f"建议使用语义化命名 (如 'color-primary') 而非具体颜色名 ('{token_name}')"
                    )

        return issues

    @staticmethod
    def validate_token_structure(tokens: Dict[str, Any]) -> ValidationResult:
        """
        验证Token结构完整性

        Args:
            tokens: Token字典

        Returns:
            验证结果
        """
        result = ValidationResult(is_valid=True, total_tokens=len(tokens))

        # 检查必需的类别
        found_categories = set()
        for token_name in tokens.keys():
            category = token_name.split('-')[0]
            found_categories.add(category)

        for required in TokenValidator.REQUIRED_CATEGORIES:
            if required not in found_categories:
                result.errors.append(TokenIssue(
                    level='error',
                    token_name=f'category:{required}',
                    message=f"缺少必需的Token类别: {required}",
                    suggestion=f"添加 {required}-* 相关的Token"
                ))

        # 验证每个Token
        for token_name, token_value in tokens.items():
            # 命名验证
            naming_issues = TokenValidator.validate_naming(token_name)
            for issue in naming_issues:
                result.warnings.append(TokenIssue(
                    level='warning',
                    token_name=token_name,
                    message=issue
                ))

            # 值验证
            if isinstance(token_value, str):
                # 颜色Token验证OKLCH格式
                if token_name.startswith('color-'):
                    from .color import ColorUtils
                    if not ColorUtils.is_valid_oklch(token_value):
                        result.errors.append(TokenIssue(
                            level='error',
                            token_name=token_name,
                            message=f"颜色Token值格式不正确: {token_value}",
                            suggestion="使用 oklch(L C H) 格式"
                        ))

                # 间距Token验证单位
                elif token_name.startswith('spacing-'):
                    if not token_value.endswith('rem') and not token_value.endswith('px'):
                        result.warnings.append(TokenIssue(
                            level='warning',
                            token_name=token_name,
                            message=f"间距Token建议使用rem或px单位: {token_value}",
                            suggestion="使用相对单位rem或绝对单位px"
                        ))

        result.is_valid = result.error_count == 0
        return result

    @staticmethod
    def validate_token_file(file_path: Path) -> ValidationResult:
        """
        验证Token文件

        Args:
            file_path: Token文件路径

        Returns:
            验证结果
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                tokens = json.load(f)
            return TokenValidator.validate_token_structure(tokens)
        except json.JSONDecodeError as e:
            return ValidationResult(
                is_valid=False,
                total_tokens=0,
                errors=[TokenIssue(
                    level='error',
                    token_name='file',
                    message=f"JSON解析错误: {e}"
                )]
            )
        except Exception as e:
            return ValidationResult(
                is_valid=False,
                total_tokens=0,
                errors=[TokenIssue(
                    level='error',
                    token_name='file',
                    message=f"文件读取错误: {e}"
                )]
            )
