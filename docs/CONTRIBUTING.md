# 贡献指南

感谢您对 Frontend Design Agent Skills 项目的关注！

---

## 🤝 如何贡献

### 报告问题

如果您发现了bug或有功能建议：

1. 检查 [Issues](../../issues) 是否已存在相同问题
2. 如果没有，创建新的Issue，包含：
   - 清晰的标题
   - 详细的问题描述
   - 复现步骤（如适用）
   - 预期行为 vs 实际行为
   - 环境信息

### 提交代码

#### 开发流程

1. **Fork项目**
   ```bash
   git clone https://github.com/your-username/frontend-design.git
   cd frontend-design
   ```

2. **创建功能分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **进行开发**
   - 遵循 [开发流程规范](DEVELOPMENT_WORKFLOW.md)
   - 更新TASK.md
   - 编写测试
   - 更新文档

4. **提交代码**
   ```bash
   git add .
   git commit -m "feat(scope): description"
   ```

5. **推送到您的Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **创建Pull Request**
   - 描述您的更改
   - 引用相关Issue
   - 确保CI检查通过

---

## 📝 代码规范

### SKILL.md规范

- **行数限制**: ≤ 200行（社区黄金标准）
- **YAML frontmatter**: < 100词
- **内容**: 导航地图，指向references/文档

### references/文档规范

- **行数限制**: 200-300行/文件
- **格式**: Markdown
- **结构**: 清晰的标题层级
- **示例**: 包含实用示例

### Git提交规范

遵循 [Conventional Commits](https://www.conventionalcommits.org/)：

```
type(scope): subject

body

footer
```

**类型**：
- `feat`: 新功能
- `fix`: 问题修复
- `docs`: 文档更新
- `style`: 代码格式
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建工具

---

## ✅ 开发检查清单

### 提交前检查

- [ ] 代码符合规范
- [ ] 测试通过
- [ ] 文档已更新
- [ ] CHANGELOG.md已更新
- [ ] TASK.md已更新
- [ ] Commit message符合规范

### PR检查

- [ ] 标题清晰
- [ ] 描述详细
- [ ] 关联Issue
- [ ] CI检查通过
- [ ] 代码审查通过

---

## 📧 联系方式

- **Issues**: [GitHub Issues](../../issues)
- **Discussions**: [GitHub Discussions](../../discussions)

---

> **最后更新**: 2025-01-03
